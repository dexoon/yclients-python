"""ImagesApi -- сгенерированные методы API."""

from __future__ import annotations

from typing import Any

from yclients._base import BaseClient
from yclients.models.schemas import PostImagesEntityResponse200


class ImagesApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def create(
        self,
        entity: str,
        extra_query: dict[str, Any] | None = None
    ) -> PostImagesEntityResponse200:
        """Загрузка изображения
        Объект ответа имеет следующие поля:
        | Поле  | Тип | Описание |
        | ------------- | ------------- | ------------- |
        |  image_binded  | boolean  |  Статус привязки изображений к сущности  |
        |  image_group  | object  | Объект группа изображений |
        """
        return await self._client.request(
            "POST",
            "/api/v1/images/{entity}",
            path_params={"entity": entity},
            response_model=PostImagesEntityResponse200,
            extra_query=extra_query,
        )

    async def delete(
        self,
        entity: str,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Удаление изображений
        Объект ответа имеет следующие поля:
        | Поле  | Тип | Описание |
        | ------------- | ------------- | ------------- |
        |  success  | boolean  |  Результат удаления  |
        """
        return await self._client.request(
            "DELETE",
            "/api/v1/images/{entity}",
            path_params={"entity": entity},
            extra_query=extra_query,
        )
