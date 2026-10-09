"""CertificatesApi -- сгенерированные методы API."""

from __future__ import annotations

import builtins
from typing import Any

from yclients._base import BaseClient


class CertificatesApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def list(
        self,
        *,
        company_id: float | None = None,
        phone: float | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[dict[str, Any]]:
        """Получить сертификаты клиента
        Возвращает список сертификатов клиента по телефону
        | Атрибут         | Тип       | Описание                                           |
        |-----------------|-----------|----------------------------------------------------|
        | id              | int       | Идентификатор сертификата                          |
        | number          | string    | Код сертификата                                    |
        | balance         | decimal   | Текущий баланс                                     |
        | default_balance | decimal   | Начальный баланс                                   |
        | type_id         | int       | Идентификатор типа сертификата                     |
        | status_id       | int       | Идентификатор статуса                              |
        | created_date    | datetime | Дата продажи                                       |
        | expiration_date | datetime  | Дата сгорания                                      |
        | type            | object    | Объект с информацией о типе сертификата            |
        | status          | object    | Объект с информацией о текущем статусе сертификата |
        """
        return await self._client.request(
            "GET",
            "/api/v1/loyalty/certificates/",
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
        """Получить сертификаты пользователя
        Возвращает список сертификатов авторизованного пользователя
        """
        return await self._client.request(
            "GET",
            "/api/v1/user/loyalty/certificates/",
            params={"company_id": company_id},
            response_model=builtins.list[dict[str, Any]],
            extra_query=extra_query,
        )
