"""Модели YCLIENTS API (f: F).

Сгенерировано scripts/generate.py -- не редактируйте вручную.
"""

from __future__ import annotations

from datetime import date, datetime
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class FinanceTransactionResponseDataTypesDataAccount(BaseModel):
    """Касса
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор кассы")
    title: str | None = Field(default=None, description="Название кассы")
    is_cash: bool | None = Field(default=None, description="Является ли наличной")
    is_default: bool | None = Field(default=None, description="Является ли кассой по умолчанию")


class FinanceTransactionResponseDataTypesDataClient(BaseModel):
    """Клиент
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор клиента")
    name: str | None = Field(default=None, description="Имя клиента")
    phone: str | None = Field(default=None, description="Телефон клиента")
    email: str | None = Field(default=None, description="Email клиента")


class FinanceTransactionResponseDataTypesDataExpense(BaseModel):
    """Тип платежа
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор типа платежа")
    title: str | None = Field(default=None, description="Название типа платежа")


class FinanceTransactionResponseDataTypesDataMaster(BaseModel):
    """Сотрудник
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор сотрудника")
    name: str | None = Field(default=None, description="Имя сотрудника")


class FinanceTransactionRequestDataTypes(BaseModel):
    """Создание финансовой транзакции
    Схема спеки: Root Type for finance_transaction_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    expense_id: float | None = Field(default=None, description="Статья платежа")
    amount: float | None = Field(default=None, description="Сумма транзакции")
    account_id: float | None = Field(default=None, description="Идентификатор кассы")
    client_id: float | None = Field(default=None, description="Идентификатор клиента")
    supplier_id: float | None = Field(default=None, description="Идентификатор контрагента")
    master_id: float | None = Field(default=None, description="Идентификатор сотрудника")
    comment: float | None = Field(default=None, description="Комментарий")
    date: str | None = Field(default=None, description="Дата создания транзакции")


class FinanceTransactionResponseDataTypesData(BaseModel):
    """Объект с данными
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор транзакции")
    document_id: float | None = Field(default=None, description="Идентификатор документа")
    date: str | None = Field(default=None, description="Дата создания транзакции")
    type_id: float | None = Field(default=None, description="Идентификатор типа платежа")
    expense_id: float | None = Field(default=None, description="Идентификатор статьи платежа")
    account_id: float | None = Field(default=None, description="Идентификатор кассы")
    amount: float | None = Field(default=None, description="Сумма транзакции")
    client_id: float | None = Field(default=None, description="Идентификатор клиента")
    master_id: float | None = Field(default=None, description="Идентификатор сотрудника")
    supplier_id: float | None = Field(default=None, description="Идентификатор контрагента")
    comment: str | None = Field(default=None, description="Комментарий")
    item_id: int | None = Field(default=None)
    target_type_id: int | None = Field(default=None)
    record_id: float | None = Field(default=None, description="Идентификатор записи")
    goods_transaction_id: float | None = Field(default=None, description="Идентификатор товарной транзакции")
    expense: FinanceTransactionResponseDataTypesDataExpense | None = Field(default=None)
    account: FinanceTransactionResponseDataTypesDataAccount | None = Field(default=None)
    client_: FinanceTransactionResponseDataTypesDataClient | None = Field(default=None, alias="client")
    master: FinanceTransactionResponseDataTypesDataMaster | None = Field(default=None)
    supplier: list[dict[str, Any]] | None = Field(default=None, description="Контрагент")


class FinanceTransactionResponseDataTypes(BaseModel):
    """Создание финансовой транзакции
    Схема спеки: Root Type for finance_transaction_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: FinanceTransactionResponseDataTypesData | None = Field(default=None, alias="data")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")

__all__ = [
    "FinanceTransactionRequestDataTypes",
    "FinanceTransactionResponseDataTypes",
    "FinanceTransactionResponseDataTypesData",
    "FinanceTransactionResponseDataTypesDataAccount",
    "FinanceTransactionResponseDataTypesDataClient",
    "FinanceTransactionResponseDataTypesDataExpense",
    "FinanceTransactionResponseDataTypesDataMaster"
]
