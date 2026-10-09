"""Модели YCLIENTS API (t: T).

Сгенерировано scripts/generate.py -- не редактируйте вручную.
"""

from __future__ import annotations

from datetime import date, datetime
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class TaxSystemResponseDataTypesDataItemVatsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    title: str | None = Field(default=None, description="Название НДС")
    slug: str | None = Field(default=None, description="Кодовое название НДС")


class TaxSystemResponseDataTypesMeta(BaseModel):
    """Метаданные (содержит количество найденных систем налогообложения)
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    count_: int | None = Field(default=None, alias="count")


class TechnologicalCardsConsumablesResponse200DataTypesDataItemConsumablesItemGood(BaseModel):
    """Товар
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор товара")
    title: str | None = Field(default=None, description="Название товара")
    unit: str | None = Field(default=None, description="Единица измерения")


class TechnologicalCardsConsumablesResponse200DataTypesDataItemTechnologicalCardsItemTechnologicalCardItemsItemGood(BaseModel):
    """Товар
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор товара")
    title: str | None = Field(default=None, description="Название товара")
    unit: str | None = Field(default=None, description="Единица измерения")


class TechnologicalCardsConsumablesResponse200DeleteDataTypesDataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    service_id: float | None = Field(default=None, description="Идентификатор услуги")
    record_id: float | None = Field(default=None, description="Идентификатор записи")
    technological_cards: list[dict[str, Any]] | None = Field(default=None, description="Массив технологических карт")
    consumables: list[dict[str, Any]] | None = Field(default=None, description="Расходники")


class TechnologicalCardsConsumablesResponse200DeleteDataTypesMeta(BaseModel):
    """Метаданные (пустой массив)
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    count_: int | None = Field(default=None, alias="count")


class TechnologicalCardsResponse200DataTypesDataItemTechnologicalCardItemsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор расходника")
    technological_card_id: float | None = Field(default=None, description="Идентификатор тех. карты")
    storage_id: float | None = Field(default=None, description="Идентификатор склада")
    good_id: float | None = Field(default=None, description="Идентификатор товара")
    amount: float | None = Field(default=None, description="Количество")
    unit: str | None = Field(default=None, description="Единица измерения")
    price: float | None = Field(default=None, description="Стоимость")
    title: str | None = Field(default=None, description="Название")


class TimetableActivityResponseDataAttributes(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор группового события.")
    master_id: int | None = Field(default=None, description="Идентификатор мастера.")
    staff_id: int | None = Field(default=None, description="Идентификатор мастера.")
    service_id: int | None = Field(default=None, description="Идентификатор услуги.")
    timestamp: int | None = Field(default=None, description="Времменая метка начала события.")
    length: int | None = Field(default=None, description="Продолжительность.")
    capacity: int | None = Field(default=None, description="Количество мест.")
    clients_count: int | None = Field(default=None, description="Количество клиентов.")
    color: str | None = Field(default=None, description="Цвет.")
    instructions: str | None = Field(default=None, description="Инструкции.")
    stream_link: str | None = Field(default=None, description="Ссылка для подключения.")
    font_color: str | None = Field(default=None, description="Цвет.")
    notified: bool | None = Field(default=None, description="Было ли отправлено уведомление.")
    comment: str | None = Field(default=None, description="Комментарий.")
    schedule_id: int | None = Field(default=None, description="Идентификатор расписания.")
    schedule_till: int | None = Field(default=None, description="Дата окончания расписания.")


class TimetableRecordResponseDataAttributes(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    company_id: int | None = Field(default=None, description="Идентификатор компании.")
    external_id: str | None = Field(default=None, description="Внешний id для идентификации новых записей.")
    visit_id: int | None = Field(default=None, description="Идентификатор визита.")
    booking_user_id: int | None = Field(default=None, description="Идентификатор клиента.")
    bookform_id: int | None = Field(default=None, description="Идентификатор формы онлайн-записи.")
    master_id: int | None = Field(default=None, description="Идентификатор сотрудника.")
    staff_id: int | None = Field(default=None, description="Идентификатор сотрудника.")
    client_id: int | None = Field(default=None, description="Идентификатор клиента.")
    comer_id: int | None = Field(default=None, description="Идентификатор посетителя.")
    attendance_status: int | None = Field(default=None, description="Статус посещения. (-2 - любой статус, -1 - клиент не пришёл, 0 - клиент пришёл, 1 - ожидание клиента, 2 - клиент подтвердил запись)")
    attendance_status_slug: Literal["absent", "waiting", "attended", "confirmed"] | None = Field(default=None, description="Строковый идентификатор статуса записи.")
    client_fictive_name: str | None = Field(default=None, description="Имя клиента, при отсутствии связанного обьекта клиента.")
    client_fictive_phone: str | None = Field(default=None, description="Телефон клиента, при отсутствии связанного обьекта клиента.")
    client_fictive_email: str | None = Field(default=None, description="Электронная почта клиента, при отсутствии связанного обьекта клиента.")
    clients_count: int | None = Field(default=None, description="Количество клиентов.")
    activity_id: int | None = Field(default=None, description="Идентификатор группового события.")
    custom_color: str | None = Field(default=None, description="Цвет фона.")
    custom_font_color: str | None = Field(default=None, description="Цвет шрифта.")
    duration: int | None = Field(default=None, description="Длительность.")
    is_paid: bool | None = Field(default=None, description="Количество мест.")
    is_overpaid: bool | None = Field(default=None, description="Признак переплаты.")
    timestamp: str | None = Field(default=None, description="Временная метка начала записи.")
    created_datetime: str | None = Field(default=None, description="Дата и время создания записи.")
    comment: str | None = Field(default=None, description="Комментарий.")
    prepaid_status: int | None = Field(default=None, description="Стаутс предоплаты.")
    payment_status: int | None = Field(default=None, description="Статус оплаты.")
    is_sale_bill_printed: bool | None = Field(default=None, description="Признак распечатанного чека.")
    is_client_notification_sent: bool | None = Field(default=None, description="Было ли отправлено уведомление.")


class TipsSettingResponseDataTypesDataItemStaffEmployee(BaseModel):
    """Сотрудник
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор сотрудника")
    phone: str | None = Field(default=None, description="Телефон")


class TipsSettingResponseDataTypesDataItemStaffPosition(BaseModel):
    """Должность
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор должности")
    title: str | None = Field(default=None, description="Название должности")


class TipsSettingResponseDataTypesDataItemStaffUser(BaseModel):
    """Пользователь
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор пользователя")
    name: str | None = Field(default=None, description="Имя пользователя")
    email: str | None = Field(default=None, description="Email адрес пользователя")
    phone: str | None = Field(default=None, description="Телефон пользователя")


class TipsSettingResponseDataTypesMeta(BaseModel):
    """Метаданные (содержит количество найденных мастеров)
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    count_: int | None = Field(default=None, alias="count")


class TransactionCompanyidResponseDataTypesDataItemAccount(BaseModel):
    """Касса
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор кассы")
    title: str | None = Field(default=None, description="Название кассы")


class TransactionCompanyidResponseDataTypesDataItemClient(BaseModel):
    """Клиент
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор клиента")
    name: str | None = Field(default=None, description="Имя клиента")
    phone: str | None = Field(default=None, description="Телефон клиента")


class TransactionCompanyidResponseDataTypesDataItemExpense(BaseModel):
    """Тип платежа
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор типа платежа")
    title: str | None = Field(default=None, description="Название типа платежа")


class TransactionCompanyidResponseDataTypesDataItemMaster(BaseModel):
    """Мастер
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор сотрудника")
    title: str | None = Field(default=None, description="Имя сотрудника")


class TransactionCompanyidResponseDataTypesDataItemSupplier(BaseModel):
    """Контрагент
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор контрагента")
    title: str | None = Field(default=None, description="Название контрагента")


class TechnologicalCardsConsumablesResponse200DeleteDataTypes(BaseModel):
    """Удалит технологическую карты из связи запись-услуга
    Схема спеки: Root Type for technological_cards_consumables_response200_delete_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: list[TechnologicalCardsConsumablesResponse200DeleteDataTypesDataItem] | None = Field(default=None, alias="data", description="Массив с объектом")
    meta: TechnologicalCardsConsumablesResponse200DeleteDataTypesMeta | None = Field(default=None)


class TipsReduce(BaseModel):
    """Информация о наличии чаевых сотруднику. Модель используется, когда текущий пользователь не является мастером в данной записи.
    Схема спеки: Объект модели "Наличие чаевых без суммы"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    has_tips: bool | None = Field(default=None, description="Есть ли чаевые в данной записи.")
    sum: float | None = Field(default=None, description="Сумма чаевых не подсчитывается и равна `null`.")


class TipsReduceWithFullInfo(BaseModel):
    """Информация о сумме всех чаевых сотруднику. Используется, если текущий пользователь является мастером в данной записи.
    Схема спеки: Объект модели "Суммарные чаевые"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    has_tips: bool | None = Field(default=None, description="Есть ли чаевые в данной записи.")
    sum: float | None = Field(default=None, description="Сумма чаевых.")


class TaxSystemResponseDataTypesDataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    title: str | None = Field(default=None, description="Название системы налогообложения")
    slug: str | None = Field(default=None, description="Кодовое название системы налогообложения")
    vats: list[TaxSystemResponseDataTypesDataItemVatsItem] | None = Field(default=None, description="Список доступных НДС для системы налогообложения")


class TechnologicalCardsConsumablesResponse200DataTypesDataItemConsumablesItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    goods_transaction_id: float | None = Field(default=None, description="Идентификатор товарной транзакции")
    record_id: float | None = Field(default=None, description="Идентификатор записи")
    service_id: float | None = Field(default=None, description="Идентификатор услуги")
    storage_id: float | None = Field(default=None, description="Идентификатор склада")
    good_id: float | None = Field(default=None, description="Идентификатор товара")
    price: float | None = Field(default=None, description="Стоимость")
    amount: float | None = Field(default=None, description="Количество")
    good: TechnologicalCardsConsumablesResponse200DataTypesDataItemConsumablesItemGood | None = Field(default=None)


class TechnologicalCardsConsumablesResponse200DataTypesDataItemTechnologicalCardsItemTechnologicalCardItemsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор расходника")
    technological_card_id: float | None = Field(default=None, description="Идентификатор тех.карты")
    storage_id: float | None = Field(default=None, description="Идентификатор склада")
    good_id: float | None = Field(default=None, description="Идентификатор товара")
    amount: float | None = Field(default=None, description="Количество")
    price: float | None = Field(default=None, description="Стоимость")
    good: TechnologicalCardsConsumablesResponse200DataTypesDataItemTechnologicalCardsItemTechnologicalCardItemsItemGood | None = Field(default=None)


class TechnologicalCardsResponse200DataTypesDataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: str | None = Field(default=None, alias="id", description="Идентификатор тех. карты")
    title: str | None = Field(default=None, description="Название тех. карты")
    technological_card_items: list[TechnologicalCardsResponse200DataTypesDataItemTechnologicalCardItemsItem] | None = Field(default=None, description="Список расходников тех. карт")


class TimetableActivityResponseData(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    type_: str | None = Field(default=None, alias="type", description="Тип сущности.")
    id_: str | None = Field(default=None, alias="id", description="Идентифкатор события.")
    attributes: TimetableActivityResponseDataAttributes | None = Field(default=None)


class TimetableRecordResponseData(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    type_: str | None = Field(default=None, alias="type", description="Тип сущности.")
    id_: str | None = Field(default=None, alias="id", description="Идентифкатор записи.")
    attributes: TimetableRecordResponseDataAttributes | None = Field(default=None)


class TipsSettingResponseDataTypesDataItemStaff(BaseModel):
    """Мастер
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор мастера")
    name: str | None = Field(default=None, description="Имя мастера")
    specialization: str | None = Field(default=None, description="Специализация")
    avatar: str | None = Field(default=None, description="Путь к аватарке сотрудника")
    employee: TipsSettingResponseDataTypesDataItemStaffEmployee | None = Field(default=None)
    user: TipsSettingResponseDataTypesDataItemStaffUser | None = Field(default=None)
    position: TipsSettingResponseDataTypesDataItemStaffPosition | None = Field(default=None)


class TransactionCompanyidResponseDataTypesDataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор транзакции")
    document_id: float | None = Field(default=None, description="Идентификатор документа")
    expense: TransactionCompanyidResponseDataTypesDataItemExpense | None = Field(default=None)
    date: str | None = Field(default=None, description="Дата создания транзакции")
    amount: float | None = Field(default=None, description="Сумма транзакции")
    comment: str | None = Field(default=None, description="Комментарий")
    master: TransactionCompanyidResponseDataTypesDataItemMaster | None = Field(default=None)
    supplier: TransactionCompanyidResponseDataTypesDataItemSupplier | None = Field(default=None)
    account: TransactionCompanyidResponseDataTypesDataItemAccount | None = Field(default=None)
    client_: TransactionCompanyidResponseDataTypesDataItemClient | None = Field(default=None, alias="client")
    last_change_date: str | None = Field(default=None, description="Дата последнего изменения")
    record_id: float | None = Field(default=None, description="Идентификатор записи")
    visit_id: float | None = Field(default=None, description="Идентификатор визита")
    sold_item_id: float | None = Field(default=None, description="Идентификатор проданного товара/услуги")
    sold_item_type: float | None = Field(default=None, description="Тип сущности продаджи (товар/услуга)")


class TaxSystemResponseDataTypes2(BaseModel):
    """Пример запроса на получение списка
    Схема спеки: Root Type for tax_system_response_data_Types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: list[TaxSystemResponseDataTypesDataItem] | None = Field(default=None, alias="data", description="Массив объектов с данными")
    meta: TaxSystemResponseDataTypesMeta | None = Field(default=None)


class TechnologicalCardsResponse200DataTypes(BaseModel):
    """Получить список тех. карт
    Схема спеки: Root Type for technological_cards_response200_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: list[TechnologicalCardsResponse200DataTypesDataItem] | None = Field(default=None, alias="data", description="Массив объеков с данными")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")


class TimetableActivityResponse(BaseModel):
    """Схема спеки: Объект модели "Групповое событие"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data_: TimetableActivityResponseData | None = Field(default=None, alias="data")


class TimetableEventScheduleEvent2(BaseModel):
    """Данные по сущности конкретной записи или события в рамках расписания.
    Схема спеки: Объект модели "Сущность записи/события в Расписании"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор сущности записи/события в расписании.")
    created_at: str | None = Field(default=None, description="Дата и время создания сущности записи/события в расписании.")
    updated_at: str | None = Field(default=None, description="Дата и время последнего обновления сущности записи/события в расписании.")
    deleted_at: str | None = Field(default=None, description="Дата и время удаления сущности записи/события в расписании.")
    event_status: Literal["stable", "event_created", "event_changed", "event_changed_force", "event_deleted", "entity_deleted", "entity_failed"] | None = Field(default=None, description="Статус сущности записи/события в расписании: `stable` - сущность стабильна; `event_created` - сущность только что создана, соответствующая запись/событие еще не создано; `event_changed` - сущность ...")
    event_datetime: str | None = Field(default=None, description="Дата и время начала записи/события, согласно расписания.")
    event_entity_type: Literal["record", "activity"] | None = Field(default=None, description="Тип сущности, созданной в рамках расписания.")
    event_entity_id: float | None = Field(default=None, description="Идентификатор сущности, созданной в рамках расписания.")
    is_entity_master_changed: bool | None = Field(default=None, description="Флаг ручного изменения сотрудника, оказывающего услуги в рамках конкретной записи/события.")
    is_entity_datetime_changed: bool | None = Field(default=None, description="Флаг ручного изменения даты и времени конкретной записи/события.")
    is_entity_duration_changed: bool | None = Field(default=None, description="Флаг ручного изменения длительности конкретной записи/события.")
    is_entity_labels_changed: bool | None = Field(default=None, description="Флаг ручного изменения категорий, привязанных к конкретной записи/событию.")
    is_entity_resource_instances_changed: bool | None = Field(default=None, description="Флаг ручного изменения экземпляров ресурсов, привязанных к конкретной записи/событию.")
    entity_master: dict[str, Any] | None = Field(default=None, description="Сотрудник, оказывающий услуги в рамках конкретной записи/события расписания.")
    entity_datetime: str | None = Field(default=None, description="Дата и время начала записи/события, актуальные на текущий момент.")
    entity_duration: str | None = Field(default=None, description="Длительность записи/события, актуальная на текущий момент.")
    entity_labels: list[Label] | None = Field(default=None, description="Категории, привязанные к записи/событию, актуальные на текущий момент.")
    entity_resource_instances: list[ResourceInstance] | None = Field(default=None, description="Экземпляры ресурсов, привязанные к записи/событию, актуальные на текущий момент.")


class TimetableRecordResponse(BaseModel):
    """Схема спеки: Объект модели "Групповое событие"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data_: TimetableRecordResponseData | None = Field(default=None, alias="data")


class TransactionCompanyidResponseDataTypes(BaseModel):
    """Получить транзакции
    Схема спеки: Root Type for transaction_companyid_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: list[TransactionCompanyidResponseDataTypesDataItem] | None = Field(default=None, alias="data", description="Массив объектов с данными")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")


class TechnologicalCardsConsumablesResponse200DataTypesDataItemTechnologicalCardsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор тех карты")
    title: str | None = Field(default=None, description="Название тех. карты")
    technological_card_items: list[TechnologicalCardsConsumablesResponse200DataTypesDataItemTechnologicalCardsItemTechnologicalCardItemsItem] | None = Field(default=None, description="Расходники тех. карты")


class TipsSettingResponseDataTypesDataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор настройки")
    location_id: int | None = Field(default=None)
    staff_id: float | None = Field(default=None, description="Идентификатор сотрудника")
    hash: str | None = Field(default=None, description="Хэш-токен")
    status: float | None = Field(default=None, description="Статус настройки")
    status_title: str | None = Field(default=None, description="Название статуса")
    is_enabled: bool | None = Field(default=None, description="Включена ли настройка чаевых")
    landing_external: str | None = Field(default=None)
    master_tips_form_link: str | None = Field(default=None, description="Ссылка на страницу, где можно оставить чаевые мастеру")
    invite_sms_sent: bool | None = Field(default=None)
    staff: TipsSettingResponseDataTypesDataItemStaff | None = Field(default=None)


class TimetableEventScheduleDay2(BaseModel):
    """Данные по существующей в филиале серии расписания.
    Схема спеки: Объект модели "Серия Расписания"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор серии расписания.")
    created_at: str | None = Field(default=None, description="Дата и время создания серии расписания.")
    updated_at: str | None = Field(default=None, description="Дата и время последнего обновления серии расписания.")
    deleted_at: str | None = Field(default=None, description="Дата и время удаления серии расписания.")
    timetable_event_schedule_id: float | None = Field(default=None, description="Идентификатор расписания, к которому привязана данная серия расписания.")
    day_of_week: Literal["mon", "tue", "wed", "thu", "fri", "sat", "sun"] | None = Field(default=None, description="День недели серии расписания.")
    events_time: str | None = Field(default=None, description="Время начала записей или событий в рамках серии расписания.")
    events_duration: float | None = Field(default=None, description="Длительность записей или событий в рамках серии расписания. ⚠️ Без учёта тех.перерыва")
    event_technical_break_duration: float | None = Field(default=None, description="Длительность технического перерыва")
    events_master: dict[str, Any] | None = Field(default=None, description="Сотрудник, оказывающий услуги в рамках серии расписания. Возвращается в ответе, если в запросе указан параметр `include` с соответствующим значением.")
    events_labels: list[Label] | None = Field(default=None, description="Категории индивидуальных записей или групповых событий, привязанные к записям или событиям в рамках серии расписания. Возвращаются в ответе, если в запросе указан параметр `include` с соответствующ...")
    events_resource_instances: list[ResourceInstance] | None = Field(default=None, description="Экземпляры ресурсов, привязанные к записям или событиям в рамках серии расписания. Возвращаются в ответе, если в запросе указан параметр `include` с соответствующим значением.")
    events: list[TimetableEventScheduleEvent2] | None = Field(default=None, description="Сущности записей или событий в рамках серии расписания. Возвращаются в ответе, если в запросе указан параметр `include` с соответствующим значением.")


class TipsSettingResponseDataTypes(BaseModel):
    """Получить список мастеров салона с их чаевыми
    Схема спеки: Root Type for tips_setting_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: list[TipsSettingResponseDataTypesDataItem] | None = Field(default=None, alias="data", description="Массив объектов с данными")
    meta: TipsSettingResponseDataTypesMeta | None = Field(default=None)


class TechnologicalCardsConsumablesResponse200DataTypesDataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    service_id: float | None = Field(default=None, description="Идентификатор услуги")
    record_id: float | None = Field(default=None, description="Идентификатор записи")
    technological_cards: list[TechnologicalCardsConsumablesResponse200DataTypesDataItemTechnologicalCardsItem] | None = Field(default=None, description="Технологические карты")
    consumables: list[TechnologicalCardsConsumablesResponse200DataTypesDataItemConsumablesItem] | None = Field(default=None)


class TechnologicalCardsConsumablesResponse200DataTypes(BaseModel):
    """Получить список тех. карт и расходников записи
    Схема спеки: Root Type for technological_cards_consumables_response200_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: list[TechnologicalCardsConsumablesResponse200DataTypesDataItem] | None = Field(default=None, alias="data", description="Массив объектов с данными")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")


class TimetableEventSchedule2(BaseModel):
    """Данные по существующему в филиале расписанию записей или событий.
    Схема спеки: Объект модели "Расписание"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор расписания.")
    created_at: str | None = Field(default=None, description="Дата и время создания расписания.")
    updated_at: str | None = Field(default=None, description="Дата и время последнего обновления расписания.")
    deleted_at: str | None = Field(default=None, description="Дата и время удаления расписания.")
    original_entity_type: Literal["record", "activity"] | None = Field(default=None, description="Тип сущности, на основе которой было создано расписание.")
    original_entity_id: float | None = Field(default=None, description="Идентификатор сущности, на основе которой было создано расписание.")
    date_start: str | None = Field(default=None, description="Дата начала действия расписания.")
    date_end: str | None = Field(default=None, description="Дата окончания действия расписания.")
    days: list[TimetableEventScheduleDay2] | None = Field(default=None, description="Серии расписания, привязанные к данному расписанию. Возвращаются в ответе, если в запросе указан параметр `include` с соответствующим значением.")


class TimetableEventScheduleClientSchedule(BaseModel):
    """Данные по существующему в филиале графику посещений клиента.
    Схема спеки: Объект модели "График посещений клиента"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор графика посещений клиента.")
    loyalty_abonement_id: float | None = Field(default=None, description="Идентификатор абонемента, использованного в графике посещений клиента.")
    final_day: str | None = Field(default=None, description="Дата и время окончания графика посещений клиента.")
    finish_date_type: Literal["end", "fixed", "abonement"] | None = Field(default=None, description="Тип окончания расписания")
    days: list[TimetableEventScheduleDay2] | None = Field(default=None, description="Серии расписания, привязанные к данному графику посещений клиента.")

__all__ = [
    "TaxSystemResponseDataTypes2",
    "TaxSystemResponseDataTypesDataItem",
    "TaxSystemResponseDataTypesDataItemVatsItem",
    "TaxSystemResponseDataTypesMeta",
    "TechnologicalCardsConsumablesResponse200DataTypes",
    "TechnologicalCardsConsumablesResponse200DataTypesDataItem",
    "TechnologicalCardsConsumablesResponse200DataTypesDataItemConsumablesItem",
    "TechnologicalCardsConsumablesResponse200DataTypesDataItemConsumablesItemGood",
    "TechnologicalCardsConsumablesResponse200DataTypesDataItemTechnologicalCardsItem",
    "TechnologicalCardsConsumablesResponse200DataTypesDataItemTechnologicalCardsItemTechnologicalCardItemsItem",
    "TechnologicalCardsConsumablesResponse200DataTypesDataItemTechnologicalCardsItemTechnologicalCardItemsItemGood",
    "TechnologicalCardsConsumablesResponse200DeleteDataTypes",
    "TechnologicalCardsConsumablesResponse200DeleteDataTypesDataItem",
    "TechnologicalCardsConsumablesResponse200DeleteDataTypesMeta",
    "TechnologicalCardsResponse200DataTypes",
    "TechnologicalCardsResponse200DataTypesDataItem",
    "TechnologicalCardsResponse200DataTypesDataItemTechnologicalCardItemsItem",
    "TimetableActivityResponse",
    "TimetableActivityResponseData",
    "TimetableActivityResponseDataAttributes",
    "TimetableEventSchedule2",
    "TimetableEventScheduleClientSchedule",
    "TimetableEventScheduleDay2",
    "TimetableEventScheduleEvent2",
    "TimetableRecordResponse",
    "TimetableRecordResponseData",
    "TimetableRecordResponseDataAttributes",
    "TipsReduce",
    "TipsReduceWithFullInfo",
    "TipsSettingResponseDataTypes",
    "TipsSettingResponseDataTypesDataItem",
    "TipsSettingResponseDataTypesDataItemStaff",
    "TipsSettingResponseDataTypesDataItemStaffEmployee",
    "TipsSettingResponseDataTypesDataItemStaffPosition",
    "TipsSettingResponseDataTypesDataItemStaffUser",
    "TipsSettingResponseDataTypesMeta",
    "TransactionCompanyidResponseDataTypes",
    "TransactionCompanyidResponseDataTypesDataItem",
    "TransactionCompanyidResponseDataTypesDataItemAccount",
    "TransactionCompanyidResponseDataTypesDataItemClient",
    "TransactionCompanyidResponseDataTypesDataItemExpense",
    "TransactionCompanyidResponseDataTypesDataItemMaster",
    "TransactionCompanyidResponseDataTypesDataItemSupplier"
]
