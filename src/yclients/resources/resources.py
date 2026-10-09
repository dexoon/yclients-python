"""ResourcesApi -- сгенерированные методы API."""

from __future__ import annotations

import builtins
from typing import Any

from yclients._base import BaseClient


class ResourcesApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def list(
        self,
        company_id: float,
        *,
        accept: str | None = None,
        content_type: str | None = None,
        authorization: str | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[dict[str, Any]]:
        """Получение ресурсов в филиале
        """
        return await self._client.request(
            "GET",
            "/api/v1/resources/{company_id}",
            path_params={"company_id": company_id},
            params={"Accept": accept, "Content-Type": content_type, "Authorization": authorization},
            response_model=builtins.list[dict[str, Any]],
            extra_query=extra_query,
        )
