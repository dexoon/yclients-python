"""Модели YCLIENTS API (e: E).

Сгенерировано scripts/generate.py -- не редактируйте вручную.
"""

from __future__ import annotations

from datetime import date, datetime
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class EmailClientsByFilterRequestDataTypes(BaseModel):
    """Отправить Email рассылку по клиентам, подходящим под фильтры
    Схема спеки: Root Type for email_clients_by_filter_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    subject: str = Field(description="Тема Email сообщения")
    text: str = Field(description="Текст Email сообщения")


class EmailClientsByIdRequestDataTypes(BaseModel):
    """Отправить Email рассылку по списку клиентов
    Схема спеки: Root Type for email_clients_by_id_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    client_ids: list[float] = Field(description="Массив идентификаторов клиентов")
    subject: str = Field(description="Тема Email сообщения")
    text: str = Field(description="Текст Email сообщения")

__all__ = [
    "EmailClientsByFilterRequestDataTypes",
    "EmailClientsByIdRequestDataTypes"
]
