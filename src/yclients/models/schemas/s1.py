"""Модели YCLIENTS API (s1: S).

Сгенерировано scripts/generate.py -- не редактируйте вручную.
"""

from __future__ import annotations

from datetime import date, datetime
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class SalaryStaffSchemeSalaryScheme(BaseModel):
    """Схема расчёта зарплаты.
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор схемы расчёта зарплаты.")
    title: str | None = Field(default=None, description="Название схемы расчёта зарплаты.")


class SearchForActivityItemAttributesStatus(BaseModel):
    """Информация о статусе абонемента
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: Literal[1, 2] | None = Field(default=None, alias="id", description="Идентификатор статуса абонемента `1 = Выпущен, 2 - Активирован`. Просроченые или исчерпанные абонементы в данном запросе не возвращаются.")
    slug: Literal["active", "created"] | None = Field(default=None, description="слаг статуса абонемента")
    title: Literal["Выпущен", "Активирован"] | None = Field(default=None, description="Статус абонемента")
    extended_title: str | None = Field(default=None, description="Расширенный статус абонемента.")


class SearchForActivityItemRelationshipsLoyaltyAbonementAvailabilityIntervalDataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    type_: str | None = Field(default=None, alias="type", description="Указывает на включение настроек ограничения применений абонемента")
    id_: str | None = Field(default=None, alias="id", description="Идентификатор настроек ограничения применений по абонемента")


class SearchForActivityItemRelationshipsLoyaltyAbonementTypeData(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    type_: str | None = Field(default=None, alias="type", description="Указывает на включение типа абонемента")
    id_: str | None = Field(default=None, alias="id", description="Идентификатор типа абонемента")


class ServiceCategoriesCompanyidResponseDataTypesData(BaseModel):
    """Объект с данными
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор категории")
    salon_service_id: float | None = Field(default=None, description="Идентификатор категории для компании в сети")
    title: str | None = Field(default=None, description="Название категории")
    api_id: str | None = Field(default=None, description="Внешний идентификатор категории")
    weight: float | None = Field(default=None, description="Вес категории (используется для сортировки категорий при отображении)")
    staff: list[float] | None = Field(default=None, description="Список ID сотрудников, оказывающих услугу из категории")


class ServicesChangeCompanyidRequestDataTypesStaffItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор сотрудника")
    seance_length: float | None = Field(default=None, description="Длительность оказания услуги (кратно 15 минутам)")


class ServicesChangeCompanyidResponseDataTypesDataStaffItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор сотрудника")
    seance_length: float | None = Field(default=None, description="Длительность оказания услуги (кратно 15 минутам)")


class ServicesCompanyidLinksRequestDataTypesMasterSettingsItemPrice(BaseModel):
    """Цена услуги для данного мастера, если она отличается от цены услуги по умолчанию (для этого указать NULL)
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    min: Any | None = Field(default=None, description="Цена услуги \"от\"")
    max: Any | None = Field(default=None, description="Цена услуги \"до\"")


class ServicesCompanyidLinksRequestDataTypesTranslationsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    language_id: float | None = Field(default=None, description="ID языка для перевода")
    translation: str | None = Field(default=None, description="Текст который будет выведен в названии при выбранном языке")


class ServicesCompanyidRequestDataTypesStaffItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор сотрудника")
    seance_length: float | None = Field(default=None, description="Длительность оказания услуги (кратно 15 минутам)")


class ServicesCompanyidResponseDataTypesDataStaffItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор сотрудника")
    seance_length: float | None = Field(default=None, description="Длительность услуги (кратна 15 минутам)")


class SmsClientsByIdResponseDataTypesMeta(BaseModel):
    """Объект, содержащий сообщение 201 статус-кода
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    message: str | None = Field(default=None)


class StorageOperationDocumentsResponseDataTypesDataCompany(BaseModel):
    """Компания
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор компании")
    title: str | None = Field(default=None, description="Название компании")
    country_id: float | None = Field(default=None, description="Идентификатор страны")
    city_id: float | None = Field(default=None, description="Идентификатор города")
    timezone: str | None = Field(default=None, description="Таймзона")
    address: str | None = Field(default=None, description="Адрес компании")
    coordinate_lat: str | None = Field(default=None, description="Широта")
    coordinate_lon: str | None = Field(default=None, description="Долгота")
    logo: str | None = Field(default=None, description="Пусть, по которому расположен логотип компании")
    zip: str | None = Field(default=None, description="Почтовый индекс")
    phones: list[dict[str, Any]] | None = Field(default=None, description="Телефон компании")
    site: str | None = Field(default=None, description="Сайт компании")


class StorageOperationDocumentsResponseDataTypesDataStorage(BaseModel):
    """Склад
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор склада")
    title: str | None = Field(default=None, description="Название склада")


class StorageOperationDocumentsResponseDataTypesDataType(BaseModel):
    """Тип документа
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор типа документа")
    title: str | None = Field(default=None, description="Название типа документа")


class StorageOperationDocumentsResponseDataTypesDataUser(BaseModel):
    """Пользователь
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор пользователя")
    name: str | None = Field(default=None, description="Имя пользователя")
    phone: str | None = Field(default=None, description="Телефон пользователя")


class StorageOperationFinanceTransactionResponseDataTypesDataItemAccount(BaseModel):
    """Касса
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор кассы")
    title: str | None = Field(default=None, description="Название кассы")
    type_id: float | None = Field(default=None, description="Идентификатор типа транзакции")
    type_: float | None = Field(default=None, alias="type", description="Тип транзакции")
    comment: str | None = Field(default=None, description="Комментарий")
    company_id: float | None = Field(default=None, description="Идентификатор компании")


class StorageOperationFinanceTransactionResponseDataTypesDataItemClient(BaseModel):
    """Клиент
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор клиента")
    name: str | None = Field(default=None, description="Имя клиента")
    phone: str | None = Field(default=None, description="Телефон клиента")


class StorageOperationFinanceTransactionResponseDataTypesDataItemExpense(BaseModel):
    """Статья платежа
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор статьи платежа")
    title: str | None = Field(default=None, description="Название статьи платежа")


class StorageOperationGoodTransactionResponse200DataTypesDataClient(BaseModel):
    """Клиент
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор клиента")
    name: str | None = Field(default=None, description="Имя клиента")
    phone: str | None = Field(default=None, description="Номер телефона клиента")
    email: str | None = Field(default=None, description="Эл.почта клиента")


class StorageOperationGoodTransactionResponse200DataTypesDataGood(BaseModel):
    """Товар
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор товара")
    title: str | None = Field(default=None, description="Название товара")
    unit: str | None = Field(default=None, description="Единица измерения")
    value: str | None = Field(default=None, description="Название товара")
    label: str | None = Field(default=None, description="Название товара")
    article: str | None = Field(default=None, description="Артикул")
    category: str | None = Field(default=None, description="Название категории товара")
    category_id: float | None = Field(default=None, description="Идентификатор категории товара")
    salon_id: float | None = Field(default=None, description="Идентификатор компании")
    good_id: float | None = Field(default=None, description="Идентификатор товара")
    cost: float | None = Field(default=None, description="Стоимость")
    unit_id: float | None = Field(default=None, description="Идентификатор единицы измерения")
    unit_short_title: str | None = Field(default=None, description="Сокращенное название единицы измерения")
    service_unit_id: str | None = Field(default=None, description="Идентификатор единицы измерения для услуги")
    service_unit_short_title: str | None = Field(default=None, description="Сокращенное название единицы измерения для услуги")
    actual_cost: float | None = Field(default=None, description="Себестоимость")
    unit_actual_cost: float | None = Field(default=None, description="Себестоимость за единицу")
    unit_actual_cost_format: str | None = Field(default=None, description="Формат себестоимости за единицу")
    unit_equals: float | None = Field(default=None, description="Значение единицы измерения")
    barcode: str | None = Field(default=None, description="Штрих-код")
    loyalty_abonement_type_id: str | None = Field(default=None, description="Идентификатор абонемента (если товар это абонемент)")
    loyalty_certificate_type_id: str | None = Field(default=None, description="Идентификатор сертификата (если товар это сертификат)")
    loyalty_allow_empty_code: float | None = Field(default=None, description="Разрешена ли продажа без кода")
    actual_amounts: list[dict[str, Any]] | None = Field(default=None, description="Количество товара")
    last_change_date: str | None = Field(default=None, description="Дата последнего изменения товара")


class StorageOperationGoodTransactionResponse200DataTypesDataMaster(BaseModel):
    """Мастер
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор мастера")
    name: str | None = Field(default=None, description="Имя мастера")


class StorageOperationGoodTransactionResponse200DataTypesDataSaleUnit(BaseModel):
    """Единица измерения для продажи
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор единиц измерения")
    title: str | None = Field(default=None, description="Полное название единиц измерения")
    short_title: str | None = Field(default=None, description="Короткое название единиц измерения")


class StorageOperationGoodTransactionResponse200DataTypesDataServiceUnit(BaseModel):
    """Единица продажи для услуги
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор единиц измерения")
    title: str | None = Field(default=None, description="Полное название единиц измерения")
    short_title: str | None = Field(default=None, description="Короткое название единиц измерения")


class StorageOperationGoodTransactionResponse200DataTypesDataStorage(BaseModel):
    """Склад
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор склада")
    title: str | None = Field(default=None, description="Название склада")


class StorageOperationGoodTransactionResponse200DataTypesDataType(BaseModel):
    """Тип транзакции
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор типа транзакции")
    title: str | None = Field(default=None, description="Название типа транзакции")


class StorageOperationGoodTransactionResponse200DataTypesDataUnit(BaseModel):
    """Единица измерения
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор единицы измерения")
    title: str | None = Field(default=None, description="Название единицы измерения")
    short_title: str | None = Field(default=None, description="Сокращенное название единицы измерения")


class StorageOperationGoodTransactionResponseDataTypesDataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор транзакции")
    document_id: float | None = Field(default=None, description="Идентификатор документа")
    type_id: float | None = Field(default=None, description="Идентификатор типа транзакции")
    company_id: float | None = Field(default=None, description="Идентификатор компании")
    good_id: float | None = Field(default=None, description="Идентификатор товара")
    amount: float | None = Field(default=None, description="Количество товара")
    cost_per_unit: float | None = Field(default=None, description="Цена за единицу товара")
    discount: float | None = Field(default=None, description="Скидка")
    cost: float | None = Field(default=None, description="Итоговая стоимость товара")
    unit_id: float | None = Field(default=None, description="Идентификатор единицы измерения")
    operation_unit_type: float | None = Field(default=None, description="Тип единицы измерения: 1 - для продажи, 2 - для списания")
    storage_id: float | None = Field(default=None, description="Идентификатор склада")
    supplier_id: float | None = Field(default=None, description="Идентификатор поставщика")
    record_id: float | None = Field(default=None, description="Идентификатор записи")
    client_id: float | None = Field(default=None, description="Идентификатор клиента")
    master_id: float | None = Field(default=None, description="Идентификатор сотрудника")
    create_date: str | None = Field(default=None, description="Дата создания")
    comment: str | None = Field(default=None, description="Комментарий")
    service_id: float | None = Field(default=None, description="Идентификатор услуги")
    user_id: float | None = Field(default=None, description="Идентификатор пользователя")
    deleted: bool | None = Field(default=None, description="Удалена ли транзакция")
    pkg_amount: float | None = Field(default=None, description="Количество в упаковке")


class StorageOperationGoodTransactionResponseDataTypesMeta(BaseModel):
    """Метаданные (количество найденных транзакций)
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    count_: int | None = Field(default=None, alias="count")


class StorageOperationOperationResponseDataTypesDataDocumentCompany(BaseModel):
    """Компания
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор компании")
    title: str | None = Field(default=None, description="Название компании")
    country_id: float | None = Field(default=None, description="Идентификатор страны")
    city_id: float | None = Field(default=None, description="Идентификатор города")
    timezone: str | None = Field(default=None, description="Таймзона")
    address: str | None = Field(default=None, description="Адрес компании")
    coordinate_lat: str | None = Field(default=None, description="Широта")
    coordinate_lon: str | None = Field(default=None, description="Долгота")
    logo: str | None = Field(default=None, description="Пусть, по которому расположен логотип компании")
    zip: str | None = Field(default=None, description="Почтовый индекс")
    phones: list[dict[str, Any]] | None = Field(default=None, description="Телефон компании")
    site: str | None = Field(default=None, description="Сайт компании")


class StorageOperationOperationResponseDataTypesDataDocumentStorage(BaseModel):
    """Склад
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор склада")
    title: str | None = Field(default=None, description="Название склада")


class StorageOperationOperationResponseDataTypesDataDocumentType(BaseModel):
    """Тип документа
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор типа документа")
    title: str | None = Field(default=None, description="Название типа документа")


class StorageOperationOperationResponseDataTypesDataDocumentUser(BaseModel):
    """Пользователь
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор пользователя")
    name: str | None = Field(default=None, description="Имя пользователя")
    phone: str | None = Field(default=None, description="Номер телефона пользователя")


class StorageOperationOperationResponseDataTypesDataTransactionsItemGood(BaseModel):
    """Товар
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор товара")
    title: str | None = Field(default=None, description="Название товара")


class StorageOperationOperationResponseDataTypesDataTransactionsItemStorage(BaseModel):
    """Склад
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор склада")
    title: str | None = Field(default=None, description="Название склада")


class StorageOperationOperationResponseDataTypesDataTransactionsItemType(BaseModel):
    """Тип документа
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор типа документа")
    title: str | None = Field(default=None, description="Название типа документа")


class StorageOperationOperationResponseDataTypesDataTransactionsItemUnit(BaseModel):
    """Единицы измерения
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор единицы измерения")
    title: str | None = Field(default=None, description="Название единицы измерения")


class StorageResponseDataTypesDataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор склада")
    title: str | None = Field(default=None, description="Название склада")
    for_service: float | None = Field(default=None, description="1 - если используется для автоматического списания расходников")
    for_sale: float | None = Field(default=None, description="1 - если склад по умолчанию для продажи товаров")
    comment: str | None = Field(default=None, description="Описание к складу")


class StoragesTransactionResponseDataTypesDataItemClients(BaseModel):
    """Клиент
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор клиента")
    name: str | None = Field(default=None, description="Имя клиента")
    phone: str | None = Field(default=None, description="Телефон клиента")


class StoragesTransactionResponseDataTypesDataItemGood(BaseModel):
    """Товар
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор товара")
    title: str | None = Field(default=None, description="Название товара")


class StoragesTransactionResponseDataTypesDataItemMaster(BaseModel):
    """Сотрудник
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор сотрудника")
    title: str | None = Field(default=None, description="Имя сотрудника")


class StoragesTransactionResponseDataTypesDataItemService(BaseModel):
    """Услуга
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор услуги")
    title: str | None = Field(default=None, description="Название услуги")


class StoragesTransactionResponseDataTypesDataItemStorage(BaseModel):
    """Склад
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор склада")
    title: str | None = Field(default=None, description="Название склада")


class StoragesTransactionResponseDataTypesDataItemSupplier(BaseModel):
    """Поставщик
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор поставщика")
    title: str | None = Field(default=None, description="Название поставщика")


class StoragesTransactionResponseDataTypesDataItemUnit(BaseModel):
    """Единица измереня
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор единицы измерения")
    title: str | None = Field(default=None, description="Название единицы измерения")


class SalaryPayrollCalculation(BaseModel):
    """Схема спеки: Объект начисления заработной платы
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор начисления.")
    company_id: float | None = Field(default=None, description="Идентификатор филиала.")
    staff_id: float | None = Field(default=None, description="Идентификатор сотрудника.")
    amount: float | None = Field(default=None, description="Сумма начисления.")
    status: Literal["draft", "confirmed"] | None = Field(default=None, description="Статус начисления.")
    date_create: str | None = Field(default=None, description="Дата создания начисления.")
    date_from: str | None = Field(default=None, description="Дата начала периода начисления.")
    date_to: str | None = Field(default=None, description="Дата окончания периода начисления.")
    comment: str | None = Field(default=None, description="Комментарий к начислению.")


class SalaryPayrollCalculationItemDiscrepancy(BaseModel):
    """Схема спеки: Объект информации о найденном расхождении по позиции начисления зарплаты
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    reason: Literal["new", "deleted", "updated_rule", "updated_sum"] | None = Field(default=None, description="Тип расхождения.")
    actual_sum: str | None = Field(default=None, description="Действительная сумма зарплаты.")
    difference_sum: str | None = Field(default=None, description="Сумма расхождения действительной и начисленной зарплаты.")


class SalaryPayrollCalculationItemInfoContainer(BaseModel):
    """Схема спеки: Объект информации о применённом правиле расчёта зарплаты
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    criteria_title: str | None = Field(default=None, description="Название критерия расчёта зарплаты.")
    param_title: str | None = Field(default=None, description="Название параметра расчёта зарплаты.")
    scheme_title: str | None = Field(default=None, description="Название схемы расчёта зарплаты.")


class SalaryPayrollCalculationItemPaidContainer(BaseModel):
    """Схема спеки: Объект детализации оплат
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    money_sum: str | None = Field(default=None, description="Сумма, оплаченная деньгами.")
    discount_sum: str | None = Field(default=None, description="Сумма скидки.")
    bonus_sum: str | None = Field(default=None, description="Сумма, оплаченная бонусными баллами.")
    certificate_sum: str | None = Field(default=None, description="Сумма, оплаченная подарочным сертификатом.")
    abonement_sum: str | None = Field(default=None, description="Сумма, оплаченная абонементом.")
    deposit_sum: str | None = Field(default=None, description="Сумма, оплаченная с личного счёта.")


class SalaryPayrollCalculationItemTargetCalculation(BaseModel):
    """Схема спеки: Объект расчёта начисления заработной платы по отдельной позиции
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    type_slug: Literal["fix", "percent"] | None = Field(default=None, description="Тип расчёта.")
    value: float | None = Field(default=None, description="Значение.")
    description: str | None = Field(default=None, description="Подробное описание расчёта.")


class SalaryPayrollCalculationItemTargetContainer(BaseModel):
    """Схема спеки: Объект детализации позиции начисления заработной платы
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    target_type_slug: Literal["service", "good"] | None = Field(default=None, description="Тип детализации.")
    target_id: float | None = Field(default=None, description="Идентификатор детализации позиции.")
    title: str | None = Field(default=None, description="Название детализации позиции.")
    cost: str | None = Field(default=None, description="Базовая стоимость детализации позиции.")
    net_cost: str | None = Field(default=None, description="Базовая себестоимость детализации позиции.")
    salary_sum: str | None = Field(default=None, description="Полная сумма начисленной зарплаты в рамках детализации позиции.")
    salary_promotion_sum: str | None = Field(default=None, description="Сумма начисленной зарплаты от применения акций в рамках детализации позиции.")
    salary_calculation: dict[str, Any] | None = Field(default=None, description="Информация о расчёте зарплаты.")


class SalaryStaffBalance(BaseModel):
    """Схема спеки: Объект баланса по заработной плате
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    income: str | None = Field(default=None, description="Приход.")
    expense: str | None = Field(default=None, description="Расход.")
    balance: str | None = Field(default=None, description="Баланс.")


class SalaryStaffCalculation(BaseModel):
    """Взаиморасчёты.
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    total_sum: SalaryStaffBalance | None = Field(default=None, description="Общая сумма.")
    currency: Currency2 | None = Field(default=None, description="Валюта.")


class SalaryStaffScheme(BaseModel):
    """Схема спеки: Объект схемы расчёта зарплаты
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    staff_id: int | None = Field(default=None, description="Идентификатор сотрудника.")
    date_start: str | None = Field(default=None, description="Дата, с которой у сотрудника действует схема расчёта зарплаты.")
    date_end: str | None = Field(default=None, description="Дата, до которой у сотрудника действует схема расчёта зарплаты или null, если не имеет даты окончания.")
    salary_scheme: SalaryStaffSchemeSalaryScheme | None = Field(default=None)


class SalaryStaffSchemesCount(BaseModel):
    """Схема спеки: Количество прикреплённых схем расчёта зарплат
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    staff_id: int | None = Field(default=None, description="Идентификатор сотрудника.")
    salary_schemes_count: int | None = Field(default=None, description="Количество прикреплённых схем расчёта зарплат.")


class SalaryStaffSummary(BaseModel):
    """Схема спеки: Объект итогов по заработной плате
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    working_days_count: int | None = Field(default=None, description="Количество рабочих дней.")
    working_hours_count: int | None = Field(default=None, description="Количество рабочих часов.")
    group_services_count: int | None = Field(default=None, description="Количество оказанных групповых услуг.")
    services_count: int | None = Field(default=None, description="Количество оказанных услуг.")
    services_sum: str | None = Field(default=None, description="Стоимость оказанных услуг.")
    goods_sales_count: int | None = Field(default=None, description="Количество проданных товаров.")
    goods_sales_sum: str | None = Field(default=None, description="Стоимость проданных товаров.")
    total_sum: str | None = Field(default=None, description="Суммарная стоимость.")
    salary: str | None = Field(default=None, description="Зарплата.")


class SalonService(BaseModel):
    """Схема спеки: Объект модели "Услуга / Категория услуг в филиале".
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор услуги (категории услуг).")
    is_category: bool | None = Field(default=None, description="Признак категории услуг (true для категории услуг, false для услуги).")
    category_id: float | None = Field(default=None, description="Идентификатор родительской категории услуг.")
    title: str | None = Field(default=None, description="Название услуги (категории услуг).")


class ServiceCategoriesCompanyidRequestDataTypes(BaseModel):
    """Создать категорию услуги
    Схема спеки: Root Type for service_categories_companyid_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    title: str | None = Field(default=None, description="Название категории услуг")
    api_id: str | None = Field(default=None, description="Внешний идентификатор категории")
    weight: float | None = Field(default=None, description="Вес категории (используется для сортировки категорий при отображении)")
    staff: list[float] | None = Field(default=None, description="Список ID сотрудников, оказывающих услуги из категории")


class ServiceCategoriesCompanyidResponseDataTypes(BaseModel):
    """Создать категорию услуг
    Схема спеки: Root Type for service_categories_companyid_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: ServiceCategoriesCompanyidResponseDataTypesData | None = Field(default=None, alias="data")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")


class ServiceTitle2(BaseModel):
    """Название услуги
    Схема спеки: Root Type for ServiceTitle
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор услуги")
    title: str | None = Field(default=None, description="Название услуги")

__all__ = [
    "SalaryPayrollCalculation",
    "SalaryPayrollCalculationItemDiscrepancy",
    "SalaryPayrollCalculationItemInfoContainer",
    "SalaryPayrollCalculationItemPaidContainer",
    "SalaryPayrollCalculationItemTargetCalculation",
    "SalaryPayrollCalculationItemTargetContainer",
    "SalaryStaffBalance",
    "SalaryStaffCalculation",
    "SalaryStaffScheme",
    "SalaryStaffSchemeSalaryScheme",
    "SalaryStaffSchemesCount",
    "SalaryStaffSummary",
    "SalonService",
    "SearchForActivityItemAttributesStatus",
    "SearchForActivityItemRelationshipsLoyaltyAbonementAvailabilityIntervalDataItem",
    "SearchForActivityItemRelationshipsLoyaltyAbonementTypeData",
    "ServiceCategoriesCompanyidRequestDataTypes",
    "ServiceCategoriesCompanyidResponseDataTypes",
    "ServiceCategoriesCompanyidResponseDataTypesData",
    "ServiceTitle2",
    "ServicesChangeCompanyidRequestDataTypesStaffItem",
    "ServicesChangeCompanyidResponseDataTypesDataStaffItem",
    "ServicesCompanyidLinksRequestDataTypesMasterSettingsItemPrice",
    "ServicesCompanyidLinksRequestDataTypesTranslationsItem",
    "ServicesCompanyidRequestDataTypesStaffItem",
    "ServicesCompanyidResponseDataTypesDataStaffItem",
    "SmsClientsByIdResponseDataTypesMeta",
    "StorageOperationDocumentsResponseDataTypesDataCompany",
    "StorageOperationDocumentsResponseDataTypesDataStorage",
    "StorageOperationDocumentsResponseDataTypesDataType",
    "StorageOperationDocumentsResponseDataTypesDataUser",
    "StorageOperationFinanceTransactionResponseDataTypesDataItemAccount",
    "StorageOperationFinanceTransactionResponseDataTypesDataItemClient",
    "StorageOperationFinanceTransactionResponseDataTypesDataItemExpense",
    "StorageOperationGoodTransactionResponse200DataTypesDataClient",
    "StorageOperationGoodTransactionResponse200DataTypesDataGood",
    "StorageOperationGoodTransactionResponse200DataTypesDataMaster",
    "StorageOperationGoodTransactionResponse200DataTypesDataSaleUnit",
    "StorageOperationGoodTransactionResponse200DataTypesDataServiceUnit",
    "StorageOperationGoodTransactionResponse200DataTypesDataStorage",
    "StorageOperationGoodTransactionResponse200DataTypesDataType",
    "StorageOperationGoodTransactionResponse200DataTypesDataUnit",
    "StorageOperationGoodTransactionResponseDataTypesDataItem",
    "StorageOperationGoodTransactionResponseDataTypesMeta",
    "StorageOperationOperationResponseDataTypesDataDocumentCompany",
    "StorageOperationOperationResponseDataTypesDataDocumentStorage",
    "StorageOperationOperationResponseDataTypesDataDocumentType",
    "StorageOperationOperationResponseDataTypesDataDocumentUser",
    "StorageOperationOperationResponseDataTypesDataTransactionsItemGood",
    "StorageOperationOperationResponseDataTypesDataTransactionsItemStorage",
    "StorageOperationOperationResponseDataTypesDataTransactionsItemType",
    "StorageOperationOperationResponseDataTypesDataTransactionsItemUnit",
    "StorageResponseDataTypesDataItem",
    "StoragesTransactionResponseDataTypesDataItemClients",
    "StoragesTransactionResponseDataTypesDataItemGood",
    "StoragesTransactionResponseDataTypesDataItemMaster",
    "StoragesTransactionResponseDataTypesDataItemService",
    "StoragesTransactionResponseDataTypesDataItemStorage",
    "StoragesTransactionResponseDataTypesDataItemSupplier",
    "StoragesTransactionResponseDataTypesDataItemUnit"
]
