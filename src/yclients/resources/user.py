"""UserApi -- сгенерированные методы API."""

from __future__ import annotations

from typing import Any

from yclients._base import BaseClient
from yclients.models.schemas import PostInviteSalonIdRequest


class UserApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def get(
        self,
        company_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Получить список прав
        + Параметр
        + company_id (required, number, `1`) - ID компании
        """
        return await self._client.request(
            "GET",
            "/api/v1/user/permissions/{company_id}",
            path_params={"company_id": company_id},
            response_model=dict[str, Any],
            extra_query=extra_query,
        )

    async def create(
        self,
        salon_id: str,
        data: PostInviteSalonIdRequest,
        extra_query: dict[str, Any] | None = None
    ) -> str:
        """Создание и отправка приглашения
        Приглашение к управлению филиалом предполагает отправку по e-mail или телефону ссылки. Перейдя по этой ссылке, пользователь после регистрации получает доступ к управлению филиалом в соответствии с назначенными правами.
        Назначение прав осуществляется после отправки приглашения отдельным запросом.
        """
        return await self._client.request(
            "POST",
            "/api/v1/user/invite/{salon_id}",
            path_params={"salon_id": salon_id},
            json_body=data,
            response_model=str,
            extra_query=extra_query,
        )
