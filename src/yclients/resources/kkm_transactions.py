"""KkmTransactionsApi -- сгенерированные методы API."""

from __future__ import annotations

import builtins
from typing import Any

from yclients._base import BaseClient
from yclients.models.schemas import (
    KkmTransactionsPrintResponseDataTypeData,
    KkmTransactionsResponseDataTypeDataItem,
)


class KkmTransactionsApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def list(
        self,
        company_id: float,
        *,
        page_: float | None = None,
        editable_length: float | None = None,
        type_: float | None = None,
        status: float | None = None,
        start_date: float | None = None,
        end_date: float | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[KkmTransactionsResponseDataTypeDataItem]:
        """Получить транзакции
        Фильтры
        | Параметр  | Описание |
        | ------------- | ------------- |
        |  page  | Номер страницы |
        |  editable_length  | Количество клиентов на странице |
        |  type  | Тип операции |
        |  status  | Статус операции |
        |  start_date  | Дата начала периода |
        |  end_date  | Дата окончания периода |
        <a name="kkm-transaction-types"></a>
        Типы всех операций c ККМ
        | Значение  | Описание |
        | ------------- | ------------- |
        """
        return await self._client.request(
            "GET",
            "/api/v1/kkm_transactions/{company_id}",
            path_params={"company_id": company_id},
            params={"page": page_, "editable_length": editable_length, "type": type_, "status": status, "start_date": start_date, "end_date": end_date},
            response_model=builtins.list[KkmTransactionsResponseDataTypeDataItem],
            extra_query=extra_query,
        )

    async def print_bill(
        self,
        company_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> KkmTransactionsPrintResponseDataTypeData:
        """Напечатать чек
        Типы всех операций c ККМ
        | Значение  | Описание |
        | ------------- | ------------- |
        |  0  | Операция продажи  (активна для документов с типами "Визит" и "Пополнение депозита") |
        |  1  | Операция возврата продажи (активна для документов с типами "Визит" и "Пополнение депозита") |
        |  2  | Операция коррекции |
        |  4  | Операция открытия смены |
        |  5  | Операция закрытия смены |
        |  9  | Операция получения статуса ККМ  |
        |  11  | Операция получения статуса команды ККМ |
        |  12  | Операция коррекции |
        |  13  | Печать X-отчёта |
        |  6  | Внесение наличных |
        """
        return await self._client.request(
            "POST",
            "/api/v1/kkm_transactions/{company_id}/print_document_bill",
            path_params={"company_id": company_id},
            response_model=KkmTransactionsPrintResponseDataTypeData,
            extra_query=extra_query,
        )
