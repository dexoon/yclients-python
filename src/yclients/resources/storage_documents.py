"""StorageDocumentsApi -- сгенерированные методы API."""

from __future__ import annotations

import builtins
from typing import Any

from yclients._base import BaseClient
from yclients.models.schemas import StorageOperationDocumentsRequestDataTypes


class StorageDocumentsApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def create(
        self,
        company_id: float,
        data: StorageOperationDocumentsRequestDataTypes,
        extra_query: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Создать документ
        """
        return await self._client.request(
            "POST",
            "/api/v1/storage_operations/documents/{company_id}",
            path_params={"company_id": company_id},
            json_body=data,
            response_model=dict[str, Any],
            extra_query=extra_query,
        )

    async def get(
        self,
        company_id: float,
        document_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Получить документ
        """
        return await self._client.request(
            "GET",
            "/api/v1/storage_operations/documents/{company_id}/{document_id}",
            path_params={"company_id": company_id, "document_id": document_id},
            response_model=dict[str, Any],
            extra_query=extra_query,
        )

    async def update(
        self,
        company_id: float,
        document_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Обновить документ
        """
        return await self._client.request(
            "PUT",
            "/api/v1/storage_operations/documents/{company_id}/{document_id}",
            path_params={"company_id": company_id, "document_id": document_id},
            response_model=dict[str, Any],
            extra_query=extra_query,
        )

    async def delete(
        self,
        company_id: float,
        document_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Удалить документ
        """
        return await self._client.request(
            "DELETE",
            "/api/v1/storage_operations/documents/{company_id}/{document_id}",
            path_params={"company_id": company_id, "document_id": document_id},
            extra_query=extra_query,
        )

    async def list(
        self,
        document_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[dict[str, Any]]:
        """Получить финансовые транзакции документа
        """
        return await self._client.request(
            "GET",
            "/api/v1/storage_operations/documents/finance_transactions/{document_id}",
            path_params={"document_id": document_id},
            response_model=builtins.list[dict[str, Any]],
            extra_query=extra_query,
        )

    async def list_goods_transactions(
        self,
        document_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[dict[str, Any]]:
        """Получить товарные транзакции документа
        """
        return await self._client.request(
            "GET",
            "/api/v1/storage_operations/documents/goods_transactions/{document_id}",
            path_params={"document_id": document_id},
            response_model=builtins.list[dict[str, Any]],
            extra_query=extra_query,
        )
