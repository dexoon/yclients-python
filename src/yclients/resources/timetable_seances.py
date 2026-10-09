"""TimetableSeancesApi -- сгенерированные методы API."""

from __future__ import annotations

from typing import Any

from yclients._base import BaseClient
from yclients.models.schemas import GetStaffIdDateResponse200


class TimetableSeancesApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def get(
        self,
        company_id: float,
        staff_id: float,
        date: str,
        extra_query: dict[str, Any] | None = None
    ) -> GetStaffIdDateResponse200:
        """Получить список сеансов для журнала
        Объект сеансы для журнала имеет следующие поля:
        | Поле  | Тип | Описание |
        | ------------- | ------------- | ------------- |
        |  time  |  string   | Время сеанса (17:30 например)   |
        |  free  | boolean  | Свободно время или занято  |
        """
        return await self._client.request(
            "GET",
            "/api/v1/timetable/seances/{company_id}/{staff_id}/{date}",
            path_params={"company_id": company_id, "staff_id": staff_id, "date": date},
            response_model=GetStaffIdDateResponse200,
            extra_query=extra_query,
        )
