"""SchedulesApi -- сгенерированные методы API."""

from __future__ import annotations

from typing import Any, Literal

from yclients._base import BaseClient
from yclients.models.common import Page
from yclients.models.schemas import (
    GetAbonementIdCheckForActivityResponse200,
    GetAbonementsSearchForActivityResponse200,
    PatchClientSchedulesClientScheduleIdRequest,
    PatchDaysDayIdRequest,
    PatchSchedulesScheduleIdRequest,
    PostCompanyIdSchedulesRequest,
    PostScheduleIdClientSchedulesRequest,
    PostScheduleIdDaysRequest,
    TimetableEventSchedule2,
    TimetableEventScheduleClientSchedule,
    TimetableEventScheduleDay2,
    TimetableEventScheduleEvent2,
)


class SchedulesApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def get(
        self,
        company_id: float,
        entity_type: str,
        entity_id: float,
        *,
        include: list[Literal["days", "days.events_master", "days.events_labels", "days.events_resource_instances"]] | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> TimetableEventSchedule2:
        """Поиск расписания по сущности
        Осуществляет поиск расписания по записи или событию, принадлежащему расписанию или на основе которого расписание было построено.
        """
        return await self._client.request(
            "GET",
            "/api/v1/company/{company_id}/schedules/search/{entity_type}/{entity_id}",
            path_params={"company_id": company_id, "entity_type": entity_type, "entity_id": entity_id},
            params={"include": include},
            response_model=TimetableEventSchedule2,
            extra_query=extra_query,
        )

    async def create(
        self,
        company_id: float,
        data: PostCompanyIdSchedulesRequest,
        *,
        include: list[Literal["days"]] | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> TimetableEventSchedule2:
        """Создание расписания
        Создает расписание записей или событий, основываясь на исходной записи или событии.
        """
        return await self._client.request(
            "POST",
            "/api/v1/company/{company_id}/schedules",
            path_params={"company_id": company_id},
            params={"include": include},
            json_body=data,
            response_model=TimetableEventSchedule2,
            extra_query=extra_query,
        )

    async def update(
        self,
        company_id: float,
        schedule_id: float,
        data: PatchSchedulesScheduleIdRequest,
        extra_query: dict[str, Any] | None = None
    ) -> TimetableEventSchedule2:
        """Обновление расписания
        Обновляет настройки расписания записей или событий.
        """
        return await self._client.request(
            "PATCH",
            "/api/v1/company/{company_id}/schedules/{schedule_id}",
            path_params={"company_id": company_id, "schedule_id": schedule_id},
            json_body=data,
            response_model=TimetableEventSchedule2,
            extra_query=extra_query,
        )

    async def delete(
        self,
        company_id: float,
        schedule_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Удаление расписания
        Полностью удаляет расписание и все записи или события, привязанные к нему.
        """
        return await self._client.request(
            "DELETE",
            "/api/v1/company/{company_id}/schedules/{schedule_id}",
            path_params={"company_id": company_id, "schedule_id": schedule_id},
            response_model=dict[str, Any],
            extra_query=extra_query,
        )

    async def create_day(
        self,
        company_id: float,
        schedule_id: float,
        data: PostScheduleIdDaysRequest,
        *,
        include: list[Literal["events_master", "events_labels", "events_resource_instances", "events"]] | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> TimetableEventScheduleDay2:
        """Создание серии расписания
        Добавляет к существующему расписанию записей или событий новую серию.
        """
        return await self._client.request(
            "POST",
            "/api/v1/company/{company_id}/schedules/{schedule_id}/days",
            path_params={"company_id": company_id, "schedule_id": schedule_id},
            params={"include": include},
            json_body=data,
            response_model=TimetableEventScheduleDay2,
            extra_query=extra_query,
        )

    async def update_days(
        self,
        company_id: float,
        schedule_id: float,
        day_id: float,
        data: PatchDaysDayIdRequest,
        *,
        include: list[Literal["events_master", "events_labels", "events_resource_instances", "events"]] | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> TimetableEventScheduleDay2:
        """Обновление серии расписания
        Обновляет настройки серии расписания записей или событий.
        """
        return await self._client.request(
            "PATCH",
            "/api/v1/company/{company_id}/schedules/{schedule_id}/days/{day_id}",
            path_params={"company_id": company_id, "schedule_id": schedule_id, "day_id": day_id},
            params={"include": include},
            json_body=data,
            response_model=TimetableEventScheduleDay2,
            extra_query=extra_query,
        )

    async def delete_days(
        self,
        company_id: float,
        schedule_id: float,
        day_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Удаление серии расписания
        Полностью удаляет серию расписания и все записи или события, привязанные к нему.
        """
        return await self._client.request(
            "DELETE",
            "/api/v1/company/{company_id}/schedules/{schedule_id}/days/{day_id}",
            path_params={"company_id": company_id, "schedule_id": schedule_id, "day_id": day_id},
            response_model=dict[str, Any],
            extra_query=extra_query,
        )

    async def list_events(
        self,
        company_id: float,
        schedule_id: float,
        day_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> Page[TimetableEventScheduleEvent2]:
        """Получение списка сущностей записей/событий в рамках серии расписания
        Выводит список сущностей записей или событий, созданных в рамках серии расписания.
        """
        return await self._client.request(
            "GET",
            "/api/v1/company/{company_id}/schedules/{schedule_id}/days/{day_id}/events",
            path_params={"company_id": company_id, "schedule_id": schedule_id, "day_id": day_id},
            response_model=Page[TimetableEventScheduleEvent2],
            extra_query=extra_query,
        )

    async def create_client_schedule(
        self,
        company_id: float,
        schedule_id: float,
        data: PostScheduleIdClientSchedulesRequest,
        extra_query: dict[str, Any] | None = None
    ) -> TimetableEventScheduleClientSchedule:
        """Создание графика посещений клиента
        Создает график посещений клиента, представляющий собой набор записей на события расписания.
        """
        return await self._client.request(
            "POST",
            "/api/v1/company/{company_id}/schedules/{schedule_id}/client_schedules",
            path_params={"company_id": company_id, "schedule_id": schedule_id},
            json_body=data,
            response_model=TimetableEventScheduleClientSchedule,
            extra_query=extra_query,
        )

    async def update_client_schedules(
        self,
        company_id: float,
        schedule_id: float,
        client_schedule_id: float,
        data: PatchClientSchedulesClientScheduleIdRequest,
        extra_query: dict[str, Any] | None = None
    ) -> TimetableEventScheduleClientSchedule:
        """Обновление графика посещений клиента
        Обновляет график посещений клиента, прикрепляя или открепляя серии расписания, что вызывает создание новых или удаление существующих записей клиента в будущих событиях расписания.
        """
        return await self._client.request(
            "PATCH",
            "/api/v1/company/{company_id}/schedules/{schedule_id}/client_schedules/{client_schedule_id}",
            path_params={"company_id": company_id, "schedule_id": schedule_id, "client_schedule_id": client_schedule_id},
            json_body=data,
            response_model=TimetableEventScheduleClientSchedule,
            extra_query=extra_query,
        )

    async def delete_client_schedules(
        self,
        company_id: float,
        schedule_id: float,
        client_schedule_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Удаление графика посещений клиента
        Полностью удаляет график посещений клиента и все записи данного клиента в рамках будущих событий расписания.
        """
        return await self._client.request(
            "DELETE",
            "/api/v1/company/{company_id}/schedules/{schedule_id}/client_schedules/{client_schedule_id}",
            path_params={"company_id": company_id, "schedule_id": schedule_id, "client_schedule_id": client_schedule_id},
            response_model=dict[str, Any],
            extra_query=extra_query,
        )

    async def get_search_for_activity(
        self,
        company_id: float,
        client_id: float,
        *,
        activity_id: float | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> GetAbonementsSearchForActivityResponse200:
        """Чтение доступных абонементов
        Получает абонементы, по которым можно создать расписание клиента на серию событий
        """
        return await self._client.request(
            "GET",
            "/api/v1/company/{company_id}/client/{client_id}/loyalty/abonements/search_for_activity/",
            path_params={"company_id": company_id, "client_id": client_id},
            params={"activity_id": activity_id},
            response_model=GetAbonementsSearchForActivityResponse200,
            extra_query=extra_query,
        )

    async def get_check_for_activity(
        self,
        company_id: float,
        client_id: float,
        abonement_id: str,
        *,
        activity_id: float | None = None,
        schedule_day_ids: Any | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> GetAbonementIdCheckForActivityResponse200:
        """Проверка абонемента на количество доступных записей и последнюю дату записи
        Метод возвращает дату последней возможной записи в расписании и количество посещений по выбранному абонементу
        """
        return await self._client.request(
            "GET",
            "/api/v1/company/{company_id}/client/{client_id}/loyalty/abonements/{abonement_id}/check_for_activity/",
            path_params={"company_id": company_id, "client_id": client_id, "abonement_id": abonement_id},
            params={"activity_id": activity_id, "schedule_day_ids": schedule_day_ids},
            response_model=GetAbonementIdCheckForActivityResponse200,
            extra_query=extra_query,
        )
