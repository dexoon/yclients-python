"""Модели YCLIENTS API (z: Z).

Сгенерировано scripts/generate.py -- не редактируйте вручную.
"""

from __future__ import annotations

from datetime import date, datetime
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class ZReportResponseDataTypesDataPaidsAccountsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    title: str | None = Field(default=None, description="Название кассы")
    amount: int | None = Field(default=None, description="Сумма")


class ZReportResponseDataTypesDataPaidsDiscountItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    title: str | None = Field(default=None, description="Название скидки/акции")
    amount: float | None = Field(default=None, description="Сумма")


class ZReportResponseDataTypesDataPaidsTotal(BaseModel):
    """Итог
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    accounts: float | None = Field(default=None, description="Суммы по всем кассам")
    discount: float | None = Field(default=None, description="Сумма, оплаченная всей лояльностью")


class ZReportResponseDataTypesDataStats(BaseModel):
    """Общая статистика
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    clients: int | None = Field(default=None, description="Количество клиентов")
    clients_average: float | None = Field(default=None, description="Среддняя оплата по клиентам")
    records: int | None = Field(default=None, description="Количество записей")
    records_average: float | None = Field(default=None, description="Среддняя оплата по записям")
    visit_records: int | None = Field(default=None, description="Количество записей с клиентами")
    visit_records_average: float | None = Field(default=None, description="Среддняя оплата по записям с клиентами")
    non_visit_records: int | None = Field(default=None, description="Количество записей без клиентов")
    non_visit_records_average: int | None = Field(default=None, description="Среддняя оплата по записям без клиентов")
    targets: int | None = Field(default=None, description="Количество услуг")
    targets_paid: int | None = Field(default=None, description="Оплата по услугам")
    goods: int | None = Field(default=None, description="Количество товаров")
    goods_paid: float | None = Field(default=None, description="Оплата по товарам")
    certificates: int | None = Field(default=None, description="Количество сертификатов")
    certificates_paid: int | None = Field(default=None, description="Оплата по сертификатам")
    abonement: int | None = Field(default=None, description="Количество абонементов")
    abonement_paid: int | None = Field(default=None, description="Оплата по абонементам")


class ZReportResponseDataTypesDataZDataParam1481101200ItemMastersItemGoodItemTransactionsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    accounts_amount: float | None = Field(default=None, description="Сумма, оплаченная в кассу")
    loyalty_amount: int | None = Field(default=None, description="Сумма, оплаченная лояльностью")
    payment_type: str | None = Field(default=None, description="Тип оплаты")


class ZReportResponseDataTypesDataZDataParam1481101200ItemMastersItemOthersTransactionsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    accounts_amount: float | None = Field(default=None, description="Сумма, оплаченная в кассу")
    loyalty_amount: int | None = Field(default=None, description="Сумма, оплаченная лояльностью")
    payment_type: str | None = Field(default=None, description="Тип оплаты")


class ZReportResponseDataTypesDataZDataParam1481101200ItemMastersItemServiceItemTransactionsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    accounts_amount: float | None = Field(default=None, description="Сумма, оплаченная в кассу")
    loyalty_amount: float | None = Field(default=None, description="Сумма, оплаченная лояльностью")
    payment_type: str | None = Field(default=None, description="Тип оплаты")


class ZReportResponseDataTypesDataPaids(BaseModel):
    """Оплаты
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    accounts: list[ZReportResponseDataTypesDataPaidsAccountsItem] | None = Field(default=None, description="Оплаты в кассы")
    discount: list[ZReportResponseDataTypesDataPaidsDiscountItem] | None = Field(default=None, description="Оплата по скидке и лояльности")
    total: ZReportResponseDataTypesDataPaidsTotal | None = Field(default=None)


class ZReportResponseDataTypesDataZDataParam1481101200ItemMastersItemGoodItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    item_title: str | None = Field(default=None, description="Название товара")
    first_cost: float | None = Field(default=None, description="Начальная стоимость")
    discount: float | None = Field(default=None, description="Скидка")
    result_cost: float | None = Field(default=None, description="Итоговая стоимость")
    transactions: list[ZReportResponseDataTypesDataZDataParam1481101200ItemMastersItemGoodItemTransactionsItem] | None = Field(default=None, description="Транзакции")


class ZReportResponseDataTypesDataZDataParam1481101200ItemMastersItemOthers(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    item_title: str | None = Field(default=None, description="Название товара/услуги")
    first_cost: float | None = Field(default=None, description="Начальная стоимость")
    discount: float | None = Field(default=None, description="Скидка")
    result_cost: float | None = Field(default=None, description="Итоговая стоимость")
    transactions: list[ZReportResponseDataTypesDataZDataParam1481101200ItemMastersItemOthersTransactionsItem] | None = Field(default=None, description="Транзакции")


class ZReportResponseDataTypesDataZDataParam1481101200ItemMastersItemServiceItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    item_title: str | None = Field(default=None, description="Название услуги")
    first_cost: float | None = Field(default=None, description="Начальная стоимость")
    discount: float | None = Field(default=None, description="Скидка")
    result_cost: float | None = Field(default=None, description="Итоговая стоимость")
    transactions: list[ZReportResponseDataTypesDataZDataParam1481101200ItemMastersItemServiceItemTransactionsItem] | None = Field(default=None, description="Транзакции")


class ZReportResponseDataTypesDataZDataParam1481101200ItemMastersItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    master_id: float | None = Field(default=None, description="Идентификатор сотрудника")
    master_name: str | None = Field(default=None, description="Имя сотрудника")
    service: list[ZReportResponseDataTypesDataZDataParam1481101200ItemMastersItemServiceItem] | None = Field(default=None, description="Услуги")
    good: list[ZReportResponseDataTypesDataZDataParam1481101200ItemMastersItemGoodItem] | None = Field(default=None, description="Товары")
    others: ZReportResponseDataTypesDataZDataParam1481101200ItemMastersItemOthers | None = Field(default=None)


class ZReportResponseDataTypesDataZDataParam1481101200Item(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    client_id: float | None = Field(default=None, description="Идентификатор клиента")
    client_name: str | None = Field(default=None, description="Имя клиента")
    client_phone: str | None = Field(default=None, description="Телефон клиента")
    client_email: str | None = Field(default=None, description="Email адрес клиента")
    masters: list[ZReportResponseDataTypesDataZDataParam1481101200ItemMastersItem] | None = Field(default=None, description="Сотрудники")


class ZReportResponseDataTypesDataZData(BaseModel):
    """Данные отчет
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    param_1481101200: list[ZReportResponseDataTypesDataZDataParam1481101200Item] | None = Field(default=None, alias="1481101200")


class ZReportResponseDataTypesData(BaseModel):
    """Объект с данными
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    stats: ZReportResponseDataTypesDataStats | None = Field(default=None)
    paids: ZReportResponseDataTypesDataPaids | None = Field(default=None)
    z_data: ZReportResponseDataTypesDataZData | None = Field(default=None)
    currency: str | None = Field(default=None, description="Валюта")


class ZReportResponseDataTypes(BaseModel):
    """Получить данные Z-Отчета
    Схема спеки: Root Type for z_report_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: ZReportResponseDataTypesData | None = Field(default=None, alias="data")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")

__all__ = [
    "ZReportResponseDataTypes",
    "ZReportResponseDataTypesData",
    "ZReportResponseDataTypesDataPaids",
    "ZReportResponseDataTypesDataPaidsAccountsItem",
    "ZReportResponseDataTypesDataPaidsDiscountItem",
    "ZReportResponseDataTypesDataPaidsTotal",
    "ZReportResponseDataTypesDataStats",
    "ZReportResponseDataTypesDataZData",
    "ZReportResponseDataTypesDataZDataParam1481101200Item",
    "ZReportResponseDataTypesDataZDataParam1481101200ItemMastersItem",
    "ZReportResponseDataTypesDataZDataParam1481101200ItemMastersItemGoodItem",
    "ZReportResponseDataTypesDataZDataParam1481101200ItemMastersItemGoodItemTransactionsItem",
    "ZReportResponseDataTypesDataZDataParam1481101200ItemMastersItemOthers",
    "ZReportResponseDataTypesDataZDataParam1481101200ItemMastersItemOthersTransactionsItem",
    "ZReportResponseDataTypesDataZDataParam1481101200ItemMastersItemServiceItem",
    "ZReportResponseDataTypesDataZDataParam1481101200ItemMastersItemServiceItemTransactionsItem"
]
