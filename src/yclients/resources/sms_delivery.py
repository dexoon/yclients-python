"""SmsDeliveryApi -- сгенерированные методы API."""

from __future__ import annotations

from typing import Any

from yclients._base import BaseClient


class SmsDeliveryApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def send_sms(
        self,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Отправка СМС
        ### Отправка СМС
        В случае ошибки возвращается ее HTTP-код. В некоторых случаях также возвращается текстовое описание ошибки.
        Все методы API могут возвращать следующие коды ошибок:
        |  Error code  |  Http status code  |  Название  |  Описание  |
        | ------------- | ------------- | ------------- | ------------- |
        |  5  |  400  |  ENTITY_VALIDATION_ERROR  |  Тело запроса не прошло валидацию  |
        |  10  |  400  |  FIELD_VALIDATION_ERROR  |  Параметр не прошел валидацию  |
        |  32  |  200  |  FIELD_VALIDATION_ERROR  |  Недостаточно средств  |
        |  15  |  403  |  ACCESS_FORBIDDEN  |  Действие недоступно, у приложения нет требуемых разрешений.  |
        |  20  |  401  |  INVALID_PARTNER_TOKEN  |  partner_token отсутствует или невалиден  |
        |  30  |  404  |  RESOURCE_NOT_FOUND  |  Ресурс по запрошенному пути не существует  |
        """
        return await self._client.request(
            "POST",
            "/api/v1/",
            extra_query=extra_query,
        )

    async def get_delivery_status(
        self,
        data: dict[str, Any],
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Получение статусов сообщений
        ### Получение статусов сообщений
        |  Номер  |  Название  |
        | ------------- | ------------- |
        |  1  |  Доставлено  |
        |  2  |  Не доставлено  |
        |  4  |  Отправлено на телефон  |
        |  8  |  Передано оператору  |
        |  16  |  Отклонено оператором  |
        |  52  |  Недостаточно средств  |
        В случае ошибки возвращается ее HTTP-код. В некоторых случаях также возвращается текстовое описание ошибки.
        Все методы API могут возвращать следующие коды ошибок:
        |  Error code  |  Http status code  |  Название  |  Описание  |
        | ------------- | ------------- | ------------- | ------------- |
        """
        return await self._client.request(
            "POST",
            "/api/v1/delivery/status",
            json_body=data,
            extra_query=extra_query,
        )
