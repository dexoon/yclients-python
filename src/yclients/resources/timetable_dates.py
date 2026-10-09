"""TimetableDatesApi -- сгенерированные методы API."""

from __future__ import annotations

from typing import Any

from yclients._base import BaseClient


class TimetableDatesApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def get(
        self,
        company_id: float,
        date: str,
        *,
        staff_id: float | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Получить список дат для журнала
        Даты для журнала представляют из себя массив с датами. (например ["2015-10-26", "2015-10-30"]).Для получения дат нужно передать дату, относительно которой будут получен список рабочих дат салона/сотрудника.
        """
        return await self._client.request(
            "GET",
            "/api/v1/timetable/dates/{company_id}/{date}",
            path_params={"company_id": company_id, "date": date},
            params={"staff_id": staff_id},
            extra_query=extra_query,
        )
