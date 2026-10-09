"""DepositsApi -- сгенерированные методы API."""

from __future__ import annotations

from typing import Any

from yclients._base import BaseClient
from yclients.models.schemas import (
    DepositOperationResponseDataTypesData,
    GetDepositHistoryDepositIdResponse200DataItem,
)


class DepositsApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def create(
        self,
        salon_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> DepositOperationResponseDataTypesData:
        """Создание операции пополнения личного счёта
        Создание операции с личным счётом предполагает создание документа, транзакции с личным счётом и финансовой транзакции в рамках одного запроса к API.
        """
        return await self._client.request(
            "POST",
            "/api/v1/deposits_operations/{salon_id}",
            path_params={"salon_id": salon_id},
            response_model=DepositOperationResponseDataTypesData,
            extra_query=extra_query,
        )

    async def get(
        self,
        company_id: float,
        client_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Получение списка личных счетов по филиалу и клиенту
        """
        return await self._client.request(
            "GET",
            "/api/v1/deposits/company/{company_id}/client/{client_id}",
            path_params={"company_id": company_id, "client_id": client_id},
            extra_query=extra_query,
        )

    async def list_chain(
        self,
        chain_id: float,
        *,
        balance_from: float | None = None,
        balance_to: float | None = None,
        page_: float | None = None,
        limit: float | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Получение списка личных счетов по сети и набору фильтров
        """
        return await self._client.request(
            "GET",
            "/api/v1/deposits/chain/{chain_id}",
            path_params={"chain_id": chain_id},
            params={"balance_from": balance_from, "balance_to": balance_to, "page": page_, "limit": limit},
            extra_query=extra_query,
        )

    async def get_phone(
        self,
        chain_id: float,
        phone: float,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Получение списка личных счетов по сети и номеру телефона клиента
        """
        return await self._client.request(
            "GET",
            "/api/v1/deposits/chain/{chain_id}/phone/{phone}",
            path_params={"chain_id": chain_id, "phone": phone},
            extra_query=extra_query,
        )

    async def get_history(
        self,
        chain_id: float,
        deposit_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> list[GetDepositHistoryDepositIdResponse200DataItem]:
        """Получение истории операции личного счета
        """
        return await self._client.request(
            "GET",
            "/api/v1/deposits/chain/{chain_id}/deposit_history/{deposit_id}",
            path_params={"chain_id": chain_id, "deposit_id": deposit_id},
            response_model=list[GetDepositHistoryDepositIdResponse200DataItem],
            extra_query=extra_query,
        )
