"""ReferencesApi -- сгенерированные методы API."""

from __future__ import annotations

from typing import Any

from yclients._base import BaseClient
from yclients.models.schemas import ReferencesBusinessGroupResponseDataTypesDataItem


class ReferencesApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def list_business_groups_with_types(
        self,
        extra_query: dict[str, Any] | None = None
    ) -> list[ReferencesBusinessGroupResponseDataTypesDataItem]:
        """Получить бизнес-типы по группам
        """
        return await self._client.request(
            "GET",
            "/api/v1/references/business_groups_with_types",
            response_model=list[ReferencesBusinessGroupResponseDataTypesDataItem],
            extra_query=extra_query,
        )
