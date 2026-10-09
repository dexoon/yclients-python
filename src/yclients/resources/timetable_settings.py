"""TimetableSettingsApi -- сгенерированные методы API."""

from __future__ import annotations

from typing import Any

from yclients._base import BaseClient
from yclients.models.schemas import (
    CompanyGetTimetableSettingsResponseDataFieldDataTypes,
    CompanyUpdateTimetableSettingsDataTypes,
)


class TimetableSettingsApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def get_timetable(
        self,
        company_id: str,
        extra_query: dict[str, Any] | None = None
    ) -> CompanyGetTimetableSettingsResponseDataFieldDataTypes:
        """Получение настроек журнала записи
        """
        return await self._client.request(
            "GET",
            "/api/v1/company/{company_id}/settings/timetable",
            path_params={"company_id": company_id},
            response_model=CompanyGetTimetableSettingsResponseDataFieldDataTypes,
            extra_query=extra_query,
        )

    async def update_timetable(
        self,
        company_id: str,
        data: CompanyUpdateTimetableSettingsDataTypes,
        extra_query: dict[str, Any] | None = None
    ) -> CompanyGetTimetableSettingsResponseDataFieldDataTypes:
        """Обновление настроек журнала записи
        """
        return await self._client.request(
            "PATCH",
            "/api/v1/company/{company_id}/settings/timetable",
            path_params={"company_id": company_id},
            json_body=data,
            response_model=CompanyGetTimetableSettingsResponseDataFieldDataTypes,
            extra_query=extra_query,
        )
