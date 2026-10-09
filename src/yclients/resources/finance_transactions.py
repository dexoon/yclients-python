"""FinanceTransactionsApi -- сгенерированные методы API."""

from __future__ import annotations

import builtins
from typing import Any

from yclients._base import BaseClient
from yclients.models.schemas import FinanceTransactionRequestDataTypes


class FinanceTransactionsApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def list(
        self,
        company_id: float,
        *,
        page_: float | None = None,
        count_: float | None = None,
        account_id: float | None = None,
        supplier_id: float | None = None,
        client_id: float | None = None,
        user_id: float | None = None,
        master_id: float | None = None,
        type_: float | None = None,
        real_money: float | None = None,
        deleted: float | None = None,
        start_date: float | None = None,
        end_date: float | None = None,
        balance_is: float | None = None,
        document_id: float | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[dict[str, Any]]:
        """Получить транзакции
        """
        return await self._client.request(
            "GET",
            "/api/v1/transactions/{company_id}",
            path_params={"company_id": company_id},
            params={"page": page_, "count": count_, "account_id": account_id, "supplier_id": supplier_id, "client_id": client_id, "user_id": user_id, "master_id": master_id, "type": type_, "real_money": real_money, "deleted": deleted, "start_date": start_date, "end_date": end_date, "balance_is": balance_is, "document_id": document_id},
            response_model=builtins.list[dict[str, Any]],
            extra_query=extra_query,
        )

    async def list_timetable(
        self,
        company_id: float,
        *,
        record_id: float | None = None,
        visit_id: float | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[dict[str, Any]]:
        """Получение транзакций по ID визита или записи
        """
        return await self._client.request(
            "GET",
            "/api/v1/timetable/transactions/{company_id}",
            path_params={"company_id": company_id},
            params={"record_id": record_id, "visit_id": visit_id},
            response_model=builtins.list[dict[str, Any]],
            extra_query=extra_query,
        )

    async def create(
        self,
        company_id: float,
        data: FinanceTransactionRequestDataTypes,
        extra_query: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Создание финансовой транзакции
        """
        return await self._client.request(
            "POST",
            "/api/v1/finance_transactions/{company_id}",
            path_params={"company_id": company_id},
            json_body=data,
            response_model=dict[str, Any],
            extra_query=extra_query,
        )

    async def get(
        self,
        company_id: float,
        transaction_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[dict[str, Any]]:
        """Получение финансовой транзакции
        """
        return await self._client.request(
            "GET",
            "/api/v1/finance_transactions/{company_id}/{transaction_id}",
            path_params={"company_id": company_id, "transaction_id": transaction_id},
            response_model=builtins.list[dict[str, Any]],
            extra_query=extra_query,
        )

    async def update(
        self,
        company_id: float,
        transaction_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[dict[str, Any]]:
        """Обновление финансовой транзакции
        """
        return await self._client.request(
            "PUT",
            "/api/v1/finance_transactions/{company_id}/{transaction_id}",
            path_params={"company_id": company_id, "transaction_id": transaction_id},
            response_model=builtins.list[dict[str, Any]],
            extra_query=extra_query,
        )

    async def delete(
        self,
        company_id: float,
        transaction_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Удаление транзакции
        """
        return await self._client.request(
            "DELETE",
            "/api/v1/finance_transactions/{company_id}/{transaction_id}",
            path_params={"company_id": company_id, "transaction_id": transaction_id},
            extra_query=extra_query,
        )
