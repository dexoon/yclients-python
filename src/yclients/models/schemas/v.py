"""Модели YCLIENTS API (v: V).

Сгенерировано scripts/generate.py -- не редактируйте вручную.
"""

from __future__ import annotations

from datetime import date, datetime
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class VisitDetailsDataTypesDataItemsItem(BaseModel):
    """Массив объектов продажи
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор сущности массива")
    item_id: float | None = Field(default=None, description="Идентификатор товара или услуги")
    item_type_id: int | None = Field(default=None)
    record_id: float | None = Field(default=None, description="Идентификатор записи")
    item_title: str | None = Field(default=None, description="Наименование товара или услуги")
    amount: float | None = Field(default=None, description="Количество")
    first_cost: float | None = Field(default=None, description="Начальная стоимость")
    manual_cost: float | None = Field(default=None, description="Стоимость, указанная вручную")
    discount: float | None = Field(default=None, description="Скидка")
    cost: float | None = Field(default=None, description="Конечная стоимость с вычетом всех скидой и акций")
    master_id: float | None = Field(default=None, description="Идентификатор сотрудника")
    good_id: float | None = Field(default=None, description="Идентификатор товара")
    service_id: float | None = Field(default=None, description="Идентификатор услуги")
    event_id: float | None = Field(default=None, description="Идентификатор акции")
    is_service: bool | None = Field(default=None, description="Это услуга")
    is_event: bool | None = Field(default=None, description="Это акция")
    is_good: bool | None = Field(default=None, description="Это товар")


class VisitDetailsDataTypesDataKkmTransactionDetailsContainerTransactionsItemCashier(BaseModel):
    """Кассир
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор сотрудника")
    name: str | None = Field(default=None, description="Имя сотрудника")


class VisitDetailsDataTypesDataKkmTransactionDetailsContainerTransactionsItemDocument(BaseModel):
    """Документа
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор документа")
    type_: float | None = Field(default=None, alias="type", description="Идентификатор типа документа")
    type_title: str | None = Field(default=None, description="Название сущности документа")


class VisitDetailsDataTypesDataKkmTransactionDetailsContainerTransactionsItemStatus(BaseModel):
    """Статус печати чека
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор статуса")
    title: str | None = Field(default=None, description="Название статуса")


class VisitDetailsDataTypesDataKkmTransactionDetailsContainerTransactionsItemType(BaseModel):
    """Тип оплаты
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор типа оплаты")
    title: str | None = Field(default=None, description="Название типа оплаты")


class VisitDetailsDataTypesDataLoyaltyTransactionsItemType(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id")
    title: str | None = Field(default=None)


class VisitDetailsDataTypesDataPaymentTransactionsItemAccount(BaseModel):
    """Касса
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор кассы")
    title: str | None = Field(default=None, description="Название кассы")


class VisitDetailsDataTypesDataPaymentTransactionsItemClient(BaseModel):
    """Клиент
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: str | None = Field(default=None, alias="id", description="Идентификатор клиента")
    name: str | None = Field(default=None, description="Имя клиента")
    phone: str | None = Field(default=None, description="Номер телефона")


class VisitDetailsDataTypesDataPaymentTransactionsItemExpense(BaseModel):
    """Статья платежа
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор статьи платежа")
    title: str | None = Field(default=None, description="Название статьи платежа")


class VisitLoyaltyApplyResponseDataTypesItemsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор объекта")
    item_id: int | None = Field(default=None, description="Идентификатор товара/услуги")
    item_type_id: int | None = Field(default=None, description="Идентификатор типа операции")
    record_id: int | None = Field(default=None, description="Идентификатор записи")
    item_title: str | None = Field(default=None, description="Название товара/услуги")
    amount: int | None = Field(default=None, description="Количество товаров/услуг")
    first_cost: float | None = Field(default=None, description="Начальная стоимость")
    manual_cost: float | None = Field(default=None, description="Стоимость, измененная вручную")
    discount: float | None = Field(default=None, description="Скидка")
    cost: float | None = Field(default=None, description="Итоговая стоимость")
    master_id: int | None = Field(default=None, description="Идентификатор сотрудника")
    good_id: int | None = Field(default=None, description="Идентификатор товара")
    service_id: int | None = Field(default=None, description="Идентификатор услуги")
    event_id: int | None = Field(default=None, description="Идентификатор акции")
    is_service: bool | None = Field(default=None, description="Является ли услугой")
    is_event: bool | None = Field(default=None, description="Является ли акцией")
    is_good: bool | None = Field(default=None, description="Является ли товаром")


class VisitLoyaltyApplyResponseDataTypesKkmTransactionDetailsContainer(BaseModel):
    """Объект с информацией о ККМ транзакциях записи
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    last_operation_type: int | None = Field(default=None, description="Распечатан ли чек (0 - чек возврата, 1 - чек продажи)")
    transactions: list[dict[str, Any]] | None = Field(default=None, description="Массив ККМ транзакций")


class VisitLoyaltyApplyResponseDataTypesLoyaltyTransactionsItemType(BaseModel):
    """Тип лояльности
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор типа лояльности")
    title: str | None = Field(default=None, description="Название типа лояльности")


class VisitLoyaltyCancelResponseDataTypesItemsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор объекта")
    item_id: int | None = Field(default=None, description="Идентификатор товара/услуги")
    item_type_id: int | None = Field(default=None, description="Идентификатор типа операции")
    record_id: int | None = Field(default=None, description="Идентификатор записи")
    item_title: str | None = Field(default=None, description="Название товара/услуги")
    amount: int | None = Field(default=None, description="Количество товаров/услуг")
    first_cost: float | None = Field(default=None, description="Начальная стоимость")
    manual_cost: float | None = Field(default=None, description="Стоимость, измененная вручную")
    discount: float | None = Field(default=None, description="Скидка")
    cost: float | None = Field(default=None, description="Итоговая стоимость")
    master_id: int | None = Field(default=None, description="Идентификатор сотрудника")
    good_id: int | None = Field(default=None, description="Идентификатор товара")
    service_id: int | None = Field(default=None, description="Идентификатор услуги")
    event_id: int | None = Field(default=None, description="Идентификатор акции")
    is_service: bool | None = Field(default=None, description="Является ли услугой")
    is_event: bool | None = Field(default=None, description="Является ли акцией")
    is_good: bool | None = Field(default=None, description="Является ли товаром")


class VisitLoyaltyCancelResponseDataTypesKkmTransactionDetailsContainer(BaseModel):
    """Объект с информацией о ККМ транзакциях записи
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    last_operation_type: int | None = Field(default=None)
    transactions: list[dict[str, Any]] | None = Field(default=None)


class VisitLoyaltyTransactionReaponseDataTypesItemProgram(BaseModel):
    """Информация об акции
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор акции")
    title: str | None = Field(default=None, description="Название акции")
    value: int | None = Field(default=None, description="Значение скидки")
    loyalty_type_id: int | None = Field(default=None, description="Идентификатор типа акции")
    item_type_id: int | None = Field(default=None, description="Начисляется ли кэшбек от товаров")
    value_unit_id: int | None = Field(default=None, description="Поле \"Бонус\". Скидка % или Фикс. сумма")
    group_id: int | None = Field(default=None, description="Идентифкатор сети, где создана акция")


class VisitLoyaltyTransactionReaponseDataTypesItemType(BaseModel):
    """Тип лояльности
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор типа лояльности")
    title: str | None = Field(default=None, description="Название типа лояльности")


class VisitsVisitidDataTypesDataRecordsItemClient(BaseModel):
    """Информация о клиенте
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор клиента")
    name: str | None = Field(default=None, description="Имя клиента")
    surname: str | None = Field(default=None, description="Фамилия клиента")
    patronymic: str | None = Field(default=None, description="Отчество клиента")
    phone: str | None = Field(default=None, description="Номер телефон клиента")
    card: str | None = Field(default=None, description="Номер карты клиента")
    email: str | None = Field(default=None, description="Email адрес клиента")
    success_visits_count: float | None = Field(default=None, description="Количество визитов клиента, в статусе \"Клиент пришел\"")
    fail_visits_count: float | None = Field(default=None, description="Количество отмененных визитов клиента")


class VisitsVisitidDataTypesDataRecordsItemDocumentsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор документа")
    type_id: float | None = Field(default=None, description="Тип документа")
    storage_id: float | None = Field(default=None, description="Идентификатор склада")
    user_id: float | None = Field(default=None, description="Идентификатор пользователя, создавшего документ")
    company_id: float | None = Field(default=None, description="Идентификатор компании")
    number: float | None = Field(default=None, description="Номер документа")
    comment: str | None = Field(default=None, description="Комментарий к документу")
    date_created: str | None = Field(default=None, description="Дата создания документа")
    category_id: int | None = Field(default=None, description="Идентификатор категории товара")
    visit_id: int | None = Field(default=None, description="Идентификатор визита")
    record_id: int | None = Field(default=None, description="Идентификатор записи")
    type_title: str | None = Field(default=None, description="Название сущности, к которой принадлежит документ")
    is_sale_bill_printed: Any | None = Field(default=None, description="Чек продажи распечатан")


class VisitsVisitidDataTypesDataRecordsItemStaffPosition(BaseModel):
    """Должность сотрудника
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор должности")
    title: str | None = Field(default=None, description="Название должности")


class VoipIntegrationResponseDataTypesMeta(BaseModel):
    """Метаданные (содержить сообщение "Accepted")
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    message: str | None = Field(default=None)


class VisitLoyaltyCancelResponseDataTypes(BaseModel):
    """Отмена лояльности в визите
    Схема спеки: Root Type for visit_loyalty_cancel_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    payment_transactions: list[dict[str, Any]] | None = Field(default=None, description="Массив с информацией о финансовых транзакциях записи")
    loyalty_transactions: list[dict[str, Any]] | None = Field(default=None, description="Массив с информацией о примененных транзакциях лояльности в визите")
    kkm_transaction_details_container: VisitLoyaltyCancelResponseDataTypesKkmTransactionDetailsContainer | None = Field(default=None)
    items_: list[VisitLoyaltyCancelResponseDataTypesItemsItem] | None = Field(default=None, alias="items", description="Массив с информацией о товарах и услугах записи")


class VisitLoyaltyRequestDataTypes(BaseModel):
    """Применить акцию
    Схема спеки: Root Type for visit_loyalty_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    record_id: float = Field(description="Идентификатор записи")
    visit_id: float = Field(description="Идентификатор визита")


class VoipIntegrationDisableRequestDataTypes(BaseModel):
    """Отключить интеграцию
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    command: str = Field(description="Slug операции 'setup'")
    type_: str = Field(alias="type", description="Тип операции, в данном случае 'disable'")
    crm_token: str = Field(description="CRM-токен из раздела Телефония-Интеграция в сети клиента")


class VoipIntegrationEnableRequestDataTypes(BaseModel):
    """Подключить интеграцию
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    command: str = Field(description="Slug операции 'setup'")
    type_: str = Field(alias="type", description="Тип операции, в данном случае 'enable'")
    crm_token: str = Field(description="CRM-токен из раздела Телефония-Интеграция в сети клиента")


class VoipIntegrationHistoryRequestDataTypes(BaseModel):
    """Сохранение информации о звонке
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    command: str = Field(description="Операции 'history'")
    type_: str = Field(alias="type", description="Тип операции (\"incoming\", \"outgoing\", \"internal\")")
    crm_token: str = Field(description="CRM-токен из раздела Телефония-Интеграция в сети клиента")
    phone: str = Field(description="Номер звонящего абонента")
    user: str | None = Field(default=None, description="Идентификатор абонента телефонии, sip")
    diversion: str = Field(description="Номер через который пришел звонок")
    duration: float | None = Field(default=None, description="Длительность звонка (в секундах)")
    link: str | None = Field(default=None, description="Ссылка на запись звонка")
    call_id: str | None = Field(default=None, description="Идентификатор звонка в системе voip")
    status: str | None = Field(default=None, description="Статус звонка 'success'|'missed'")
    date: str | None = Field(default=None, description="Дата и время звонка (ISO8601)")


class VoipIntegrationNotificationRequestDataTypes(BaseModel):
    """Уведомление о звонке
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    command: str = Field(description="Slug операции 'event'")
    type_: str = Field(alias="type", description="Тип операции, в данном случае \"incoming\"")
    crm_token: str = Field(description="CRM-токен из раздела Телефония-Интеграция в сети клиента")
    phone: str = Field(description="Номер звонящего абонента")
    user: str | None = Field(default=None, description="SIP номер телефонии")
    diversion: str = Field(description="Номер через который пришел звонок")


class VoipIntegrationResponseDataTypes(BaseModel):
    """Подключить интеграцию
    Схема спеки: Root Type for voip_integration_setup_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успшности выполнения (true)")
    data_: str | None = Field(default=None, alias="data", description="Содержит null")
    meta: VoipIntegrationResponseDataTypesMeta | None = Field(default=None)


class VisitDetailsDataTypesDataKkmTransactionDetailsContainerTransactionsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор транзакции")
    print_date: str | None = Field(default=None, description="Дата печати чека")
    printed_count: int | None = Field(default=None)
    sum: float | None = Field(default=None, description="Сумма оплаты с точностью 2 знака после запятой")
    type_: VisitDetailsDataTypesDataKkmTransactionDetailsContainerTransactionsItemType | None = Field(default=None, alias="type")
    status: VisitDetailsDataTypesDataKkmTransactionDetailsContainerTransactionsItemStatus | None = Field(default=None)
    document: VisitDetailsDataTypesDataKkmTransactionDetailsContainerTransactionsItemDocument | None = Field(default=None)
    cashier: VisitDetailsDataTypesDataKkmTransactionDetailsContainerTransactionsItemCashier | None = Field(default=None)


class VisitDetailsDataTypesDataLoyaltyTransactionsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор транзакции")
    status_id: float | None = Field(default=None, description="Идентификатор статуса транзакции")
    amount: float | None = Field(default=None, description="Сумма оплаты лояльностью")
    type_id: float | None = Field(default=None, description="Тип транзакции лояльности")
    program_id: float | None = Field(default=None, description="Идентификатор программы лояльности")
    card_id: float | None = Field(default=None, description="Идентификатор карты лояльности")
    salon_group_id: float | None = Field(default=None, description="ID сети салонов, в рамках лояльности которой была создана данная транзакция")
    item_id: float | None = Field(default=None, description="Идентификатор позиции в заказе, если транзакция связана с продажей товара или услуги")
    item_type_id: float | None = Field(default=None, description="Тип позиции в заказе, к которой относится данная транзакция (1 Оказание услуги, 7 Продажа товара), если применимо")
    item_record_id: float | None = Field(default=None, description="ID записи к которой относится позиция в заказе, если применимо")
    goods_transaction_id: float | None = Field(default=None, description="ID транзакции продажи товара")
    is_discount: bool | None = Field(default=None)
    is_loyalty_withdraw: bool | None = Field(default=None)
    type_: VisitDetailsDataTypesDataLoyaltyTransactionsItemType | None = Field(default=None, alias="type")


class VisitDetailsDataTypesDataPaymentTransactionsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор транзакции оплаты")
    document_id: float | None = Field(default=None, description="Идентификатор документу")
    date: str | None = Field(default=None, description="Дата транзакции")
    type_id: float | None = Field(default=None, description="Тип транзакции")
    expense_id: float | None = Field(default=None, description="Идентификатор статьи платежа")
    account_id: float | None = Field(default=None, description="Идентификатор кассы")
    amount: float | None = Field(default=None, description="Сумма оплаты")
    client_id: float | None = Field(default=None, description="Идентификатор клиента")
    master_id: float | None = Field(default=None, description="Идентификатор сотрудника")
    supplier_id: float | None = Field(default=None, description="Идентификатор поставщика")
    comment: str | None = Field(default=None, description="Комментарий")
    item_id: float | None = Field(default=None, description="Идентификатор товара")
    target_type_id: int | None = Field(default=None)
    record_id: float | None = Field(default=None, description="Идентификатор записи")
    goods_transaction_id: float | None = Field(default=None, description="Идентификатор товарной транзакции")
    expense: VisitDetailsDataTypesDataPaymentTransactionsItemExpense | None = Field(default=None)
    account: VisitDetailsDataTypesDataPaymentTransactionsItemAccount | None = Field(default=None)
    client_: VisitDetailsDataTypesDataPaymentTransactionsItemClient | None = Field(default=None, alias="client")
    master: list[dict[str, Any]] | None = Field(default=None, description="Сотрудник")
    supplier: list[dict[str, Any]] | None = Field(default=None, description="Поставщик")


class VisitLoyaltyApplyResponseDataTypesLoyaltyTransactionsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор транзакции лояльности")
    status_id: int | None = Field(default=None, description="Идентификатор статуса")
    amount: float | None = Field(default=None, description="Сумма транзакции")
    type_id: int | None = Field(default=None, description="Идентификатор типа транзакции")
    program_id: int | None = Field(default=None, description="Идентификатор программы лояльности")
    card_id: int | None = Field(default=None, description="Идентификатор карты лояльности")
    salon_group_id: int | None = Field(default=None, description="Идентификатор сети, которой принадлежит лояльность")
    item_id: int | None = Field(default=None, description="Идентификатор товара/услуги, к которой применяется акция")
    item_type_id: int | None = Field(default=None, description="Идентификатор типа операции")
    item_record_id: int | None = Field(default=None, description="Идентификатор записи, которой принадлежит услуга/товар")
    goods_transaction_id: int | None = Field(default=None, description="Идентификатор товарной транзакции")
    is_discount: bool | None = Field(default=None, description="Является ли скидкой")
    is_loyalty_withdraw: bool | None = Field(default=None, description="Отменено ли применение лояльности")
    type_: VisitLoyaltyApplyResponseDataTypesLoyaltyTransactionsItemType | None = Field(default=None, alias="type")


class VisitLoyaltyTransactionReaponseDataTypesItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор транзакции лояльности")
    status_id: int | None = Field(default=None, description="Идентификатор статуса")
    amount: float | None = Field(default=None, description="Сумма транзакции")
    type_id: int | None = Field(default=None, description="Идентификатор типа транзакции")
    program_id: int | None = Field(default=None, description="Идентификатор программы лояльности")
    card_id: int | None = Field(default=None, description="Идентификатор карты лояльности")
    salon_group_id: int | None = Field(default=None, description="Идентификатор сети, которой принадлежит лояльность")
    item_id: int | None = Field(default=None, description="Идентификатор товара/услуги, к которой применяется акция")
    item_type_id: int | None = Field(default=None, description="Идентификатор типа операции")
    item_record_id: int | None = Field(default=None, description="Идентификатор записи, которой принадлежит услуга/товар")
    goods_transaction_id: int | None = Field(default=None, description="Идентификатор товарной транзакции")
    is_discount: bool | None = Field(default=None, description="Является ли скидкой")
    is_loyalty_withdraw: bool | None = Field(default=None, description="Отменено ли применение лояльности")
    type_: VisitLoyaltyTransactionReaponseDataTypesItemType | None = Field(default=None, alias="type")
    program: VisitLoyaltyTransactionReaponseDataTypesItemProgram | None = Field(default=None)


class VisitsVisitidDataTypesDataRecordsItemStaff(BaseModel):
    """Информация о сотруднике
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор сотрудника")
    name: str | None = Field(default=None, description="Имя сотрудника")
    specialization: str | None = Field(default=None, description="Специализация сотрудника")
    position: VisitsVisitidDataTypesDataRecordsItemStaffPosition | None = Field(default=None)
    avatar: str | None = Field(default=None, description="Путь к файлу с аватаркой сотрудника")
    avatar_big: str | None = Field(default=None, description="Путь к файлу с аватаркой сотрудника большего разрешения")
    rating: float | None = Field(default=None, description="Рейтинг")
    votes_count: float | None = Field(default=None, description="Кол-во голосов, оценивших сотрудника")


class VisitLoyaltyApplyResponseDataTypes(BaseModel):
    """Применение лояльности в визите
    Схема спеки: Root Type for visit_loyalty_apply_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    payment_transactions: list[dict[str, Any]] | None = Field(default=None, description="Массив с информацией о финансовых транзакциях записи")
    loyalty_transactions: list[VisitLoyaltyApplyResponseDataTypesLoyaltyTransactionsItem] | None = Field(default=None, description="Массив с информацией о примененных транзакциях лояльности в визите")
    kkm_transaction_details_container: VisitLoyaltyApplyResponseDataTypesKkmTransactionDetailsContainer | None = Field(default=None)
    items_: list[VisitLoyaltyApplyResponseDataTypesItemsItem] | None = Field(default=None, alias="items", description="Массив с информацией о товарах и услугах записи")


class VisitDetailsDataTypesDataKkmTransactionDetailsContainer(BaseModel):
    """Детали ККМ транзакции
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    last_operation_type: float | None = Field(default=None, description="Тип последней операции ККМ")
    transactions: list[VisitDetailsDataTypesDataKkmTransactionDetailsContainerTransactionsItem] | None = Field(default=None, description="Транзакция ККМ")


class VisitsVisitidDataTypesDataRecordsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор записи")
    company_id: float | None = Field(default=None, description="Идентификатор компании")
    staff_id: float | None = Field(default=None, description="Идентификатор сотрудника")
    services: list[dict[str, Any]] | None = Field(default=None, description="Массив услуг")
    events: list[dict[str, Any]] | None = Field(default=None)
    goods_transactions: list[dict[str, Any]] | None = Field(default=None, description="Массив товарных транзакций")
    staff: VisitsVisitidDataTypesDataRecordsItemStaff | None = Field(default=None)
    client_: VisitsVisitidDataTypesDataRecordsItemClient | None = Field(default=None, alias="client")
    date: str | None = Field(default=None, description="Дата визита")
    datetime: str | None = Field(default=None, description="Дата визита в формате ISO")
    create_date: str | None = Field(default=None, description="Дата создания визита")
    comment: str | None = Field(default=None, description="Комментарий к визиту")
    online: bool | None = Field(default=None, description="(Только при чтении) Запись онлайновая или нет (false если запись внес администратор)")
    visit_attendance: float | None = Field(default=None, description="Статус визита")
    attendance: float | None = Field(default=None, description="Статус записи в визите")
    confirmed: float | None = Field(default=None, description="Подтверждена ли запись")
    seance_length: float | None = Field(default=None, description="Длительность визита")
    length: float | None = Field(default=None, description="Длительность услуги в визите")
    sms_before: float | None = Field(default=None, description="Отправить ли клиенту смс с напоминанием о записи (если клиент указан)")
    sms_now: float | None = Field(default=None, description="Отправляли ли смс при добавлении записи")
    sms_now_text: str | None = Field(default=None, description="Текст смс")
    email_now: float | None = Field(default=None, description="Отправлено ли уведомление по email")
    notified: float | None = Field(default=None, description="Флаг пождтверждения записи администратором филиала, если клиент попросил подтвердить запись")
    master_request: float | None = Field(default=None, description="Был ли указан определенный специалист при записи (false если был указан \"не имеет значения\")")
    api_id: str | None = Field(default=None, description="Внешний идентификатор записи")
    from_url: str | None = Field(default=None, description="С какой страницы был совершён переход для оформления записи (сайт, приложение ВК и прочее)")
    review_requested: float | None = Field(default=None, description="Флаг запроса у клиента отзыва о посещении")
    activity_id: float | None = Field(default=None, description="Идентификатор групповой записи")
    documents: list[VisitsVisitidDataTypesDataRecordsItemDocumentsItem] | None = Field(default=None)


class VisitDetailsDataTypesData(BaseModel):
    """Объект с данными
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    payment_transactions: list[VisitDetailsDataTypesDataPaymentTransactionsItem] | None = Field(default=None, description="Транзакции оплаты")
    loyalty_transactions: list[VisitDetailsDataTypesDataLoyaltyTransactionsItem] | None = Field(default=None, description="Транзакции лояльности")
    kkm_transaction_details_container: VisitDetailsDataTypesDataKkmTransactionDetailsContainer | None = Field(default=None)
    items_: list[VisitDetailsDataTypesDataItemsItem] | None = Field(default=None, alias="items", description="Массив товаров\\услуг")


class VisitsVisitidDataTypesData(BaseModel):
    """Объект с данными
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    attendance: float | None = Field(default=None, description="Статус визита")
    datetime: str | None = Field(default=None, description="Дата визита")
    comment: int | None = Field(default=None, description="Комментарий")
    records: list[VisitsVisitidDataTypesDataRecordsItem] | None = Field(default=None, description="Массив записей")


class VisitDetailsDataTypes(BaseModel):
    """Получить детали визита
    Схема спеки: Root Type for visit_details_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: VisitDetailsDataTypesData | None = Field(default=None, alias="data")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")


class VisitsVisitidDataTypes(BaseModel):
    """Получить визит
    Схема спеки: Root Type for visits_visitid_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: VisitsVisitidDataTypesData | None = Field(default=None, alias="data")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")

__all__ = [
    "VisitDetailsDataTypes",
    "VisitDetailsDataTypesData",
    "VisitDetailsDataTypesDataItemsItem",
    "VisitDetailsDataTypesDataKkmTransactionDetailsContainer",
    "VisitDetailsDataTypesDataKkmTransactionDetailsContainerTransactionsItem",
    "VisitDetailsDataTypesDataKkmTransactionDetailsContainerTransactionsItemCashier",
    "VisitDetailsDataTypesDataKkmTransactionDetailsContainerTransactionsItemDocument",
    "VisitDetailsDataTypesDataKkmTransactionDetailsContainerTransactionsItemStatus",
    "VisitDetailsDataTypesDataKkmTransactionDetailsContainerTransactionsItemType",
    "VisitDetailsDataTypesDataLoyaltyTransactionsItem",
    "VisitDetailsDataTypesDataLoyaltyTransactionsItemType",
    "VisitDetailsDataTypesDataPaymentTransactionsItem",
    "VisitDetailsDataTypesDataPaymentTransactionsItemAccount",
    "VisitDetailsDataTypesDataPaymentTransactionsItemClient",
    "VisitDetailsDataTypesDataPaymentTransactionsItemExpense",
    "VisitLoyaltyApplyResponseDataTypes",
    "VisitLoyaltyApplyResponseDataTypesItemsItem",
    "VisitLoyaltyApplyResponseDataTypesKkmTransactionDetailsContainer",
    "VisitLoyaltyApplyResponseDataTypesLoyaltyTransactionsItem",
    "VisitLoyaltyApplyResponseDataTypesLoyaltyTransactionsItemType",
    "VisitLoyaltyCancelResponseDataTypes",
    "VisitLoyaltyCancelResponseDataTypesItemsItem",
    "VisitLoyaltyCancelResponseDataTypesKkmTransactionDetailsContainer",
    "VisitLoyaltyRequestDataTypes",
    "VisitLoyaltyTransactionReaponseDataTypesItem",
    "VisitLoyaltyTransactionReaponseDataTypesItemProgram",
    "VisitLoyaltyTransactionReaponseDataTypesItemType",
    "VisitsVisitidDataTypes",
    "VisitsVisitidDataTypesData",
    "VisitsVisitidDataTypesDataRecordsItem",
    "VisitsVisitidDataTypesDataRecordsItemClient",
    "VisitsVisitidDataTypesDataRecordsItemDocumentsItem",
    "VisitsVisitidDataTypesDataRecordsItemStaff",
    "VisitsVisitidDataTypesDataRecordsItemStaffPosition",
    "VoipIntegrationDisableRequestDataTypes",
    "VoipIntegrationEnableRequestDataTypes",
    "VoipIntegrationHistoryRequestDataTypes",
    "VoipIntegrationNotificationRequestDataTypes",
    "VoipIntegrationResponseDataTypes",
    "VoipIntegrationResponseDataTypesMeta"
]
