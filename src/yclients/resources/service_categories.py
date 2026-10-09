"""ServiceCategoriesApi -- сгенерированные методы API."""

from __future__ import annotations

import builtins
from typing import Any

from yclients._base import BaseClient
from yclients.models.schemas import (
    ServiceCategoriesCompanyidRequestDataTypes,
    ServiceCategoryTitle2,
)


class ServiceCategoriesApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def create(
        self,
        company_id: str,
        data: ServiceCategoriesCompanyidRequestDataTypes,
        extra_query: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Создать категорию услугу
        """
        return await self._client.request(
            "POST",
            "/api/v1/service_categories/{company_id}",
            path_params={"company_id": company_id},
            json_body=data,
            response_model=dict[str, Any],
            extra_query=extra_query,
        )

    async def get(
        self,
        company_id: float,
        id_: float,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[dict[str, Any]]:
        """Получить категорию услуг
        """
        return await self._client.request(
            "GET",
            "/api/v1/service_category/{company_id}/{id}",
            path_params={"company_id": company_id, "id": id_},
            response_model=builtins.list[dict[str, Any]],
            extra_query=extra_query,
        )

    async def update(
        self,
        company_id: float,
        id_: float,
        data: ServiceCategoriesCompanyidRequestDataTypes,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[dict[str, Any]]:
        """Изменить категорию услуг
        """
        return await self._client.request(
            "PUT",
            "/api/v1/service_category/{company_id}/{id}",
            path_params={"company_id": company_id, "id": id_},
            json_body=data,
            response_model=builtins.list[dict[str, Any]],
            extra_query=extra_query,
        )

    async def delete(
        self,
        company_id: float,
        id_: float,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Удалить категорию услуг
        """
        return await self._client.request(
            "DELETE",
            "/api/v1/service_category/{company_id}/{id}",
            path_params={"company_id": company_id, "id": id_},
            extra_query=extra_query,
        )

    async def list(
        self,
        chain_id: int,
        *,
        include: str | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[ServiceCategoryTitle2]:
        """Получить список категорий услуг сети
        """
        return await self._client.request(
            "GET",
            "/api/v1/chain/{chain_id}/service_categories",
            path_params={"chain_id": chain_id},
            params={"include": include},
            response_model=builtins.list[ServiceCategoryTitle2],
            extra_query=extra_query,
        )

    async def list_company(
        self,
        company_id: float,
        id_: float,
        *,
        staff_id: float | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[dict[str, Any]]:
        """Получить список категорий услуг
        + Параметры
        + company_id (required, number) - ID компании
        + id (optional, number) - ID категории услуг (для работы с конкретной категорией)
        + staff_id (optional, number) - ID сотрудника (для получения категорий, привязанных к сотруднику)
        """
        return await self._client.request(
            "GET",
            "/api/v1/company/{company_id}/service_categories/{id}",
            path_params={"company_id": company_id, "id": id_},
            params={"staff_id": staff_id},
            response_model=builtins.list[dict[str, Any]],
            extra_query=extra_query,
        )

    async def list_deprecated(
        self,
        company_id: float,
        id_: float,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[dict[str, Any]]:
        """Устаревшее. Получить список категорий услуг
        Получить список категорий услуг
        """
        return await self._client.request(
            "GET",
            "/api/v1/service_categories/{company_id}/{id}",
            path_params={"company_id": company_id, "id": id_},
            response_model=builtins.list[dict[str, Any]],
            extra_query=extra_query,
        )
