"""StaffApi -- сгенерированные методы API."""

from __future__ import annotations

import builtins
from typing import Any

from yclients._base import BaseClient
from yclients.models.schemas import (
    MasterWithPosition,
    PostStaffQuickRequest,
    StaffCompanyidRequestDataTypes,
)


class StaffApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def create_quick(
        self,
        company_id: float,
        data: PostStaffQuickRequest,
        extra_query: dict[str, Any] | None = None
    ) -> MasterWithPosition:
        """Быстрое создание сотрудника
        Создает нового сотрудника в филиале с минимальным набором входных параметров.
        """
        return await self._client.request(
            "POST",
            "/api/v1/company/{company_id}/staff/quick",
            path_params={"company_id": company_id},
            json_body=data,
            response_model=MasterWithPosition,
            extra_query=extra_query,
        )

    async def create(
        self,
        company_id: float,
        data: StaffCompanyidRequestDataTypes,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[dict[str, Any]]:
        """Устаревшее. Добавить нового сотрудника
        """
        return await self._client.request(
            "POST",
            "/api/v1/staff/{company_id}",
            path_params={"company_id": company_id},
            json_body=data,
            response_model=builtins.list[dict[str, Any]],
            extra_query=extra_query,
        )

    async def list(
        self,
        company_id: float,
        staff_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[dict[str, Any]]:
        """Получить список сотрудников / конкретного сотрудника
        """
        return await self._client.request(
            "GET",
            "/api/v1/company/{company_id}/staff/{staff_id}",
            path_params={"company_id": company_id, "staff_id": staff_id},
            response_model=builtins.list[dict[str, Any]],
            extra_query=extra_query,
        )

    async def list_company(
        self,
        company_id: float,
        staff_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[dict[str, Any]]:
        """Устаревшее. Получить список сотрудников / конкретного сотрудника
        """
        return await self._client.request(
            "GET",
            "/api/v1/staff/{company_id}/{staff_id}",
            path_params={"company_id": company_id, "staff_id": staff_id},
            response_model=builtins.list[dict[str, Any]],
            extra_query=extra_query,
        )

    async def update(
        self,
        company_id: float,
        staff_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[dict[str, Any]]:
        """Изменить сотрудника
        """
        return await self._client.request(
            "PUT",
            "/api/v1/staff/{company_id}/{staff_id}",
            path_params={"company_id": company_id, "staff_id": staff_id},
            response_model=builtins.list[dict[str, Any]],
            extra_query=extra_query,
        )

    async def delete(
        self,
        company_id: float,
        staff_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Удалить сотрудника
        """
        return await self._client.request(
            "DELETE",
            "/api/v1/staff/{company_id}/{staff_id}",
            path_params={"company_id": company_id, "staff_id": staff_id},
            extra_query=extra_query,
        )
