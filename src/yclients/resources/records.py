"""RecordsApi -- сгенерированные методы API."""

from __future__ import annotations

import builtins
from typing import Any

from yclients._base import BaseClient
from yclients.models.schemas import (
    RecordCompanyidResponse201DataTypesData,
    RecordCompanyidResponseDataTypesData,
    RecordsCompanyidRequestDataTypes,
    RecordsCompanyidResponseDataTypesDataItem,
)


class RecordsApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def list(
        self,
        company_id: float,
        *,
        page_: float | None = None,
        count_: float | None = None,
        staff_id: float | None = None,
        client_id: float | None = None,
        created_user_id: float | None = None,
        start_date: Any | None = None,
        end_date: Any | None = None,
        c_start_date: Any | None = None,
        c_end_date: Any | None = None,
        changed_after: Any | None = None,
        changed_before: Any | None = None,
        include_consumables: float | None = None,
        include_finance_transactions: float | None = None,
        with_deleted: bool | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[RecordsCompanyidResponseDataTypesDataItem]:
        """Получить список записей
        """
        return await self._client.request(
            "GET",
            "/api/v1/records/{company_id}",
            path_params={"company_id": company_id},
            params={"page": page_, "count": count_, "staff_id": staff_id, "client_id": client_id, "created_user_id": created_user_id, "start_date": start_date, "end_date": end_date, "c_start_date": c_start_date, "c_end_date": c_end_date, "changed_after": changed_after, "changed_before": changed_before, "include_consumables": include_consumables, "include_finance_transactions": include_finance_transactions, "with_deleted": with_deleted},
            response_model=builtins.list[RecordsCompanyidResponseDataTypesDataItem],
            extra_query=extra_query,
        )

    async def create(
        self,
        company_id: float,
        data: RecordsCompanyidRequestDataTypes,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[RecordsCompanyidResponseDataTypesDataItem]:
        """Создать новую запись
        Для групповых событий
        При создании записи в групповом событии параметр activity_id становится обязательным,
        параметры staff_id, services, datetime, seance_length становятся необязательными.
        Дополнительные поля
        При создании дополнительных полей записи(см. раздел "Дополнительные поля") становится возможным передавать собственные значения для полей.
        Дополнительные поля уникальны для каждой компании. После создания дополнительных полей, их значения для конкретной записи могут
        передаваться в необязательном поле custom_fields в виде пар ключ-значение где ключ это поле "code" дополнительного поля. Пример:
        * Создали дополнительное поле записи с code="my_custom_field" type="number", и второе поле code="some_another_field" type="list"
        * Передали при создании записи еще один атрибут:
        custom_fields: {
        "my_custom_field": 123,
        "some_another_field": ["first value", "second value"]
        }
        """
        return await self._client.request(
            "POST",
            "/api/v1/records/{company_id}",
            path_params={"company_id": company_id},
            json_body=data,
            response_model=builtins.list[RecordsCompanyidResponseDataTypesDataItem],
            extra_query=extra_query,
        )

    async def get_partner(
        self,
        *,
        page_: float | None = None,
        editable_length: float | None = None,
        salon_id: float | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        created_start_date: str | None = None,
        created_end_date: str | None = None,
        user_id: float | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Получить список записей партнёра
        """
        return await self._client.request(
            "GET",
            "/api/v1/records/partner/",
            params={"page": page_, "editable_length": editable_length, "salon_id": salon_id, "start_date": start_date, "end_date": end_date, "created_start_date": created_start_date, "created_end_date": created_end_date, "user_id": user_id},
            extra_query=extra_query,
        )

    async def get(
        self,
        company_id: float,
        record_id: float,
        *,
        include_consumables: float | None = None,
        include_finance_transactions: float | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> RecordCompanyidResponseDataTypesData:
        """Получить запись
        """
        return await self._client.request(
            "GET",
            "/api/v1/record/{company_id}/{record_id}",
            path_params={"company_id": company_id, "record_id": record_id},
            params={"include_consumables": include_consumables, "include_finance_transactions": include_finance_transactions},
            response_model=RecordCompanyidResponseDataTypesData,
            extra_query=extra_query,
        )

    async def update(
        self,
        company_id: float,
        record_id: float,
        data: RecordsCompanyidRequestDataTypes,
        *,
        include_consumables: float | None = None,
        include_finance_transactions: float | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> RecordCompanyidResponse201DataTypesData:
        """Изменить запись
        При изменении записи в групповом событии параметр activity_id становится обязательным,
        параметры staff_id, services, datetime, seance_length становятся необязательными
        """
        return await self._client.request(
            "PUT",
            "/api/v1/record/{company_id}/{record_id}",
            path_params={"company_id": company_id, "record_id": record_id},
            params={"include_consumables": include_consumables, "include_finance_transactions": include_finance_transactions},
            json_body=data,
            response_model=RecordCompanyidResponse201DataTypesData,
            extra_query=extra_query,
        )

    async def delete(
        self,
        company_id: float,
        record_id: float,
        *,
        include_consumables: float | None = None,
        include_finance_transactions: float | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Удалить запись
        """
        return await self._client.request(
            "DELETE",
            "/api/v1/record/{company_id}/{record_id}",
            path_params={"company_id": company_id, "record_id": record_id},
            params={"include_consumables": include_consumables, "include_finance_transactions": include_finance_transactions},
            extra_query=extra_query,
        )
