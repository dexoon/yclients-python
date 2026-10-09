"""AbonementTypesApi -- сгенерированные методы API."""

from __future__ import annotations

from typing import Any

from yclients._base import BaseClient
from yclients.models.schemas import (
    LoyaltyAbonementTypeWithSalons,
    PatchAbonementTypesLoyaltyAbonementTypeIdRequest,
    PostAbonementTypesLoyaltyAbonementTypeIdRequest,
    PostLoyaltyAbonementTypesRequest,
    PutAbonementTypesLoyaltyAbonementTypeIdRequest,
)


class AbonementTypesApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def create(
        self,
        chain_id: float,
        data: PostLoyaltyAbonementTypesRequest,
        extra_query: dict[str, Any] | None = None
    ) -> LoyaltyAbonementTypeWithSalons:
        """Создание типа абонемента
        Создает новый тип абонемента в сети; при создании можно указать филиалы в которых будет доступна сущность.
        """
        return await self._client.request(
            "POST",
            "/api/v1/chain/{chain_id}/loyalty/abonement_types",
            path_params={"chain_id": chain_id},
            json_body=data,
            response_model=LoyaltyAbonementTypeWithSalons,
            extra_query=extra_query,
        )

    async def update(
        self,
        chain_id: float,
        loyalty_abonement_type_id: str,
        data: PostAbonementTypesLoyaltyAbonementTypeIdRequest,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Восстановление удалённого типа абонемента
        Восстановление удалённого типа абонемента.
        """
        return await self._client.request(
            "POST",
            "/api/v1/chain/{chain_id}/loyalty/abonement_types/{loyalty_abonement_type_id}",
            path_params={"chain_id": chain_id, "loyalty_abonement_type_id": loyalty_abonement_type_id},
            json_body=data,
            extra_query=extra_query,
        )

    async def update_loyalty(
        self,
        chain_id: float,
        loyalty_abonement_type_id: str,
        data: PutAbonementTypesLoyaltyAbonementTypeIdRequest,
        extra_query: dict[str, Any] | None = None
    ) -> LoyaltyAbonementTypeWithSalons:
        """Обновление типа абонемента
        Обновляет тип абонемента по идентификатору.
        """
        return await self._client.request(
            "PUT",
            "/api/v1/chain/{chain_id}/loyalty/abonement_types/{loyalty_abonement_type_id}",
            path_params={"chain_id": chain_id, "loyalty_abonement_type_id": loyalty_abonement_type_id},
            json_body=data,
            response_model=LoyaltyAbonementTypeWithSalons,
            extra_query=extra_query,
        )

    async def update_chain(
        self,
        chain_id: float,
        loyalty_abonement_type_id: str,
        data: PatchAbonementTypesLoyaltyAbonementTypeIdRequest,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Архивация/восстановление типа абонемента
        Используется для архивации/разархивации типа абонемента.
        """
        return await self._client.request(
            "PATCH",
            "/api/v1/chain/{chain_id}/loyalty/abonement_types/{loyalty_abonement_type_id}",
            path_params={"chain_id": chain_id, "loyalty_abonement_type_id": loyalty_abonement_type_id},
            json_body=data,
            extra_query=extra_query,
        )

    async def delete(
        self,
        chain_id: float,
        loyalty_abonement_type_id: str,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Удаление типа абонемента
        Удаление типа абонемента.
        """
        return await self._client.request(
            "DELETE",
            "/api/v1/chain/{chain_id}/loyalty/abonement_types/{loyalty_abonement_type_id}",
            path_params={"chain_id": chain_id, "loyalty_abonement_type_id": loyalty_abonement_type_id},
            extra_query=extra_query,
        )

    async def clone(
        self,
        chain_id: float,
        loyalty_abonement_type_id: str,
        extra_query: dict[str, Any] | None = None
    ) -> LoyaltyAbonementTypeWithSalons:
        """Клонирование типа абонемента по идентификатору
        Клонирует тип абонемента по идентификатору.
        """
        return await self._client.request(
            "POST",
            "/api/v1/chain/{chain_id}/loyalty/abonement_types/{loyalty_abonement_type_id}/clone",
            path_params={"chain_id": chain_id, "loyalty_abonement_type_id": loyalty_abonement_type_id},
            response_model=LoyaltyAbonementTypeWithSalons,
            extra_query=extra_query,
        )
