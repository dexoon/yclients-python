"""CustomFieldsApi -- сгенерированные методы API."""

from __future__ import annotations

import builtins
from typing import Any

from yclients._base import BaseClient
from yclients.models.schemas import CustomFieldsRequestDataType


class CustomFieldsApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def list(
        self,
        field_category: str,
        company_id: int,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[dict[str, Any]]:
        """Получение коллекции полей филиала
        """
        return await self._client.request(
            "GET",
            "/api/v1/custom_fields/{field_category}/{company_id}",
            path_params={"field_category": field_category, "company_id": company_id},
            response_model=builtins.list[dict[str, Any]],
            extra_query=extra_query,
        )

    async def create(
        self,
        field_category: str,
        company_id: int,
        data: CustomFieldsRequestDataType,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[dict[str, Any]]:
        """Добавление дополнительного поля
        Для добавления поля пользователь должен быть добавлен в **связанной с филиалом сети**, и иметь права доступа в разделе: <br>**Настройки - Доступ к разделу Дополнительные поля - Создание доп. полей**
        """
        return await self._client.request(
            "POST",
            "/api/v1/custom_fields/{field_category}/{company_id}",
            path_params={"field_category": field_category, "company_id": company_id},
            json_body=data,
            response_model=builtins.list[dict[str, Any]],
            extra_query=extra_query,
        )

    async def update(
        self,
        field_category: str,
        company_id: int,
        field_id: int,
        data: CustomFieldsRequestDataType,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[dict[str, Any]]:
        """Обновление дополнительного поля
        Для добавления поля пользователь должен быть добавлен в **связанной с филиалом сети**, и иметь права доступа в разделе: <br>**Настройки - Доступ к разделу Дополнительные поля - Изменение доп. полей**
        """
        return await self._client.request(
            "PUT",
            "/api/v1/custom_fields/{field_category}/{company_id}/{field_id}",
            path_params={"field_category": field_category, "company_id": company_id, "field_id": field_id},
            json_body=data,
            response_model=builtins.list[dict[str, Any]],
            extra_query=extra_query,
        )

    async def delete(
        self,
        field_category: str,
        company_id: int,
        field_id: int,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[dict[str, Any]]:
        """Удаление дополнительного поля из филиала
        Для добавления поля пользователь должен быть добавлен в **связанной с филиалом сети**, и иметь права доступа в разделе: <br>**Настройки - Доступ к разделу Дополнительные поля - Удаление доп. полей**
        """
        return await self._client.request(
            "DELETE",
            "/api/v1/custom_fields/{field_category}/{company_id}/{field_id}",
            path_params={"field_category": field_category, "company_id": company_id, "field_id": field_id},
            response_model=builtins.list[dict[str, Any]],
            extra_query=extra_query,
        )
