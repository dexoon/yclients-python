"""BookingUsersApi -- сгенерированные методы API."""

from __future__ import annotations

from typing import Any

from yclients._base import BaseClient
from yclients.models.schemas import (
    AuthRequest2,
    BookingAuthResponse,
    BookingAuthResponse2,
    BookingAuthWithCode,
    BookingUserGetDataResponseDataTypes,
    BookingUserUpdateInfoRequestDataTypes,
    BookingUserUpdatePasswordRequestDataTypes,
    BookingUserUpdatePasswordResponseDataTypesData,
)


class BookingUsersApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def auth(
        self,
        data: BookingAuthWithCode,
        extra_query: dict[str, Any] | None = None
    ) -> BookingAuthResponse2:
        """Авторизоваться по номеру телефона и коду
        Для авторизации по коду, сначала необходимо запросить код подтверждения. Это можно сделать методом
        [Отправить СМС код подтверждения номера телефона](#tag/Polzovateli-onlajn-zapisi/operation/Отправить%20СМС%20код%20подтверждения%20номера%20телефона)
        """
        return await self._client.request(
            "POST",
            "/api/v1/user/auth",
            json_body=data,
            response_model=BookingAuthResponse2,
            extra_query=extra_query,
        )

    async def auth_by_phone(
        self,
        data: AuthRequest2,
        extra_query: dict[str, Any] | None = None
    ) -> BookingAuthResponse:
        """Авторизовать пользователя онлайн-записи
        При смене пароля пользователем онлайн-записи его API-ключ изменится и
        потребуется новая авторизация
        """
        return await self._client.request(
            "POST",
            "/api/v1/booking/auth",
            json_body=data,
            response_model=BookingAuthResponse,
            extra_query=extra_query,
        )

    async def send_phone_confirmation_code(
        self,
        *,
        company_id: int | None = None,
        group_id: int | None = None,
        phone: str | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Отправить СМС код подтверждения номера телефона для изменения данных
        В запросе должен обязательно присутствовать один из двух параметров: company_id или group_id
        """
        return await self._client.request(
            "GET",
            "/api/v1/booking/user/phone_confirmation",
            params={"company_id": company_id, "group_id": group_id, "phone": phone},
            extra_query=extra_query,
        )

    async def update_password(
        self,
        data: BookingUserUpdatePasswordRequestDataTypes,
        extra_query: dict[str, Any] | None = None
    ) -> BookingUserUpdatePasswordResponseDataTypesData:
        """Обновление пароля пользователя онлайн-записи
        Обновление пароля пользователя онлайн-записи.
        В ответе приходит новый токен пользователя.
        """
        return await self._client.request(
            "PUT",
            "/api/v1/booking/user/password",
            json_body=data,
            response_model=BookingUserUpdatePasswordResponseDataTypesData,
            extra_query=extra_query,
        )

    async def update(
        self,
        data: BookingUserUpdateInfoRequestDataTypes,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Обновление данных пользователя онлайн-записи
        Обновление основных данных пользователя онлайн-записи.
        При обновлении номера телефона нужно отправлять поле confirmation_code с кодом, который нужно получить
        из ресурса [СМС код подтверждения номера телефона для изменения
        данных](#operation/Отправить%20СМС%20код%20подтверждения%20номера%20телефона%20для%20изменения%20данных)
        """
        return await self._client.request(
            "PUT",
            "/api/v1/booking/user",
            json_body=data,
            extra_query=extra_query,
        )

    async def get_data(
        self,
        extra_query: dict[str, Any] | None = None
    ) -> BookingUserGetDataResponseDataTypes:
        """Получение данных пользователя онлайн-записи
        Получение данных пользователя онлайн-записи.
        """
        return await self._client.request(
            "GET",
            "/api/v1/booking/user/data",
            response_model=BookingUserGetDataResponseDataTypes,
            extra_query=extra_query,
        )
