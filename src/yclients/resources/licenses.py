"""LicensesApi -- сгенерированные методы API."""

from __future__ import annotations

from typing import Any

from yclients._base import BaseClient
from yclients.models.schemas import GetLicenseCompanyIdResponse200


class LicensesApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def get(
        self,
        company_id: str,
        extra_query: dict[str, Any] | None = None
    ) -> GetLicenseCompanyIdResponse200:
        """Получение информация о лицензии компании
        """
        return await self._client.request(
            "GET",
            "/api/v1/license/{company_id}",
            path_params={"company_id": company_id},
            response_model=GetLicenseCompanyIdResponse200,
            extra_query=extra_query,
        )
