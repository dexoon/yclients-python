"""Модели YCLIENTS API (c3: C).

Сгенерировано scripts/generate.py -- не редактируйте вручную.
"""

from __future__ import annotations

from datetime import date, datetime
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class CompanySalonidSaleDocumentidPaymentLoyaltyProgramPayment(BaseModel):
    """Объект, содержащий метод оплаты
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    method: CompanySalonidSaleDocumentidPaymentLoyaltyProgramPaymentMethod | None = Field(default=None)


class CompanySalonidSaleDocumentidPaymentReferalPayment(BaseModel):
    """Объект, содержащий метод оплаты
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    method: CompanySalonidSaleDocumentidPaymentReferalPaymentMethod | None = Field(default=None)
    referrer_phone: str | None = Field(default=None, description="Телефон пригласившего")


class CompanyUsersDeprecatedResponseDataTypesDataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор пользователя")
    firstname: str | None = Field(default=None, description="Имя пользователя")
    login: str | None = Field(default=None, description="login пользователя для авторизации в системе (для авторизации так же можно в качестве логина поля phone и email)")
    email: str | None = Field(default=None, description="Почтовый адрес пользователя")
    phone: str | None = Field(default=None, description="Телефон пользователя")
    information: str | None = Field(default=None, description="Информация о пользователе")
    access: CompanyUsersDeprecatedResponseDataTypesDataItemAccess | None = Field(default=None)


class CustomFieldsResponseDataTypesDataItemCustomField(BaseModel):
    """Дополнительные поля
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор поля")
    code: str | None = Field(default=None, description="Код поля по которому устанавливаются значения для полей записи")
    entity_type: str | None = Field(default=None, description="Тип сущности, для которой действует поле (карточка клиента, окно записи)")
    show_in_ui: bool | None = Field(default=None, description="Показывать ли поля в интерфейсе")
    title: str | None = Field(default=None, description="Название доп. поля")
    user_can_edit: bool | None = Field(default=None, description="Разрешено ли редактирование")
    type_: CustomFieldsResponseDataTypesDataItemCustomFieldType | None = Field(default=None, alias="type")
    values_: str | None = Field(default=None, alias="values", description="Список допустимых значений для типа \"список\"")


class ClientCommentContainer(BaseModel):
    """Данные по комментарию к клиенту.
    Схема спеки: Объект модели "Комментарий к клиенту"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор комментария к клиенту.")
    create_date: str | None = Field(default=None, description="Дата и время создания комментария к клиенту.")
    update_date: str | None = Field(default=None, description="Дата и время последнего обновления комментария к клиенту.")
    type_: Literal["default", "file"] | None = Field(default=None, alias="type", description="Тип комментария к клиенту: `default`: - текстовый комментарий; `file`: - загруженный файл.")
    text: str | None = Field(default=None, description="Текст комментария к клиенту (`type` = \"default\", для `type` = \"file\" текст комментария возвращается пустым).")
    files: list[ClientCommentFileDto] | None = Field(default=None, description="Файлы в карточке клиента, загрузка которых породила создание комментария к клиенту (`type` = \"file\", для `type` = \"default\" массив файлов возвращается пустым).")
    user: dict[str, Any] | None = Field(default=None, description="Пользователь, оставивший комментарий к клиенту или загрузивший файлы в карточку клиента.")


class ClientVisitsHistoryRecordService(BaseModel):
    """Данные по услуге.
    Схема спеки: Объект модели "Услуга в записи истории посещений клиента"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор услуги.")
    title: str | None = Field(default=None, description="Наименование услуги.")
    first_cost: float | None = Field(default=None, description="Стоимость услуги без скидки.")
    discount_percent: float | None = Field(default=None, description="Процент скидки.")
    cost_to_pay: float | None = Field(default=None, description="Стоимость услуги с учетом скидки.")
    paid_sum: float | None = Field(default=None, description="Сумма, которая была оплачена клиентом.")
    payment_status: Literal["not_paid", "paid_not_full", "paid_full", "paid_over"] | None = Field(default=None, description="Статус оплаты визита: `not_paid` - визит неоплачен, никаких оплат по визиту не проходило; `paid_not_full` - визит оплачен частично; `paid_full` - визит оплачен полностью, переплаты нет; `paid_over`...")
    consumables: list[ClientVisitsHistoryRecordServiceConsumable] | None = Field(default=None, description="Расходники товаров, прикрепленные к данной услуге.")


class ClientsCompanyidResponseDeprecatedDataTypes(BaseModel):
    """Устаревшее. Получить список клиентов
    Схема спеки: Root Type for clients_companyid_response_deprecated_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: list[ClientsCompanyidResponseDeprecatedDataTypesDataItem] | None = Field(default=None, alias="data", description="Массив объектов с данными")
    meta: ClientsCompanyidResponseDeprecatedDataTypesMeta | None = Field(default=None)


class CompanyAnalyticsLoyaltyProgramsStaffDataTypes(BaseModel):
    """Получить статистику позвращаемости по сотруднику.
    Схема спеки: Root Type for company_analytics_loyalty_programs_staff_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения")
    data_: list[CompanyAnalyticsLoyaltyProgramsStaffDataTypesDataItem] | None = Field(default=None, alias="data", description="Массив с объектами данных")
    meta: CompanyAnalyticsLoyaltyProgramsStaffDataTypesMeta | None = Field(default=None)


class CompanyCompanyidClientsSearchRequestDataTypes(BaseModel):
    """Получить список клиентов
    Схема спеки: Root Type for company_cpmpanuid_clients_search_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    page_: float | None = Field(default=None, alias="page", description="Номер страница")
    page_size: float | None = Field(default=None, description="Количество выводимых строк на странице. Максимум 200. (По умолчанию 25)")
    fields: list[str] | None = Field(default=None, description="Поля, которые нужно вернуть в ответе")
    order_by: Literal["id", "name", "phone", "email", "discount", "first_visit_date", "last_visit_date", "sold_amount", "visits_count"] | None = Field(default=None, description="По какому полю сортировать")
    order_by_direction: Literal["ASC", "DESC"] | None = Field(default=None, description="Как сортировать (по возрастанию / по убыванию)")
    operation: Literal["AND", "OR"] | None = Field(default=None, description="Тип операции")
    filters: list[CompanyCompanyidClientsSearchRequestDataTypesFiltersItem] | None = Field(default=None, description="Фильтры для поиска по клиентам")


class CompanyCompanyidStaffStaffidResponseDataTypes(BaseModel):
    """Получить список сотрудников / конкретного сотрудника
    Схема спеки: Root Type for company_companyid_staff_staffid_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: list[CompanyCompanyidStaffStaffidResponseDataTypesDataItem] | None = Field(default=None, alias="data", description="Массив объектов с данными")
    meta: CompanyCompanyidStaffStaffidResponseDataTypesMeta | None = Field(default=None)


class CompanySalonidSaleDocumentidPaymentAbonements(BaseModel):
    """В случае оплаты абонементом, если у пользователя нет права "Оплата сертификатом и абонементом без кода" в теле запроса также необходимо передать пераметр "number" (string), содержащий код абонемента.
    Схема спеки: Оплата при помощи абонемента - работает только для визита.
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    payment: CompanySalonidSaleDocumentidPaymentAbonementsPayment | None = Field(default=None)


class CompanySalonidSaleDocumentidPaymentAccount(BaseModel):
    """Оплата в кассу
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    payment: CompanySalonidSaleDocumentidPaymentAccountPayment | None = Field(default=None)


class CompanySalonidSaleDocumentidPaymentCertificate(BaseModel):
    """В случае оплаты сертификатом, если у пользователя нет права "Оплата сертификатом и абонементом без кода" в теле запроса также необходимо передать пераметр "number" (string), содержащий код сертификата.
    Схема спеки: Оплата при помощи сертификата
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    payment: CompanySalonidSaleDocumentidPaymentCertificatePayment | None = Field(default=None)


class CompanySalonidSaleDocumentidPaymentDeposit(BaseModel):
    """Оплата лояльностью (различными методами)
    Схема спеки: Оплата при помощи личного счета - депозита
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    payment: CompanySalonidSaleDocumentidPaymentDepositPayment | None = Field(default=None)


class CompanySalonidSaleDocumentidPaymentLoyaltyCard(BaseModel):
    """Оплата при помощи карты лояльности
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    payment: CompanySalonidSaleDocumentidPaymentLoyaltyCardPayment | None = Field(default=None)


class CompanySalonidSaleDocumentidPaymentLoyaltyProgram(BaseModel):
    """Оплата при помощи программы лояльности
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    payment: CompanySalonidSaleDocumentidPaymentLoyaltyProgramPayment | None = Field(default=None)


class CompanySalonidSaleDocumentidPaymentReferal(BaseModel):
    """Оплата при помощи реферальной программы - работает только для визита
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    payment: CompanySalonidSaleDocumentidPaymentReferalPayment | None = Field(default=None)


class CompanyStaffPositionListDataType(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data_: list[StaffPosition2] = Field(alias="data", description="Массив объектов с данными")
    meta: list[dict[str, Any]] = Field(description="Метаданные (содержит количество найденных должностей)")
    success: bool = Field(description="Статус успешности выполнения (true)")


class CompanyUsersDeprecatedResponseDataTypes(BaseModel):
    """Получить пользователей компании
    Схема спеки: Root Type for company_users_deprecated_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: list[CompanyUsersDeprecatedResponseDataTypesDataItem] | None = Field(default=None, alias="data", description="Массив объектов с данными")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")


class CompanyAnalyticsLoyaltyProgramsIncomeDataTypesData(BaseModel):
    """Объект с данными
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    income_stats: CompanyAnalyticsLoyaltyProgramsIncomeDataTypesDataIncomeStats | None = Field(default=None)
    currency: CompanyAnalyticsLoyaltyProgramsIncomeDataTypesDataCurrency | None = Field(default=None)
    income_stats_by_day: list[CompanyAnalyticsLoyaltyProgramsIncomeDataTypesDataIncomeStatsByDayItem] | None = Field(default=None, description="Статистика по выручке в разрезе дня")


class CompanyAnalyticsLoyaltyProgramsVisitsDataTypesData(BaseModel):
    """Объект с данными
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    client_stats: CompanyAnalyticsLoyaltyProgramsVisitsDataTypesDataClientStats | None = Field(default=None)
    visits_stats_by_day: list[CompanyAnalyticsLoyaltyProgramsVisitsDataTypesDataVisitsStatsByDayItem] | None = Field(default=None, description="Количество клиентов в разрезе дня")


class CompanyCompanyidStaffStaffidResponseDataTypesDeprecatedDataItemImageGroup(BaseModel):
    """Группа изображений сотрудника
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id")
    entity: str | None = Field(default=None)
    entity_id: int | None = Field(default=None)
    images: CompanyCompanyidStaffStaffidResponseDataTypesDeprecatedDataItemImageGroupImages | None = Field(default=None)


class CompanyGetResponseDataTypesData(BaseModel):
    """Объект с данными
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор компании")
    title: str | None = Field(default=None, description="Название компании")
    country_id: float | None = Field(default=None, description="Идентификатор страны, в которой расположена компания")
    country: str | None = Field(default=None, description="Название страны, в которой расположена компания")
    city_id: float | None = Field(default=None, description="Идентификатор города, в котором расположена компания")
    city: str | None = Field(default=None, description="Название города, в котором расположена компания")
    timezone_name: str | None = Field(default=None, description="Наименование временной зоны, в которой расположена компания")
    address: str | None = Field(default=None, description="Адрес, по которому расположена компания")
    zip: float | None = Field(default=None, description="Индекс")
    social: CompanyGetResponseDataTypesDataSocial | None = Field(default=None)
    site: str | None = Field(default=None, description="Сайт компании")
    coordinate_lat: float | None = Field(default=None, description="Широта")
    coordinate_lon: float | None = Field(default=None, description="Долгота")
    phone_confirmation: bool | None = Field(default=None, description="Нужно ли подтверждать телефон по смс, при бронировании")
    active_staff_count: float | None = Field(default=None, description="Количество сотрудников, доступных для бронирования. Поле будет присутствовать только если передан GET параметр forBooking=1")
    next_slot: str | None = Field(default=None, description="Дата и время ближайшего свободного сеанса в компании (ISO8601). Поле будет присутствовать только если передан GET параметр forBooking=1")
    group_priority: int | None = Field(default=None, description="Чем больше приоритет, тем выше компания при выводе в списке филиалов сети")
    push_notification_phone_confirm: bool | None = Field(default=None, description="Подтверждать номер клиента для отправки push уведомлений")
    main_group_id: float | None = Field(default=None, description="Идентификатор основной сети компании")
    main_group: list[CompanyGetResponseDataTypesDataMainGroupItem] | None = Field(default=None, description="Основная сеть компании")
    groups: CompanyGetResponseDataTypesDataGroups | None = Field(default=None)
    bookforms: list[CompanyGetResponseDataTypesDataBookformsItem] | None = Field(default=None, description="Виджеты онлайн-записи компании")
    online_sales_form_url: str | None = Field(default=None, description="Адрес виджета онлайн-записи. Поле будет присутствовать только если передан GET параметр bookform_id")
    access: dict[str, Any] | None = Field(default=None, description="Список прав. Поле будет присутствовать только если передан GET параметр my=1")


class CompanySalonIdSaleDocumentidResponseDataTypesDataKkmState(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    last_operation_type: int | None = Field(default=None, description="Тип последней операции ККМ")
    transactions: list[CompanySalonIdSaleDocumentidResponseDataTypesDataKkmStateTransactionsItem] | None = Field(default=None, description="Транзакция ККМ")


class CompanySalonIdSaleDocumentidResponseDataTypesDataStateLoyaltyTransactionsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор транзакции лояльности")
    document_id: int | None = Field(default=None, description="Идентификатор документа")
    sale_item_id: int | None = Field(default=None, description="Идентификатор проданной единицы")
    sale_item_type: str | None = Field(default=None, description="Тип проданной единицы")
    amount: float | None = Field(default=None, description="Сумма транзакции")
    type_id: int | None = Field(default=None, description="Идентификатор типа транзакции")
    created_at: str | None = Field(default=None, description="Дата создания")
    deposit_transaction_id: int | None = Field(default=None, description="Идентификатор транзакции (зависит от типа)")
    chain: CompanySalonIdSaleDocumentidResponseDataTypesDataStateLoyaltyTransactionsItemChain | None = Field(default=None)
    type_: CompanySalonIdSaleDocumentidResponseDataTypesDataStateLoyaltyTransactionsItemType | None = Field(default=None, alias="type")
    deposit: CompanySalonIdSaleDocumentidResponseDataTypesDataStateLoyaltyTransactionsItemDeposit | None = Field(default=None)


class CustomFieldsResponseDataTypesDataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор поля")
    salon_id: float | None = Field(default=None, description="Идетификатор компании")
    custom_field: CustomFieldsResponseDataTypesDataItemCustomField | None = Field(default=None)


class ClientVisitsHistoryGoodsTransaction(BaseModel):
    """Данные о продаже товара.
    Схема спеки: Объект модели "Продажа товара в истории посещений клиента"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор транзакции по продаже товара.")
    comment: str | None = Field(default=None, description="Комментарий.")
    date: str | None = Field(default=None, description="Дата продажи.")
    visit_id: float | None = Field(default=None, description="Идентификатор визита. Равно `0`, если нет связи с визитом.")
    record_id: float | None = Field(default=None, description="Идентификатор записи. Равно `0`, если нет связи с записью.")
    goods: list[ClientVisitsHistoryGoodsTransactionGood] | None = Field(default=None, description="Список проданных товаров.")
    staff: dict[str, Any] | None = Field(default=None, description="Сотрудник, продавший товар.")
    company: dict[str, Any] | None = Field(default=None, description="Минимальная информация о салоне, в котором был продан товар.")


class ClientVisitsHistoryRecord(BaseModel):
    """Данные по записи клиента.
    Схема спеки: Объект модели "Запись в истории посещений клиента"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор записи.")
    comment: str | None = Field(default=None, description="Комментарий.")
    date: str | None = Field(default=None, description="Дата записи.")
    visit_id: float | None = Field(default=None, description="Идентификатор визита.")
    attendance: float | None = Field(default=None, description="Статус записи в визите")
    services: list[ClientVisitsHistoryRecordService] | None = Field(default=None, description="Услуги в записи.")
    staff: dict[str, Any] | None = Field(default=None, description="Сотрудник, оказавший услугу.")
    company: dict[str, Any] | None = Field(default=None, description="Минимальная информация о салоне, в котором был продан товар.")
    tips: TipsReduce | TipsReduceWithFullInfo | None = Field(default=None, description="Данные о чаевых. Используются разные модели в зависимости от того, является ли текущий пользователь мастером в записи.")
    comer: dict[str, Any] | None = Field(default=None, description="Данные о посетителе. Если посетитель не указан, то поле не выводится.")


class CompanyAnalyticsLoyaltyProgramsIncomeDataTypes(BaseModel):
    """Статистика по выручке
    Схема спеки: Root Type for company_analytics_loyalty_programs_income_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения")
    data_: CompanyAnalyticsLoyaltyProgramsIncomeDataTypesData | None = Field(default=None, alias="data")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")


class CompanyAnalyticsLoyaltyProgramsVisitsDataTypes(BaseModel):
    """Получение статистики по клиентам
    Схема спеки: Root Type for company_analytics_loyalty_programs_visits_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения")
    data_: CompanyAnalyticsLoyaltyProgramsVisitsDataTypesData | None = Field(default=None, alias="data")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")


class CompanyGetResponseDataTypes(BaseModel):
    """Получить компанию
    Схема спеки: Root Type for company_get_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешного выполнения (true)")
    data_: CompanyGetResponseDataTypesData | None = Field(default=None, alias="data")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")


class CustomFieldsResponseDataTypes(BaseModel):
    """Получение коллекции полей филиала
    Схема спеки: Root Type for custom_fields_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: list[CustomFieldsResponseDataTypesDataItem] | None = Field(default=None, alias="data", description="Массив объектов с данными")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")


class CompanyCompanyidStaffStaffidResponseDataTypesDeprecatedDataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор сотрудника")
    api_id: str | None = Field(default=None, description="Внешний идентификатор сотрудника")
    name: str | None = Field(default=None, description="Имя сотрудника")
    specialization: str | None = Field(default=None, description="Сециализация сотрудника")
    position: CompanyCompanyidStaffStaffidResponseDataTypesDeprecatedDataItemPosition | None = Field(default=None)
    show_rating: float | None = Field(default=None, description="Показывать ли рейтинг сотрудника (1 - показывать, 0 - не показывать)")
    rating: float | None = Field(default=None, description="Рейтинг сотрудника")
    votes_count: float | None = Field(default=None, description="Кол-во голосов, оценивших сотрудника")
    user_id: float | None = Field(default=None, description="Идентификатор пользователя сотрудника")
    avatar: str | None = Field(default=None, description="Путь к файлу аватарки сотрудника")
    avatar_big: str | None = Field(default=None, description="Путь к файлу аватарки сотрудника в более высоком разрешении")
    comments_count: float | None = Field(default=None, description="Кол-во комментариев к сотруднику")
    weight: str | None = Field(default=None, description="Вес сотрудника. При выводе сотрудники сортируются по весу, сначала более тяжелые")
    information: str | None = Field(default=None, description="Дополнительная информация о сотруднике (HTML формат)")
    hidden: str | None = Field(default=None, description="Статус отображения сотрудника в онлайн-записи, 1 - скрыт, 0 - не скрыт")
    fired: str | None = Field(default=None, description="Статус увольнения сотрудника, 1 - уволен, 0 - не уволен")
    status: str | None = Field(default=None, description="Статус удаления сотрудника, 1 - удален, 0 - не удален")
    image_group: CompanyCompanyidStaffStaffidResponseDataTypesDeprecatedDataItemImageGroup | None = Field(default=None)


class CompanySalonIdSaleDocumentidResponseDataTypesDataState(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    items_: list[CompanySalonIdSaleDocumentidResponseDataTypesDataStateItemsItem] | None = Field(default=None, alias="items")
    loyalty_transactions: list[CompanySalonIdSaleDocumentidResponseDataTypesDataStateLoyaltyTransactionsItem] | None = Field(default=None, description="Транзакция оплаты с помощью лояльности")
    payment_transactions: list[CompanySalonIdSaleDocumentidResponseDataTypesDataStatePaymentTransactionsItem] | None = Field(default=None, description="Транзакция оплаты в кассу")


class ClientVisitsHistory(BaseModel):
    """Данные по визитам клиента, включая записи и продажи товаров.
    Схема спеки: Объект модели "История посещений клиента"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    goods_transactions: list[ClientVisitsHistoryGoodsTransaction] | None = Field(default=None, description="Список транзакций по продажам товаров.")
    records: list[ClientVisitsHistoryRecord] | None = Field(default=None, description="Список записей клиента.")


class CompanyAnalyticsOverallDataType(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data_: AnalyticsReportOverallStats2 = Field(alias="data")
    meta: list[dict[str, Any]] = Field(description="Метаданные")
    success: bool = Field(description="Статус успешности выполнения (true)")


class CompanyCompanyidStaffStaffidResponseDataTypesDeprecated(BaseModel):
    """Устаревшее. Получить список сотрудников / конкретного сотрудника
    Схема спеки: Root Type for company_companyid_staff_staffid_response_data_types_deprecated
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: list[CompanyCompanyidStaffStaffidResponseDataTypesDeprecatedDataItem] | None = Field(default=None, alias="data", description="Массив объектов с данными")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")


class CompanySalonIdSaleDocumentidResponseDataTypesData(BaseModel):
    """Объект с данными
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    state: CompanySalonIdSaleDocumentidResponseDataTypesDataState | None = Field(default=None)
    kkm_state: CompanySalonIdSaleDocumentidResponseDataTypesDataKkmState | None = Field(default=None)
    payment_methods: list[CompanySalonIdSaleDocumentidResponseDataTypesDataPaymentMethodsItem] | None = Field(default=None)


class CompanySalonIdSaleDocumentidResponseDataTypes(BaseModel):
    """Получение операции продажи
    Схема спеки: Root Type for company_salon_id_sale_documentid_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: CompanySalonIdSaleDocumentidResponseDataTypesData | None = Field(default=None, alias="data")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")

__all__ = [
    "ClientCommentContainer",
    "ClientVisitsHistory",
    "ClientVisitsHistoryGoodsTransaction",
    "ClientVisitsHistoryRecord",
    "ClientVisitsHistoryRecordService",
    "ClientsCompanyidResponseDeprecatedDataTypes",
    "CompanyAnalyticsLoyaltyProgramsIncomeDataTypes",
    "CompanyAnalyticsLoyaltyProgramsIncomeDataTypesData",
    "CompanyAnalyticsLoyaltyProgramsStaffDataTypes",
    "CompanyAnalyticsLoyaltyProgramsVisitsDataTypes",
    "CompanyAnalyticsLoyaltyProgramsVisitsDataTypesData",
    "CompanyAnalyticsOverallDataType",
    "CompanyCompanyidClientsSearchRequestDataTypes",
    "CompanyCompanyidStaffStaffidResponseDataTypes",
    "CompanyCompanyidStaffStaffidResponseDataTypesDeprecated",
    "CompanyCompanyidStaffStaffidResponseDataTypesDeprecatedDataItem",
    "CompanyCompanyidStaffStaffidResponseDataTypesDeprecatedDataItemImageGroup",
    "CompanyGetResponseDataTypes",
    "CompanyGetResponseDataTypesData",
    "CompanySalonIdSaleDocumentidResponseDataTypes",
    "CompanySalonIdSaleDocumentidResponseDataTypesData",
    "CompanySalonIdSaleDocumentidResponseDataTypesDataKkmState",
    "CompanySalonIdSaleDocumentidResponseDataTypesDataState",
    "CompanySalonIdSaleDocumentidResponseDataTypesDataStateLoyaltyTransactionsItem",
    "CompanySalonidSaleDocumentidPaymentAbonements",
    "CompanySalonidSaleDocumentidPaymentAccount",
    "CompanySalonidSaleDocumentidPaymentCertificate",
    "CompanySalonidSaleDocumentidPaymentDeposit",
    "CompanySalonidSaleDocumentidPaymentLoyaltyCard",
    "CompanySalonidSaleDocumentidPaymentLoyaltyProgram",
    "CompanySalonidSaleDocumentidPaymentLoyaltyProgramPayment",
    "CompanySalonidSaleDocumentidPaymentReferal",
    "CompanySalonidSaleDocumentidPaymentReferalPayment",
    "CompanyStaffPositionListDataType",
    "CompanyUsersDeprecatedResponseDataTypes",
    "CompanyUsersDeprecatedResponseDataTypesDataItem",
    "CustomFieldsResponseDataTypes",
    "CustomFieldsResponseDataTypesDataItem",
    "CustomFieldsResponseDataTypesDataItemCustomField"
]
