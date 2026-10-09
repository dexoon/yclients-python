"""OnlineSettingsApi -- сгенерированные методы API."""

from __future__ import annotations

from typing import Any

from yclients._base import BaseClient
from yclients.models.schemas import (
    CompanyGetOnlineSettingsResponseDataFieldDataTypes,
    CompanyUpdateOnlineSettingsDataTypes,
)


class OnlineSettingsApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def get_online(
        self,
        company_id: str,
        extra_query: dict[str, Any] | None = None
    ) -> CompanyGetOnlineSettingsResponseDataFieldDataTypes:
        """Получение настроек онлайн-записи
        """
        return await self._client.request(
            "GET",
            "/api/v1/company/{company_id}/settings/online",
            path_params={"company_id": company_id},
            response_model=CompanyGetOnlineSettingsResponseDataFieldDataTypes,
            extra_query=extra_query,
        )

    async def update_online(
        self,
        company_id: str,
        data: CompanyUpdateOnlineSettingsDataTypes,
        extra_query: dict[str, Any] | None = None
    ) -> CompanyGetOnlineSettingsResponseDataFieldDataTypes:
        """Обновление настроек онлайн-записи
        """
        return await self._client.request(
            "PATCH",
            "/api/v1/company/{company_id}/settings/online",
            path_params={"company_id": company_id},
            json_body=data,
            response_model=CompanyGetOnlineSettingsResponseDataFieldDataTypes,
            extra_query=extra_query,
        )
