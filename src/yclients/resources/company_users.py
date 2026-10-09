"""CompanyUsersApi -- сгенерированные методы API."""

from __future__ import annotations

import builtins
from typing import Any

from yclients._base import BaseClient


class CompanyUsersApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def list_deprecated(
        self,
        company_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[dict[str, Any]]:
        """Устаревшее. Получить пользователей компании
        Объект пользователь компании имеет следующие поля:
        | Поле  | Тип | Описание |
        | ------------- | ------------- | ------------- |
        |  id  |  number   | Id пользователя   |
        |  firstname  | string  | Имя пользователя  |
        |  login  | string  | login пользователя для авторизации в системе (для авторизации так же можно в качестве логина поля phone и email) |
        |  email  | string  | Почтовый адрес пользователя |
        |  phone  | string  | Телефон пользоватя |
        | information  | string  | Информация о пользователе |
        |  access  | object  | Объект прав доступа пользоватей к модулям системы |
        Объект access имеет следующие поля:
        | Поле  | Тип | Описание |
        | ------------- | ------------- | ------------- |
        """
        return await self._client.request(
            "GET",
            "/api/v1/company_users/{company_id}",
            path_params={"company_id": company_id},
            response_model=builtins.list[dict[str, Any]],
            extra_query=extra_query,
        )

    async def list(
        self,
        company_id: float,
        *,
        filter_is_approved: float | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[dict[str, Any]]:
        """Получить пользователей компании
        Метод позволяет получить пользователей компании.
        Объект имеет следующие поля:
        | Поле  | Тип | Описание |
        | ------------- | ------------- | ------------- |
        |  id  |  number   | Id пользователя   |
        |  name  | string  | Имя пользователя  |
        |  phone  | string  | Телефон пользоватя |
        | email  | string  | Почтовый адрес пользователя |
        | information  | string  | Информация о пользователе |
        |  is_approved  |  boolean | Принял ли пользователь приглашение к управлению филиалом  |
        |  is_non_deletable  |  boolean  | Является ли пользователь неудаляемым  |
        |  user_role_slug  |  string |  Роль пользователя в филиале (доступно только для типа бизнеса "Красота")
        """
        return await self._client.request(
            "GET",
            "/api/v1/company/{company_id}/users",
            path_params={"company_id": company_id},
            params={"filter[is_approved]": filter_is_approved},
            response_model=builtins.list[dict[str, Any]],
            extra_query=extra_query,
        )

    async def delete(
        self,
        company_id: float,
        user_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Удалить пользователя в компании
        """
        return await self._client.request(
            "DELETE",
            "/api/v1/company/{company_id}/users/{user_id}",
            path_params={"company_id": company_id, "user_id": user_id},
            extra_query=extra_query,
        )
