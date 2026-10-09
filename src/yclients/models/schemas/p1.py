"""Модели YCLIENTS API (p1: P).

Сгенерировано scripts/generate.py -- не редактируйте вручную.
"""

from __future__ import annotations

from datetime import date, datetime
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class PatchAbonementTypesLoyaltyAbonementTypeIdRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    is_archived: bool = Field(description="Признак архивации абонемента. (true - заархивирован, false - не заархивирован).")


class PatchClientSchedulesClientScheduleIdRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    schedule_days_ids: list[float] = Field(description="Идентификаторы серий расписания, минимально 1 серия, максимально 7 серий.")
    finish_date_type: Literal["end", "fixed", "abonement"] | None = Field(default=None, description="Тип окончания расписания")
    finish_date: str | None = Field(default=None, description="Дата окончания клиентского расписания **⚠️ Обязательно**, если `finish_date_type=fixed`.")
    abonement_id: int | None = Field(default=None, description="Идентификатор абонемента **⚠️Обязателен, если finish_date_type=abonement**")


class PatchDaysDayIdRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    force: bool = Field(description="Флаг переопределения ручных изменений в записях/событиях при обновлении серии расписания.")
    events_master_id: float | None = Field(default=None, description="Идентификатор сотрудника, оказывающего услуги в рамках серии расписания.")
    events_time: str | None = Field(default=None, description="Время начала записей или событий в рамках серии расписания (в формате HH:MM:SS).")
    events_duration: float | None = Field(default=None, description="Длительность записей или событий в рамках серии расписания (в секундах).")
    events_capacity: float | None = Field(default=None, description="Вместимость событий в рамках серии расписания (для записей значение должно быть равно 1).")
    labels_ids: list[float] | None = Field(default=None, description="Идентификаторы категорий, привязанных к записям или событиям в рамках серии расписания.")
    resource_instances_ids: list[float] | None = Field(default=None, description="Идентификаторы экземпляров ресурсов, привязанных к записям или событиям в рамках серии расписания.")


class PatchSchedulesScheduleIdRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    date_end: str | None = Field(default=None, description="Дата окончания расписания.")


class PostAbonementIdFreezeRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    freeze_till: str = Field(description="Дата, до которой будет заморожен абонемент.")


class PostAbonementIdSetBalanceRequestServicesBalanceCountItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    service_id: int | None = Field(default=None)
    balance: int | None = Field(default=None)


class PostAbonementIdSetPeriodRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    period: float = Field(description="Длительность периода")
    period_unit_id: float = Field(description="Тип периода (1 - день, 2 - неделя, 3 - месяц, 4 - год)")


class PostAbonementTypesLoyaltyAbonementTypeIdRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    restore_in_title: bool = Field(description="Новое название типа абонемента, которое сохранится после восстановления типа абонемента.")


class PostActivityIdRecordsRequestClientClientAgreementsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    is_newsletter_allowed: bool | None = Field(default=None, description="Признак согласия на рассылку новостей.")
    is_personal_data_processing_allowed: bool | None = Field(default=None, description="Признак согласия на обработку персональных данных.")


class PostActivityIdRecordsRequestClientClientCustomFieldValuesItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    code: str | None = Field(default=None, description="Название поля.")
    value: str | None = Field(default=None, description="Значение поля.")


class PostActivityIdRecordsRequestComer(BaseModel):
    """Посетитель.
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    name: str | None = Field(default=None, description="Имя.")


class PostApplicationAddDiscountRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    salon_ids: list[float] = Field(description="Список ID салонов")
    application_id: float = Field(description="Идентификатор приложения.")
    discount: float = Field(description="Величина скидки")


class PostApplicationUpdateChannelRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    salon_id: float = Field(description="Идентификатор филиала.")
    application_id: float = Field(description="Идентификатор приложения (выдается после создания в витрине YCLIENTS).")
    channel_slug: Literal["sms", "whatsapp"] = Field(description="Канал, доступность которого необходимо изменить.")
    is_available: bool = Field(description="Флаг доступности канала отправки.")


class PostCallbackRedirectRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    salon_id: float = Field(description="Идентификатор филиала.")
    application_id: float = Field(description="Идентификатор приложения (выдается после создания в витрине YCLIENTS).")
    api_key: float | None = Field(default=None, description="API-ключ для отправки уведомлений.")
    webhook_urls: list[str] | None = Field(default=None, description="Массив адресов вебхуков.")


class PostCardIdManualTransactionRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    amount: float = Field(description="Сумма списания/пополнения. Положительная для пополнения, отрицательная для списания.")
    title: str | None = Field(default=None, description="Примечание к транзакции.")


class PostCardIdManualTransactionRequest2(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    amount: float = Field(description="Сумма списания/пополнения. Положительная для пополнения, отрицательная для списания.")
    title: str | None = Field(default=None, description="Примечание к транзакции.")


class PostClientIdCommentsRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    text: str = Field(description="Текст комментария к клиенту.")


class PostCompanyIdSchedulesRequestDaysItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    day_of_week: Literal["mon", "tue", "wed", "thu", "fri", "sat", "sun"] = Field(description="День недели серии расписания.")
    events_master_id: float = Field(description="Идентификатор сотрудника, оказывающего услуги в рамках серии расписания.")
    events_time: str = Field(description="Время начала записей или событий в рамках серии расписания (в формате HH:MM:SS).")
    events_duration: float = Field(description="Длительность записей или событий в рамках серии расписания (в секундах).")
    events_capacity: float = Field(description="Вместимость событий в рамках серии расписания (для записей значение должно быть равно 1).")
    labels_ids: list[float] | None = Field(default=None, description="Идентификаторы категорий, привязанных к записям или событиям в рамках серии расписания.")
    resource_instances_ids: list[float] | None = Field(default=None, description="Идентификаторы экземпляров ресурсов, привязанных к записям или событиям в рамках серии расписания.")


class PostCompanyIdWaitingListRequestClient(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float = Field(alias="id", description="Идентификатор клиента")
    name: str = Field(description="Имя клиента. ⚠️Обновляет имя клиента в клиентской базе, если значение отличается от существующего")
    surname: str = Field(description="Фамилия клиента")
    patronymic: str = Field(description="Отчество клиента")


class PostCompanyIdWaitingListRequestIntervalsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    date_from: str | None = Field(default=None, description="Дата начала")
    date_to: str | None = Field(default=None, description="Дата окончания")
    time_from: float | None = Field(default=None)
    time_to: float | None = Field(default=None)


class PostInviteSalonIdRequestInvitesItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    name: str | None = Field(default=None, description="Имя пользователя")
    search: str | None = Field(default=None, description="Номер телефона или email адрес пользователя")
    position: str | None = Field(default=None, description="Должность")
    user_role: Literal["worker", "administrator", "accountant", "manager", "owner"] | None = Field(default=None, description="Название роли")
    user_permissions: list[Any] | None = Field(default=None, description="Список значений прав пользователя")
    staff_id: float | None = Field(default=None, description="Идентификатор сотрудника привязанного к пользователю")


class PostLoyaltyAbonementTypesRequestAvailabilityItemIntervalsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    from_: int | None = Field(default=None, alias="from", description="Начало интервала в секундах.")
    to: int | None = Field(default=None, description="Конец интервала в секундах.")


class PostMarketplaceWebhookRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    salon_id: float = Field(description="Идентификатор филиала.")
    application_id: float = Field(description="Идентификатор приложения.")
    event: Literal["uninstall", "freeze"] = Field(description="Slug произошедшего события.")
    partner_token: str = Field(description="Bearer токен компании разработчика (для удостоверения происхождения вебхука).")


class PostPartnerCallbackRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    salon_id: float = Field(description="Идентификатор филиала.")
    application_id: float = Field(description="Идентификатор приложения (выдается после создания в витрине YCLIENTS).")
    api_key: float | None = Field(default=None, description="API-ключ для отправки уведомлений.")
    webhook_urls: list[str] | None = Field(default=None, description="Массив адресов вебхуков.")
    channels: list[Literal["sms", "whatsapp"]] | None = Field(default=None, description="Каналы, по которым доступна отправка уведомлений (только для приложений из категорий Чат-Боты и СМС-агрегаторы).")


class PostPartnerPaymentRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    salon_id: float = Field(description="Идентификатор филиала.")
    application_id: float = Field(description="Идентификатор приложения (выдается после создания в витрине YCLIENTS).")
    payment_sum: float = Field(description="Сумма платежа.")
    currency_iso: str = Field(description="ISO валюты платежа (например: RUB, EUR, BYN)")
    payment_date: str = Field(description="Дата и время платежа.")
    period_from: str = Field(description="Дата, с которой начинается оплаченный период (включительно).")
    period_to: str = Field(description="Дата, которой заканчивается оплаченный период (включительно).")


class PostPartnerPaymentResponse200Data(BaseModel):
    """Данные по запросу.
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="ID платежа")


class PostPartnerShortNamesRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    salon_id: float = Field(description="Идентификатор филиала.")
    application_id: float = Field(description="Идентификатор приложения (выдается после создания в витрине YCLIENTS).")
    short_names: list[str] = Field(description="Массив коротких имен отправителя SMS-сообщений")


class PostPositionsQuickRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    title: str = Field(description="Название должности.")


class PostRecordsRecordIdRequestAttendanceGoodItemsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int = Field(alias="id", description="Идентификатор.")
    good_id: int = Field(description="Идентификатор товара.")
    unit_id: int = Field(description="Единица измерения продажи.")
    storage_id: int = Field(description="Склад продажи.")
    staff_id: int = Field(description="Идентификатор сотрудника.")
    operation_unit_type: Literal["sale", "consumable", "unknown"] = Field(description="Тип единицы операции продажи.")
    number: int = Field(description="Номер, если применимо.")
    planned_activation_date: str = Field(description="Дата активации товара, если применимо.")
    marks: list[str] = Field(description="Список значений маркировки.")
    quantity: int = Field(description="Количество.")
    cost_per_unit: float = Field(description="Стоимость за единицу товара.")
    manual_cost: float = Field(description="Итоговая общая стоимость.")
    discount_percent: float = Field(description="Скидка в процентах.")


class PostRecordsRecordIdRequestAttendanceServiceItem(BaseModel):
    """Услуги.
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    cost_per_unit: float = Field(description="Исходная стоимость за единицу.")
    discount_percent: float = Field(description="Значение скидки в процентах.")
    manual_cost: float = Field(description="Общая стоимость с учетом скидки.")


class PostSalonIdActivitiesRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    staff_id: int = Field(description="Идентификатор мастера.")
    service_id: int = Field(description="Идентификатор услуги.")
    resource_instance_ids: list[int] | None = Field(default=None, description="Список идентификаторов ресурса.")
    label_ids: list[int] | None = Field(default=None, description="Список идентификаторов категорий.")
    date: str = Field(description="Дата события.")
    length: int = Field(description="Продолжительность события в секундах.")
    technical_break_duration: float | None = Field(default=None, description="Длительность технического перерыва - Если не передан. Значение по умолчанию null - Значение null, соответствует общей настройке филиала, и задается в разделе *Настройки → Журнал записи → Технически...")
    capacity: int = Field(description="Количество мест в событии.")
    comment: str | None = Field(default=None, description="Комментарий.")
    color: str | None = Field(default=None, description="Цвет события.")
    instructions: str | None = Field(default=None, description="Инструкции.")
    stream_link: str | None = Field(default=None, description="Ссылка для подключения.")
    force: bool | None = Field(default=None, description="Признак проверки доступности ресурсов (true - не проверяем, false - проверяем).")


class PostScheduleIdClientSchedulesRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    client_id: float = Field(description="Идентификатор клиента, для которого будет создан график посещений.")
    comer_id: float | None = Field(default=None, description="Идентификатор посетителя клиента, для которого будет создан график посещений.")
    schedule_days_ids: list[float] = Field(description="Идентификаторы серий расписания ⚠️**Число элементов массива строго от 1 до 7**")
    finish_date_type: Literal["end", "fixed", "abonement"] = Field(description="Тип окончания расписания")
    finish_date: str | None = Field(default=None, description="Дата окончания клиентского расписания **⚠️ Обязательно**, если `finish_date_type=fixed`.")
    abonement_id: int | None = Field(default=None, description="Идентификатор абонемента **⚠️Обязателен, если finish_date_type=abonement**")


class PostScheduleIdDaysRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    day_of_week: Literal["mon", "tue", "wed", "thu", "fri", "sat", "sun"] = Field(description="День недели серии расписания.")
    events_master_id: float = Field(description="Идентификатор сотрудника, оказывающего услуги в рамках серии расписания.")
    events_time: str = Field(description="Время начала записей или событий в рамках серии расписания (в формате HH:MM:SS).")
    events_duration: float = Field(description="Длительность записей или событий в рамках серии расписания (в секундах).")
    events_capacity: float = Field(description="Вместимость событий в рамках серии расписания (для записей значение должно быть равно 1).")
    labels_ids: list[float] | None = Field(default=None, description="Идентификаторы категорий, привязанных к записям или событиям в рамках серии расписания.")
    resource_instances_ids: list[float] | None = Field(default=None, description="Идентификаторы экземпляров ресурсов, привязанных к записям или событиям в рамках серии расписания.")


class PostServiceIdStaffRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    master_id: float = Field(description="Идентификатор сотрудника, оказывающего услугу.")
    seance_length: float = Field(description="Длительность оказания услуги указанным сотрудником в секундах, минимально 300 секунд (5 минут), максимально 86100 секунд (23 часа 55 минут).")
    technological_card_id: float = Field(description="Идентификатор технологической карты, используемой при оказании услуги указанным сотрудником.")


class PostStaffQuickRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    name: str = Field(description="Имя сотрудника.")
    specialization: str = Field(description="Специализация сотрудника.")
    position_id: float = Field(description="Идентификатор должности, к которой необходимо привязать сотрудника.")
    phone_number: str = Field(description="Номер телефона пользователя, к которому необходимо привязать сотрудника (без \"+\", от 9 до 15 цифр).")


class PostUserIdCopyToCompaniesRequestUserCompanyLinksItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    company_id: float = Field(description="ID филиала")
    user_permissions: list[Any] | None = Field(default=None, description="Список значений прав пользователя, которые необходимо изменить при копировании")


class PostUserIdRemoveFromCompaniesRequestUserCompanyLinksItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    company_id: float = Field(description="ID филиала")


class PostVisitsSearchRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    client_id: float = Field(description="Идентификатор клиента.")
    client_phone: str = Field(description="Номер телефона клиента.")
    from_: str = Field(alias="from", description="Дата начала периода.")
    to: str = Field(description="Дата конца периода.")
    payment_statuses: list[Literal["not_paid", "paid_not_full", "paid_full", "paid_over"]] = Field(description="Статус оплаты визита: `not_paid` - визит неоплачен, никаких оплат по визиту не проходило; `paid_not_full` - визит оплачен частично; `paid_full` - визит оплачен полностью, переплаты нет; `paid_over`...")
    attendance: Literal[-1, 0, 1, 2] = Field(description="Статус посещения: `-1`: - клиент не пришёл; `0`: - ожидание клиента; `1`: - клиент пришёл; `2`: - клиент подтвердил запись.")


class PutAbonementTypesLoyaltyAbonementTypeIdRequestAvailabilityItemIntervalsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    from_: int | None = Field(default=None, alias="from", description="Начало интервала в секундах.")
    to: int | None = Field(default=None, description="Конец интервала в секундах.")


class PutActivitiesActivityIdRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    staff_id: int = Field(description="Идентификатор мастера.")
    service_id: int = Field(description="Идентификатор услуги.")
    resource_instance_ids: list[int] | None = Field(default=None, description="Список идентификаторов ресурса.")
    label_ids: list[int] | None = Field(default=None, description="Список идентификаторов категорий.")
    date: str = Field(description="Дата события.")
    length: int = Field(description="Продолжительность события в секундах.")
    technical_break_duration: float | None = Field(default=None, description="Длительность технического перерыва - Если не передан. Значение по умолчанию null - Значение null, соответствует общей настройке филиала, и задается в разделе *Настройки → Журнал записи → Технически...")
    capacity: int = Field(description="Количество мест в событии.")
    comment: str | None = Field(default=None, description="Комментарий.")
    color: str | None = Field(default=None, description="Цвет события.")
    instructions: str | None = Field(default=None, description="Инструкции.")
    stream_link: str | None = Field(default=None, description="Ссылка для подключения.")
    force: bool | None = Field(default=None, description="Признак проверки доступности ресурсов (true - не проверяем, false - проверяем).")


class PutStaffMasterIdRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    seance_length: float = Field(description="Длительность оказания услуги указанным сотрудником в секундах, минимально 300 секунд (5 минут), максимально 86100 секунд (23 часа 55 минут).")
    technological_card_id: float = Field(description="Идентификатор технологической карты, используемой при оказании услуги указанным сотрудником.")


class PutStaffScheduleRequestSchedulesToDeleteItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    staff_id: float | None = Field(default=None, description="Идентификатор сотрудника.")
    dates: list[str] | None = Field(default=None, description="Дата для удаления графика работы сотрудника в формате Y-m-d.")


class PutStaffScheduleRequestSchedulesToSetItemSlotsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    from_: str | None = Field(default=None, alias="from", description="Начало интервала графика работы сотрудника в формате H:i.")
    to: str | None = Field(default=None, description="Конец интервала графика работы сотрудника в формате H:i.")


class PutUserIdPermissionsRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    user_role: Literal["worker", "administrator", "accountant", "manager", "owner"] | None = Field(default=None, description="Название роли")
    user_permissions: list[Any] | None = Field(default=None, description="Список значений прав пользователя")
    staff_id: float | None = Field(default=None, description="Идентификатор сотрудника привязанного к пользователю")


class PutWaitingListWaitingListEntryIdRequestClient(BaseModel):
    """Объект клиента
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float = Field(alias="id", description="Идентификатор клиента")
    name: str = Field(description="Имя клиента. ⚠️Обновляет имя клиента в клиентской базе, если значение отличается от существующего")
    surname: str = Field(description="Фамилия клиента")
    patronymic: str = Field(description="Отчество клиента")


class PutWaitingListWaitingListEntryIdRequestIntervalsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    date_from: str | None = Field(default=None, description="Дата начала")
    date_to: str | None = Field(default=None, description="Дата окончания")
    time_from: float | None = Field(default=None)
    time_to: float | None = Field(default=None)


class Position(BaseModel):
    """Данные существующей должности в сети.
    Схема спеки: Объект модели "Должность"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор должности.")
    chain_id: float | None = Field(default=None, description="Идентификатор сети, в которой создана должность.")
    title: str | None = Field(default=None, description="Наименование должности.")
    description: str | None = Field(default=None, description="Описание должности.")
    services_binding_type: Literal[0, 2] | None = Field(default=None, description="Тип привязки услуг к должности: `0`: - привязка отключена; `2`: - жесткая привязка.")
    rules_required_fields: list[str] | None = Field(default=None, description="Набор полей, необходимых для заполнения перед возможностью назначения сотрудника на должность.")
    only_chain_appointment: bool | None = Field(default=None, description="Доступность привязки должности к сотруднику только в сети.")


class PositionCompact(BaseModel):
    """Данные существующей должности в сети.
    Схема спеки: Объект модели "Должность"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор должности.")
    title: str | None = Field(default=None, description="Наименование должности.")


class PostAbonementIdSetBalanceRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    united_balance_services_count: float = Field(description="Количество услуг для абонемента с объединенным балансом")
    services_balance_count: list[PostAbonementIdSetBalanceRequestServicesBalanceCountItem] = Field(description="Перечисление услуга-количество для абонемента с раздельным балансом")


class PostActivityIdRecordsRequestClientClient(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    name: str = Field(description="Имя.")
    phone_string: str = Field(description="Телефон.")
    email: str = Field(description="Почта.")
    surname: str | None = Field(default=None, description="Фамилия.")
    patronymic: str | None = Field(default=None, description="Отчество.")
    sex: Literal[0, 1, 2] | None = Field(default=None, description="Пол. (0 - неизвестен, 1 - мужской, 2 - женский.)")
    birthday: str | None = Field(default=None, description="Дата рождения.")
    custom_field_values: list[PostActivityIdRecordsRequestClientClientCustomFieldValuesItem] | None = Field(default=None, description="Список значений доп полей.")
    agreements: list[PostActivityIdRecordsRequestClientClientAgreementsItem] | None = Field(default=None, description="Пользовательские соглашения.")


class PostCardIdManualTransactionResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: LoyaltyCard2 | None = Field(default=None, alias="data")
    meta: dict[str, Any] | None = Field(default=None)


class PostCardIdManualTransactionResponse2002(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: LoyaltyCard2 | None = Field(default=None, alias="data")
    meta: dict[str, Any] | None = Field(default=None)


class PostCompanyIdSchedulesRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    original_entity_type: Literal["record", "activity"] = Field(description="Тип сущности, на основе которой будет построено расписание: `record` - индивидуальная запись, не поддерживается в текущий момент; `activity` - групповое событие.")
    original_entity_id: float = Field(description="Идентификатор сущности, на основе которой будет построено расписание.")
    date_end: str = Field(description="Дата окончания расписания.")
    days: list[PostCompanyIdSchedulesRequestDaysItem] = Field(description="Настройки серий расписания, минимально 1 серия, максимально 7 серий (серия соответствует дню недели).")


class PostCompanyIdWaitingListRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    comment: str | None = Field(default=None, description="Комментарий")
    client_: PostCompanyIdWaitingListRequestClient = Field(alias="client")
    service_ids: list[Any] = Field(description="Идентификаторы услуг")
    staff_ids: list[Any] | None = Field(default=None, description="Идентификаторы сотрудников")
    intervals: list[PostCompanyIdWaitingListRequestIntervalsItem] | None = Field(default=None, description="Интервалы дат и времени, на которые клиент хочет создать запись")


class PostInviteSalonIdRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    invites: list[PostInviteSalonIdRequestInvitesItem] = Field(description="Массив приглашений")


class PostLoyaltyAbonementTypesRequestAvailabilityItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    week_days: list[int] | None = Field(default=None, description="Дни недели, в которых действует условие. (1 - понедельник, 7 - воскресенье).")
    intervals: list[PostLoyaltyAbonementTypesRequestAvailabilityItemIntervalsItem] | None = Field(default=None, description="Интервалы доступности.")


class PostPartnerPaymentResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус запроса.")
    data_: PostPartnerPaymentResponse200Data | None = Field(default=None, alias="data")


class PostPositionsQuickResponse201(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: Position | None = Field(default=None, alias="data")
    meta: dict[str, Any] | None = Field(default=None)


class PostRecordsRecordIdRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    attendance_service_item: PostRecordsRecordIdRequestAttendanceServiceItem
    attendance_good_items: list[PostRecordsRecordIdRequestAttendanceGoodItemsItem] | None = Field(default=None, description="Товары.")
    comment: str | None = Field(default=None, description="Комментарий.")
    label_ids: list[int] | None = Field(default=None, description="Список идентификаторов категорий.")
    color: str | None = Field(default=None, description="Цвет.")
    clients_count: int = Field(description="Количество посетителей.")


class PostServiceIdStaffResponse201(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: MasterServiceLink2 | None = Field(default=None, alias="data")
    meta: dict[str, Any] | None = Field(default=None)

__all__ = [
    "PatchAbonementTypesLoyaltyAbonementTypeIdRequest",
    "PatchClientSchedulesClientScheduleIdRequest",
    "PatchDaysDayIdRequest",
    "PatchSchedulesScheduleIdRequest",
    "Position",
    "PositionCompact",
    "PostAbonementIdFreezeRequest",
    "PostAbonementIdSetBalanceRequest",
    "PostAbonementIdSetBalanceRequestServicesBalanceCountItem",
    "PostAbonementIdSetPeriodRequest",
    "PostAbonementTypesLoyaltyAbonementTypeIdRequest",
    "PostActivityIdRecordsRequestClientClient",
    "PostActivityIdRecordsRequestClientClientAgreementsItem",
    "PostActivityIdRecordsRequestClientClientCustomFieldValuesItem",
    "PostActivityIdRecordsRequestComer",
    "PostApplicationAddDiscountRequest",
    "PostApplicationUpdateChannelRequest",
    "PostCallbackRedirectRequest",
    "PostCardIdManualTransactionRequest",
    "PostCardIdManualTransactionRequest2",
    "PostCardIdManualTransactionResponse200",
    "PostCardIdManualTransactionResponse2002",
    "PostClientIdCommentsRequest",
    "PostCompanyIdSchedulesRequest",
    "PostCompanyIdSchedulesRequestDaysItem",
    "PostCompanyIdWaitingListRequest",
    "PostCompanyIdWaitingListRequestClient",
    "PostCompanyIdWaitingListRequestIntervalsItem",
    "PostInviteSalonIdRequest",
    "PostInviteSalonIdRequestInvitesItem",
    "PostLoyaltyAbonementTypesRequestAvailabilityItem",
    "PostLoyaltyAbonementTypesRequestAvailabilityItemIntervalsItem",
    "PostMarketplaceWebhookRequest",
    "PostPartnerCallbackRequest",
    "PostPartnerPaymentRequest",
    "PostPartnerPaymentResponse200",
    "PostPartnerPaymentResponse200Data",
    "PostPartnerShortNamesRequest",
    "PostPositionsQuickRequest",
    "PostPositionsQuickResponse201",
    "PostRecordsRecordIdRequest",
    "PostRecordsRecordIdRequestAttendanceGoodItemsItem",
    "PostRecordsRecordIdRequestAttendanceServiceItem",
    "PostSalonIdActivitiesRequest",
    "PostScheduleIdClientSchedulesRequest",
    "PostScheduleIdDaysRequest",
    "PostServiceIdStaffRequest",
    "PostServiceIdStaffResponse201",
    "PostStaffQuickRequest",
    "PostUserIdCopyToCompaniesRequestUserCompanyLinksItem",
    "PostUserIdRemoveFromCompaniesRequestUserCompanyLinksItem",
    "PostVisitsSearchRequest",
    "PutAbonementTypesLoyaltyAbonementTypeIdRequestAvailabilityItemIntervalsItem",
    "PutActivitiesActivityIdRequest",
    "PutStaffMasterIdRequest",
    "PutStaffScheduleRequestSchedulesToDeleteItem",
    "PutStaffScheduleRequestSchedulesToSetItemSlotsItem",
    "PutUserIdPermissionsRequest",
    "PutWaitingListWaitingListEntryIdRequestClient",
    "PutWaitingListWaitingListEntryIdRequestIntervalsItem"
]
