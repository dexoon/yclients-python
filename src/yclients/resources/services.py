"""ServicesApi -- сгенерированные методы API."""

from __future__ import annotations

import builtins
from typing import Any

from yclients._base import BaseClient
from yclients.models.schemas import (
    DeprecatedServicesCompanyidRequestDataTypes,
    MasterServiceLink2,
    PostServiceIdStaffRequest,
    PutStaffMasterIdRequest,
    ServicesChangeCompanyidRequestDataTypes,
    ServicesCompanyidLinksRequestDataTypes,
    ServicesCompanyidRequestDataTypes,
)


class ServicesApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def create(
        self,
        company_id: float,
        data: ServicesCompanyidRequestDataTypes,
        extra_query: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Создать услугу
        Метод, позволяющий создать услугу
        """
        return await self._client.request(
            "POST",
            "/api/v1/services/{company_id}",
            path_params={"company_id": company_id},
            json_body=data,
            response_model=dict[str, Any],
            extra_query=extra_query,
        )

    async def list(
        self,
        company_id: float,
        service_id: float,
        *,
        staff_id: float | None = None,
        category_id: float | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[dict[str, Any]]:
        """Получить список услуг / конкретную услугу
        + Параметр
        + company_id (required, number, `1`) - ID компании
        + service_id (optional, number, `1`) - ID услуги
        """
        return await self._client.request(
            "GET",
            "/api/v1/company/{company_id}/services/{service_id}",
            path_params={"company_id": company_id, "service_id": service_id},
            params={"staff_id": staff_id, "category_id": category_id},
            response_model=builtins.list[dict[str, Any]],
            extra_query=extra_query,
        )

    async def update(
        self,
        company_id: float,
        service_id: float,
        data: ServicesChangeCompanyidRequestDataTypes,
        extra_query: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Изменить услугу
        Метод, позволяющий изменить услугу
        """
        return await self._client.request(
            "PATCH",
            "/api/v1/company/{company_id}/services/{service_id}",
            path_params={"company_id": company_id, "service_id": service_id},
            json_body=data,
            response_model=dict[str, Any],
            extra_query=extra_query,
        )

    async def list_company(
        self,
        company_id: float,
        service_id: float,
        *,
        staff_id: float | None = None,
        category_id: float | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[dict[str, Any]]:
        """Устаревшее. Получить список услуг / конкретную услугу
        """
        return await self._client.request(
            "GET",
            "/api/v1/services/{company_id}/{service_id}",
            path_params={"company_id": company_id, "service_id": service_id},
            params={"staff_id": staff_id, "category_id": category_id},
            response_model=builtins.list[dict[str, Any]],
            extra_query=extra_query,
        )

    async def update_company(
        self,
        company_id: float,
        service_id: float,
        data: DeprecatedServicesCompanyidRequestDataTypes,
        extra_query: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Устаревшее. Изменить услугу
        Устаревшее. Метод, позволяющий изменить услугу
        """
        return await self._client.request(
            "PUT",
            "/api/v1/services/{company_id}/{service_id}",
            path_params={"company_id": company_id, "service_id": service_id},
            json_body=data,
            response_model=dict[str, Any],
            extra_query=extra_query,
        )

    async def delete(
        self,
        company_id: float,
        service_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Удалить услугу
        Метод, позволяющий удалить услугу
        """
        return await self._client.request(
            "DELETE",
            "/api/v1/services/{company_id}/{service_id}",
            path_params={"company_id": company_id, "service_id": service_id},
            extra_query=extra_query,
        )

    async def create_link(
        self,
        company_id: float,
        data: ServicesCompanyidLinksRequestDataTypes,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Изменить длительность оказания услуги сотрудниками, технические карты, названия на других языках
        Метод, позволяющий изменить длительность оказания услуги сотрудниками, технические карты, названия на других языках
        """
        return await self._client.request(
            "POST",
            "/api/v1/company/{company_id}/services/links",
            path_params={"company_id": company_id},
            json_body=data,
            extra_query=extra_query,
        )

    async def create_staff(
        self,
        company_id: float,
        service_id: float,
        data: PostServiceIdStaffRequest,
        extra_query: dict[str, Any] | None = None
    ) -> MasterServiceLink2:
        """Привязка сотрудника, оказывающего услугу
        Создает привязку сотрудника к услуге с указанием длительности и технологической карты.
        """
        return await self._client.request(
            "POST",
            "/api/v1/company/{company_id}/services/{service_id}/staff",
            path_params={"company_id": company_id, "service_id": service_id},
            json_body=data,
            response_model=MasterServiceLink2,
            extra_query=extra_query,
        )

    async def update_staff(
        self,
        company_id: float,
        service_id: float,
        master_id: float,
        data: PutStaffMasterIdRequest,
        extra_query: dict[str, Any] | None = None
    ) -> MasterServiceLink2:
        """Изменение настроек оказания услуги сотрудником
        Обновляет данные привязки сотрудника к услуге с указанием длительности и технологической карты.
        """
        return await self._client.request(
            "PUT",
            "/api/v1/company/{company_id}/services/{service_id}/staff/{master_id}",
            path_params={"company_id": company_id, "service_id": service_id, "master_id": master_id},
            json_body=data,
            response_model=MasterServiceLink2,
            extra_query=extra_query,
        )

    async def delete_staff(
        self,
        company_id: float,
        service_id: float,
        master_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Отвязка сотрудника, оказывающего услугу
        Удаляет привязку сотрудника к услуге.
        """
        return await self._client.request(
            "DELETE",
            "/api/v1/company/{company_id}/services/{service_id}/staff/{master_id}",
            path_params={"company_id": company_id, "service_id": service_id, "master_id": master_id},
            response_model=dict[str, Any],
            extra_query=extra_query,
        )
