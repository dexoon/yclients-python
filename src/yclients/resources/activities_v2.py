"""ActivitiesV2Api -- сгенерированные методы API."""

from __future__ import annotations

from typing import Any

from yclients._base import BaseClient
from yclients.models.schemas import (
    PostActivityIdRecordsRequest,
    PostRecordsRecordIdRequest,
    PostSalonIdActivitiesRequest,
    PutActivitiesActivityIdRequest,
    TimetableActivityResponse,
    TimetableRecordResponse,
)


class ActivitiesV2Api:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def create(
        self,
        salon_id: str,
        data: PostSalonIdActivitiesRequest,
        extra_query: dict[str, Any] | None = None
    ) -> TimetableActivityResponse:
        """Создание события
        Создаёт групповое событие.
        """
        return await self._client.request(
            "POST",
            "/api/v2/companies/{salonId}/activities",
            path_params={"salonId": salon_id},
            json_body=data,
            response_model=TimetableActivityResponse,
            extra_query=extra_query,
        )

    async def get(
        self,
        salon_id: str,
        activity_id: str,
        extra_query: dict[str, Any] | None = None
    ) -> TimetableActivityResponse:
        """Чтение события
        Возвращает групповое событие.
        """
        return await self._client.request(
            "GET",
            "/api/v2/companies/{salonId}/activities/{activityId}",
            path_params={"salonId": salon_id, "activityId": activity_id},
            response_model=TimetableActivityResponse,
            extra_query=extra_query,
        )

    async def update(
        self,
        salon_id: str,
        activity_id: str,
        data: PutActivitiesActivityIdRequest,
        extra_query: dict[str, Any] | None = None
    ) -> TimetableActivityResponse:
        """Обновление события
        Обновляет групповое событие.
        """
        return await self._client.request(
            "PUT",
            "/api/v2/companies/{salonId}/activities/{activityId}",
            path_params={"salonId": salon_id, "activityId": activity_id},
            json_body=data,
            response_model=TimetableActivityResponse,
            extra_query=extra_query,
        )

    async def delete(
        self,
        salon_id: str,
        activity_id: str,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Удаление события
        Удаляет групповое событие.
        """
        return await self._client.request(
            "DELETE",
            "/api/v2/companies/{salonId}/activities/{activityId}",
            path_params={"salonId": salon_id, "activityId": activity_id},
            extra_query=extra_query,
        )

    async def create_record(
        self,
        salon_id: str,
        activity_id: str,
        data: PostActivityIdRecordsRequest,
        extra_query: dict[str, Any] | None = None
    ) -> TimetableRecordResponse:
        """Создание записи в событии
        Создаёт запись в групповом событии.
        """
        return await self._client.request(
            "POST",
            "/api/v2/companies/{salonId}/activities/{activityId}/records",
            path_params={"salonId": salon_id, "activityId": activity_id},
            json_body=data,
            response_model=TimetableRecordResponse,
            extra_query=extra_query,
        )

    async def create_records(
        self,
        salon_id: str,
        activity_id: str,
        record_id: str,
        data: PostRecordsRecordIdRequest,
        extra_query: dict[str, Any] | None = None
    ) -> TimetableRecordResponse:
        """Создание записи в событии
        Создаёт запись в групповом событии.
        """
        return await self._client.request(
            "POST",
            "/api/v2/companies/{salonId}/activities/{activityId}/records/{recordId}",
            path_params={"salonId": salon_id, "activityId": activity_id, "recordId": record_id},
            json_body=data,
            response_model=TimetableRecordResponse,
            extra_query=extra_query,
        )
