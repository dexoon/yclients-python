"""SalesApi -- сгенерированные методы API."""

from __future__ import annotations

from typing import Any

from yclients._base import BaseClient
from yclients.models.schemas import (
    CompanySalonidSaleDocumentidPaymentAbonements,
    CompanySalonidSaleDocumentidPaymentAccount,
    CompanySalonidSaleDocumentidPaymentCertificate,
    CompanySalonidSaleDocumentidPaymentDeposit,
    CompanySalonidSaleDocumentidPaymentLoyaltyCard,
    CompanySalonidSaleDocumentidPaymentLoyaltyProgram,
    CompanySalonidSaleDocumentidPaymentReferal,
)


class SalesApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def get(
        self,
        company_id: float,
        document_id: int,
        extra_query: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Получение Операции продажи
        """
        return await self._client.request(
            "GET",
            "/api/v1/company/{company_id}/sale/{document_id}",
            path_params={"company_id": company_id, "document_id": document_id},
            response_model=dict[str, Any],
            extra_query=extra_query,
        )

    async def delete(
        self,
        company_id: float,
        document_id: int,
        payment_transaction_id: int,
        extra_query: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Удаление транзакции оплаты в кассу
        В качестве ответа возвращается информация об [Операции продажи](#sale-operation)
        """
        return await self._client.request(
            "DELETE",
            "/api/v1/company/{company_id}/sale/{document_id}/payment/payment_transaction/{payment_transaction_id}",
            path_params={"company_id": company_id, "document_id": document_id, "payment_transaction_id": payment_transaction_id},
            response_model=dict[str, Any],
            extra_query=extra_query,
        )

    async def delete_loyalty_transaction(
        self,
        company_id: float,
        document_id: int,
        payment_transaction_id: int,
        extra_query: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Удаление транзакции оплаты лояльностью
        В качестве ответа возвращается информация об [Операции продажи](#sale-operation)
        """
        return await self._client.request(
            "DELETE",
            "/api/v1/company/{company_id}/sale/{document_id}/payment/loyalty_transaction/{payment_transaction_id}",
            path_params={"company_id": company_id, "document_id": document_id, "payment_transaction_id": payment_transaction_id},
            response_model=dict[str, Any],
            extra_query=extra_query,
        )

    async def payment(
        self,
        company_id: float,
        document_id: float,
        data: CompanySalonidSaleDocumentidPaymentAccount | CompanySalonidSaleDocumentidPaymentDeposit | CompanySalonidSaleDocumentidPaymentCertificate | CompanySalonidSaleDocumentidPaymentAbonements | CompanySalonidSaleDocumentidPaymentReferal | CompanySalonidSaleDocumentidPaymentLoyaltyCard | CompanySalonidSaleDocumentidPaymentLoyaltyProgram,
        extra_query: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Оплата в кассу и лояльностью (различными методами)
        В качестве ответа возвращается информация об [Операции продажи](#sale-operation)
        """
        return await self._client.request(
            "POST",
            "/api/v1/company/{company_id}/sale/{document_id}/payment",
            path_params={"company_id": company_id, "document_id": document_id},
            json_body=data,
            response_model=dict[str, Any],
            extra_query=extra_query,
        )
