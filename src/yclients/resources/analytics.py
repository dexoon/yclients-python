"""AnalyticsApi -- сгенерированные методы API."""

from __future__ import annotations

from typing import Any

from yclients._base import BaseClient
from yclients.models.schemas import (
    AnalyticsReportOverallChartDailyRow2,
    AnalyticsReportOverallChartScalarItem2,
    AnalyticsReportOverallStats2,
)


class AnalyticsApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def get_overall(
        self,
        company_id: float,
        *,
        date_from: str | None = None,
        date_to: str | None = None,
        staff_id: int | None = None,
        position_id: int | None = None,
        user_id: int | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> AnalyticsReportOverallStats2:
        """Получить основные показатели компании
        Метод позволяет получить основные показатели компании за выбранный период и сравнить с предыдущим периодом той же длительности
        """
        return await self._client.request(
            "GET",
            "/api/v1/company/{company_id}/analytics/overall/",
            path_params={"company_id": company_id},
            params={"date_from": date_from, "date_to": date_to, "staff_id": staff_id, "position_id": position_id, "user_id": user_id},
            response_model=AnalyticsReportOverallStats2,
            extra_query=extra_query,
        )

    async def list_income_daily(
        self,
        company_id: float,
        *,
        date_from: str | None = None,
        date_to: str | None = None,
        staff_id: int | None = None,
        position_id: int | None = None,
        user_id: int | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> list[AnalyticsReportOverallChartDailyRow2]:
        """Получить данные о выручке в разрезе по дням
        """
        return await self._client.request(
            "GET",
            "/api/v1/company/{company_id}/analytics/overall/charts/income_daily/",
            path_params={"company_id": company_id},
            params={"date_from": date_from, "date_to": date_to, "staff_id": staff_id, "position_id": position_id, "user_id": user_id},
            response_model=list[AnalyticsReportOverallChartDailyRow2],
            extra_query=extra_query,
        )

    async def list_records_daily(
        self,
        company_id: float,
        *,
        date_from: str | None = None,
        date_to: str | None = None,
        staff_id: int | None = None,
        user_id: int | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> list[AnalyticsReportOverallChartDailyRow2]:
        """Получить данные о количестве записей в разрезе по дням
        """
        return await self._client.request(
            "GET",
            "/api/v1/company/{company_id}/analytics/overall/charts/records_daily/",
            path_params={"company_id": company_id},
            params={"date_from": date_from, "date_to": date_to, "staff_id": staff_id, "user_id": user_id},
            response_model=list[AnalyticsReportOverallChartDailyRow2],
            extra_query=extra_query,
        )

    async def list_fullness_daily(
        self,
        company_id: float,
        *,
        date_from: str | None = None,
        date_to: str | None = None,
        staff_id: int | None = None,
        user_id: int | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> list[AnalyticsReportOverallChartDailyRow2]:
        """Получить данные о заполненности в разрезе по дням
        """
        return await self._client.request(
            "GET",
            "/api/v1/company/{company_id}/analytics/overall/charts/fullness_daily/",
            path_params={"company_id": company_id},
            params={"date_from": date_from, "date_to": date_to, "staff_id": staff_id, "user_id": user_id},
            response_model=list[AnalyticsReportOverallChartDailyRow2],
            extra_query=extra_query,
        )

    async def list_record_source(
        self,
        company_id: float,
        *,
        date_from: str | None = None,
        date_to: str | None = None,
        staff_id: int | None = None,
        user_id: int | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> list[AnalyticsReportOverallChartScalarItem2]:
        """Получить структуру записей по источникам
        """
        return await self._client.request(
            "GET",
            "/api/v1/company/{company_id}/analytics/overall/charts/record_source/",
            path_params={"company_id": company_id},
            params={"date_from": date_from, "date_to": date_to, "staff_id": staff_id, "user_id": user_id},
            response_model=list[AnalyticsReportOverallChartScalarItem2],
            extra_query=extra_query,
        )

    async def list_record_status(
        self,
        company_id: float,
        *,
        date_from: str | None = None,
        date_to: str | None = None,
        staff_id: int | None = None,
        user_id: int | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> list[AnalyticsReportOverallChartScalarItem2]:
        """Получить структуру записей по статусам визитов
        """
        return await self._client.request(
            "GET",
            "/api/v1/company/{company_id}/analytics/overall/charts/record_status/",
            path_params={"company_id": company_id},
            params={"date_from": date_from, "date_to": date_to, "staff_id": staff_id, "user_id": user_id},
            response_model=list[AnalyticsReportOverallChartScalarItem2],
            extra_query=extra_query,
        )
