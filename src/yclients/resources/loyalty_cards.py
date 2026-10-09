"""LoyaltyCardsApi -- сгенерированные методы API."""

from __future__ import annotations

import builtins
from typing import Any

from yclients._base import BaseClient
from yclients.models.schemas import (
    LoyaltyCard2,
    LoyaltyCardsRequestDataTypes,
    LoyaltyCardsResponseDataTypes,
    LoyaltyCardType2,
    LoyaltyCardTypesResponseDataTypesItem,
    PostCardIdManualTransactionRequest,
    PostCardIdManualTransactionRequest2,
)


class LoyaltyCardsApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def get_salon_card_types(
        self,
        company_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[LoyaltyCardTypesResponseDataTypesItem]:
        """Получить список типов карт доступных в филиале
        Возвращает список типов карт, которые действуют для данного филиала.
        Атрибуты и их описания соответсвуют методу "Коллекция типов карт доступных клиенту", описанному выше.
        """
        return await self._client.request(
            "GET",
            "/api/v1/loyalty/card_types/salon/{company_id}",
            path_params={"company_id": company_id},
            response_model=builtins.list[LoyaltyCardTypesResponseDataTypesItem],
            extra_query=extra_query,
        )

    async def get(
        self,
        phone: str,
        group_id: float,
        company_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> LoyaltyCardsResponseDataTypes:
        """Получить список карт клиента по номеру телефона
        Возвращает список карт клиента с программами, которые активны в данном салоне
        | Атрибут        | Тип    | Описание|
        |----------------|--------|--------------------------------------------------------------------------------------------------------------|
        | id             | int    | Идентификатор карты лояльности                                                                                  |
        | balance        | decimal| Баланс карты лояльности                                                                                        |
        | paid_amount    | decimal| Сумма "Оплачено" |
        | sold_amount    | decimal| Сумма "Продано"                                                                                        |
        | visits_count   | int    | Количество визитов                                                                     |
        | number         | string | Номер карты |
        | type_id        | int    | Идентификатор типа карты лояльности                                                                               |
        | salon_group_id | int    | Идентификатор сети, где создана карта                                                                    |
        | type           | object | Объект, содержащий в себе поля "id" и "title": идентификатор типа карты и название типа карты, соотвественно
        | salon_group    | object | Объект, содержащий в себе поля "id" и "title": идентификатор сети, где создан тип карты и название этой сети                                                                                        |
        """
        return await self._client.request(
            "GET",
            "/api/v1/loyalty/cards/{phone}/{group_id}/{company_id}",
            path_params={"phone": phone, "group_id": group_id, "company_id": company_id},
            response_model=LoyaltyCardsResponseDataTypes,
            extra_query=extra_query,
        )

    async def get_client_cards(
        self,
        client_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> LoyaltyCardsResponseDataTypes:
        """Получить список карт клиента по ID
        Возвращает список карт клиента с программами, которые активны в данном салоне
        Атрибуты в ответе на запрос полностью совпадают с методом "Получить список выданных карт по номеру телефона", описанным выше
        """
        return await self._client.request(
            "GET",
            "/api/v1/loyalty/client_cards/{client_id}",
            path_params={"client_id": client_id},
            response_model=LoyaltyCardsResponseDataTypes,
            extra_query=extra_query,
        )

    async def get_loyalty_cards(
        self,
        group_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> LoyaltyCardsResponseDataTypes:
        """Получить карты лояльности пользователя
        Возвращает список карт авторизованного пользователя с программами, фильтруя карты по сети салонов/салону
        """
        return await self._client.request(
            "GET",
            "/api/v1/user/loyalty_cards/{group_id}",
            path_params={"group_id": group_id},
            response_model=LoyaltyCardsResponseDataTypes,
            extra_query=extra_query,
        )

    async def create(
        self,
        company_id: float,
        data: LoyaltyCardsRequestDataTypes,
        extra_query: dict[str, Any] | None = None
    ) -> LoyaltyCardsResponseDataTypes:
        """Выдать карту лояльности
        | Атрибут              | Тип    | Описание                                     |
        |----------------------|--------|----------------------------------------------|
        | loyalty_card_number  | number | Номер карты лояльности                       |
        | loyalty_card_type_id | number | Идентификатор типа карты лояльности          |
        | phone                | number | Номер телефона клиента в формате 70001234567 |
        """
        return await self._client.request(
            "POST",
            "/api/v1/loyalty/cards/{company_id}",
            path_params={"company_id": company_id},
            json_body=data,
            response_model=LoyaltyCardsResponseDataTypes,
            extra_query=extra_query,
        )

    async def delete(
        self,
        company_id: float,
        card_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Удалить карту  лояльности
        """
        return await self._client.request(
            "DELETE",
            "/api/v1/loyalty/cards/{company_id}/{card_id}",
            path_params={"company_id": company_id, "card_id": card_id},
            extra_query=extra_query,
        )

    async def create_manual_transaction(
        self,
        chain_id: float,
        card_id: float,
        data: PostCardIdManualTransactionRequest,
        extra_query: dict[str, Any] | None = None
    ) -> LoyaltyCard2:
        """Ручное списание/пополнение карты лояльности в сети
        Ручное списание/пополнение карты лояльности в сети
        """
        return await self._client.request(
            "POST",
            "/api/v1/chain/{chain_id}/loyalty/cards/{card_id}/manual_transaction",
            path_params={"chain_id": chain_id, "card_id": card_id},
            json_body=data,
            response_model=LoyaltyCard2,
            extra_query=extra_query,
        )

    async def list(
        self,
        chain_id: int,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[LoyaltyCardType2]:
        """Получить список типов карт, доступных в сети
        """
        return await self._client.request(
            "GET",
            "/api/v1/chain/{chain_id}/loyalty/card_types",
            path_params={"chain_id": chain_id},
            response_model=builtins.list[LoyaltyCardType2],
            extra_query=extra_query,
        )

    async def create_manual_transaction_card(
        self,
        company_id: float,
        card_id: float,
        data: PostCardIdManualTransactionRequest2,
        extra_query: dict[str, Any] | None = None
    ) -> LoyaltyCard2:
        """Ручное списание/пополнение карты лояльности в компании
        Ручное списание/пополнение карты лояльности в компании
        """
        return await self._client.request(
            "POST",
            "/api/v1/company/{company_id}/loyalty/cards/{card_id}/manual_transaction",
            path_params={"company_id": company_id, "card_id": card_id},
            json_body=data,
            response_model=LoyaltyCard2,
            extra_query=extra_query,
        )

    async def get_client_card_types(
        self,
        company_id: float,
        phone: float,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[LoyaltyCardTypesResponseDataTypesItem]:
        """Получить список типов карт доступных для выдачи клиенту
        Возвращает список типов карт, которые доступны для выдачи клиенту салона.
        | Атрибут        | Тип    | Описание                                                                                                     |
        |----------------|--------|--------------------------------------------------------------------------------------------------------------|
        | id             | int    | Идентификатор типа карты                                                                                     |
        | title          | string | Название типа карты                                                                                          |
        | salon_group_id | int    | Идентификатор сети, где создан тип карты                                                                     |
        | salon_group    | object | Объект, содержащий в себе поля "id" и "title": идентификатор сети, где создан тип карты и название этой сети |
        """
        return await self._client.request(
            "GET",
            "/api/v1/loyalty/card_types/client/{company_id}/{phone}",
            path_params={"company_id": company_id, "phone": phone},
            response_model=builtins.list[LoyaltyCardTypesResponseDataTypesItem],
            extra_query=extra_query,
        )
