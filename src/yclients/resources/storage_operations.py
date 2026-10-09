"""StorageOperationsApi -- сгенерированные методы API."""

from __future__ import annotations

from typing import Any

from yclients._base import BaseClient


class StorageOperationsApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def create(
        self,
        company_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Создание складской операции
        Создание складской операции предполагает создание документа и нескольких товарных транзакций в рамках одного запроса к API.
        """
        return await self._client.request(
            "POST",
            "/api/v1/storage_operations/operation/{company_id}",
            path_params={"company_id": company_id},
            response_model=dict[str, Any],
            extra_query=extra_query,
        )
