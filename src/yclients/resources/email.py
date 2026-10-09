"""EmailApi -- сгенерированные методы API."""

from __future__ import annotations

from typing import Any

from yclients._base import BaseClient
from yclients.models.schemas import (
    EmailClientsByFilterRequestDataTypes,
    EmailClientsByIdRequestDataTypes,
)


class EmailApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def list_by_id(
        self,
        company_id: float,
        data: EmailClientsByIdRequestDataTypes,
        extra_query: dict[str, Any] | None = None
    ) -> str:
        """Отправить Email рассылку по списку клиентов
        Объект для создания Email рассылки имеет следующие поля:
        | Поле  | Тип | Описание |
        | ------------- | ------------- | ------------- |
        |  client_ids  |  array of number   | Массив ID клиентов  |
        |  text  | string  | Текст Email сообщения  |
        |  subject  | string  | Тема Email сообщения  |
        """
        return await self._client.request(
            "POST",
            "/api/v1/email/clients/by_id/{company_id}",
            path_params={"company_id": company_id},
            json_body=data,
            response_model=str,
            extra_query=extra_query,
        )

    async def list_by_filter(
        self,
        company_id: float,
        data: EmailClientsByFilterRequestDataTypes,
        *,
        fullname: str | None = None,
        phone: str | None = None,
        email: str | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> str:
        """Отправить Email рассылку по клиентам, подходящим под фильтры
        Объект для создания Email рассылки имеет следующие поля:
        | Поле  | Тип | Описание |
        | ------------- | ------------- | ------------- |
        |  text  | string  | Текст Email сообщения  |
        |  subject  | string  | Тема Email сообщения  |
        #### Фильтрация клиентов
        + fullname:'Joh' (optional, string) - Имя (часть имени) для фильтрации клиентов
        + phone:'7916' (optional, string) - Телефон (часть номера) для фильтрации клиентов
        + email:'test@' (optional, string) - Email (часть) для фильтрации клиентов
        + card:'5663rt' (optional, string) - Card (часть) для фильтрации клиентов по номеру карты лояльности
        Внимание: При отсутствии фильтров Email рассылка уйдет по всей базе!
        """
        return await self._client.request(
            "POST",
            "/api/v1/email/clients/by_filter/{company_id}",
            path_params={"company_id": company_id},
            params={"fullname": fullname, "phone": phone, "email": email},
            json_body=data,
            response_model=str,
            extra_query=extra_query,
        )
