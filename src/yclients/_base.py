"""Асинхронный HTTP-слой клиента: аутентификация, конверт ответов, повторные попытки."""

from __future__ import annotations

import asyncio
import contextlib
import datetime as dt
from typing import TYPE_CHECKING, Any

import httpx
from pydantic import BaseModel, TypeAdapter

from .exceptions import (
    YclientsApiError,
    YclientsAuthError,
    YclientsForbiddenError,
    YclientsNotFoundError,
    YclientsRateLimitError,
    YclientsServerError,
    YclientsTransportError,
    YclientsValidationError,
)
from .models.common import Page

if TYPE_CHECKING:
    from collections.abc import Mapping

DEFAULT_BASE_URL = "https://api.yclients.ru"
DEFAULT_ACCEPT = "application/vnd.yclients.v2+json"
DEFAULT_TIMEOUT = 30.0

_RETRYABLE_STATUS = frozenset({429, 502, 503, 504})

__all__ = ["DEFAULT_ACCEPT", "DEFAULT_BASE_URL", "DEFAULT_TIMEOUT", "BaseClient"]


def _clean_param(value: Any) -> Any:
    """Приводит значение параметра запроса к виду, который ожидает API."""
    if isinstance(value, bool):
        return "1" if value else "0"
    if isinstance(value, (dt.datetime, dt.date, dt.time)):
        return value.isoformat()
    if isinstance(value, (list, tuple, set)):
        return ",".join(str(_clean_param(v)) for v in value)
    if isinstance(value, BaseModel):
        return value.model_dump(mode="json", by_alias=True, exclude_none=True)
    return value


class BaseClient:
    """Низкоуровневый асинхронный транспорт YCLIENTS API.

    Не используйте напрямую: работайте через :class:`yclients.client.YclientsClient`.
    """

    def __init__(
        self,
        partner_token: str,
        user_token: str | None = None,
        *,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float = DEFAULT_TIMEOUT,
        headers: Mapping[str, str] | None = None,
        max_retries: int = 2,
        retry_backoff: float = 0.5,
        http_client: httpx.AsyncClient | None = None,
    ) -> None:
        self.partner_token = partner_token
        self.user_token = user_token
        self.max_retries = max_retries
        self.retry_backoff = retry_backoff
        self._owns_client = http_client is None
        if http_client is not None:
            # Пользовательский клиент: проставляем Accept, если он не задан явно
            # (httpx по умолчанию подставляет */*, а API требует vendor-тип).
            if http_client.headers.get("Accept", "*/*") in ("", "*/*"):
                http_client.headers["Accept"] = DEFAULT_ACCEPT
            self._http = http_client
        else:
            self._http = httpx.AsyncClient(
                base_url=base_url,
                timeout=timeout,
                headers={"Accept": DEFAULT_ACCEPT, **(dict(headers) if headers else {})},
            )

    # ------------------------------------------------------------------ auth

    def set_user_token(self, user_token: str | None) -> None:
        """Задаёт User-токен (например, после :meth:`login`)."""
        self.user_token = user_token

    @property
    def _authorization(self) -> str:
        header = f"Bearer {self.partner_token}"
        if self.user_token:
            header += f", User {self.user_token}"
        return header

    # --------------------------------------------------------------- lifecycle

    async def aclose(self) -> None:
        if self._owns_client:
            await self._http.aclose()

    async def __aenter__(self) -> BaseClient:
        return self

    async def __aexit__(self, *exc_info: object) -> None:
        await self.aclose()

    # ------------------------------------------------------------------ request

    async def request(
        self,
        method: str,
        path: str,
        *,
        path_params: Mapping[str, Any] | None = None,
        params: Mapping[str, Any] | None = None,
        json_body: Any = None,
        response_model: Any = None,
        extra_query: Mapping[str, Any] | None = None,
    ) -> Any:
        """Выполняет запрос и возвращает ``data`` из конверта, провалидированное моделью.

        Для эндпоинтов без конверта возвращает тело ответа целиком.
        """
        if path_params:
            path = path.format(
                **{k: _clean_param(v) for k, v in path_params.items()}
            )

        query: dict[str, Any] = {}
        for source in (params, extra_query):
            for key, value in (source or {}).items():
                if value is None:
                    continue
                query[key] = _clean_param(value)

        if isinstance(json_body, BaseModel):
            json_body = json_body.model_dump(mode="json", by_alias=True, exclude_none=True)

        payload = await self._send(method, path, query, json_body)
        return self._unwrap(payload, response_model)

    async def _send(
        self,
        method: str,
        path: str,
        query: dict[str, Any],
        json_body: Any,
    ) -> Any:
        attempt = 0
        while True:
            try:
                response = await self._http.request(
                    method,
                    path,
                    params=query or None,
                    json=json_body,
                    headers={"Authorization": self._authorization},
                )
            except httpx.HTTPError as exc:
                raise YclientsTransportError(
                    f"Ошибка сети при обращении к {method} {path}: {exc!r}"
                ) from exc

            if response.status_code in _RETRYABLE_STATUS and attempt < self.max_retries:
                delay = self._retry_delay(response, attempt)
                attempt += 1
                await asyncio.sleep(delay)
                continue

            if response.status_code >= 400:
                raise self._error_for(response)

            return self._parse_json(response)

    def _retry_delay(self, response: httpx.Response, attempt: int) -> float:
        retry_after = response.headers.get("Retry-After")
        if retry_after is not None:
            try:
                return max(0.0, float(retry_after))
            except ValueError:
                pass
        # int ** int -> Any в typeshed, поэтому явное приведение
        return self.retry_backoff * float(2**attempt)

    @staticmethod
    def _parse_json(response: httpx.Response) -> Any:
        if not response.content:
            return None
        try:
            return response.json()
        except ValueError as exc:
            raise YclientsApiError(
                "Не удалось разобрать JSON-ответ",
                status_code=response.status_code,
                body=response.text,
            ) from exc

    def _unwrap(self, payload: Any, response_model: Any) -> Any:
        """Достаёт ``data`` из конверта и валидирует моделью ответа."""
        meta = payload.get("meta") if isinstance(payload, dict) else None
        if isinstance(payload, dict) and "success" in payload:
            if not payload["success"]:
                # success=false при 2xx — тоже ошибка API
                raise self._error_for_payload(payload)
            data = payload.get("data")
        else:
            data = payload

        if response_model is None:
            return data
        # Page[T] собирается из data + meta.count, а не из одного data
        # (в pydantic v2 Page[T] — уже конкретный класс, а не typing-алиас)
        if (
            isinstance(response_model, type)
            and issubclass(response_model, Page)
            and isinstance(data, list)
        ):
            count = meta.get("count") if isinstance(meta, dict) else None
            return TypeAdapter(response_model).validate_python(
                {"data": data, "count": count}
            )
        return TypeAdapter(response_model).validate_python(data)

    @staticmethod
    def _error_for(response: httpx.Response) -> YclientsApiError:
        payload = BaseClient._parse_json(response)
        error = _build_error(response.status_code, payload)
        if isinstance(error, YclientsRateLimitError):
            retry_after = response.headers.get("Retry-After")
            if retry_after is not None:
                with contextlib.suppress(ValueError):
                    error.retry_after = float(retry_after)
        return error

    @staticmethod
    def _error_for_payload(payload: Any) -> YclientsApiError:
        return _build_error(None, payload)


def _meta_message(payload: Any) -> str:
    meta = payload.get("meta") if isinstance(payload, dict) else None
    if isinstance(meta, dict) and meta.get("message"):
        return str(meta["message"])
    return "Запрос выполнен неуспешно"


def _validation_errors(meta: Any) -> dict[str, list[str]] | None:
    if not isinstance(meta, dict):
        return None
    raw = meta.get("errors")
    if not isinstance(raw, list):
        return None
    errors: dict[str, list[str]] = {}
    for item in raw:
        if isinstance(item, dict):
            for field, message in item.items():
                errors.setdefault(str(field), []).append(str(message))
    return errors or None


def _build_error(status_code: int | None, payload: Any) -> YclientsApiError:
    message = _meta_message(payload)
    meta = payload.get("meta") if isinstance(payload, dict) else None
    kwargs: dict[str, Any] = {"status_code": status_code, "meta": meta, "body": payload}

    if status_code == 401:
        return YclientsAuthError(message, **kwargs)
    if status_code == 403:
        return YclientsForbiddenError(message, **kwargs)
    if status_code == 404:
        return YclientsNotFoundError(message, **kwargs)
    if status_code == 422:
        return YclientsValidationError(
            message, errors=_validation_errors(meta), **kwargs
        )
    if status_code == 429:
        return YclientsRateLimitError(message, **kwargs)
    if status_code is not None and status_code >= 500:
        return YclientsServerError(message, **kwargs)
    return YclientsApiError(message, **kwargs)
