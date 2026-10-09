"""Общие фикстуры тестов: клиент поверх httpx.MockTransport."""

from __future__ import annotations

import json
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any

import httpx
import pytest

from yclients import YclientsClient

PARTNER_TOKEN = "partner-token"
USER_TOKEN = "user-token"

Handler = Callable[[httpx.Request], httpx.Response]


@dataclass
class RecordedCall:
    """Один зафиксированный HTTP-вызов."""

    method: str
    url: str
    headers: dict[str, str]
    json_body: Any = None


def envelope(data: Any, meta: Any = None) -> dict[str, Any]:
    """Строит стандартный конверт ответа YCLIENTS."""
    return {"success": True, "data": data, "meta": meta}


def error_envelope(
    message: str,
    *,
    status_code: int,
    meta: Any = None,
) -> httpx.Response:
    """Строит ответ с ``success: false``."""
    meta = meta if meta is not None else {"message": message}
    return httpx.Response(
        status_code,
        json={"success": False, "data": None, "meta": meta},
    )


def recording_transport(calls: list[RecordedCall], handler: Handler) -> httpx.MockTransport:
    """Оборачивает handler, записывая каждый вызов в ``calls``."""

    def wrapped(request: httpx.Request) -> httpx.Response:
        body = request.content
        calls.append(
            RecordedCall(
                method=request.method,
                url=str(request.url),
                headers=dict(request.headers),
                json_body=json.loads(body) if body else None,
            )
        )
        return handler(request)

    return httpx.MockTransport(wrapped)


def build_client(
    handler: Handler,
    calls: list[RecordedCall] | None = None,
    *,
    user_token: str | None = None,
    max_retries: int = 2,
    retry_backoff: float = 0.0,
) -> YclientsClient:
    """Создаёт клиент с мок-транспортом; вызовы дописываются в ``calls``."""
    log = calls if calls is not None else []
    http = httpx.AsyncClient(
        base_url="https://api.yclients.ru",
        transport=recording_transport(log, handler),
    )
    return YclientsClient(
        PARTNER_TOKEN,
        user_token,
        http_client=http,
        max_retries=max_retries,
        retry_backoff=retry_backoff,
    )


@pytest.fixture
def calls() -> list[RecordedCall]:
    return []
