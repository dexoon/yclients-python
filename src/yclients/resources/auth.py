"""AuthApi -- сгенерированные методы API."""

from __future__ import annotations

from typing import Any

from yclients._base import BaseClient
from yclients.models.schemas import AuthRequest2, AuthRequest2fa, AuthResponse2


class AuthApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def login(
        self,
        data: AuthRequest2 | AuthRequest2fa,
        extra_query: dict[str, Any] | None = None
    ) -> (AuthResponse2 | dict[str, Any]):
        """Авторизовать пользователя
        При смене пароля пользователем его API-ключ изменится и потребуется новая авторизация.
        ⚠️ В зависимости от того, включена у пользователя 2fa или нет, будет зависеть ответ и необходимость
        отправить запрос авторизации с кодом подтверждения.
        """
        return await self._client.request(
            "POST",
            "/api/v1/auth",
            json_body=data,
            response_model=(AuthResponse2 | dict[str, Any]),
            extra_query=extra_query,
        )
