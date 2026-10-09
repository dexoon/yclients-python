"""Сгенерированные ресурсы: типизация ответов, подстановка path-параметров, фасад."""

from __future__ import annotations

import json
from typing import Any

import httpx
import pytest

from conftest import PARTNER_TOKEN, USER_TOKEN, RecordedCall, build_client, envelope
from yclients import YclientsClient
from yclients.models import (
    AuthResponse2,
    BookCodeCompanyidDataTypesRequest,
    ClientCommentContainer,
    Page,
)

ACCEPT = "application/vnd.yclients.v2+json"


def route_by_path(routes: dict[tuple[str, str], Any]) -> Any:
    """Строит handler, выбирающий ответ по (method, точный путь).

    Значением может быть httpx.Response, тело ``data`` либо пара ``(data, meta)``.
    """

    def handler(request: httpx.Request) -> httpx.Response:
        key = (request.method, request.url.path)
        if key not in routes:
            pytest.fail(f"Неожиданный запрос: {key}")
        response = routes[key]
        if isinstance(response, httpx.Response):
            return response
        if isinstance(response, tuple):
            return httpx.Response(200, json=envelope(response[0], meta=response[1]))
        return httpx.Response(200, json=envelope(response))

    return handler


async def test_companies_list_typed_response(calls: list[RecordedCall]) -> None:
    data = [{"id": 1, "title": "Салон", "unknown_extra": "сохранён"}]
    handler = route_by_path({("GET", "/api/v1/companies"): data})

    async with build_client(handler, calls) as client:
        companies = await client.companies.list(my=1)

    assert isinstance(companies, list)
    assert companies[0].title == "Салон"
    assert companies[0].model_extra == {"unknown_extra": "сохранён"}
    assert "my=1" in calls[0].url


async def test_clients_comments_page_model(calls: list[RecordedCall]) -> None:
    comments = [
        {"id": 10, "text": "Первый", "type": "default"},
        {"id": 11, "text": "", "type": "file"},
    ]
    handler = route_by_path(
        {("GET", "/api/v1/company/7/clients/3/comments"): (comments, {"count": 2})}
    )

    async with build_client(handler, calls) as client:
        page = await client.clients.list_comments(7, 3)

    assert isinstance(page, Page)
    assert page.count == 2
    assert isinstance(page.data[0], ClientCommentContainer)
    assert page.data[0].text == "Первый"
    assert page.data[0].type_ == "default"  # алиас type -> type_
    assert calls[0].url == "https://api.yclients.ru/api/v1/company/7/clients/3/comments"


async def test_path_params_substituted(calls: list[RecordedCall]) -> None:
    handler = route_by_path({("GET", "/api/v1/client/7/3"): {"id": 3, "name": "Иван"}})

    async with build_client(handler, calls) as client:
        client_record = await client.clients.get(7, 3)

    assert client_record["name"] == "Иван"
    (call,) = calls
    assert call.url == "https://api.yclients.ru/api/v1/client/7/3"


async def test_facade_login_stores_user_token(calls: list[RecordedCall]) -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.path == "/api/v1/auth"
        assert request.headers["authorization"] == f"Bearer {PARTNER_TOKEN}"
        body = json.loads(request.content)
        assert body == {"login": "+79001234567", "password": "secret"}
        return httpx.Response(
            200,
            json=envelope({"id": 5, "user_token": USER_TOKEN, "name": "Илья"}),
        )

    async with build_client(handler, calls) as client:
        assert client.user_token is None
        result = await client.login("+79001234567", "secret")

    assert isinstance(result, AuthResponse2)
    assert result.user_token == USER_TOKEN
    assert client.user_token == USER_TOKEN
    (call,) = calls
    assert call.headers["accept"] == ACCEPT


async def test_user_token_sent_after_login(calls: list[RecordedCall]) -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/api/v1/auth":
            return httpx.Response(
                200, json=envelope({"id": 5, "user_token": USER_TOKEN})
            )
        assert request.headers["authorization"] == f"Bearer {PARTNER_TOKEN}, User {USER_TOKEN}"
        return httpx.Response(200, json=envelope([]))

    async with build_client(handler, calls) as client:
        await client.login("user", "pass")
        await client.companies.list()


async def test_extra_query_merged(calls: list[RecordedCall]) -> None:
    async with build_client(lambda _: httpx.Response(200, json=envelope([])), calls) as client:
        await client.companies.list(extra_query={"custom_field": "v"})

    (call,) = calls
    assert "custom_field=v" in call.url


async def test_post_body_sent(calls: list[RecordedCall]) -> None:
    handler = route_by_path({("POST", "/api/v1/book_code/7"): {"ok": 1}})

    async with build_client(handler, calls) as client:
        result = await client.booking.send_code(
            7, BookCodeCompanyidDataTypesRequest(phone="79991234567")
        )

    (call,) = calls
    assert call.method == "POST"
    assert call.url == "https://api.yclients.ru/api/v1/book_code/7"
    assert call.json_body == {"phone": "79991234567"}
    assert result.ok == 1


def test_facade_exposes_domains() -> None:
    client = YclientsClient(PARTNER_TOKEN)
    for domain in (
        "auth", "companies", "clients", "booking", "services", "staff",
        "records", "schedules", "storages", "users", "loyalty", "payroll",
    ):
        assert getattr(client, domain) is not None
