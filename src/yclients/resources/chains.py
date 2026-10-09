"""ChainsApi -- сгенерированные методы API."""

from __future__ import annotations

import builtins
from typing import Any

from yclients._base import BaseClient
from yclients.models.schemas import GroupsResponseDataTypesDataItem


class ChainsApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def list(
        self,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[GroupsResponseDataTypesDataItem]:
        """Получение доступных пользователю сетей
        Объект сети салонов имеет следующие поля:
        | Поле  | Тип | Описание |
        | ------------- | ------------- | ------------- |
        |  id  | number  |  Id сети салонов  |
        |  title  | string  | Название сети салонов |
        |  companies  | array  | Список салонов сети |
        |  access  | object  | Объект с правами доступа для управления сетью |
        """
        return await self._client.request(
            "GET",
            "/api/v1/groups",
            response_model=builtins.list[GroupsResponseDataTypesDataItem],
            extra_query=extra_query,
        )
