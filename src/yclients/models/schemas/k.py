"""Модели YCLIENTS API (k: K).

Сгенерировано scripts/generate.py -- не редактируйте вручную.
"""

from __future__ import annotations

from datetime import date, datetime
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class KkmTransactionsPrintResponseDataTypeDataKkmTransactionsItemCashier(BaseModel):
    """Кассир
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор сотрудника")
    name: str | None = Field(default=None, description="Имя сотрудника")


class KkmTransactionsPrintResponseDataTypeDataKkmTransactionsItemDocument(BaseModel):
    """Документ транзакции
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор документа")
    type_: int | None = Field(default=None, alias="type", description="Идентификатор типа документа")
    type_title: str | None = Field(default=None, description="Название сущности, которой принадлежит документ")


class KkmTransactionsPrintResponseDataTypeDataKkmTransactionsItemStatus(BaseModel):
    """Статус печати чека
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор статуса")
    title: str | None = Field(default=None, description="Название статуса")


class KkmTransactionsPrintResponseDataTypeDataKkmTransactionsItemType(BaseModel):
    """Тип операции
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор типа операции")
    title: str | None = Field(default=None, description="Название операции")


class KkmTransactionsResponseDataTypeDataItemCashier(BaseModel):
    """Кассир
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор сотрудника")
    name: str | None = Field(default=None, description="Имя сотрудника")


class KkmTransactionsResponseDataTypeDataItemDocument(BaseModel):
    """Документ транзакции
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор документа")
    type_: int | None = Field(default=None, alias="type", description="Идентификатор типа документа")
    type_title: str | None = Field(default=None, description="Название сущности, которой принадлежит документ")


class KkmTransactionsResponseDataTypeDataItemStatus(BaseModel):
    """Статус печати чека
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор статуса")
    title: str | None = Field(default=None, description="Название статуса")


class KkmTransactionsResponseDataTypeDataItemType(BaseModel):
    """Тип операции
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор типа операции")
    title: str | None = Field(default=None, description="Название операции")


class KkmTransactionsResponseDataTypeMeta(BaseModel):
    """Метаданные (содержит количество найденных транзакций)
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    count_: int | None = Field(default=None, alias="count")


class KkmTransactionsPrintResponseDataTypeDataKkmTransactionsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор транзакции")
    print_date: str | None = Field(default=None, description="Дата печати чека")
    printed_count: float | None = Field(default=None, description="Количество напечатанных чеков")
    sum: int | None = Field(default=None, description="Сумма")
    type_: KkmTransactionsPrintResponseDataTypeDataKkmTransactionsItemType | None = Field(default=None, alias="type")
    status: KkmTransactionsPrintResponseDataTypeDataKkmTransactionsItemStatus | None = Field(default=None)
    document: KkmTransactionsPrintResponseDataTypeDataKkmTransactionsItemDocument | None = Field(default=None)
    cashier: KkmTransactionsPrintResponseDataTypeDataKkmTransactionsItemCashier | None = Field(default=None)


class KkmTransactionsResponseDataTypeDataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор транзакции")
    print_date: str | None = Field(default=None, description="Дата печати чека")
    printed_count: float | None = Field(default=None, description="Количество напечатанных чеков")
    sum: int | None = Field(default=None, description="Сумма")
    type_: KkmTransactionsResponseDataTypeDataItemType | None = Field(default=None, alias="type")
    status: KkmTransactionsResponseDataTypeDataItemStatus | None = Field(default=None)
    document: KkmTransactionsResponseDataTypeDataItemDocument | None = Field(default=None)
    cashier: KkmTransactionsResponseDataTypeDataItemCashier | None = Field(default=None)


class KkmTransactionsResponseDataType(BaseModel):
    """Получить транзакции
    Схема спеки: Root Type for kkm_transactions_response_data_type
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: list[KkmTransactionsResponseDataTypeDataItem] | None = Field(default=None, alias="data", description="Массив объектов с данными")
    meta: KkmTransactionsResponseDataTypeMeta | None = Field(default=None)


class KkmTransactionsPrintResponseDataTypeData(BaseModel):
    """Массив объектов с данными
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    kkm_type: int | None = Field(default=None, description="Тип операции ККМ")
    kkm_transactions: list[KkmTransactionsPrintResponseDataTypeDataKkmTransactionsItem] | None = Field(default=None)
    status: int | None = Field(default=None)
    bill_json: list[dict[str, Any]] | None = Field(default=None)


class KkmTransactionsPrintResponseDataType(BaseModel):
    """Напечатать чек
    Схема спеки: Root Type for kkm_transactions_print_response_data_type
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: KkmTransactionsPrintResponseDataTypeData | None = Field(default=None, alias="data")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")

__all__ = [
    "KkmTransactionsPrintResponseDataType",
    "KkmTransactionsPrintResponseDataTypeData",
    "KkmTransactionsPrintResponseDataTypeDataKkmTransactionsItem",
    "KkmTransactionsPrintResponseDataTypeDataKkmTransactionsItemCashier",
    "KkmTransactionsPrintResponseDataTypeDataKkmTransactionsItemDocument",
    "KkmTransactionsPrintResponseDataTypeDataKkmTransactionsItemStatus",
    "KkmTransactionsPrintResponseDataTypeDataKkmTransactionsItemType",
    "KkmTransactionsResponseDataType",
    "KkmTransactionsResponseDataTypeDataItem",
    "KkmTransactionsResponseDataTypeDataItemCashier",
    "KkmTransactionsResponseDataTypeDataItemDocument",
    "KkmTransactionsResponseDataTypeDataItemStatus",
    "KkmTransactionsResponseDataTypeDataItemType",
    "KkmTransactionsResponseDataTypeMeta"
]
