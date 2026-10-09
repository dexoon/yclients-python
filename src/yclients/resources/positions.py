"""PositionsApi -- сгенерированные методы API."""

from __future__ import annotations

import builtins
from typing import Any

from yclients._base import BaseClient
from yclients.models.schemas import Position, PostPositionsQuickRequest, StaffPosition2


class PositionsApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def list(
        self,
        company_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[StaffPosition2]:
        """Получить список должностей компании
        Метод позволяет получить список актуальных должностей компании
        """
        return await self._client.request(
            "GET",
            "/api/v1/company/{company_id}/staff/positions/",
            path_params={"company_id": company_id},
            response_model=builtins.list[StaffPosition2],
            extra_query=extra_query,
        )

    async def create_quick(
        self,
        company_id: float,
        data: PostPositionsQuickRequest,
        extra_query: dict[str, Any] | None = None
    ) -> Position:
        """Быстрое создание должности
        Создает новую должность в филиале; должность создается как сетевая сущность и одновременно привязывается к филиалу, в которой запрошено ее создание.
        """
        return await self._client.request(
            "POST",
            "/api/v1/company/{company_id}/positions/quick/",
            path_params={"company_id": company_id},
            json_body=data,
            response_model=Position,
            extra_query=extra_query,
        )
