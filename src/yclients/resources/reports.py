"""ReportsApi -- сгенерированные методы API."""

from __future__ import annotations

from typing import Any

from yclients._base import BaseClient


class ReportsApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def get_z_report(
        self,
        company_id: int,
        *,
        start_date: str | None = None,
        master_id: int | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Получить данные Z-Отчета
        + start_date: Дата отчета
        + master_id: ID сотрудника
        """
        return await self._client.request(
            "GET",
            "/api/v1/reports/z_report/{company_id}",
            path_params={"company_id": company_id},
            params={"start_date": start_date, "master_id": master_id},
            response_model=dict[str, Any],
            extra_query=extra_query,
        )
