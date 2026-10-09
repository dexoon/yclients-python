"""Модели YCLIENTS API (n: N).

Сгенерировано scripts/generate.py -- не редактируйте вручную.
"""

from __future__ import annotations

from datetime import date, datetime
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class NotificationSettingsNotificationTypesDataTypeDataItemChannels(BaseModel):
    """Каналы, по которым будут отправляться уведомления
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    push: int | None = Field(default=None, description="PUSH-уведомления")
    sms: int | None = Field(default=None, description="SMS-уведомления")
    email: int | None = Field(default=None, description="Email-уведомления")


class NotificationSettingsNotificationTypesDataTypeMeta(BaseModel):
    """Метаданные (содержит количество объектов)
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    count_: int | None = Field(default=None, alias="count")


class NotificationSettingsUsersDataTypeDataNotificationTypesItemChannels(BaseModel):
    """Каналы, по которым будут отправляться уведомления
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    push: int | None = Field(default=None, description="PUSH-уведомления")
    sms: int | None = Field(default=None, description="SMS-уведомления")
    email: int | None = Field(default=None, description="Email-уведомления")


class NotificationSettingsUsersRequestDataTypeNotificationTypesItemChannels(BaseModel):
    """Канал, по которому будет отправляться уведомление
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    push: int | None = Field(default=None, description="PUSH-уведомление")


class NotificationSettingsNotificationTypesDataTypeDataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    type_: str | None = Field(default=None, alias="type", description="Тип уведомления")
    channels: NotificationSettingsNotificationTypesDataTypeDataItemChannels | None = Field(default=None)


class NotificationSettingsUsersDataTypeDataNotificationTypesItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    type_: Literal["record_create_online_staff", "record_create_offline_staff", "record_delete_staff", "record_move_staff", "record_create_online_admin", "record_create_offline_admin", "record_delete_admin", "record_move_admin", "license_expire"] | None = Field(default=None, alias="type", description="Тип уведомления")
    channels: NotificationSettingsUsersDataTypeDataNotificationTypesItemChannels | None = Field(default=None)


class NotificationSettingsUsersRequestDataTypeNotificationTypesItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    type_: Literal["record_create_online_staff", "record_create_offline_staff", "record_delete_staff", "record_move_staff", "record_create_online_admin", "record_create_offline_admin", "record_delete_admin", "record_move_admin", "license_expire"] | None = Field(default=None, alias="type", description="Тип уведомления")
    channels: NotificationSettingsUsersRequestDataTypeNotificationTypesItemChannels | None = Field(default=None)


class NotificationSettingsNotificationTypesDataType(BaseModel):
    """Настройки уведомлений филиала
    Схема спеки: Root Type for notification_settings_notification_types_data_type
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения")
    data_: list[NotificationSettingsNotificationTypesDataTypeDataItem] | None = Field(default=None, alias="data", description="Массив объектов")
    meta: NotificationSettingsNotificationTypesDataTypeMeta | None = Field(default=None)


class NotificationSettingsUsersRequestDataType(BaseModel):
    """Изменить настройки PUSH-уведомлений пользователя
    Схема спеки: Root Type for notification_settings_users_request_data_type
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    notification_types: list[NotificationSettingsUsersRequestDataTypeNotificationTypesItem] | None = Field(default=None, description="Массив объектов")


class NotificationSettingsUsersDataTypeData(BaseModel):
    """Объект с данными
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    mode: Literal["admin", "staff", "disabled"] | None = Field(default=None, description="Тип уведомления (для сотрудника/для администратора)")
    notification_types: list[NotificationSettingsUsersDataTypeDataNotificationTypesItem] | None = Field(default=None)


class NotificationSettingsUsersDataType(BaseModel):
    """Получить настройки уведомлений пользователя
    Схема спеки: Root Type for notification_settings_users_data_type
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения")
    data_: NotificationSettingsUsersDataTypeData | None = Field(default=None, alias="data")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")

__all__ = [
    "NotificationSettingsNotificationTypesDataType",
    "NotificationSettingsNotificationTypesDataTypeDataItem",
    "NotificationSettingsNotificationTypesDataTypeDataItemChannels",
    "NotificationSettingsNotificationTypesDataTypeMeta",
    "NotificationSettingsUsersDataType",
    "NotificationSettingsUsersDataTypeData",
    "NotificationSettingsUsersDataTypeDataNotificationTypesItem",
    "NotificationSettingsUsersDataTypeDataNotificationTypesItemChannels",
    "NotificationSettingsUsersRequestDataType",
    "NotificationSettingsUsersRequestDataTypeNotificationTypesItem",
    "NotificationSettingsUsersRequestDataTypeNotificationTypesItemChannels"
]
