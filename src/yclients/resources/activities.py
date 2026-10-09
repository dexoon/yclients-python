"""ActivitiesApi -- сгенерированные методы API."""

from __future__ import annotations

from typing import Any

from yclients._base import BaseClient
from yclients.models.common import Page
from yclients.models.schemas import (
    ActivityCompanyidRequestDataTypes,
    ActivityCompanyidResponseDataTypesData,
    ActivityCompanyidSearchResponseDataTypesDataItem,
    ActivityCompanyidServicesRequestDataTypes,
    ActivityCompanyidServicesResponseDataTypesDataItem,
    ActivityDatesRange,
    ActivityFilter,
)


class ActivitiesApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def create(
        self,
        company_id: float,
        data: ActivityCompanyidRequestDataTypes,
        extra_query: dict[str, Any] | None = None
    ) -> ActivityCompanyidResponseDataTypesData:
        """Создание группового события
        """
        return await self._client.request(
            "POST",
            "/api/v1/activity/{company_id}",
            path_params={"company_id": company_id},
            json_body=data,
            response_model=ActivityCompanyidResponseDataTypesData,
            extra_query=extra_query,
        )

    async def get(
        self,
        company_id: float,
        activity_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> ActivityCompanyidResponseDataTypesData:
        """Чтение группового события
        """
        return await self._client.request(
            "GET",
            "/api/v1/activity/{company_id}/{activity_id}",
            path_params={"company_id": company_id, "activity_id": activity_id},
            response_model=ActivityCompanyidResponseDataTypesData,
            extra_query=extra_query,
        )

    async def update(
        self,
        company_id: float,
        activity_id: float,
        data: ActivityCompanyidRequestDataTypes,
        extra_query: dict[str, Any] | None = None
    ) -> ActivityCompanyidResponseDataTypesData:
        """Обновление группового события
        """
        return await self._client.request(
            "PUT",
            "/api/v1/activity/{company_id}/{activity_id}",
            path_params={"company_id": company_id, "activity_id": activity_id},
            json_body=data,
            response_model=ActivityCompanyidResponseDataTypesData,
            extra_query=extra_query,
        )

    async def delete(
        self,
        company_id: float,
        activity_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Удаление группового события
        """
        return await self._client.request(
            "DELETE",
            "/api/v1/activity/{company_id}/{activity_id}",
            path_params={"company_id": company_id, "activity_id": activity_id},
            extra_query=extra_query,
        )

    async def filters(
        self,
        company_id: float,
        *,
        service_ids: list[int] | None = None,
        staff_ids: list[int] | None = None,
        resource_ids: list[int] | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> Page[ActivityFilter]:
        """Фильтры групповых событий
        """
        return await self._client.request(
            "GET",
            "/api/v1/activity/{company_id}/filters/",
            path_params={"company_id": company_id},
            params={"service_ids": service_ids, "staff_ids": staff_ids, "resource_ids": resource_ids},
            response_model=Page[ActivityFilter],
            extra_query=extra_query,
        )

    async def get_search_dates_range(
        self,
        company_id: float,
        *,
        service_ids: list[int] | None = None,
        staff_ids: list[int] | None = None,
        resource_ids: list[int] | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> ActivityDatesRange:
        """Поиск диапазона дат групповых событий
        """
        return await self._client.request(
            "GET",
            "/api/v1/activity/{company_id}/search_dates_range/",
            path_params={"company_id": company_id},
            params={"service_ids": service_ids, "staff_ids": staff_ids, "resource_ids": resource_ids},
            response_model=ActivityDatesRange,
            extra_query=extra_query,
        )

    async def get_search_dates(
        self,
        company_id: float,
        *,
        from_: str | None = None,
        till: str | None = None,
        service_ids: list[int] | None = None,
        staff_ids: list[int] | None = None,
        resource_ids: list[int] | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Поиск дат групповых событий
        """
        return await self._client.request(
            "GET",
            "/api/v1/activity/{company_id}/search_dates/",
            path_params={"company_id": company_id},
            params={"from": from_, "till": till, "service_ids": service_ids, "staff_ids": staff_ids, "resource_ids": resource_ids},
            extra_query=extra_query,
        )

    async def search(
        self,
        company_id: float,
        *,
        from_: str | None = None,
        till: str | None = None,
        service_ids: list[int] | None = None,
        staff_ids: list[int] | None = None,
        resource_ids: list[int] | None = None,
        page_: float | None = None,
        count_: float | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> list[ActivityCompanyidSearchResponseDataTypesDataItem]:
        """Поиск групповых событий
        """
        return await self._client.request(
            "GET",
            "/api/v1/activity/{company_id}/search/",
            path_params={"company_id": company_id},
            params={"from": from_, "till": till, "service_ids": service_ids, "staff_ids": staff_ids, "resource_ids": resource_ids, "page": page_, "count": count_},
            response_model=list[ActivityCompanyidSearchResponseDataTypesDataItem],
            extra_query=extra_query,
        )

    async def list_services(
        self,
        company_id: float,
        data: ActivityCompanyidServicesRequestDataTypes,
        *,
        staff_id: float | None = None,
        term: str | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> list[ActivityCompanyidServicesResponseDataTypesDataItem]:
        """Поиск групповых услуг
        """
        return await self._client.request(
            "GET",
            "/api/v1/activity/{company_id}/services",
            path_params={"company_id": company_id},
            params={"staff_id": staff_id, "term": term},
            json_body=data,
            response_model=list[ActivityCompanyidServicesResponseDataTypesDataItem],
            extra_query=extra_query,
        )

    async def duplication_strategy(
        self,
        company_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Получение стратегий дублирования групповых событий
        Дублирование событий происходит на основе набора параметров, объединенных в сущность "стратегия дублирования"
        | Поле          | Тип           | Описание                                  |
        | ------------- | ------------- | ----------------------------------------- |
        | title         | string        | Название стратегии                        |
        | repeat_mode_id| integer       | Режим повторения                          |
        | days          | integer[]     | Перечень дней недели: 0 вс, 6 пт          |
        | interval      | integer       | Перерыв в поиске дат, в единицах типа     |
        | content_type  | integer       | Дублировать записи? 1 - нет, 2 - да       |
        Режим повторения может принимать значения
        | Значение | Описание | Единица измерения перерыва  |
        | -------- | ------------- | ----------------------------- |
        | 1 | Ежедневно     | День                          |
        | 2 | По будням     | -                             |
        """
        return await self._client.request(
            "GET",
            "/api/v1/activity/{company_id}/duplication_strategy",
            path_params={"company_id": company_id},
            extra_query=extra_query,
        )

    async def create_duplication_strategy(
        self,
        company_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Создание шаблона дублирования группового события
        """
        return await self._client.request(
            "POST",
            "/api/v1/activity/{company_id}/duplication_strategy",
            path_params={"company_id": company_id},
            extra_query=extra_query,
        )

    async def update_duplication_strategy(
        self,
        company_id: float,
        strategy_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Обновление шаблона дублирования группового события
        """
        return await self._client.request(
            "POST",
            "/api/v1/activity/{company_id}/duplication_strategy/{strategy_id}",
            path_params={"company_id": company_id, "strategy_id": strategy_id},
            extra_query=extra_query,
        )

    async def duplicate(
        self,
        company_id: float,
        activity_id: float,
        data: dict[str, Any],
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Запрос дублирования группового события
        Запрос на дублирование можно оформить 3 способами:
        - Указав список дат и времени для дублирования
        - Указав id стратегии повторения
        - Указав все параметры повторения
        """
        return await self._client.request(
            "POST",
            "/api/v1/activity/{company_id}/{activity_id}/duplicate/",
            path_params={"company_id": company_id, "activity_id": activity_id},
            json_body=data,
            extra_query=extra_query,
        )
