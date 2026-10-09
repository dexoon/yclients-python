"""VisitLoyaltyApi -- сгенерированные методы API."""

from __future__ import annotations

import builtins
from typing import Any

from yclients._base import BaseClient
from yclients.models.schemas import (
    VisitLoyaltyApplyResponseDataTypes,
    VisitLoyaltyCancelResponseDataTypes,
    VisitLoyaltyRequestDataTypes,
    VisitLoyaltyTransactionReaponseDataTypesItem,
)


class VisitLoyaltyApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def apply_discount_program(
        self,
        company_id: float,
        card_id: float,
        program_id: float,
        data: VisitLoyaltyRequestDataTypes,
        extra_query: dict[str, Any] | None = None
    ) -> VisitLoyaltyApplyResponseDataTypes:
        """Применить акцию скидки в визите
        Применение акции к визиту, имеет смысл тольо если есть визит
        """
        return await self._client.request(
            "POST",
            "/api/v1/visit/loyalty/apply_discount_program/{company_id}/{card_id}/{program_id}",
            path_params={"company_id": company_id, "card_id": card_id, "program_id": program_id},
            json_body=data,
            response_model=VisitLoyaltyApplyResponseDataTypes,
            extra_query=extra_query,
        )

    async def cancel_discount_program(
        self,
        company_id: float,
        card_id: float,
        program_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> VisitLoyaltyCancelResponseDataTypes:
        """Отменить применение акции скидки в визите
        Отмена примененной к визиту акции.
        """
        return await self._client.request(
            "POST",
            "/api/v1/visit/loyalty/cancel_discount_program/{company_id}/{card_id}/{program_id}",
            path_params={"company_id": company_id, "card_id": card_id, "program_id": program_id},
            response_model=VisitLoyaltyCancelResponseDataTypes,
            extra_query=extra_query,
        )

    async def apply_card_withdrawal(
        self,
        company_id: float,
        card_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> VisitLoyaltyApplyResponseDataTypes:
        """Применить списание с карты лояльности в визите
        Списание бонусов с карты Сумма не будет превышать остаток на оплату Если 0 то транзакции не будет
        """
        return await self._client.request(
            "POST",
            "/api/v1/visit/loyalty/apply_card_withdrawal/{company_id}/{card_id}",
            path_params={"company_id": company_id, "card_id": card_id},
            response_model=VisitLoyaltyApplyResponseDataTypes,
            extra_query=extra_query,
        )

    async def cancel_card_withdrawal(
        self,
        company_id: float,
        card_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> VisitLoyaltyCancelResponseDataTypes:
        """Отменить списание с карты лояльности в визите
        Отмена списания с карты лояльности.
        """
        return await self._client.request(
            "POST",
            "/api/v1/visit/loyalty/cancel_card_withdrawal/{company_id}/{card_id}",
            path_params={"company_id": company_id, "card_id": card_id},
            response_model=VisitLoyaltyCancelResponseDataTypes,
            extra_query=extra_query,
        )

    async def apply_referral_program(
        self,
        company_id: float,
        group_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> VisitLoyaltyApplyResponseDataTypes:
        """Применить реферальную программу в записи
        Применение реферальной программы к визиту
        """
        return await self._client.request(
            "POST",
            "/api/v1/visit/loyalty/apply_referral_program/{company_id}/{group_id}",
            path_params={"company_id": company_id, "group_id": group_id},
            response_model=VisitLoyaltyApplyResponseDataTypes,
            extra_query=extra_query,
        )

    async def list(
        self,
        visit_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[VisitLoyaltyTransactionReaponseDataTypesItem]:
        """Получить транзакции лояльности по визиту
        Список транзакций по акциям лояльнсти для данного визита
        """
        return await self._client.request(
            "GET",
            "/api/v1/visit/loyalty/transactions/{visit_id}",
            path_params={"visit_id": visit_id},
            response_model=builtins.list[VisitLoyaltyTransactionReaponseDataTypesItem],
            extra_query=extra_query,
        )
