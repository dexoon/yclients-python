"""CommentsApi -- сгенерированные методы API."""

from __future__ import annotations

import builtins
from typing import Any

from yclients._base import BaseClient
from yclients.models.schemas import CommentsCompanyidRequestDataTypes


class CommentsApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def list(
        self,
        company_id: float,
        *,
        start_date: str | None = None,
        end_date: str | None = None,
        staff_id: float | None = None,
        rating: float | None = None,
        page_: float | None = None,
        count_: float | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[dict[str, Any]]:
        """Получить комментарии
        Объект комментарии имеет следующие поля:
        | Поле  | Тип | Описание |
        | ------------- | ------------- | ------------- |
        |  id  |  number   | Id комментария   |
        |  salon_id  |  number   | Id компании   |
        |  type  | number  | 1 - комментарий к мастеру, 0 - к салону  |
        |  master_id  | number  | ID мастера, если type = 1  |
        |  text  | string  | Текст комментария |
        |  date  | string  | Дата, когда был оставлен комментарий |
        |  rating  | number  | Оценка ( от 1 до 5) |
        |  user_id  | number  | Id пользователя, оставившего комментарий |
        |  user_name  | string  | Имя пользователя, оставившего комментарий |
        |  user_avatar  | string  | Аватар пользователя, оставившего комментарий |
        """
        return await self._client.request(
            "GET",
            "/api/v1/comments/{company_id}/",
            path_params={"company_id": company_id},
            params={"start_date": start_date, "end_date": end_date, "staff_id": staff_id, "rating": rating, "page": page_, "count": count_},
            response_model=builtins.list[dict[str, Any]],
            extra_query=extra_query,
        )

    async def create(
        self,
        company_id: float,
        staff_id: float,
        data: CommentsCompanyidRequestDataTypes,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[dict[str, Any]]:
        """Оставить комментарии
        """
        return await self._client.request(
            "POST",
            "/api/v1/comments/{company_id}/{staff_id}",
            path_params={"company_id": company_id, "staff_id": staff_id},
            json_body=data,
            response_model=builtins.list[dict[str, Any]],
            extra_query=extra_query,
        )
