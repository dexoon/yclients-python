"""PrivacyPolicyApi -- сгенерированные методы API."""

from __future__ import annotations

from typing import Any

from yclients._base import BaseClient


class PrivacyPolicyApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def get(
        self,
        company_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Получение информация о правилах обработки персональных данных компании
        """
        return await self._client.request(
            "GET",
            "/api/v1/privacy_policy/{company_id}",
            path_params={"company_id": company_id},
            extra_query=extra_query,
        )
