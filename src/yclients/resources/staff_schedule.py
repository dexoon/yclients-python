"""StaffScheduleApi -- сгенерированные методы API."""

from __future__ import annotations

from typing import Any, Literal

from yclients._base import BaseClient
from yclients.models.common import Page
from yclients.models.schemas import (
    GetStartDateEndDateResponse200,
    MasterScheduleDayContainer,
    PutStaffScheduleRequest,
)


class StaffScheduleApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def schedule(
        self,
        company_id: float,
        *,
        start_date: str | None = None,
        end_date: str | None = None,
        staff_ids: list[float] | None = None,
        include: list[Literal["busy_intervals", "off_day_type"]] | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> Page[MasterScheduleDayContainer]:
        """Получение графиков работы сотрудников
        Осуществляет поиск графиков сотрудников в виде рабочих интервалов с опциональным включением интервалов, занятых записями/событиями, а также типов нерабочих дней.
        """
        return await self._client.request(
            "GET",
            "/api/v1/company/{company_id}/staff/schedule",
            path_params={"company_id": company_id},
            params={"start_date": start_date, "end_date": end_date, "staff_ids": staff_ids, "include": include},
            response_model=Page[MasterScheduleDayContainer],
            extra_query=extra_query,
        )

    async def update(
        self,
        company_id: float,
        data: PutStaffScheduleRequest,
        extra_query: dict[str, Any] | None = None
    ) -> Page[MasterScheduleDayContainer]:
        """Установка графиков работы сотрудников
        Устанавливает графики работы сотрудников по заданным интервалам, после чего возвращает результирующие графики измененных сотрудников в интервале с минимальной измененной даты до максимальной.
        """
        return await self._client.request(
            "PUT",
            "/api/v1/company/{company_id}/staff/schedule",
            path_params={"company_id": company_id},
            json_body=data,
            response_model=Page[MasterScheduleDayContainer],
            extra_query=extra_query,
        )

    async def get(
        self,
        company_id: float,
        staff_id: float,
        start_date: str,
        end_date: str,
        extra_query: dict[str, Any] | None = None
    ) -> GetStartDateEndDateResponse200:
        """Устаревшее. Получить расписание сотрудника
        """
        return await self._client.request(
            "GET",
            "/api/v1/schedule/{company_id}/{staff_id}/{start_date}/{end_date}",
            path_params={"company_id": company_id, "staff_id": staff_id, "start_date": start_date, "end_date": end_date},
            response_model=GetStartDateEndDateResponse200,
            extra_query=extra_query,
        )

    async def update_company(
        self,
        company_id: float,
        staff_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Устаревшее. Изменить расписание работы сотрудника
        """
        return await self._client.request(
            "PUT",
            "/api/v1/schedule/{company_id}/{staff_id}",
            path_params={"company_id": company_id, "staff_id": staff_id},
            extra_query=extra_query,
        )
