"""Иерархия исключений YCLIENTS API."""

from __future__ import annotations

from typing import Any

__all__ = [
    "YclientsApiError",
    "YclientsAuthError",
    "YclientsError",
    "YclientsForbiddenError",
    "YclientsNotFoundError",
    "YclientsRateLimitError",
    "YclientsServerError",
    "YclientsTransportError",
    "YclientsValidationError",
]


class YclientsError(Exception):
    """Базовая ошибка клиента YCLIENTS."""


class YclientsApiError(YclientsError):
    """Ответ API с ``success: false`` или неуспешным HTTP-статусом.

    Атрибуты:
        message: человекочитаемое описание ошибки (из ``meta.message``).
        status_code: HTTP-статус ответа.
        meta: поле ``meta`` из тела ответа, если есть.
        body: разобранное тело ответа целиком.
    """

    def __init__(
        self,
        message: str,
        *,
        status_code: int | None = None,
        meta: Any = None,
        body: Any = None,
    ) -> None:
        suffix = f" (HTTP {status_code})" if status_code is not None else ""
        super().__init__(f"{message}{suffix}")
        self.message = message
        self.status_code = status_code
        self.meta = meta
        self.body = body


class YclientsAuthError(YclientsApiError):
    """401 — не передан или неверен Partner/User токен."""


class YclientsForbiddenError(YclientsApiError):
    """403 — нет прав на операцию."""


class YclientsNotFoundError(YclientsApiError):
    """404 — сущность не найдена."""


class YclientsValidationError(YclientsApiError):
    """422 — ошибка валидации данных запроса.

    Атрибуты:
        errors: словарь ``{поле: [сообщения]}`` из ``meta.errors``, если передан.
    """

    def __init__(
        self,
        message: str,
        *,
        status_code: int | None = 422,
        meta: Any = None,
        body: Any = None,
        errors: dict[str, list[str]] | None = None,
    ) -> None:
        super().__init__(message, status_code=status_code, meta=meta, body=body)
        self.errors = errors or {}


class YclientsRateLimitError(YclientsApiError):
    """429 — превышен лимит запросов (200 запросов в минуту на IP).

    Атрибуты:
        retry_after: значение заголовка ``Retry-After`` в секундах, если передан.
    """

    def __init__(
        self,
        message: str,
        *,
        status_code: int | None = 429,
        meta: Any = None,
        body: Any = None,
        retry_after: float | None = None,
    ) -> None:
        super().__init__(message, status_code=status_code, meta=meta, body=body)
        self.retry_after = retry_after


class YclientsServerError(YclientsApiError):
    """5xx — ошибка на стороне YCLIENTS."""


class YclientsTransportError(YclientsError):
    """Сетевая ошибка или таймаут при обращении к API."""
