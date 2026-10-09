"""UsersApi -- сгенерированные методы API."""

from __future__ import annotations

from typing import Any, Literal

from yclients._base import BaseClient
from yclients.models.schemas import (
    PostUserIdCopyToCompaniesRequest,
    PostUserIdRemoveFromCompaniesRequest,
    PutUserIdPermissionsRequest,
    UserRolePermissions,
    UserRoleWithSalonAndUser,
)


class UsersApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def list_roles(
        self,
        company_id: float,
        *,
        include: list[Literal["user_permissions"]] | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> list[UserRoleWithSalonAndUser]:
        """Получение списка ролей пользователей
        Возвращает список ролей пользователей вместе с правами для каждой роли.
        """
        return await self._client.request(
            "GET",
            "/api/v1/company/{company_id}/users/roles",
            path_params={"company_id": company_id},
            params={"include": include},
            response_model=list[UserRoleWithSalonAndUser],
            extra_query=extra_query,
        )

    async def list_user_roles(
        self,
        company_id: float,
        user_id: float,
        *,
        include: list[Literal["user_permissions"]] | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> list[UserRoleWithSalonAndUser]:
        """Получение списка ролей в контексте существующего пользователя
        Возвращает список ролей пользователей вместе с правами для каждой роли. Позволяет увидеть возможность изменить конкретные права (поле `is_editable`) у существующего пользователя филиала в зависимости от набора прав пользователя, от имени которого выполняется запрос.
        """
        return await self._client.request(
            "GET",
            "/api/v1/company/{company_id}/users/{user_id}/roles",
            path_params={"company_id": company_id, "user_id": user_id},
            params={"include": include},
            response_model=list[UserRoleWithSalonAndUser],
            extra_query=extra_query,
        )

    async def get_permissions(
        self,
        company_id: float,
        user_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> UserRolePermissions:
        """Получение значений прав и роли пользователя
        Возвращает роль пользователя и список прав со значениями.
        """
        return await self._client.request(
            "GET",
            "/api/v1/company/{company_id}/users/{user_id}/permissions",
            path_params={"company_id": company_id, "user_id": user_id},
            response_model=UserRolePermissions,
            extra_query=extra_query,
        )

    async def update_permissions(
        self,
        company_id: float,
        user_id: float,
        data: PutUserIdPermissionsRequest,
        extra_query: dict[str, Any] | None = None
    ) -> UserRolePermissions:
        """Обновление прав и роли пользователя
        Обновляет роль и права пользователя, а так же сотрудника который к этому пользователю прикреплен.
        """
        return await self._client.request(
            "PUT",
            "/api/v1/company/{company_id}/users/{user_id}/permissions",
            path_params={"company_id": company_id, "user_id": user_id},
            json_body=data,
            response_model=UserRolePermissions,
            extra_query=extra_query,
        )

    async def copy_to_companies(
        self,
        company_id: float,
        user_id: float,
        data: PostUserIdCopyToCompaniesRequest,
        extra_query: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Копирование пользователя в филиалы
        Копирует пользователя с правами в несколько указанных филиалов. Если пользователя ранее не было в этих филиалах, он будет добавлен в них как активный. Если пользователь был приглашен в филиал, будут обновлены только его права, пользователю по-прежнему будет необходимо принять приглашение.
        """
        return await self._client.request(
            "POST",
            "/api/v1/company/{company_id}/users/{user_id}/copy_to_companies",
            path_params={"company_id": company_id, "user_id": user_id},
            json_body=data,
            response_model=dict[str, Any],
            extra_query=extra_query,
        )

    async def remove_from_companies(
        self,
        company_id: float,
        user_id: float,
        data: PostUserIdRemoveFromCompaniesRequest,
        extra_query: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Удаление пользователя из филиалов
        Удаляет пользователя из нескольких указанных филиалов.
        """
        return await self._client.request(
            "POST",
            "/api/v1/company/{company_id}/users/{user_id}/remove_from_companies",
            path_params={"company_id": company_id, "user_id": user_id},
            json_body=data,
            response_model=dict[str, Any],
            extra_query=extra_query,
        )
