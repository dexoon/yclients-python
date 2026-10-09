"""CitiesApi -- сгенерированные методы API."""

from __future__ import annotations

import builtins
from typing import Any

from yclients._base import BaseClient
from yclients.models.schemas import CitiesResponseDataTypesDataItem


class CitiesApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def list(
        self,
        *,
        country_id: float | None = None,
        company_id: float | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[CitiesResponseDataTypesDataItem]:
        """Получить список городов
        """
        return await self._client.request(
            "GET",
            "/api/v1/cities",
            params={"country_id": country_id, "company_id": company_id},
            response_model=builtins.list[CitiesResponseDataTypesDataItem],
            extra_query=extra_query,
        )
