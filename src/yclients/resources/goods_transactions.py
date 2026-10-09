"""GoodsTransactionsApi -- сгенерированные методы API."""

from __future__ import annotations

import builtins
from typing import Any

from yclients._base import BaseClient
from yclients.models.schemas import (
    StorageOperationGoodTransactionRequestDataTypes,
    StorageOperationGoodTransactionResponse200DataTypesData,
    StoragesTransactionResponseDataTypesDataItem,
)


class GoodsTransactionsApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def list(
        self,
        company_id: float,
        *,
        page_: float | None = None,
        count_: float | None = None,
        start_date: Any | None = None,
        end_date: Any | None = None,
        document_id: str | None = None,
        changed_after: Any | None = None,
        changed_before: Any | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[StoragesTransactionResponseDataTypesDataItem]:
        """Поиск товарных транзакций
        """
        return await self._client.request(
            "GET",
            "/api/v1/storages/transactions/{company_id}",
            path_params={"company_id": company_id},
            params={"page": page_, "count": count_, "start_date": start_date, "end_date": end_date, "document_id": document_id, "changed_after": changed_after, "changed_before": changed_before},
            response_model=builtins.list[StoragesTransactionResponseDataTypesDataItem],
            extra_query=extra_query,
        )

    async def create(
        self,
        company_id: float,
        data: StorageOperationGoodTransactionRequestDataTypes,
        extra_query: dict[str, Any] | None = None
    ) -> StorageOperationGoodTransactionResponse200DataTypesData:
        """Создать транзакцию
        """
        return await self._client.request(
            "POST",
            "/api/v1/storage_operations/goods_transactions/{company_id}",
            path_params={"company_id": company_id},
            json_body=data,
            response_model=StorageOperationGoodTransactionResponse200DataTypesData,
            extra_query=extra_query,
        )

    async def get(
        self,
        company_id: float,
        transaction_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> StorageOperationGoodTransactionResponse200DataTypesData:
        """Получение транзакции
        """
        return await self._client.request(
            "GET",
            "/api/v1/storage_operations/goods_transactions/{company_id}/{transaction_id}",
            path_params={"company_id": company_id, "transaction_id": transaction_id},
            response_model=StorageOperationGoodTransactionResponse200DataTypesData,
            extra_query=extra_query,
        )

    async def update(
        self,
        company_id: float,
        transaction_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> StorageOperationGoodTransactionResponse200DataTypesData:
        """Обновление транзакции
        """
        return await self._client.request(
            "PUT",
            "/api/v1/storage_operations/goods_transactions/{company_id}/{transaction_id}",
            path_params={"company_id": company_id, "transaction_id": transaction_id},
            response_model=StorageOperationGoodTransactionResponse200DataTypesData,
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
            "/api/v1/storage_operations/goods_transactions/{company_id}/{transaction_id}",
            path_params={"company_id": company_id, "transaction_id": transaction_id},
            extra_query=extra_query,
        )
