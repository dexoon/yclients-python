"""StoragesApi -- сгенерированные методы API."""

from __future__ import annotations

import builtins
from typing import Any

from yclients._base import BaseClient


class StoragesApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def list(
        self,
        company_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[dict[str, Any]]:
        """Получить склады компании
        Объект склада компании имеет следующие поля:
        | Поле  | Тип | Описание |
        | ------------- | ------------- | ------------- |
        |  id  |  number   | ID  склада  |
        |  title  | string  | Название  |
        |  for_services  | number  | 1 - если используется для автоматического списания расходников |
        |  for_sale  | number  | 1 - если склад по умолчанию для продажи товаров |
        |  comment  | string  | Описание к складу |
        """
        return await self._client.request(
            "GET",
            "/api/v1/storages/{company_id}",
            path_params={"company_id": company_id},
            response_model=builtins.list[dict[str, Any]],
            extra_query=extra_query,
        )
