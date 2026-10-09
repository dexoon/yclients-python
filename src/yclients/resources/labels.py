"""LabelsApi -- сгенерированные методы API."""

from __future__ import annotations

import builtins
from typing import Any

from yclients._base import BaseClient
from yclients.models.schemas import LabelsUpdateRequestDataTypes


class LabelsApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def list(
        self,
        company_id: float,
        entity: float,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[dict[str, Any]]:
        """Получить категории компании
        """
        return await self._client.request(
            "GET",
            "/api/v1/labels/{company_id}/{entity}",
            path_params={"company_id": company_id, "entity": entity},
            response_model=builtins.list[dict[str, Any]],
            extra_query=extra_query,
        )

    async def create_for_clients(
        self,
        company_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Создать клиентскую категорию компании
        """
        return await self._client.request(
            "POST",
            "/api/v1/labels/{company_id}/clients/create",
            path_params={"company_id": company_id},
            response_model=dict[str, Any],
            extra_query=extra_query,
        )

    async def create(
        self,
        company_id: float,
        *,
        title: str | None = None,
        color: str | None = None,
        entity: float | None = None,
        icon: str | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Создать категорию
        """
        return await self._client.request(
            "POST",
            "/api/v1/labels/{company_id}",
            path_params={"company_id": company_id},
            params={"title": title, "color": color, "entity": entity, "icon": icon},
            response_model=dict[str, Any],
            extra_query=extra_query,
        )

    async def update(
        self,
        company_id: float,
        label_id: float,
        data: LabelsUpdateRequestDataTypes,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Обновить категорию
        """
        return await self._client.request(
            "PUT",
            "/api/v1/labels/{company_id}/{label_id}",
            path_params={"company_id": company_id, "label_id": label_id},
            json_body=data,
            extra_query=extra_query,
        )

    async def delete(
        self,
        company_id: float,
        label_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Удалить категорию компании
        """
        return await self._client.request(
            "DELETE",
            "/api/v1/labels/{company_id}/{label_id}",
            path_params={"company_id": company_id, "label_id": label_id},
            extra_query=extra_query,
        )

    async def list_clients(
        self,
        company_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[dict[str, Any]]:
        """Получить клиентские категории с поиском по названию
        """
        return await self._client.request(
            "GET",
            "/api/v1/labels/{company_id}/clients",
            path_params={"company_id": company_id},
            response_model=builtins.list[dict[str, Any]],
            extra_query=extra_query,
        )
