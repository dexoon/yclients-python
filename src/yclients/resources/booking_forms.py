"""BookingFormsApi -- сгенерированные методы API."""

from __future__ import annotations

import builtins
from typing import Any

from yclients._base import BaseClient
from yclients.models.schemas import BookformSettingsResponse2


class BookingFormsApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def list(
        self,
        company_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[BookformSettingsResponse2]:
        """Получить список букформ
        """
        return await self._client.request(
            "GET",
            "/api/v1/company/{company_id}/booking_forms/",
            path_params={"company_id": company_id},
            response_model=builtins.list[BookformSettingsResponse2],
            extra_query=extra_query,
        )

    async def create(
        self,
        company_id: float,
        data: dict[str, Any],
        extra_query: dict[str, Any] | None = None
    ) -> BookformSettingsResponse2:
        """Создать букформу
        """
        return await self._client.request(
            "POST",
            "/api/v1/company/{company_id}/booking_forms/",
            path_params={"company_id": company_id},
            json_body=data,
            response_model=BookformSettingsResponse2,
            extra_query=extra_query,
        )

    async def get(
        self,
        company_id: float,
        form_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> BookformSettingsResponse2:
        """Получить букформу
        """
        return await self._client.request(
            "GET",
            "/api/v1/company/{company_id}/booking_forms/{form_id}/",
            path_params={"company_id": company_id, "form_id": form_id},
            response_model=BookformSettingsResponse2,
            extra_query=extra_query,
        )

    async def update(
        self,
        company_id: float,
        form_id: float,
        data: dict[str, Any],
        extra_query: dict[str, Any] | None = None
    ) -> BookformSettingsResponse2:
        """Изменить букформу
        """
        return await self._client.request(
            "PATCH",
            "/api/v1/company/{company_id}/booking_forms/{form_id}/",
            path_params={"company_id": company_id, "form_id": form_id},
            json_body=data,
            response_model=BookformSettingsResponse2,
            extra_query=extra_query,
        )

    async def delete(
        self,
        company_id: float,
        form_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Удалить букформу
        """
        return await self._client.request(
            "DELETE",
            "/api/v1/company/{company_id}/booking_forms/{form_id}/",
            path_params={"company_id": company_id, "form_id": form_id},
            extra_query=extra_query,
        )
