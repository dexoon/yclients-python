"""Общие модели: конверт ответов, постраничная выдача."""

from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel

T = TypeVar("T")

__all__ = ["Page", "ValidationErrorItem"]


class Page(BaseModel, Generic[T]):
    """Постраничный результат запроса.

    Возвращается методами, у которых API отдаёт ``meta.count``.

    Атрибуты:
        data: элементы текущей страницы.
        count: общее количество найденных записей (если API его передал).
    """

    data: list[T]
    count: int | None = None


class ValidationErrorItem(BaseModel):
    """Одна ошибка валидации из ``meta.errors``."""

    field: str
    message: str


class ApiEnvelope(BaseModel):
    """Сырой конверт ответа YCLIENTS API."""

    success: bool
    data: Any = None
    meta: Any = None
