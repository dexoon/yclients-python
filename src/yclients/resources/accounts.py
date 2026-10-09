"""AccountsApi -- сгенерированные методы API."""

from __future__ import annotations

import builtins
from typing import Any

from yclients._base import BaseClient


class AccountsApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def list(
        self,
        company_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[dict[str, Any]]:
        """Получить кассы компании
        Объект кассы компании имеет следующие поля:
        | Поле  | Тип | Описание |
        | ------------- | ------------- | ------------- |
        |  id  |  number   | Id  кассы  |
        |  title  | string  | Название  |
        |  type  | number  | 1 - для безналичных платежей, 0 для наличных |
        |  comment  | string  | Описание к кассе |
        """
        return await self._client.request(
            "GET",
            "/api/v1/accounts/{company_id}",
            path_params={"company_id": company_id},
            response_model=builtins.list[dict[str, Any]],
            extra_query=extra_query,
        )
