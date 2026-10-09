"""TipsApi -- сгенерированные методы API."""

from __future__ import annotations

from typing import Any

from yclients._base import BaseClient
from yclients.models.schemas import TipsSettingResponseDataTypesDataItem


class TipsApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def settings(
        self,
        company_id: int,
        extra_query: dict[str, Any] | None = None
    ) -> list[TipsSettingResponseDataTypesDataItem]:
        """Получить список мастеров салона с их настройками чаевых
        """
        return await self._client.request(
            "GET",
            "/api/v1/tips/{company_id}/settings",
            path_params={"company_id": company_id},
            response_model=list[TipsSettingResponseDataTypesDataItem],
            extra_query=extra_query,
        )

    async def list_enable(
        self,
        company_id: float,
        master_tips_settings_id: int,
        extra_query: dict[str, Any] | None = None
    ) -> list[TipsSettingResponseDataTypesDataItem]:
        """Включить чаевые у мастера
        """
        return await self._client.request(
            "GET",
            "/api/v1/tips/{company_id}/settings/{master_tips_settings_id}/enable",
            path_params={"company_id": company_id, "master_tips_settings_id": master_tips_settings_id},
            response_model=list[TipsSettingResponseDataTypesDataItem],
            extra_query=extra_query,
        )

    async def disable(
        self,
        company_id: int,
        master_tips_settings_id: int,
        extra_query: dict[str, Any] | None = None
    ) -> list[TipsSettingResponseDataTypesDataItem]:
        """Отключить чаевые у мастера
        """
        return await self._client.request(
            "POST",
            "/api/v1/tips/{company_id}/settings/{master_tips_settings_id}/disable",
            path_params={"company_id": company_id, "master_tips_settings_id": master_tips_settings_id},
            response_model=list[TipsSettingResponseDataTypesDataItem],
            extra_query=extra_query,
        )
