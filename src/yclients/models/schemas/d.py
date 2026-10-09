"""Модели YCLIENTS API (d: D).

Сгенерировано scripts/generate.py -- не редактируйте вручную.
"""

from __future__ import annotations

from datetime import date, datetime
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class DeliveryStatusRequestDataTypesItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: str | None = Field(default=None, alias="id", description="Идентификатор")
    status: float | None = Field(default=None, description="Статус сообщения")
    payment_sum: float | None = Field(default=None, description="Полная стоимость сообщения")
    currency_iso: str | None = Field(default=None, description="ISO валюты платежа (например: RUB, EUR, BYN)")
    parts_amount: float | None = Field(default=None, description="Количество частей сообщения")


class DepositOperationResponseDataTypesDataDepositsTransactionsItemDeposit(BaseModel):
    """Личный счет
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор личного счета")
    deposit_type_id: int | None = Field(default=None, description="Идентификатор типа личного счета")
    salon_group_id: int | None = Field(default=None, description="Идентификатор сети")
    initial_balance: float | None = Field(default=None, description="Начальный баланс")
    balance: float | None = Field(default=None, description="Текущий баланс")
    blocked: bool | None = Field(default=None, description="Заблокирован ли личны счет")
    date_create: str | None = Field(default=None, description="Дата создания")


class DepositOperationResponseDataTypesDataDepositsTransactionsItemDepositType(BaseModel):
    """Тип личного счета
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор типа личного счета")
    salon_group_id: float | None = Field(default=None, description="Идентификатор сети")
    title: str | None = Field(default=None, description="Название типа личного счета")
    date_create: str | None = Field(default=None, description="Дата создания")
    deleted: bool | None = Field(default=None, description="Удален ли тип личного счета")
    date_delete: str | None = Field(default=None, description="Дата удаления")


class DepositOperationResponseDataTypesDataDocumentSalon(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор компании")
    title: str | None = Field(default=None, description="Название компании")
    public_title: str | None = Field(default=None, description="Название компании для отображения на внешних ресурсах")
    business_group_id: float | None = Field(default=None, description="Идентификатор бизнес-группы")
    business_type_id: float | None = Field(default=None, description="Идентификатор бизнес-типа")
    country_id: float | None = Field(default=None, description="Идентификатор страны, в которой расположена компания")
    city_id: float | None = Field(default=None, description="Идентификатор города, в котором расположена компания")
    timezone: float | None = Field(default=None, description="Таймзона компании")
    timezone_name: str | None = Field(default=None, description="Название таймзоны")
    address: str | None = Field(default=None, description="Адрес, по которому расположена компания")
    coordinate_lat: float | None = Field(default=None, description="Широта")
    coordinate_lon: float | None = Field(default=None, description="Долгота")
    logo: str | None = Field(default=None, description="Путь к изображению с логотипом компании")
    zip: str | None = Field(default=None, description="Почтовый индекс")
    phone: str | None = Field(default=None, description="Телефонг")
    phones: list[str] | None = Field(default=None, description="Телефоны")
    site: str | None = Field(default=None, description="Сайт компании")
    allow_delete_record: bool | None = Field(default=None, description="Можно ли удалять запись")
    allow_change_record: bool | None = Field(default=None, description="Можно ли изменять запись")


class DepositOperationResponseDataTypesDataDocumentType(BaseModel):
    """Тип документа
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор типа документа")
    title: str | None = Field(default=None, description="Название типа документа")


class DepositOperationResponseDataTypesDataDocumentUser(BaseModel):
    """Пользователь
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор пользователя")
    name: str | None = Field(default=None, description="Имя пользователя")
    phone: str | None = Field(default=None, description="Телефон пользователя")


class DepositOperationResponseDataTypesDataPaymentTransactionsItemType(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор типа транзакции")
    title: str | None = Field(default=None, description="Название транзакции")


class DeprecatedServicesCompanyidRequestDataTypesStaffItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор сотрудника")
    seance_length: float | None = Field(default=None, description="Длительность оказания услуги (кратно 15 минутам)")


class DeprecatedServicesCompanyidResponseDataTypesDataStaffItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор сотрудника")
    seance_length: float | None = Field(default=None, description="Длительность услуги (кратна 15 минутам)")


class DepositTransaction(BaseModel):
    """Транзакция по личному счету.
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="ID транзакции.")
    salon_id: float | None = Field(default=None, description="ID филиала.")
    salon_group_id: float | None = Field(default=None, description="ID сети.")
    user_id: float | None = Field(default=None, description="Пользователь, на счету которого совершена транзакция.")
    amount: float | None = Field(default=None, description="Сумма транзакции.")
    date_create: str | None = Field(default=None, description="Дата и время создания транзакции.")
    comment: str | None = Field(default=None, description="Комментарий к транзакции.")
    deleted: bool | None = Field(default=None, description="Флаг удалена ли транзакция.")


class DepositTransactionType(BaseModel):
    """Тип транзакции по личному счету.
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="ID типа транзакции.")
    comment: str | None = Field(default=None, description="Название типа транзакции.")


class DeprecatedServicesCompanyidRequestDataTypes(BaseModel):
    """Изменить услугу
    Схема спеки: Root Type for deprecated_services_companyid_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    title: str | None = Field(default=None, description="Название услуги")
    category_id: float | None = Field(default=None, description="ID категории услуг")
    price_min: float | None = Field(default=None, description="Минимальная стоимость услуги")
    price_max: float | None = Field(default=None, description="Максимальная стоимость услуги")
    duration: float | None = Field(default=None, description="Длительность услуги, по умолчанию равна 3600 секундам")
    discount: float | None = Field(default=None, description="Скидка при оказании услуги")
    comment: str | None = Field(default=None, description="Комментарий к услуге")
    weight: float | None = Field(default=None, description="Вес услуги (используется для сортировки услуг при отображении)")
    service_type: float | None = Field(default=None, description="Доступна ли для онлайн записи услуга. 1 - доступна, 0 не доступна.")
    api_service_id: str | None = Field(default=None, description="Внешний идентификатор услуги")
    staff: list[DeprecatedServicesCompanyidRequestDataTypesStaffItem] | None = Field(default=None, description="Сотрудники, оказываюшие услугу и длительность оказания услуги каждым из них")


class DeleteClientSchedulesClientScheduleIdResponse204(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: dict[str, Any] | None = Field(default=None, alias="data")
    meta: dict[str, Any] | None = Field(default=None)


class DeleteCommentsCommentIdResponse204(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: dict[str, Any] | None = Field(default=None, alias="data")
    meta: dict[str, Any] | None = Field(default=None)


class DeleteDaysDayIdResponse204(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: dict[str, Any] | None = Field(default=None, alias="data")
    meta: dict[str, Any] | None = Field(default=None)


class DeleteSchedulesScheduleIdResponse204(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: dict[str, Any] | None = Field(default=None, alias="data")
    meta: dict[str, Any] | None = Field(default=None)


class DeleteStaffMasterIdResponse204(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: dict[str, Any] | None = Field(default=None, alias="data")
    meta: dict[str, Any] | None = Field(default=None)


class DepositOperationResponseDataTypesDataDepositsTransactionsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор депозитной транзакции")
    salon_id: float | None = Field(default=None, description="Идентификатор компании")
    salon_group_id: float | None = Field(default=None, description="Идентификатор сети")
    document_id: float | None = Field(default=None, description="Идентификатор документа")
    deposit_id: float | None = Field(default=None, description="Идентификатор личного счета")
    deposit_type_id: float | None = Field(default=None, description="Идентификатор типа личного счета")
    master_id: float | None = Field(default=None, description="Идентификатор сотрудника")
    user_id: float | None = Field(default=None, description="Идентификатор пользователя")
    amount: float | None = Field(default=None, description="Сумма пополнения")
    comment: str | None = Field(default=None, description="Комментарий")
    date_create: str | None = Field(default=None, description="Дата создания")
    deleted: bool | None = Field(default=None, description="Удалена ли транзакция")
    date_delete: str | None = Field(default=None, description="Дата удаления")
    deposit: DepositOperationResponseDataTypesDataDepositsTransactionsItemDeposit | None = Field(default=None)
    deposit_type: DepositOperationResponseDataTypesDataDepositsTransactionsItemDepositType | None = Field(default=None)


class DepositOperationResponseDataTypesDataDocument(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор документа")
    user_id: float | None = Field(default=None, description="Идентификатор пользователя")
    salon_id: float | None = Field(default=None, description="Идентификатор компании")
    type_id: float | None = Field(default=None, description="Идентификатор типа документа")
    type_: DepositOperationResponseDataTypesDataDocumentType | None = Field(default=None, alias="type")
    comment: str | None = Field(default=None, description="Комментарий")
    number: float | None = Field(default=None, description="Номер документа")
    salon: DepositOperationResponseDataTypesDataDocumentSalon | None = Field(default=None)
    user: DepositOperationResponseDataTypesDataDocumentUser | None = Field(default=None)


class DepositOperationResponseDataTypesDataPaymentTransactionsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор транзакции оплаты")
    document_id: int | None = Field(default=None, description="Идентификатор документа")
    date: str | None = Field(default=None, description="Дата оплаты")
    type_id: float | None = Field(default=None, description="Идентификатор типа документа")
    expense_id: float | None = Field(default=None, description="Идентификатор статьи платежа")
    account_id: float | None = Field(default=None, description="Идентификатор кассы")
    amount: float | None = Field(default=None, description="Сумма транзакции")
    client_id: float | None = Field(default=None, description="Идентификатор клиента")
    master_id: float | None = Field(default=None, description="Идентификатор сотрудника")
    supplier_id: float | None = Field(default=None, description="Идентификатор поставщика")
    comment: str | None = Field(default=None, description="Комментарий")
    item_id: int | None = Field(default=None)
    target_type_id: int | None = Field(default=None)
    record_id: int | None = Field(default=None, description="Идентификатор записи")
    goods_transaction_id: int | None = Field(default=None, description="Идентификатор товарной транзакции")
    type_: DepositOperationResponseDataTypesDataPaymentTransactionsItemType | None = Field(default=None, alias="type")


class DeprecatedServicesCompanyidResponseDataTypesData(BaseModel):
    """Объект с данными
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор услуги")
    salon_service_id: float | None = Field(default=None, description="Идентификатор услуги для компании в сети")
    title: str | None = Field(default=None, description="Название услуги")
    category_id: float | None = Field(default=None, description="Идентификатор категории, в которой состоит услуги")
    price_min: float | None = Field(default=None, description="Минимальная цена на услугу")
    price_max: float | None = Field(default=None, description="Максимальная цена на услугу")
    duration: float | None = Field(default=None, description="Длительность услуги, по умолчанию равна 3600 секундам")
    discount: float | None = Field(default=None, description="Скидка")
    comment: str | None = Field(default=None, description="Комментарий к услуге")
    weight: float | None = Field(default=None, description="Вес услуги (используется для сортировки категорий при отображении)")
    active: float | None = Field(default=None, description="1 - доступна для онлайн записи, 0 - не доступна")
    api_id: str | None = Field(default=None, description="Внедний идентификатор услуги")
    staff: list[DeprecatedServicesCompanyidResponseDataTypesDataStaffItem] | None = Field(default=None, description="Список сотрудников, оказывающих услугу и длительность сеанса")


class DeprecatedServicesCompanyidResponseDataTypes(BaseModel):
    """Изменить услугу
    Схема спеки: Root Type for deprecated_services_companyid_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: DeprecatedServicesCompanyidResponseDataTypesData | None = Field(default=None, alias="data")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")


class DepositOperationResponseDataTypesData(BaseModel):
    """Объект с данными
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    document: DepositOperationResponseDataTypesDataDocument | None = Field(default=None)
    deposits_transactions: list[DepositOperationResponseDataTypesDataDepositsTransactionsItem] | None = Field(default=None, description="Депозитная транзакция")
    payment_transactions: list[DepositOperationResponseDataTypesDataPaymentTransactionsItem] | None = Field(default=None, description="Транзакция оплаты")


class DepositOperationResponseDataTypes(BaseModel):
    """Создание операции поплонения личного счета
    Схема спеки: Root Type for deposit_operation_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: DepositOperationResponseDataTypesData | None = Field(default=None, alias="data")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")

__all__ = [
    "DeleteClientSchedulesClientScheduleIdResponse204",
    "DeleteCommentsCommentIdResponse204",
    "DeleteDaysDayIdResponse204",
    "DeleteSchedulesScheduleIdResponse204",
    "DeleteStaffMasterIdResponse204",
    "DeliveryStatusRequestDataTypesItem",
    "DepositOperationResponseDataTypes",
    "DepositOperationResponseDataTypesData",
    "DepositOperationResponseDataTypesDataDepositsTransactionsItem",
    "DepositOperationResponseDataTypesDataDepositsTransactionsItemDeposit",
    "DepositOperationResponseDataTypesDataDepositsTransactionsItemDepositType",
    "DepositOperationResponseDataTypesDataDocument",
    "DepositOperationResponseDataTypesDataDocumentSalon",
    "DepositOperationResponseDataTypesDataDocumentType",
    "DepositOperationResponseDataTypesDataDocumentUser",
    "DepositOperationResponseDataTypesDataPaymentTransactionsItem",
    "DepositOperationResponseDataTypesDataPaymentTransactionsItemType",
    "DepositTransaction",
    "DepositTransactionType",
    "DeprecatedServicesCompanyidRequestDataTypes",
    "DeprecatedServicesCompanyidRequestDataTypesStaffItem",
    "DeprecatedServicesCompanyidResponseDataTypes",
    "DeprecatedServicesCompanyidResponseDataTypesData",
    "DeprecatedServicesCompanyidResponseDataTypesDataStaffItem"
]
