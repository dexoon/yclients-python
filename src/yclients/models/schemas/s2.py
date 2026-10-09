"""Модели YCLIENTS API (s2: S).

Сгенерировано scripts/generate.py -- не редактируйте вручную.
"""

from __future__ import annotations

from datetime import date, datetime
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class ServicesChangeCompanyidRequestDataTypes(BaseModel):
    """Создать услугу
    Схема спеки: Root Type for services_change_companyid_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    title: str = Field(description="Название услуги")
    booking_title: str = Field(description="Название услуги для онлайн-записи")
    category_id: float = Field(description="ID категории услуг")
    price_min: float = Field(description="Минимальная стоимость услуги")
    price_max: float = Field(description="Максимальная стоимость услуги")
    duration: float = Field(description="Длительность услуги, по умолчанию равна 3600 секундам")
    technical_break_duration: float | None = Field(default=None, description="Длительность технического перерыва - Если не передан. Значение по умолчанию null - Значение null, соответствует общей настройке филиала, и задается в разделе *Настройки → Журнал записи → Технически...")
    discount: float | None = Field(default=None, description="Скидка при оказании услуги")
    comment: str | None = Field(default=None, description="Комментарий к услуге")
    is_multi: bool = Field(description="false - индивидуальная услуга, true - групповая услуга")
    tax_variant: float = Field(description="ID системы налогообложения")
    vat_id: float = Field(description="ID НДС")
    is_need_limit_date: bool = Field(description="Ограничение по датам для онлайн-записи")
    date_from: str | None = Field(default=None, description="Дата с которой услуга будет доступна в формате yyyy-mm-dd")
    date_to: str | None = Field(default=None, description="Дата до которой услуга будет доступна в формате yyyy-mm-dd")
    dates: Any | None = Field(default=None, description="Список дат в которые будет доступна онлайн запись (если массив не передан, все даты за указанный период будут доступны)")
    seance_search_start: float = Field(description="Начало периода в какое время доступна запись, указывается в секундах")
    seance_search_finish: float = Field(description="Конец периода в какое время доступна запись, указывается в секундах")
    step: float = Field(description="Шаг вывода сеансов, указывается в секундах")
    seance_search_step: float = Field(description="Шаг поиска сеансов, указывается в секундах")
    weight: float | None = Field(default=None, description="Вес услуги (используется для сортировки услуг при отображении)")
    service_type: float | None = Field(default=None, description="Доступна ли для онлайн записи услуга. 1 - доступна, 0 не доступна.")
    api_service_id: int | None = Field(default=None, description="Внешний идентификатор услуги")
    online_invoicing_status: int | None = Field(default=None, description="Онлайн-предоплата включена (0-выключена, 2-включена)")
    price_prepaid_percent: int | None = Field(default=None, description="Размер предоплаты в процентах (от минимальной стоимости услуги)")
    price_prepaid_amount: int | None = Field(default=None, description="Сумма предоплаты")
    abonement_restriction_value: int | None = Field(default=None, description="Запрет записи без абонемента (Только если online_invoicing_status=0)")
    is_abonement_autopayment_enabled: int | None = Field(default=None, description="Автосписание с абонемента")
    autopayment_before_visit_time: int | None = Field(default=None, description="За какое время до визита производится автосписание")
    staff: list[ServicesChangeCompanyidRequestDataTypesStaffItem] | None = Field(default=None, description="Сотрудники, оказываюшие услугу и длительность оказания услуги каждым из них")


class ServicesCompanyidRequestDataTypes(BaseModel):
    """Создать услугу
    Схема спеки: Root Type for services_companyid_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    title: str | None = Field(default=None, description="Название услуги")
    category_id: float | None = Field(default=None, description="ID категории услуг")
    price_min: float | None = Field(default=None, description="Минимальная стоимость услуги")
    price_max: float | None = Field(default=None, description="Максимальная стоимость услуги")
    duration: float | None = Field(default=None, description="Длительность услуги, по умолчанию равна 3600 секундам")
    technical_break_duration: float | None = Field(default=None, description="Длительность технического перерыва - Если не передан. Значение по умолчанию null - Значение null, соответствует общей настройке филиала, и задается в разделе *Настройки → Журнал записи → Технически...")
    discount: float | None = Field(default=None, description="Скидка при оказании услуги")
    comment: str | None = Field(default=None, description="Комментарий к услуге")
    weight: float | None = Field(default=None, description="Вес услуги (используется для сортировки услуг при отображении)")
    service_type: float | None = Field(default=None, description="Доступна ли для онлайн записи услуга. 1 - доступна, 0 не доступна.")
    api_service_id: str | None = Field(default=None, description="Внешний идентификатор услуги")
    staff: list[ServicesCompanyidRequestDataTypesStaffItem] | None = Field(default=None, description="Сотрудники, оказываюшие услугу и длительность оказания услуги каждым из них")


class SmsClientsByFilterRequestDataTypes(BaseModel):
    """Отправить SMS рассылку по клиентам, подходящим под фильтры
    Схема спеки: Root Type for sms_clients_by_filter_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    text: str | None = Field(default=None, description="Текст SMS сообщения")


class SmsClientsByIdRequestDataTypes(BaseModel):
    """Отправить SMS рассылку по списку клиентов
    Схема спеки: Root Type for sms_clients_by_id_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    client_ids: list[float] | None = Field(default=None, description="Массив идентификаторов клиентов")
    text: str | None = Field(default=None, description="Текст SMS сообщения")


class SmsClientsByIdResponseDataTypes(BaseModel):
    """Отправить SMS рассылку по списку клиентов
    Схема спеки: Root Type for sms_clients_by_id_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: str | None = Field(default=None, alias="data", description="Имеет значение null")
    meta: SmsClientsByIdResponseDataTypesMeta | None = Field(default=None)


class StaffCompanyidRequestDataTypes(BaseModel):
    """Добавить нового сотрудника
    Схема спеки: Root Type for staff_companyid_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    name: str | None = Field(default=None, description="Имя сотрудника")
    specialization: str | None = Field(default=None, description="Специализация сотрудника")
    weight: float | None = Field(default=None, description="Вес сотрудника. При выводе сотрудники сортируются по весу, сначала более тяжелые")
    information: str | None = Field(default=None, description="Информация о сотруднике (HTML-формат)")
    api_id: str | None = Field(default=None, description="Внещний идентификатор сотрудника")
    hidden: float | None = Field(default=None, description="Статус отображения в онлайн-записи, 1 - скрыт, 0 - не скрыт")
    fired: float | None = Field(default=None, description="Статус увольнения сотрудника, 1 - уволен, 0 - не уволен")
    user_id: float | None = Field(default=None, description="ID привязанного пользователя, 0 - удалить связь с пользователем")


class StaffPosition2(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float = Field(alias="id", description="id должности")
    title: str = Field(description="название должности")


class StorageOperationDocumentsRequestDataTypes(BaseModel):
    """Создать документ
    Схема спеки: Root Type for storage_operation_documents_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    type_id: float = Field(description="Тип документа (1 продажа, 3 приход, 4 списание)")
    comment: str | None = Field(default=None, description="Комментарий")
    storage_id: float = Field(description="Идентификатор склада")
    create_date: str = Field(description="Дата проведения складской операции")


class StorageOperationGoodTransactionRequestDataTypes(BaseModel):
    """Создать транзакцию
    Схема спеки: Root Type for storage_operation_good_transaction_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    document_id: float = Field(description="Идентификатор документа")
    good_id: float = Field(description="Идентификатор товара")
    amount: float = Field(description="Количество")
    cost_per_unit: float = Field(description="Стоимость за единицу товара")
    discount: float = Field(description="Скидка в %")
    cost: float = Field(description="Итоговая сумма транзакции")
    operation_unit_type: float = Field(description="тип единицы измерения: 1 - для продажи, 2 - для списания")
    good_special_number: str | None = Field(default=None, description="Код абонемента\\сертификата, если товар является абонементом или сертификатом")
    master_id: float | None = Field(default=None, description="Идентификатор мастера, продавшего товар")
    client_id: float | None = Field(default=None, description="Идентификатор клиента, купившего товар")
    supplier_id: float | None = Field(default=None, description="Идентификатор поставщика")
    comment: str | None = Field(default=None, description="Комментарий")


class StorageOperationGoodTransactionResponseDataTypes(BaseModel):
    """Получить товарные транзакции документа
    Схема спеки: Root Type for storage_operation_good_transaction_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: list[StorageOperationGoodTransactionResponseDataTypesDataItem] | None = Field(default=None, alias="data", description="Массив объектов с данными")
    meta: StorageOperationGoodTransactionResponseDataTypesMeta | None = Field(default=None)


class StorageResponseDataTypes(BaseModel):
    """Получить склады компании
    Схема спеки: Root Type for storage_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: list[StorageResponseDataTypesDataItem] | None = Field(default=None, alias="data", description="Массив объектов с данными")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")


class SalaryStaffCalculationDailyPayrollDailyItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    date: str | None = Field(default=None, description="Дата.")
    payroll_sum: SalaryStaffBalance | None = Field(default=None, description="Общая сумма за эту дату.")


class SalaryStaffPeriodDailyPeriodCalculationDailyItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    date: str | None = Field(default=None, description="Дата.")
    period_calculation: SalaryStaffSummary | None = Field(default=None, description="Итоги начислений за эту дату.")


class SalaryStaffPeriodVariant1(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    currency: Currency2 | None = Field(default=None, description="Валюта.")


class SearchForActivityItemAttributes(BaseModel):
    """Параметры абонемента
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    number: str | None = Field(default=None, description="Номер абонемента")
    created_date: str | None = Field(default=None, description="Дата создания абонемента")
    activated_date: str | None = Field(default=None, description="Дата активации абонемента")
    planned_activation_date: str | None = Field(default=None, description="Дата когда абонемент будет активирован.")
    is_frozen: bool | None = Field(default=None, description="Заморожен ли абонемент")
    freeze_period: int | None = Field(default=None, description="Срок заморозки абонемента")
    period: float | None = Field(default=None, description="Продолжительность периода действия.")
    period_unit_id: int | None = Field(default=None, description="Тип единиц измерения продолжительности периода действия типа абонемента `(1 - день, 2 - неделя, 3 - месяц, 4 - год)`.")
    expiration_date: str | None = Field(default=None, description="Дата сгорания абонемента")
    status: SearchForActivityItemAttributesStatus | None = Field(default=None)
    is_united_balance: bool | None = Field(default=None, description="У абонемента общий баланс для всех услуг.")
    united_balance_services_count: int | None = Field(default=None, description="Отображает текущий баланс абонемента (если тип баланса `общий`) ⚠️ Если `is_united_balance: false` значение всегда равно 0")
    balance_service_count: int | None = Field(default=None, description="Отображает текущий баланс абонемента (если тип баланса `раздельный`) ⚠️ Если `is_united_balance: true` значение всегда равно 0")
    goods_transaction_id: int | None = Field(default=None, description="Идентификатор складской операции, в которой абонемент был продан (создан)")


class SearchForActivityItemRelationshipsLoyaltyAbonementAvailabilityInterval(BaseModel):
    """Указывыет на настройки ограничения применений абонемента по дням и времени
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data_: list[SearchForActivityItemRelationshipsLoyaltyAbonementAvailabilityIntervalDataItem] | None = Field(default=None, alias="data")


class SearchForActivityItemRelationshipsLoyaltyAbonementType(BaseModel):
    """Включение типа абонемента
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data_: SearchForActivityItemRelationshipsLoyaltyAbonementTypeData | None = Field(default=None, alias="data")


class ServicesChangeCompanyidResponseDataTypesData(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    title: str | None = Field(default=None, description="Название услуги")
    booking_title: str | None = Field(default=None, description="Название услуги для онлайн-записи")
    category_id: float | None = Field(default=None, description="ID категории услуг")
    price_min: float | None = Field(default=None, description="Минимальная стоимость услуги")
    price_max: float | None = Field(default=None, description="Максимальная стоимость услуги")
    duration: float | None = Field(default=None, description="Длительность услуги, по умолчанию равна 3600 секундам")
    discount: float | None = Field(default=None, description="Скидка при оказании услуги")
    comment: str | None = Field(default=None, description="Комментарий к услуге")
    is_multi: bool | None = Field(default=None, description="false - индивидуальная услуга, true - групповая услуга")
    tax_variant: float | None = Field(default=None, description="ID системы налогообложения")
    vat_id: float | None = Field(default=None, description="ID НДС")
    is_need_limit_date: bool | None = Field(default=None, description="Ограничение по датам для онлайн-записи")
    seance_search_start: float | None = Field(default=None, description="Начало периода в какое время доступна запись, указывается в секундах")
    seance_search_finish: float | None = Field(default=None, description="Конец периода в какое время доступна запись, указывается в секундах")
    step: float | None = Field(default=None, description="Шаг вывода сеансов, указывается в секундах")
    seance_search_step: float | None = Field(default=None, description="Шаг поиска сеансов, указывается в секундах")
    weight: float | None = Field(default=None, description="Вес услуги (используется для сортировки услуг при отображении)")
    technical_break_duration: float | None = Field(default=None, description="Длительность технического перерыва")
    active: float | None = Field(default=None, description="Доступна ли для онлайн записи услуга. 1 - доступна, 0 не доступна.")
    api_id: str | None = Field(default=None, description="Внешний идентификатор услуги")
    staff: list[ServicesChangeCompanyidResponseDataTypesDataStaffItem] | None = Field(default=None, description="Сотрудники, оказываюшие услугу и длительность оказания услуги каждым из них")


class ServicesCompanyidLinksRequestDataTypesMasterSettingsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    master_id: float | None = Field(default=None, description="ID сотрудника оказывающего услугу")
    technological_card_id: float | None = Field(default=None, description="ID технологической карты по которой сотрудник оказывает услугу")
    hours: float | None = Field(default=None, description="Количество часов необходимых для оказания услуги")
    minutes: float | None = Field(default=None, description="Количество минут необходимых для оказания услуги")
    price: ServicesCompanyidLinksRequestDataTypesMasterSettingsItemPrice | None = Field(default=None)


class ServicesCompanyidResponseDataTypesData(BaseModel):
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
    technical_break_duration: float | None = Field(default=None, description="Длительность технического перерыва")
    discount: float | None = Field(default=None, description="Скидка")
    comment: str | None = Field(default=None, description="Комментарий к услуге")
    weight: float | None = Field(default=None, description="Вес услуги (используется для сортировки категорий при отображении)")
    active: float | None = Field(default=None, description="1 - доступна для онлайн записи, 0 - не доступна")
    api_id: str | None = Field(default=None, description="Внедний идентификатор услуги")
    staff: list[ServicesCompanyidResponseDataTypesDataStaffItem] | None = Field(default=None, description="Список сотрудников, оказывающих услугу и длительность сеанса")


class StorageOperationDocumentsResponseDataTypesData(BaseModel):
    """Объект с данными
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор документа")
    type_id: float | None = Field(default=None, description="Идентификатор типа документа")
    type_: StorageOperationDocumentsResponseDataTypesDataType | None = Field(default=None, alias="type")
    storage_id: float | None = Field(default=None, description="Идентификатор склада")
    user_id: float | None = Field(default=None, description="Идентификатор пользователя")
    company_id: float | None = Field(default=None, description="Идентификатор компании")
    number: float | None = Field(default=None, description="Номер документа")
    comment: str | None = Field(default=None, description="Комментарий")
    create_date: str | None = Field(default=None, description="Дата создания")
    storage: StorageOperationDocumentsResponseDataTypesDataStorage | None = Field(default=None)
    company: StorageOperationDocumentsResponseDataTypesDataCompany | None = Field(default=None)
    user: StorageOperationDocumentsResponseDataTypesDataUser | None = Field(default=None)


class StorageOperationFinanceTransactionResponseDataTypesDataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор транзакции")
    date: str | None = Field(default=None)
    type_id: float | None = Field(default=None, description="Идентификатор типа транзакции")
    expense_id: float | None = Field(default=None, description="Идентификатор статьи платежа")
    account_id: float | None = Field(default=None, description="Идентификатор кассы")
    amount: float | None = Field(default=None, description="Сумма транзакции")
    client_id: float | None = Field(default=None, description="Идентификатор клиента")
    master_id: float | None = Field(default=None, description="Идентификатор сотрудника")
    supplier_id: float | None = Field(default=None, description="Идентификатор поставщика")
    comment: str | None = Field(default=None, description="Комментарий")
    item_id: int | None = Field(default=None)
    target_type_id: int | None = Field(default=None)
    record_id: float | None = Field(default=None, description="Идентификатор записи")
    expense: StorageOperationFinanceTransactionResponseDataTypesDataItemExpense | None = Field(default=None)
    account: StorageOperationFinanceTransactionResponseDataTypesDataItemAccount | None = Field(default=None)
    client_: StorageOperationFinanceTransactionResponseDataTypesDataItemClient | None = Field(default=None, alias="client")
    master: list[dict[str, Any]] | None = Field(default=None, description="Сотрудник")
    supplier: list[dict[str, Any]] | None = Field(default=None, description="Поставщик")


class StorageOperationGoodTransactionResponse200DataTypesData(BaseModel):
    """Объект с данными
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор товарной транзакции")
    document_id: int | None = Field(default=None, description="Идентификатор документа в системе YCLIENTS")
    type_id: int | None = Field(default=None, description="Идентификатор типа товарной транзакции")
    type_: StorageOperationGoodTransactionResponse200DataTypesDataType | None = Field(default=None, alias="type")
    company_id: float | None = Field(default=None, description="Идентификатор компании")
    good_id: float | None = Field(default=None, description="Идентификатор товара")
    amount: float | None = Field(default=None, description="Количество товара")
    service_amount: int | None = Field(default=None, description="Количество товара в единицах для списания")
    sale_amount: int | None = Field(default=None, description="Количество товара в единицах для продажи")
    cost_per_unit: float | None = Field(default=None, description="Цена за единицу")
    cost: float | None = Field(default=None, description="Цена")
    discount: float | None = Field(default=None, description="Скидка")
    unit_id: float | None = Field(default=None, description="Идентификатор единицы измерения")
    service_unit_id: float | None = Field(default=None, description="Идентификатор единиц измерения для списания")
    sale_unit_id: float | None = Field(default=None, description="Идентификатор единиц измерения для продажи")
    operation_unit_type: float | None = Field(default=None, description="Тип транзакции")
    storage_id: float | None = Field(default=None, description="Идентификатор склада")
    supplier_id: float | None = Field(default=None, description="Идентификатор поставщика")
    client_id: float | None = Field(default=None, description="Идентификатор клиена")
    master_id: float | None = Field(default=None, description="Идентификатор сотрудника")
    create_date: str | None = Field(default=None, description="Дата создания")
    last_change_date: str | None = Field(default=None, description="Дата последнего изменения")
    comment: str | None = Field(default=None, description="Комментарий")
    deleted: bool | None = Field(default=None, description="Флаг удаления транзакции")
    good: StorageOperationGoodTransactionResponse200DataTypesDataGood | None = Field(default=None)
    sale_unit: StorageOperationGoodTransactionResponse200DataTypesDataSaleUnit | None = Field(default=None)
    service_unit: StorageOperationGoodTransactionResponse200DataTypesDataServiceUnit | None = Field(default=None)
    storage: StorageOperationGoodTransactionResponse200DataTypesDataStorage | None = Field(default=None)
    supplier: list[dict[str, Any]] | None = Field(default=None, description="Поставщик")
    client_: StorageOperationGoodTransactionResponse200DataTypesDataClient | None = Field(default=None, alias="client")
    master: StorageOperationGoodTransactionResponse200DataTypesDataMaster | None = Field(default=None)
    unit: StorageOperationGoodTransactionResponse200DataTypesDataUnit | None = Field(default=None)


class StorageOperationOperationResponseDataTypesDataDocument(BaseModel):
    """Документ
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор документа")
    type_id: float | None = Field(default=None, description="Идентификатор типа документа")
    type_: StorageOperationOperationResponseDataTypesDataDocumentType | None = Field(default=None, alias="type")
    storage_id: float | None = Field(default=None, description="Идентификатор склада")
    user_id: float | None = Field(default=None, description="Идентификатор пользователя")
    company_id: float | None = Field(default=None, description="Идентификатор компании")
    number: float | None = Field(default=None, description="Номер документа")
    comment: str | None = Field(default=None, description="Комментарий")
    create_date: str | None = Field(default=None, description="Дата создания")
    storage: StorageOperationOperationResponseDataTypesDataDocumentStorage | None = Field(default=None)
    company: StorageOperationOperationResponseDataTypesDataDocumentCompany | None = Field(default=None)
    user: StorageOperationOperationResponseDataTypesDataDocumentUser | None = Field(default=None)


class StorageOperationOperationResponseDataTypesDataTransactionsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор транзакции")
    document_id: float | None = Field(default=None, description="Идентификатор документа")
    type_id: float | None = Field(default=None, description="Идентификатор типа документа")
    type_: StorageOperationOperationResponseDataTypesDataTransactionsItemType | None = Field(default=None, alias="type")
    company_id: float | None = Field(default=None, description="Идентификатор компании")
    good_id: float | None = Field(default=None, description="Идентификатор товара")
    amount: float | None = Field(default=None, description="Количество")
    cost_per_unit: float | None = Field(default=None, description="Цена за единицы")
    discount: float | None = Field(default=None, description="Скдика")
    cost: float | None = Field(default=None, description="Итоговая цена")
    unit_id: float | None = Field(default=None, description="Идентификатор единпиы измерения")
    storage_id: float | None = Field(default=None, description="Идентификатор склада")
    supplier_id: float | None = Field(default=None, description="Идентификатор поставщика")
    client_id: float | None = Field(default=None, description="Идентификатор клиента")
    master_id: float | None = Field(default=None, description="Идентификатор мастера")
    create_date: str | None = Field(default=None, description="Дата создания")
    comment: str | None = Field(default=None, description="Комментарий")
    deleted: bool | None = Field(default=None, description="Удалена ли транзакция")
    good: StorageOperationOperationResponseDataTypesDataTransactionsItemGood | None = Field(default=None)
    storage: StorageOperationOperationResponseDataTypesDataTransactionsItemStorage | None = Field(default=None)
    supplier: list[dict[str, Any]] | None = Field(default=None, description="Поставщик")
    client_: list[dict[str, Any]] | None = Field(default=None, alias="client", description="Клиент")
    master: list[dict[str, Any]] | None = Field(default=None, description="Мастер")
    unit: StorageOperationOperationResponseDataTypesDataTransactionsItemUnit | None = Field(default=None)


class StoragesTransactionResponseDataTypesDataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор транзакции")
    document_id: float | None = Field(default=None, description="Идентификатор документа")
    type_id: float | None = Field(default=None, description="Идентификатор типа транзакции")
    type_: str | None = Field(default=None, alias="type", description="Тип транзакции")
    good: StoragesTransactionResponseDataTypesDataItemGood | None = Field(default=None)
    storage: StoragesTransactionResponseDataTypesDataItemStorage | None = Field(default=None)
    unit: StoragesTransactionResponseDataTypesDataItemUnit | None = Field(default=None)
    operation_unit_type: float | None = Field(default=None, description="Тип единицы измерения: 1 - для продажи, 2 - для списания")
    create_date: str | None = Field(default=None, description="Дата создания")
    last_change_date: str | None = Field(default=None, description="Дата последнего изменения")
    cost_per_unit: float | None = Field(default=None, description="Цена за единицу")
    cost: float | None = Field(default=None, description="Цена")
    discount: float | None = Field(default=None, description="Скидка")
    master: StoragesTransactionResponseDataTypesDataItemMaster | None = Field(default=None)
    supplier: StoragesTransactionResponseDataTypesDataItemSupplier | None = Field(default=None)
    record_id: float | None = Field(default=None, description="Идентификатор записи")
    service: StoragesTransactionResponseDataTypesDataItemService | None = Field(default=None)
    clients: StoragesTransactionResponseDataTypesDataItemClients | None = Field(default=None)


class SalaryPayrollCalculationItemContainer(BaseModel):
    """Схема спеки: Объект позиции начисления заработной платы
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    date: str | None = Field(default=None, description="Дата.")
    time: str | None = Field(default=None, description="Время.")
    item_id: float | None = Field(default=None, description="Идентификатор сущности, за что производится начисление (например, идентификатор записи или продажи товара).")
    item_type_slug: Literal["periodic", "sale", "record", "bonus", "penalty", "retro_bonus", "activity"] | None = Field(default=None, description="Тип сущности, за что производится начисление (например, запись или продажа товара).")
    salary_sum: str | None = Field(default=None, description="Сумма начисленной заработной платы.")
    record_id: float | None = Field(default=None, description="Идентификатор записи.")
    client_id: float | None = Field(default=None, description="Идентификатор клиента.")
    cost: str | None = Field(default=None, description="Базовая стоимость.")
    paid: dict[str, Any] | None = Field(default=None, description="Информация об оплате.")
    salary_calculation_info: SalaryPayrollCalculationItemInfoContainer | None = Field(default=None, description="Информация о применённом правиле расчёта зарплаты.")
    targets: list[SalaryPayrollCalculationItemTargetContainer] | None = Field(default=None)
    salary_discrepancy: dict[str, Any] | None = Field(default=None, description="Информация о расхождениях в начислении зарплаты.")


class SalaryStaffCalculationDaily(BaseModel):
    """Взаиморасчёты с группировкой по дате.
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    payroll_daily: list[SalaryStaffCalculationDailyPayrollDailyItem] | None = Field(default=None)
    currency: Currency2 | None = Field(default=None, description="Валюта.")


class SalaryStaffPeriodDaily(BaseModel):
    """Получение расчёта за период по конкретному сотруднику с группировкой по дате.
    Схема спеки: Расчёт за период по конкретному сотруднику с группировкой по дате
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    period_calculation_daily: list[SalaryStaffPeriodDailyPeriodCalculationDailyItem] | None = Field(default=None)
    currency: Currency2 | None = Field(default=None, description="Валюта.")


class ServiceCategoryTitle2(BaseModel):
    """Название категории услуг
    Схема спеки: Root Type for ServiceCategoryTitle
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор категории услуг")
    title: str | None = Field(default=None, description="Название категории услуг")
    services: list[ServiceTitle2] | None = Field(default=None, description="Услуги в категории (по запросу)")


class ServicesChangeCompanyidResponseDataTypes(BaseModel):
    """Изменить услугу
    Схема спеки: Root Type for services_change_companyid_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: ServicesChangeCompanyidResponseDataTypesData | None = Field(default=None, alias="data")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")


class ServicesCompanyidLinksRequestDataTypes(BaseModel):
    """Изменить длительность оказания услуги сотрудниками, технические карты, названия на других языках
    Схема спеки: Root Type for services_companyid_links_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    service_id: float = Field(description="ID услуги")
    master_settings: list[ServicesCompanyidLinksRequestDataTypesMasterSettingsItem] = Field(description="Список сотрудников, оказывающих услугу c длительностью сеанса и технологическими картами")
    resource_ids: list[float] = Field(description="Список ресурсов необходимых для оказания услуги")
    translations: list[ServicesCompanyidLinksRequestDataTypesTranslationsItem] = Field(description="Список переводов для каждого языка")


class ServicesCompanyidResponseDataTypes(BaseModel):
    """Создать услугу
    Схема спеки: Root Type for services_companyid_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: ServicesCompanyidResponseDataTypesData | None = Field(default=None, alias="data")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")


class StorageOperationDocumentsResponseDataTypes(BaseModel):
    """Создать документ
    Схема спеки: Root Type for storage_operation_documents_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: StorageOperationDocumentsResponseDataTypesData | None = Field(default=None, alias="data")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")


class StorageOperationFinanceTransactionResponseDataTypes(BaseModel):
    """Получить финансовые транзакции документа
    Схема спеки: Root Type for storage_operation_finance_transaction_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: list[StorageOperationFinanceTransactionResponseDataTypesDataItem] | None = Field(default=None, alias="data", description="Массив объектов с данными")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")


class StorageOperationGoodTransactionResponse200DataTypes(BaseModel):
    """Создать транзакцию
    Схема спеки: Root Type for storage_operation_good_transaction_response200_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: StorageOperationGoodTransactionResponse200DataTypesData | None = Field(default=None, alias="data")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")


class StoragesTransactionResponseDataTypes(BaseModel):
    """Поиск товарных транзакций
    Схема спеки: Root Type for storages_transaction_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: list[StoragesTransactionResponseDataTypesDataItem] | None = Field(default=None, alias="data", description="Массив объектов с данными")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")


class SalaryPayrollCalculationContainerVariant1(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    salary_items: list[SalaryPayrollCalculationItemContainer] | None = Field(default=None, description="Позиции начисления заработной платы.")
    currency: Currency2 | None = Field(default=None, description="Валюта.")


class SearchForActivityItemRelationships(BaseModel):
    """Дополнительные включения
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    loyalty_abonement_type: SearchForActivityItemRelationshipsLoyaltyAbonementType | None = Field(default=None)
    loyalty_abonement_availability_interval: SearchForActivityItemRelationshipsLoyaltyAbonementAvailabilityInterval | None = Field(default=None)


class StorageOperationOperationResponseDataTypesData(BaseModel):
    """Объект с данными
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    document: StorageOperationOperationResponseDataTypesDataDocument | None = Field(default=None)
    transactions: list[StorageOperationOperationResponseDataTypesDataTransactionsItem] | None = Field(default=None, description="Транзакция")


class StorageOperationOperationResponseDataTypes(BaseModel):
    """Создание складской операции
    Схема спеки: Root Type for storage_operation_operation_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: StorageOperationOperationResponseDataTypesData | None = Field(default=None, alias="data")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")


class SearchForActivityItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: str | None = Field(default=None, alias="id", description="Идентификатор абонемента")
    type_: str | None = Field(default=None, alias="type", description="Описание сущности. В данном случае всегда `loyalty_abonement`")
    attributes: SearchForActivityItemAttributes | None = Field(default=None)
    relationships: SearchForActivityItemRelationships | None = Field(default=None)

__all__ = [
    "SalaryPayrollCalculationContainerVariant1",
    "SalaryPayrollCalculationItemContainer",
    "SalaryStaffCalculationDaily",
    "SalaryStaffCalculationDailyPayrollDailyItem",
    "SalaryStaffPeriodDaily",
    "SalaryStaffPeriodDailyPeriodCalculationDailyItem",
    "SalaryStaffPeriodVariant1",
    "SearchForActivityItem",
    "SearchForActivityItemAttributes",
    "SearchForActivityItemRelationships",
    "SearchForActivityItemRelationshipsLoyaltyAbonementAvailabilityInterval",
    "SearchForActivityItemRelationshipsLoyaltyAbonementType",
    "ServiceCategoryTitle2",
    "ServicesChangeCompanyidRequestDataTypes",
    "ServicesChangeCompanyidResponseDataTypes",
    "ServicesChangeCompanyidResponseDataTypesData",
    "ServicesCompanyidLinksRequestDataTypes",
    "ServicesCompanyidLinksRequestDataTypesMasterSettingsItem",
    "ServicesCompanyidRequestDataTypes",
    "ServicesCompanyidResponseDataTypes",
    "ServicesCompanyidResponseDataTypesData",
    "SmsClientsByFilterRequestDataTypes",
    "SmsClientsByIdRequestDataTypes",
    "SmsClientsByIdResponseDataTypes",
    "StaffCompanyidRequestDataTypes",
    "StaffPosition2",
    "StorageOperationDocumentsRequestDataTypes",
    "StorageOperationDocumentsResponseDataTypes",
    "StorageOperationDocumentsResponseDataTypesData",
    "StorageOperationFinanceTransactionResponseDataTypes",
    "StorageOperationFinanceTransactionResponseDataTypesDataItem",
    "StorageOperationGoodTransactionRequestDataTypes",
    "StorageOperationGoodTransactionResponse200DataTypes",
    "StorageOperationGoodTransactionResponse200DataTypesData",
    "StorageOperationGoodTransactionResponseDataTypes",
    "StorageOperationOperationResponseDataTypes",
    "StorageOperationOperationResponseDataTypesData",
    "StorageOperationOperationResponseDataTypesDataDocument",
    "StorageOperationOperationResponseDataTypesDataTransactionsItem",
    "StorageResponseDataTypes",
    "StoragesTransactionResponseDataTypes",
    "StoragesTransactionResponseDataTypesDataItem"
]
