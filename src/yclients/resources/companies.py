"""CompaniesApi -- сгенерированные методы API."""

from __future__ import annotations

import builtins
from typing import Any, Literal

from yclients._base import BaseClient
from yclients.models.schemas import (
    CompanyCreateRequestDataTypes,
    CompanyPutRequestDataTypes,
    CompanyPutResponseDataTypes,
)


class CompaniesApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def list(
        self,
        *,
        id_: float | None = None,
        group_id: float | None = None,
        my: float | None = None,
        active: float | None = None,
        moderated: float | None = None,
        for_booking: float | None = None,
        show_groups: float | None = None,
        city_id: float | None = None,
        show_bookforms: float | None = None,
        vk_api_id: float | None = None,
        min_id: float | None = None,
        show_deleted: float | None = None,
        hide_record_type_single: float | None = None,
        hide_record_type_activity: float | None = None,
        hide_record_type_mixed: float | None = None,
        business_group_id: float | None = None,
        business_type_id: float | None = None,
        yandex: float | None = None,
        include: builtins.list[Literal["staff", "positions", "accounts", "storages", "expenses"]] | None = None,
        count_: float | None = None,
        page_: float | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[dict[str, Any]]:
        """Получить список компаний
        Получить список с данными о компаниях
        """
        return await self._client.request(
            "GET",
            "/api/v1/companies",
            params={"id": id_, "group_id": group_id, "my": my, "active": active, "moderated": moderated, "forBooking": for_booking, "show_groups": show_groups, "city_id": city_id, "showBookforms": show_bookforms, "vk_api_id": vk_api_id, "min_id": min_id, "show_deleted": show_deleted, "hide_record_type_single": hide_record_type_single, "hide_record_type_activity": hide_record_type_activity, "hide_record_type_mixed": hide_record_type_mixed, "business_group_id": business_group_id, "business_type_id": business_type_id, "yandex": yandex, "include": include, "count": count_, "page": page_},
            response_model=builtins.list[dict[str, Any]],
            extra_query=extra_query,
        )

    async def create(
        self,
        data: CompanyCreateRequestDataTypes,
        extra_query: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Создать компанию
        Создать новую компанию.
        """
        return await self._client.request(
            "POST",
            "/api/v1/companies",
            json_body=data,
            response_model=dict[str, Any],
            extra_query=extra_query,
        )

    async def get(
        self,
        id_: float,
        *,
        my: float | None = None,
        for_booking: float | None = None,
        show_groups: float | None = None,
        show_bookforms: float | None = None,
        bookform_id: float | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Получить компанию
        Получение данных о компании.
        """
        return await self._client.request(
            "GET",
            "/api/v1/company/{id}/",
            path_params={"id": id_},
            params={"my": my, "forBooking": for_booking, "show_groups": show_groups, "showBookforms": show_bookforms, "bookform_id": bookform_id},
            response_model=dict[str, Any],
            extra_query=extra_query,
        )

    async def update(
        self,
        id_: float,
        data: CompanyPutRequestDataTypes,
        extra_query: dict[str, Any] | None = None
    ) -> CompanyPutResponseDataTypes:
        """Изменить компанию
        Изменение данных о компании.
        """
        return await self._client.request(
            "PUT",
            "/api/v1/company/{id}/",
            path_params={"id": id_},
            json_body=data,
            response_model=CompanyPutResponseDataTypes,
            extra_query=extra_query,
        )

    async def delete(
        self,
        id_: float,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Удалить компанию
        Удаление компании.
        """
        return await self._client.request(
            "DELETE",
            "/api/v1/company/{id}/",
            path_params={"id": id_},
            extra_query=extra_query,
        )
