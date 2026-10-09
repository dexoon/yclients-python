"""NotificationsApi -- сгенерированные методы API."""

from __future__ import annotations

from typing import Any

from yclients._base import BaseClient
from yclients.models.schemas import NotificationSettingsUsersRequestDataType


class NotificationsApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def notification_types(
        self,
        company_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> list[dict[str, Any]]:
        """Получить настройки уведомлений в филиале
        Метод позволяет получить настройки уведомлений в филиале.
        """
        return await self._client.request(
            "GET",
            "/api/v1/notification_settings/{company_id}/notification_types",
            path_params={"company_id": company_id},
            response_model=list[dict[str, Any]],
            extra_query=extra_query,
        )

    async def get(
        self,
        company_id: float,
        user_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Получить настройки уведомлений пользователя
        Метод позволяет получить настройки уведомлений конкретного пользователя филиала.
        """
        return await self._client.request(
            "GET",
            "/api/v1/notification_settings/{company_id}/users/{user_id}",
            path_params={"company_id": company_id, "user_id": user_id},
            response_model=dict[str, Any],
            extra_query=extra_query,
        )

    async def create(
        self,
        company_id: float,
        user_id: float,
        data: NotificationSettingsUsersRequestDataType,
        extra_query: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Изменить настройки PUSH-уведомлений пользователя
        Метод позволяет изменить настройки PUSH-уведомлений пользователя.
        Выбирать тип уведомления для изменения (record_create_online_staff или record_create_online_admin и т.д.) следует исходя их указанного типа уведомления у пользователя (mode: admin или mode: staff)
        """
        return await self._client.request(
            "POST",
            "/api/v1/notification_settings/{company_id}/users/{user_id}",
            path_params={"company_id": company_id, "user_id": user_id},
            json_body=data,
            response_model=dict[str, Any],
            extra_query=extra_query,
        )
