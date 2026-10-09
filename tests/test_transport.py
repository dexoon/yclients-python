"""Транспортный слой: заголовки, конверт, ошибки, повторы, сериализация параметров."""

from __future__ import annotations

import datetime as dt

import httpx
import pytest

import yclients._base as base_module
from conftest import (
    PARTNER_TOKEN,
    USER_TOKEN,
    RecordedCall,
    build_client,
    envelope,
    error_envelope,
)
from yclients import (
    YclientsApiError,
    YclientsAuthError,
    YclientsClient,
    YclientsForbiddenError,
    YclientsNotFoundError,
    YclientsRateLimitError,
    YclientsServerError,
    YclientsTransportError,
    YclientsValidationError,
)
from yclients._base import BaseClient, _clean_param
from yclients.models import ClientCommentContainer

ACCEPT = "application/vnd.yclients.v2+json"


async def test_partner_token_header(calls: list[RecordedCall]) -> None:
    async with build_client(lambda _: httpx.Response(200, json=envelope([])), calls) as client:
        await client.companies.list()

    (call,) = calls
    assert call.headers["authorization"] == f"Bearer {PARTNER_TOKEN}"
    assert call.headers["accept"] == ACCEPT


async def test_user_token_header(calls: list[RecordedCall]) -> None:
    async with build_client(
        lambda _: httpx.Response(200, json=envelope([])),
        calls,
        user_token=USER_TOKEN,
    ) as client:
        await client.companies.list()

    (call,) = calls
    assert call.headers["authorization"] == f"Bearer {PARTNER_TOKEN}, User {USER_TOKEN}"


async def test_user_accept_header_not_overridden() -> None:
    sent_headers: list[dict[str, str]] = []

    def route(request: httpx.Request) -> httpx.Response:
        sent_headers.append(dict(request.headers))
        return httpx.Response(200, json=envelope([]))

    custom = httpx.AsyncClient(
        base_url="https://api.yclients.ru",
        headers={"Accept": "application/json"},
        transport=httpx.MockTransport(route),
    )
    async with YclientsClient(PARTNER_TOKEN, http_client=custom) as client:
        await client.companies.list()

    assert sent_headers[0]["accept"] == "application/json"


async def test_envelope_unwrap(calls: list[RecordedCall]) -> None:
    payload = [{"id": 1, "title": "Салон"}]

    def handler(_: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json=envelope(payload, meta={"count": 1}))

    async with build_client(handler) as client:
        result = await client.companies.list()

    assert result == payload


async def test_non_envelope_passthrough() -> None:
    async with build_client(lambda _: httpx.Response(200, json={"foo": "bar"})) as client:
        result = await client._base.request("GET", "/api/v1/whatever")

    assert result == {"foo": "bar"}


async def test_success_false_raises_api_error() -> None:
    def handler(_: httpx.Request) -> httpx.Response:
        return httpx.Response(
            200,
            json={"success": False, "data": None, "meta": {"message": "Что-то не так"}},
        )

    async with build_client(handler) as client:
        with pytest.raises(YclientsApiError) as exc_info:
            await client.companies.list()

    error = exc_info.value
    assert error.status_code is None
    assert error.message == "Что-то не так"
    assert error.meta == {"message": "Что-то не так"}
    assert not isinstance(error, YclientsAuthError)


@pytest.mark.parametrize(
    ("status_code", "expected_class"),
    [
        (401, YclientsAuthError),
        (403, YclientsForbiddenError),
        (404, YclientsNotFoundError),
        (429, YclientsRateLimitError),
        (500, YclientsServerError),
        (503, YclientsServerError),
        (400, YclientsApiError),
    ],
)
async def test_http_error_mapping(status_code: int, expected_class: type[YclientsApiError]) -> None:
    def handler(_: httpx.Request) -> httpx.Response:
        return error_envelope("Ошибка", status_code=status_code)

    async with build_client(handler, max_retries=0) as client:
        with pytest.raises(expected_class) as exc_info:
            await client.companies.list()

    assert exc_info.value.status_code == status_code
    assert isinstance(exc_info.value, YclientsApiError)


async def test_validation_error_collects_field_messages() -> None:
    def handler(_: httpx.Request) -> httpx.Response:
        return error_envelope(
            "Ошибка валидации",
            status_code=422,
            meta={"message": "Ошибка валидации", "errors": [{"name": "обязательное поле"}]},
        )

    async with build_client(handler, max_retries=0) as client:
        with pytest.raises(YclientsValidationError) as exc_info:
            await client.companies.list()

    assert exc_info.value.errors == {"name": ["обязательное поле"]}


async def test_rate_limit_error_keeps_retry_after() -> None:
    def handler(_: httpx.Request) -> httpx.Response:
        response = error_envelope("Превышен лимит", status_code=429)
        response.headers["Retry-After"] = "7"
        return response

    async with build_client(handler, max_retries=0) as client:
        with pytest.raises(YclientsRateLimitError) as exc_info:
            await client.companies.list()

    assert exc_info.value.retry_after == 7.0


async def test_retry_on_429_then_success(calls: list[RecordedCall], monkeypatch: pytest.MonkeyPatch) -> None:
    delays: list[float] = []

    async def fake_sleep(seconds: float) -> None:
        delays.append(seconds)

    monkeypatch.setattr(base_module.asyncio, "sleep", fake_sleep)
    attempts = {"n": 0}

    def handler(_: httpx.Request) -> httpx.Response:
        attempts["n"] += 1
        if attempts["n"] < 3:
            return httpx.Response(429, json={"success": False, "meta": {"message": "лимит"}})
        return httpx.Response(200, json=envelope([]))

    async with build_client(handler, calls, max_retries=5, retry_backoff=0.5) as client:
        await client.companies.list()

    assert len(calls) == 3
    assert delays == [0.5, 1.0]  # экспоненциальная задержка: backoff * 2**attempt


async def test_retry_honors_retry_after_header(
    calls: list[RecordedCall],
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    delays: list[float] = []

    async def fake_sleep(seconds: float) -> None:
        delays.append(seconds)

    monkeypatch.setattr(base_module.asyncio, "sleep", fake_sleep)
    attempts = {"n": 0}

    def handler(_: httpx.Request) -> httpx.Response:
        attempts["n"] += 1
        if attempts["n"] == 1:
            response = httpx.Response(429, json={"success": False})
            response.headers["Retry-After"] = "3"
            return response
        return httpx.Response(200, json=envelope([]))

    async with build_client(handler, calls, max_retries=5, retry_backoff=99.0) as client:
        await client.companies.list()

    assert delays == [3.0]  # Retry-After приоритетнее backoff


async def test_retry_exhausted_raises_rate_limit(calls: list[RecordedCall], monkeypatch: pytest.MonkeyPatch) -> None:
    async def fake_sleep(_: float) -> None:
        return None

    monkeypatch.setattr(base_module.asyncio, "sleep", fake_sleep)

    def handler(_: httpx.Request) -> httpx.Response:
        return error_envelope("Превышен лимит", status_code=429)

    async with build_client(handler, calls, max_retries=2) as client:
        with pytest.raises(YclientsRateLimitError):
            await client.companies.list()

    assert len(calls) == 3  # изначальный запрос + 2 повтора


async def test_non_retryable_status_not_retried(calls: list[RecordedCall], monkeypatch: pytest.MonkeyPatch) -> None:
    async def fake_sleep(_: float) -> None:
        return None

    monkeypatch.setattr(base_module.asyncio, "sleep", fake_sleep)

    def handler(_: httpx.Request) -> httpx.Response:
        return error_envelope("Нет доступа", status_code=403)

    async with build_client(handler, calls, max_retries=3) as client:
        with pytest.raises(YclientsForbiddenError):
            await client.companies.list()

    assert len(calls) == 1


async def test_network_error_raises_transport_error() -> None:
    def handler(_: httpx.Request) -> httpx.Response:
        raise httpx.ConnectError("connection refused")

    async with build_client(handler, max_retries=0) as client:
        with pytest.raises(YclientsTransportError):
            await client.companies.list()


async def test_invalid_json_raises_api_error() -> None:
    async with build_client(lambda _: httpx.Response(200, content=b"not json")) as client:
        with pytest.raises(YclientsApiError):
            await client.companies.list()


class TestCleanParam:
    def test_bool(self) -> None:
        assert _clean_param(True) == "1"
        assert _clean_param(False) == "0"

    def test_datetime_and_date(self) -> None:
        assert _clean_param(dt.datetime(2026, 1, 2, 15, 4, 5)) == "2026-01-02T15:04:05"
        assert _clean_param(dt.date(2026, 1, 2)) == "2026-01-02"

    def test_sequence_joined_with_comma(self) -> None:
        assert _clean_param([1, 2, 3]) == "1,2,3"
        assert _clean_param(("a", "b")) == "a,b"
        assert _clean_param([True, False]) == "1,0"

    def test_scalars_passthrough(self) -> None:
        assert _clean_param(42) == 42
        assert _clean_param("x") == "x"
        assert _clean_param(None) is None

    def test_model_dumps_to_json(self) -> None:
        model = ClientCommentContainer(type_="default", text="привет")
        assert _clean_param(model) == {"type": "default", "text": "привет"}


async def test_none_query_params_dropped(calls: list[RecordedCall]) -> None:
    async with build_client(lambda _: httpx.Response(200, json=envelope([])), calls) as client:
        await client.companies.list(my=1, active=None)

    (call,) = calls
    assert "my=1" in call.url
    assert "active" not in call.url


async def test_bool_query_param_serialized(calls: list[RecordedCall]) -> None:
    # bool в query: используем произвольный эндпоинт через low-level request
    async with build_client(lambda _: httpx.Response(200, json=envelope([])), calls) as client:
        await client._base.request(
            "GET",
            "/api/v1/book_check/{company_id}",
            path_params={"company_id": 1},
            params={"appointment": 1, "fullname": "x"},
        )

    (call,) = calls
    assert "/api/v1/book_check/1" in call.url


async def test_body_serialized_with_aliases_and_no_none(
    calls: list[RecordedCall],
) -> None:
    body = ClientCommentContainer(type_="default", text="текст", id_=None)

    async with build_client(lambda _: httpx.Response(200, json=envelope([])), calls) as client:
        await client._base.request("POST", "/api/v1/test", json_body=body)

    (call,) = calls
    assert call.json_body == {"type": "default", "text": "текст"}  # alias + exclude_none
    assert "id" not in call.json_body


def test_authorization_property() -> None:
    client = BaseClient(PARTNER_TOKEN)
    assert client._authorization == f"Bearer {PARTNER_TOKEN}"
    client.set_user_token(USER_TOKEN)
    assert client._authorization == f"Bearer {PARTNER_TOKEN}, User {USER_TOKEN}"
    client.set_user_token(None)
    assert client._authorization == f"Bearer {PARTNER_TOKEN}"
