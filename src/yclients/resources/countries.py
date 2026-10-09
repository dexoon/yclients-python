"""CountriesApi -- сгенерированные методы API."""

from __future__ import annotations

import builtins
from typing import Any

from yclients._base import BaseClient
from yclients.models.schemas import CountriesResponseDataTypesDataItem


class CountriesApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def list(
        self,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[CountriesResponseDataTypesDataItem]:
        """Получить список стран
        """
        return await self._client.request(
            "GET",
            "/api/v1/countries",
            response_model=builtins.list[CountriesResponseDataTypesDataItem],
            extra_query=extra_query,
        )
