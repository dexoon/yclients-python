"""ChainClientsApi -- сгенерированные методы API."""

from __future__ import annotations

from typing import Any

from yclients._base import BaseClient
from yclients.models.schemas import GroupGroupidClientsResponseDataTypesData


class ChainClientsApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def get(
        self,
        group_id: float,
        *,
        phone: str | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> GroupGroupidClientsResponseDataTypesData:
        """Получить сетевого клиента по номеру телефона.
        + Параметр
        + group_id (required, number, `43877`) - Id сети салонов
        #### Фильтрация клиентов
        + phone:'70001234567' (optional, string) - Телефон для фильтрации клиентов
        """
        return await self._client.request(
            "GET",
            "/api/v1/group/{group_id}/clients/",
            path_params={"group_id": group_id},
            params={"phone": phone},
            response_model=GroupGroupidClientsResponseDataTypesData,
            extra_query=extra_query,
        )
