"""WaitingListApi -- сгенерированные методы API."""

from __future__ import annotations

import builtins
from typing import Any

from yclients._base import BaseClient
from yclients.models.schemas import (
    ApiV2CompanyWaitingListCreateResponse,
    ApiV2CompanyWaitingListGetResponse,
    PostCompanyIdWaitingListRequest,
    PutWaitingListWaitingListEntryIdRequest,
)


class WaitingListApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def list(
        self,
        company_id: float,
        *,
        include: builtins.list[str] | None = None,
        filter_status: str | None = None,
        filter_date: str | None = None,
        filter_client_phone: float | None = None,
        filter_client_name: str | None = None,
        sort: str | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> ApiV2CompanyWaitingListGetResponse:
        """Получить заявки в листе ожидания
        """
        return await self._client.request(
            "GET",
            "/api/v2/companies/{company_id}/waiting_list",
            path_params={"company_id": company_id},
            params={"include[]": include, "filter[status]": filter_status, "filter[date]": filter_date, "filter[client_phone]": filter_client_phone, "filter[client_name]": filter_client_name, "sort": sort},
            response_model=ApiV2CompanyWaitingListGetResponse,
            extra_query=extra_query,
        )

    async def create(
        self,
        company_id: float,
        data: PostCompanyIdWaitingListRequest,
        extra_query: dict[str, Any] | None = None
    ) -> ApiV2CompanyWaitingListCreateResponse:
        """Создание заявки в листе ожидания
        """
        return await self._client.request(
            "POST",
            "/api/v2/companies/{company_id}/waiting_list",
            path_params={"company_id": company_id},
            json_body=data,
            response_model=ApiV2CompanyWaitingListCreateResponse,
            extra_query=extra_query,
        )

    async def update(
        self,
        company_id: float,
        waiting_list_entry_id: str,
        data: PutWaitingListWaitingListEntryIdRequest,
        extra_query: dict[str, Any] | None = None
    ) -> ApiV2CompanyWaitingListCreateResponse:
        """Обновление заявки в листе ожидания
        """
        return await self._client.request(
            "PUT",
            "/api/v2/companies/{company_id}/waiting_list/{waiting_list_entry_id}",
            path_params={"company_id": company_id, "waiting_list_entry_id": waiting_list_entry_id},
            json_body=data,
            response_model=ApiV2CompanyWaitingListCreateResponse,
            extra_query=extra_query,
        )

    async def delete(
        self,
        company_id: float,
        waiting_list_entry_id: str,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Удаление заявки в листе ожидания
        """
        return await self._client.request(
            "DELETE",
            "/api/v2/companies/{company_id}/waiting_list/{waiting_list_entry_id}",
            path_params={"company_id": company_id, "waiting_list_entry_id": waiting_list_entry_id},
            extra_query=extra_query,
        )
