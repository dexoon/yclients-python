"""TechnologicalCardsApi -- сгенерированные методы API."""

from __future__ import annotations

import builtins
from typing import Any

from yclients._base import BaseClient


class TechnologicalCardsApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def list(
        self,
        company_id: float,
        *,
        search: str | None = None,
        page_: float | None = None,
        count_: float | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[dict[str, Any]]:
        """Получить список тех карт
        """
        return await self._client.request(
            "GET",
            "/api/v1/technological_cards/{company_id}/",
            path_params={"company_id": company_id},
            params={"search": search, "page": page_, "count": count_},
            response_model=builtins.list[dict[str, Any]],
            extra_query=extra_query,
        )

    async def get_staff_service_card(
        self,
        company_id: float,
        staff_id: float,
        service_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[dict[str, Any]]:
        """Получить тех карту для связи сотрудник услуга
        """
        return await self._client.request(
            "GET",
            "/api/v1/technological_cards/default_for_staff_and_service/{company_id}/{staffId}/{serviceId}/",
            path_params={"company_id": company_id, "staffId": staff_id, "serviceId": service_id},
            response_model=builtins.list[dict[str, Any]],
            extra_query=extra_query,
        )

    async def list_record_consumables(
        self,
        company_id: float,
        record_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[dict[str, Any]]:
        """Получить список тех карт и расходников записи
        """
        return await self._client.request(
            "GET",
            "/api/v1/technological_cards/record_consumables/{company_id}/{record_id}/",
            path_params={"company_id": company_id, "record_id": record_id},
            response_model=builtins.list[dict[str, Any]],
            extra_query=extra_query,
        )

    async def delete_record_technological_card(
        self,
        company_id: float,
        record_id: float,
        service_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[dict[str, Any]]:
        """Удалить технологическую из связи запись-услуга
        """
        return await self._client.request(
            "DELETE",
            "/api/v1/technological_cards/record_consumables/technological_cards/{company_id}/{record_id}/{service_id}",
            path_params={"company_id": company_id, "record_id": record_id, "service_id": service_id},
            response_model=builtins.list[dict[str, Any]],
            extra_query=extra_query,
        )

    async def update_record_consumables(
        self,
        company_id: float,
        record_id: float,
        service_id: float,
        data: dict[str, Any],
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[dict[str, Any]]:
        """Изменить список расходников связи запись-услуга
        """
        return await self._client.request(
            "PUT",
            "/api/v1/technological_cards/record_consumables/consumables/{company_id}/{record_id}/{service_id}/",
            path_params={"company_id": company_id, "record_id": record_id, "service_id": service_id},
            json_body=data,
            response_model=builtins.list[dict[str, Any]],
            extra_query=extra_query,
        )
