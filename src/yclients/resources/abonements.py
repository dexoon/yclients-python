"""AbonementsApi -- сгенерированные методы API."""

from __future__ import annotations

import builtins
from typing import Any

from yclients._base import BaseClient
from yclients.models.schemas import (
    PostAbonementIdFreezeRequest,
    PostAbonementIdSetBalanceRequest,
    PostAbonementIdSetPeriodRequest,
)


class AbonementsApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def freeze(
        self,
        chain_id: float,
        abonement_id: float,
        data: PostAbonementIdFreezeRequest,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Заморозить абонемент
        """
        return await self._client.request(
            "POST",
            "/api/v1/chain/{chain_id}/loyalty/abonements/{abonementId}/freeze",
            path_params={"chain_id": chain_id, "abonementId": abonement_id},
            json_body=data,
            extra_query=extra_query,
        )

    async def unfreeze(
        self,
        chain_id: float,
        abonement_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Разморозить абонемент
        """
        return await self._client.request(
            "POST",
            "/api/v1/chain/{chain_id}/loyalty/abonements/{abonementId}/unfreeze",
            path_params={"chain_id": chain_id, "abonementId": abonement_id},
            extra_query=extra_query,
        )

    async def set_period(
        self,
        chain_id: float,
        abonement_id: float,
        data: PostAbonementIdSetPeriodRequest,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Изменить длительность абонемента
        """
        return await self._client.request(
            "POST",
            "/api/v1/chain/{chain_id}/loyalty/abonements/{abonementId}/set_period",
            path_params={"chain_id": chain_id, "abonementId": abonement_id},
            json_body=data,
            extra_query=extra_query,
        )

    async def set_balance(
        self,
        chain_id: float,
        abonement_id: float,
        data: PostAbonementIdSetBalanceRequest,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Изменить количество использований абонемента
        """
        return await self._client.request(
            "POST",
            "/api/v1/chain/{chain_id}/loyalty/abonements/{abonementId}/set_balance",
            path_params={"chain_id": chain_id, "abonementId": abonement_id},
            json_body=data,
            extra_query=extra_query,
        )

    async def list(
        self,
        chain_id: float,
        *,
        created_after: str | None = None,
        created_before: str | None = None,
        abonements_ids: builtins.list[float] | None = None,
        page_: float | None = None,
        count_: float | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Получить список абонементов по фильтру
        """
        return await self._client.request(
            "GET",
            "/api/v1/chain/{chain_id}/loyalty/abonements",
            path_params={"chain_id": chain_id},
            params={"created_after": created_after, "created_before": created_before, "abonements_ids": abonements_ids, "page": page_, "count": count_},
            extra_query=extra_query,
        )

    async def list_loyalty(
        self,
        *,
        company_id: float | None = None,
        phone: float | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[dict[str, Any]]:
        """Получить абонементы клиента
        Возвращает список абонементов клиента по телефону
        """
        return await self._client.request(
            "GET",
            "/api/v1/loyalty/abonements/",
            params={"company_id": company_id, "phone": phone},
            response_model=builtins.list[dict[str, Any]],
            extra_query=extra_query,
        )

    async def list_user(
        self,
        *,
        company_id: float | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[dict[str, Any]]:
        """Получить абонементы пользователя
        Возвращает список абонементов авторизованного пользователя
        """
        return await self._client.request(
            "GET",
            "/api/v1/user/loyalty/abonements/",
            params={"company_id": company_id},
            response_model=builtins.list[dict[str, Any]],
            extra_query=extra_query,
        )
