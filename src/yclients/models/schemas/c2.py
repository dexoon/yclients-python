"""Модели YCLIENTS API (c2: C).

Сгенерировано scripts/generate.py -- не редактируйте вручную.
"""

from __future__ import annotations

from datetime import date, datetime
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class CompanySalonidSaleDocumentidPaymentDepositPaymentMethod(BaseModel):
    """Метод оплаты
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    slug: str | None = Field(default=None, description="Тип метода оплаты")
    deposit_id: int | None = Field(default=None, description="Идентификатор личного счета клиента")


class CompanySalonidSaleDocumentidPaymentLoyaltyCardPaymentMethod(BaseModel):
    """Метод оплаты
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    slug: str | None = Field(default=None, description="Тип метода оплаты")
    loyalty_card_id: int | None = Field(default=None, description="Идентификатор карты лояльности")


class CompanySalonidSaleDocumentidPaymentLoyaltyProgramPaymentMethod(BaseModel):
    """Метод оплаты
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    slug: str | None = Field(default=None, description="Тип метода оплаты")
    loyalty_program_id: int | None = Field(default=None, description="Идентификатор программы лояльности")
    loyalty_card_id: int | None = Field(default=None, description="Идентификатор карты лояльности")


class CompanySalonidSaleDocumentidPaymentReferalPaymentMethod(BaseModel):
    """Метод оплаты
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    slug: str | None = Field(default=None, description="Тип метода оплаты")
    loyalty_program_id: int | None = Field(default=None, description="Идентификатор программы лояльности")


class CompanyUsersDeprecatedResponseDataTypesDataItemAccess(BaseModel):
    """Объект прав доступа пользователей к модулям системы
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    stat_access: bool | None = Field(default=None, description="true - есть доступ к аналитике, false - нет доступа")
    schedule_edit_access: bool | None = Field(default=None, description="true - есть доступ к графику работы сотрудника в журнале, false - нет доступа")
    client_phones_access: bool | None = Field(default=None, description="true - есть доступ к номерам телефонов в списке клиентов, false - нет доступа")
    clients_access: bool | None = Field(default=None, description="true - есть доступ к клиентской базе, false - нет доступа")
    settings_access: bool | None = Field(default=None, description="true - есть доступ к разделу настройки, false - нет доступа")
    edit_records_access: bool | None = Field(default=None, description="true - есть доступ к изменение записей, false - нет доступа")
    timetable_access: bool | None = Field(default=None, description="true - есть доступ к журналу записи, false - нет доступа")
    billing_access: bool | None = Field(default=None, description="true - есть доступ к биллингу (раздел меню баланс), false - нет доступа")
    users_access: bool | None = Field(default=None, description="true - есть доступ к управлению пользователями, false - нет доступа")
    excel_access: bool | None = Field(default=None, description="1 - есть доступ к выгрузке списка клиентов в Excel, 0 - нет доступа")
    finances_access: bool | None = Field(default=None, description="true - есть доступ к финансам, false - нет доступа")
    storages_access: bool | None = Field(default=None, description="true - есть доступ к складу, false - нет доступа")
    send_sms: bool | None = Field(default=None, description="true - есть доступ к SMS рассылки клиентам, false - нет доступа")
    master_id: float | None = Field(default=None, description="0 - если пользователь может просматривать расписание и записи всех сотрудников, иначе только того сотрудника, ID которого задан")


class ConsumablesConsumablesItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    goods_transaction_id: float | None = Field(default=None, description="id товарной транзакции")
    record_id: float | None = Field(default=None, description="id записи")
    service_id: float | None = Field(default=None, description="id услуги")
    storage_id: float | None = Field(default=None, description="id склада,")
    good_id: float | None = Field(default=None, description="id товара,")
    price: float | None = Field(default=None, description="себестоимость расходника в записи,")
    amount: float | None = Field(default=None, description="количество расходника в записи,")


class CountriesResponseDataTypesDataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: str | None = Field(default=None, alias="id", description="Идентификатор страны")
    title: str | None = Field(default=None, description="Краткое азвание страны")
    full_title: str | None = Field(default=None, description="Полное название страны")
    phone_code: str | None = Field(default=None, description="Телефонный код страны")
    phone_template: str | None = Field(default=None, description="Маска номера телефона страны")
    phone_example: str | None = Field(default=None, description="Пример номера телефона страны")
    currency: str | None = Field(default=None, description="Валюта страны")
    exchange: str | None = Field(default=None, description="Ставка обмена валют по отношению к рублю")


class CustomFieldsResponseDataTypesDataItemCustomFieldType(BaseModel):
    """Тип поля
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    code: str | None = Field(default=None, description="Код типа поля")
    title: str | None = Field(default=None, description="Название типа поля")


class CheckForActivity(BaseModel):
    """Описание количества доступных записей и дату последней возможной записи по абонементу
    Схема спеки: Проверка абонемента на количество доступных записей и последнюю дату записи
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: str | None = Field(default=None, alias="id", description="Идентификатор абонемента")
    type_: str | None = Field(default=None, alias="type", description="Тип объекта.")
    attributes: CheckForActivityAttributes | None = Field(default=None)


class CitiesResponseDataTypes(BaseModel):
    """Получить список городов
    Схема спеки: Root Type for cities_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: list[CitiesResponseDataTypesDataItem] | None = Field(default=None, alias="data", description="Массив объектов с данными")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")


class ClientCommentFileDto(BaseModel):
    """Данные существующего файла в карточке клиента.
    Схема спеки: Объект модели "Файл в карточке клиента"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    link: str | None = Field(default=None, description="Ссылка на скачивание файла в карточке клиента.")
    filename: str | None = Field(default=None, description="Название файла в карточке клиента.")


class ClientVisitsHistoryGoodsTransactionGood(BaseModel):
    """Данные о проданном товаре.
    Схема спеки: Объект модели "Проданный товар в истории посещений клиента"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор товара.")
    title: str | None = Field(default=None, description="Наименование товара.")
    amount: float | None = Field(default=None, description="Количество проданного товара.")
    unit: str | None = Field(default=None, description="Единица измерения проданного товара.")
    cost_per_unit: float | None = Field(default=None, description="Стоимость единицы товара без скидки.")
    first_cost: float | None = Field(default=None, description="Стоимость всего товара без скидки.")
    discount_percent: float | None = Field(default=None, description="Процент скидки.")
    cost_to_pay: float | None = Field(default=None, description="Стоимость товара с учетом скидки.")
    paid_sum: float | None = Field(default=None, description="Стоимость товара с учетом скидки.")
    payment_status: Literal["not_paid", "paid_not_full", "paid_full", "paid_over"] | None = Field(default=None, description="Статус оплаты визита: `not_paid` - визит неоплачен, никаких оплат по визиту не проходило; `paid_not_full` - визит оплачен частично; `paid_full` - визит оплачен полностью, переплаты нет; `paid_over`...")


class ClientVisitsHistoryRecordServiceConsumable(BaseModel):
    """Данные по расходнику.
    Схема спеки: Объект модели "Расходник в услуге"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    title: str | None = Field(default=None, description="Наименование расходника.")
    amount: float | None = Field(default=None, description="Количество товара в выбранной пользователем единице измерения.")
    cost_per_unit: float | None = Field(default=None, description="Стоимость за единицу товара.")
    unit: str | None = Field(default=None, description="Наименование единицы измерения товара.")


class ClientsFilesClientidReaponseDataTypes(BaseModel):
    """Пример запроса на получение списка файлов клиента
    Схема спеки: Root Type for clients_files_clientid_reaponse_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: list[ClientsFilesClientidReaponseDataTypesDataItem] | None = Field(default=None, alias="data", description="Массив объектов с данными")
    meta: ClientsFilesClientidReaponseDataTypesMeta | None = Field(default=None)


class Comer(BaseModel):
    """Схема спеки: Объект модели "Посетитель"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор посетителя.")
    title: str | None = Field(default=None, description="Имя посетителя.")
    slug: Literal["person", "pet", "vehicle"] | None = Field(default=None, description="Тип посетителя: `person` - человек; `pet` - питомец; `vehicle` - транспортное средство.")


class CommentsCompanyidRequestDataTypes(BaseModel):
    """Оставить комментарии
    Схема спеки: Root Type for comments_companyid_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    mark: float = Field(description="Оценка от 1 до 5")
    text: str = Field(description="Текст отзыва")
    name: str = Field(description="Имя пользователя, которое будет отображено на странице с отзывами")


class CommentsCompanyidRessponse200DataTypes(BaseModel):
    """Получить комментарии
    Схема спеки: Root Type for comments_companyid_ressponse200_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: list[CommentsCompanyidRessponse200DataTypesDataItem] | None = Field(default=None, alias="data", description="Массив объектов с данными")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")


class CompaniesDataTypes(BaseModel):
    """Получить список компаний
    Схема спеки: Root Type for companies_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешного выполнения (true)")
    data_: list[CompaniesDataTypesDataItem] | None = Field(default=None, alias="data", description="Массив объектов")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")


class CompaniesDataTypes2(BaseModel):
    """Получить список компаний
    Схема спеки: Root Type for companies_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешного выполнения (true)")
    data_: list[CompaniesDataTypes2DataItem] | None = Field(default=None, alias="data", description="Массив объектов")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")


class Company2(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float = Field(alias="id", description="ID копаниии")
    title: str = Field(description="Название организации")
    country: str = Field(description="Название страны, в которой расположена организация")
    country_id: float = Field(description="ID страны")
    city: str = Field(description="Название города, в котором расположена организация")
    city_id: float = Field(description="ID города")
    phone: str = Field(description="Телефон компании")
    timezone: str = Field(description="Временная зона компании")
    address: str = Field(description="Адрес компании")
    coordinate_lat: float = Field(description="Широта")
    coordinate_lng: float = Field(description="Долгота")


class CompanyCompanyIdUsersResponseDataTypes(BaseModel):
    """Получить пользователей компании
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: list[CompanyCompanyIdUsersResponseDataTypesDataItem] | None = Field(default=None, alias="data", description="Массив объектов с данными")
    meta: CompanyCompanyIdUsersResponseDataTypesMeta | None = Field(default=None)


class CompanyCompanyidClientsSearchResponseDataTypes(BaseModel):
    """Получить список клиентов
    Схема спеки: Root Type for company_companyid_clients_search_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: list[CompanyCompanyidClientsSearchResponseDataTypesDataItem] | None = Field(default=None, alias="data", description="Массив объектов с данными")
    meta: CompanyCompanyidClientsSearchResponseDataTypesMeta | None = Field(default=None)


class CompanyCompanyidServiceCategoriesResponse200DataTypes(BaseModel):
    """Получить список категорий услуг
    Схема спеки: Root Type for company_companyid_service_categories_response200_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: list[CompanyCompanyidServiceCategoriesResponse200DataTypesDataItem] | None = Field(default=None, alias="data", description="Массив объектов")
    meta: CompanyCompanyidServiceCategoriesResponse200DataTypesMeta | None = Field(default=None)


class CompanyCompanyidServicesServiceidResponse200DataTypes(BaseModel):
    """Получить список услуг / конкретную услугу
    Схема спеки: Root Type for company_companyid_services_serviceid_response200_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: list[CompanyCompanyidServicesServiceidResponse200DataTypesDataItem] | None = Field(default=None, alias="data", description="Массив объектов с данными")
    meta: CompanyCompanyidServicesServiceidResponse200DataTypesMeta | None = Field(default=None)


class CompanyCreateRequestDataTypes(BaseModel):
    """Создать компанию
    Схема спеки: Root Type for company_create_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    title: str | None = Field(default=None, description="Название компании")
    country_id: float | None = Field(default=None, description="Идентификатор страны, в которой расположена копания ([метод получения стран](#countries))")
    city_id: float | None = Field(default=None, description="Идентификатор города, в котором расположена компания ([метод получения городов](#cities))")
    address: str | None = Field(default=None, description="Адрес компании")
    site: str | None = Field(default=None, description="Сайт компании")
    coordinate_lat: float | None = Field(default=None, description="Широта")
    coordinate_lot: float | None = Field(default=None, description="Долгота")
    business_type_id: float | None = Field(default=None, description="Сфера бизнеса")
    short_descr: str | None = Field(default=None, description="Категория компании")


class CompanyCreateResponseDataTypes(BaseModel):
    """Создать компанию
    Схема спеки: Root Type for company_create_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешного выполнения (true)")
    data_: CompanyCreateResponseDataTypesData | None = Field(default=None, alias="data")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")


class CompanyGetOnlineSettingsResponseDataFieldDataTypes(BaseModel):
    """Схема спеки: Root Type for company_get_online_settings_response_data_field_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    confirm_number: bool = Field(description="Подтверждать номер клиента по SMS")
    any_master: bool = Field(description="Режим \"Любой сотрудник\"")
    seance_delay_step: int = Field(description="Задержка до ближайшего сеанса, в минутах от 0 до 23 часов (включительно) с шагом 30 минут")
    activity_online_record_clients_count_max: int = Field(description="Максимальное количество мест в одной записи события")


class CompanyGetOnlineSettingsResponseDataTypes(BaseModel):
    """Получение настроек онлайн-записи
    Схема спеки: Root Type for company_get_online_settings_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: CompanyGetOnlineSettingsResponseDataFieldDataTypes | None = Field(default=None, alias="data")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные")


class CompanyGetTimetableSettingsResponseDataFieldDataTypes(BaseModel):
    """Схема спеки: Root Type for company_get_timetable_settings_response_data_field_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    record_type: int = Field(description="Тип записи по умолчанию: 0 - Смешанная запись, 1 - Индивидуальная запись, 2 - Групповая запись")
    activity_record_clients_count_max: int = Field(description="Максимальное количество мест в одной записи события")


class CompanyGetTimetableSettingsResponseDataTypes(BaseModel):
    """Получение настроек журнала записи
    Схема спеки: Root Type for company_get_timetable_settings_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: CompanyGetTimetableSettingsResponseDataFieldDataTypes | None = Field(default=None, alias="data")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные")


class CompanyGridSettingContainer(BaseModel):
    """Правила построения слотов.
    Схема спеки: Объект модели "Настройки формирования сетки"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    grid_first_timeslot: float | None = Field(default=None, description="Нижнее ограничение доступности слотов (“время для онлайн записи” в интерфейсе).")
    grid_last_timeslot: float | None = Field(default=None, description="Верхнее ограничение доступности слотов (“время для онлайн записи” в интерфейсе).")
    grid_display_step: float | None = Field(default=None, description="Шаг вывода слотов (в секундах).")
    grid_nearest_timeslot_delay: float | None = Field(default=None, description="Задержка до ближайшего сеанса (в секундах).")
    grid_base_type: str | None = Field(default=None, description="Тип сетки `predefined` - “фиксированно”/“оптимально” + “от времени для онлайн записи”; `schedule` - “фиксированно”/“оптимально” + “от графика сотрудника”; `timeslots` - “динамически” enum: - predef...")
    is_grid_flexible: bool | None = Field(default=None, description="Флаг добавления \"гибкого\" слота.")


class CompanyGridWeekdaysContainer(BaseModel):
    """Получение настроек формирования таймслотов филиала.
    Схема спеки: Настройки слотов по дням недели
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    weekday: float | None = Field(default=None, description="День недели [1 - 7].")
    timeslots: list[float] | None = Field(default=None, description="Включенные для записи слоты (для режима \"predefined\", в остальных случаях незаполнено).")
    setting: CompanyGridSettingContainer | None = Field(default=None)


class CompanyLoyaltyProgramsSearchDataTypes(BaseModel):
    """Получение списка акций, доступных для филиала
    Схема спеки: Root Type for company_loyalty_programs_search_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения.")
    data_: list[CompanyLoyaltyProgramsSearchDataTypesDataItem] | None = Field(default=None, alias="data", description="Массив объектов с данными.")
    meta: CompanyLoyaltyProgramsSearchDataTypesMeta | None = Field(default=None)


class CompanyMinimal(BaseModel):
    """Схема спеки: Объект модели "Филиал, минимальная информация"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор филиала.")
    title: str | None = Field(default=None, description="Наименование филиала.")


class CompanyPutRequestDataTypes(BaseModel):
    """Изменить компанию
    Схема спеки: Root Type for company_put_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    title: str | None = Field(default=None, description="Название компании")
    country_id: float | None = Field(default=None, description="Идентификатор страны (приоритетнее параметра country)")
    country: str | None = Field(default=None, description="Страна")
    city_id: float | None = Field(default=None, description="Идентификатор города (приоритетнее параметра city)")
    city: str | None = Field(default=None, description="Город")
    address: str | None = Field(default=None, description="Адрес компании")
    zip: str | None = Field(default=None, description="Индекс")
    phones: list[str] | None = Field(default=None, description="Телефоны")
    social: CompanyPutRequestDataTypesSocial | None = Field(default=None)
    site: str | None = Field(default=None, description="Сайт компании")
    coordinate_lat: float | None = Field(default=None, description="Широта")
    coordinate_lon: float | None = Field(default=None, description="Долгота")
    description: str | None = Field(default=None, description="Описание")
    business_type_id: float | None = Field(default=None, description="Сфера бизнеса")
    short_descr: str | None = Field(default=None, description="Категория бизнеса")


class CompanyPutResponseDataTypes(BaseModel):
    """Изменить компанию
    Схема спеки: Root Type for company_put_response_data_types
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
    social: CompanyPutResponseDataTypesSocial | None = Field(default=None)
    site: str | None = Field(default=None, description="Сайт компании")
    coordinate_lat: float | None = Field(default=None, description="Широта")
    coordinate_lon: float | None = Field(default=None, description="Долгота")
    description: str | None = Field(default=None, description="Описание")
    business_type_id: float | None = Field(default=None, description="Сфера бизнеса")
    short_descr: str | None = Field(default=None, description="Категория бизнеса")
    phone_confirmation: bool | None = Field(default=None, description="Нужно ли подтверждать телефон по смс, при бронировании")
    group_priority: int | None = Field(default=None, description="Чем больше приоритет, тем выше компания при выводе в списке филиалов сети")
    push_notification_phone_confirm: bool | None = Field(default=None, description="Подтверждать номер клиента для отправки push уведомлений")
    access: dict[str, Any] | None = Field(default=None, description="Список прав")


class CompanyUpdateOnlineSettingsDataTypes(BaseModel):
    """Схема спеки: Root Type for company_update_online_settings_data_type
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    confirm_number: bool = Field(description="Подтверждать номер клиента по SMS")
    any_master: bool = Field(description="Режим \"Любой сотрудник\"")
    seance_delay_step: int = Field(description="Задержка до ближайшего сеанса, в минутах от 0 до 23 часов (включительно) с шагом 30 минут")
    activity_online_record_clients_count_max: int = Field(description="Максимальное количество мест в одной записи события")


class CompanyUpdateTimetableSettingsDataTypes(BaseModel):
    """Схема спеки: Root Type for company_update_timetable_settings_data_type
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    record_type: int = Field(description="Тип записи по умолчанию: 0 - Смешанная запись, 1 - Индивидуальная запись, 2 - Групповая запись")
    activity_record_clients_count_max: int = Field(description="Максимальное количество мест в одной записи события")


class Consumables2(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    consumables: list[ConsumablesConsumablesItem] | None = Field(default=None, description="Список расходников")


class CountriesResponseDataTypes(BaseModel):
    """Получить список стран
    Схема спеки: Root Type for countries_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: list[CountriesResponseDataTypesDataItem] | None = Field(default=None, alias="data", description="Массив объектов с данными")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")


class Currency2(BaseModel):
    """Валюта
    Схема спеки: Root Type for Currency
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор валюты")
    iso: str | None = Field(default=None, description="Трехбуквенный код валюты в соответствии с ISO 4217")
    name: str | None = Field(default=None, description="Название валюты")
    symbol: str | None = Field(default=None, description="Символ валюты, указываемый рядом с суммой")
    is_symbol_after_amount: bool | None = Field(default=None, description="Флаг, где отображать символ валюты относительно суммы (true - после суммы, false - перед)")


class CustomFieldsRequestDataType(BaseModel):
    """Добавление дополнительного поля
    Схема спеки: Root Type for custom_fields_request_data_type
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    type_: str = Field(alias="type", description="Тип поля")
    code: str = Field(description="Идентификатор поля")
    title: str = Field(description="Название поля")
    user_can_edit: bool = Field(description="Может ли пользователь редактировать поле")
    show_in_ui: bool = Field(description="Показывать ли поле в интерфейсе")


class ClientsCompanyidResponseDeprecatedDataTypesDataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор клиента")
    name: str | None = Field(default=None, description="Имя клиента")
    phone: str | None = Field(default=None, description="Телефон клиента")
    email: str | None = Field(default=None, description="Email клиента")
    categories: list[ClientsCompanyidResponseDeprecatedDataTypesDataItemCategoriesItem] | None = Field(default=None, description="Категории клиента")
    sex_id: float | None = Field(default=None, description="Идентификатор, обозначающий пол, 0 - неизвестно, 1 - мужской, 2 - женский")
    sex: str | None = Field(default=None, description="Название пола")
    discount: float | None = Field(default=None, description="Скидка")
    importance_id: int | None = Field(default=None, description="Класс важности клиента (0 - нет, 1 - бронза, 2 - серебро, 3 - золото)")
    importance: str | None = Field(default=None, description="Название класса важности клиента")
    card: float | None = Field(default=None, description="Номер карты клиента")
    birth_date: str | None = Field(default=None, description="Дата рождения клиента")
    comment: str | None = Field(default=None, description="Комментарий о клиенте")
    sms_check: float | None = Field(default=None, description="1 - Поздравлять с Днем Рождения по SMS, 0 - не поздравлять")
    sms_not: float | None = Field(default=None, description="1 - Исключить клиента из SMS рассылок, 0 - не исключать")
    spent: float | None = Field(default=None, description="Сколько потратил средств в компании на момент добавления")
    balance: float | None = Field(default=None, description="Баланс клиента")
    visits: float | None = Field(default=None, description="Количество визитов")
    last_change_date: str | None = Field(default=None, description="Дата последнего изменения")
    custom_fields: dict[str, Any] | None = Field(default=None, description="Дополнительные поля клиента")


class CompanyAnalyticsLoyaltyProgramsIncomeDataTypesDataIncomeStats(BaseModel):
    """Статистика по выручке
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    new: CompanyAnalyticsLoyaltyProgramsIncomeDataTypesDataIncomeStatsNew | None = Field(default=None)
    old: CompanyAnalyticsLoyaltyProgramsIncomeDataTypesDataIncomeStatsOld | None = Field(default=None)
    total: CompanyAnalyticsLoyaltyProgramsIncomeDataTypesDataIncomeStatsTotal | None = Field(default=None)


class CompanyAnalyticsLoyaltyProgramsStaffDataTypesDataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    client_stats: CompanyAnalyticsLoyaltyProgramsStaffDataTypesDataItemClientStats | None = Field(default=None)
    staff: CompanyAnalyticsLoyaltyProgramsStaffDataTypesDataItemStaff | None = Field(default=None)


class CompanyAnalyticsLoyaltyProgramsVisitsDataTypesDataClientStats(BaseModel):
    """Статистика по клиентам
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    new: CompanyAnalyticsLoyaltyProgramsVisitsDataTypesDataClientStatsNew | None = Field(default=None)
    old: CompanyAnalyticsLoyaltyProgramsVisitsDataTypesDataClientStatsOld | None = Field(default=None)
    total: CompanyAnalyticsLoyaltyProgramsVisitsDataTypesDataClientStatsTotal | None = Field(default=None)


class CompanyCompanyidClientsSearchRequestDataTypesFiltersItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    type_: str | None = Field(default=None, alias="type")
    state: CompanyCompanyidClientsSearchRequestDataTypesFiltersItemState | None = Field(default=None)


class CompanyCompanyidStaffStaffidResponseDataTypesDataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор сотрудника")
    name: str | None = Field(default=None, description="Имя сотрудника")
    company_id: float | None = Field(default=None, description="Идентификатор компании")
    specialization: str | None = Field(default=None, description="Специализация сотрудника")
    position: CompanyCompanyidStaffStaffidResponseDataTypesDataItemPosition | None = Field(default=None)
    avatar: str | None = Field(default=None, description="Путь к файлу аватарки сотрудника")
    avatar_big: str | None = Field(default=None, description="Путь к файлу аватарки сотрудника в более высоком разрешении")
    fired: float | None = Field(default=None, description="Уволен ли сотрудник, 1 - уволен, 0 - не уволен")
    status: float | None = Field(default=None, description="Удален ли сотрудник, 1 - удален, 0 - не удален")
    hidden: float | None = Field(default=None, description="Скрыт ли сотрудник для онлайн-записи, 1 - скрыт, 0 - не скрыт")
    user_id: float | None = Field(default=None, description="Идентификатор пользователя сотрудника")


class CompanyCompanyidStaffStaffidResponseDataTypesDeprecatedDataItemImageGroupImages(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    sm: CompanyCompanyidStaffStaffidResponseDataTypesDeprecatedDataItemImageGroupImagesSm | None = Field(default=None)
    norm: CompanyCompanyidStaffStaffidResponseDataTypesDeprecatedDataItemImageGroupImagesNorm | None = Field(default=None)
    origin: CompanyCompanyidStaffStaffidResponseDataTypesDeprecatedDataItemImageGroupImagesOrigin | None = Field(default=None)


class CompanyGetResponseDataTypesDataGroups(BaseModel):
    """Сети в которые входит компания. Поле будет присутствовать только если передан GET параметр show_groups=1
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_1: CompanyGetResponseDataTypesDataGroupsId1 | None = Field(default=None, alias="ID-1")
    id_2: CompanyGetResponseDataTypesDataGroupsId2 | None = Field(default=None, alias="ID-2")


class CompanyGridDaysSettingsContainerItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    date: Any | None = Field(default=None, description="День, на который переопределены настройки (Y-m-d).")
    timeslots: list[float] | None = Field(default=None, description="Пустой массив таймслотов.")
    setting: CompanyGridSettingContainer | None = Field(default=None)


class CompanySalonIdSaleDocumentidResponseDataTypesDataKkmStateTransactionsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор транзакции ККМ")
    document_id: int | None = Field(default=None, description="Идентификатор документа")
    print_date: str | None = Field(default=None, description="Дата печати чека")
    printed_count: int | None = Field(default=None)
    sum: int | None = Field(default=None)
    type_: CompanySalonIdSaleDocumentidResponseDataTypesDataKkmStateTransactionsItemType | None = Field(default=None, alias="type")
    status: CompanySalonIdSaleDocumentidResponseDataTypesDataKkmStateTransactionsItemStatus | None = Field(default=None)
    document: CompanySalonIdSaleDocumentidResponseDataTypesDataKkmStateTransactionsItemDocument | None = Field(default=None)
    cashier: CompanySalonIdSaleDocumentidResponseDataTypesDataKkmStateTransactionsItemCashier | None = Field(default=None)


class CompanySalonIdSaleDocumentidResponseDataTypesDataPaymentMethodsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    slug: str | None = Field(default=None, description="Тип метода оплаты")
    is_applicable: bool | None = Field(default=None, description="Возможно ли применить данный метод")
    applicable_amount: float | None = Field(default=None, description="Возможная сумма, принимаемая к оплате")
    applicable_count: int | None = Field(default=None, description="Возможное количество посещений (в случае абонемента)")
    applicable_value: float | None = Field(default=None, description="Применимый бонус (в случае программы лояльности)")
    account_id: int | None = Field(default=None, description="Идентификатор кассы (щависит от slug)")
    account: CompanySalonIdSaleDocumentidResponseDataTypesDataPaymentMethodsItemAccount | None = Field(default=None)


class CompanySalonIdSaleDocumentidResponseDataTypesDataStateLoyaltyTransactionsItemDeposit(BaseModel):
    """Списание с личного счета
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор личного счета")
    balance: float | None = Field(default=None, description="Баланс личного счета")
    type_: CompanySalonIdSaleDocumentidResponseDataTypesDataStateLoyaltyTransactionsItemDepositType | None = Field(default=None, alias="type")


class CompanySalonIdSaleDocumentidResponseDataTypesDataStatePaymentTransactionsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор транзакции оплаты")
    document_id: int | None = Field(default=None, description="Идентификатор документа")
    sale_item_id: int | None = Field(default=None, description="Идентификатор проданной единицы")
    sale_item_type: str | None = Field(default=None, description="Тип проданной единицы")
    expense_id: int | None = Field(default=None, description="Идентификатор статьи платежа")
    account_id: int | None = Field(default=None, description="Идентификатор кассы")
    created_at: str | None = Field(default=None, description="Дата создания")
    account: CompanySalonIdSaleDocumentidResponseDataTypesDataStatePaymentTransactionsItemAccount | None = Field(default=None)
    expense: CompanySalonIdSaleDocumentidResponseDataTypesDataStatePaymentTransactionsItemExpense | None = Field(default=None)


class CompanySalonidSaleDocumentidPaymentAbonementsPayment(BaseModel):
    """Объект, содержащий метод оплаты
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    method: CompanySalonidSaleDocumentidPaymentAbonementsPaymentMethod | None = Field(default=None)
    number: str | None = Field(default=None, description="Код абонемента")


class CompanySalonidSaleDocumentidPaymentAccountPayment(BaseModel):
    """Объект, содержащий метод оплаты
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    method: CompanySalonidSaleDocumentidPaymentAccountPaymentMethod | None = Field(default=None)
    amount: float | None = Field(default=None, description="Сумма оплаты")


class CompanySalonidSaleDocumentidPaymentCertificatePayment(BaseModel):
    """Объект, содержащий метод оплаты
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    method: CompanySalonidSaleDocumentidPaymentCertificatePaymentMethod | None = Field(default=None)
    amount: float | None = Field(default=None, description="Сумма оплаты")
    number: str | None = Field(default=None, description="Код сертификата")


class CompanySalonidSaleDocumentidPaymentDepositPayment(BaseModel):
    """Объект, содержащий метод оплаты
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    method: CompanySalonidSaleDocumentidPaymentDepositPaymentMethod | None = Field(default=None)
    amount: float | None = Field(default=None, description="Сумма оплаты")


class CompanySalonidSaleDocumentidPaymentLoyaltyCardPayment(BaseModel):
    """Объект, содержащий метод оплаты
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    method: CompanySalonidSaleDocumentidPaymentLoyaltyCardPaymentMethod | None = Field(default=None)
    amount: float | None = Field(default=None, description="Сумма оплаты")

__all__ = [
    "CheckForActivity",
    "CitiesResponseDataTypes",
    "ClientCommentFileDto",
    "ClientVisitsHistoryGoodsTransactionGood",
    "ClientVisitsHistoryRecordServiceConsumable",
    "ClientsCompanyidResponseDeprecatedDataTypesDataItem",
    "ClientsFilesClientidReaponseDataTypes",
    "Comer",
    "CommentsCompanyidRequestDataTypes",
    "CommentsCompanyidRessponse200DataTypes",
    "CompaniesDataTypes",
    "CompaniesDataTypes2",
    "Company2",
    "CompanyAnalyticsLoyaltyProgramsIncomeDataTypesDataIncomeStats",
    "CompanyAnalyticsLoyaltyProgramsStaffDataTypesDataItem",
    "CompanyAnalyticsLoyaltyProgramsVisitsDataTypesDataClientStats",
    "CompanyCompanyIdUsersResponseDataTypes",
    "CompanyCompanyidClientsSearchRequestDataTypesFiltersItem",
    "CompanyCompanyidClientsSearchResponseDataTypes",
    "CompanyCompanyidServiceCategoriesResponse200DataTypes",
    "CompanyCompanyidServicesServiceidResponse200DataTypes",
    "CompanyCompanyidStaffStaffidResponseDataTypesDataItem",
    "CompanyCompanyidStaffStaffidResponseDataTypesDeprecatedDataItemImageGroupImages",
    "CompanyCreateRequestDataTypes",
    "CompanyCreateResponseDataTypes",
    "CompanyGetOnlineSettingsResponseDataFieldDataTypes",
    "CompanyGetOnlineSettingsResponseDataTypes",
    "CompanyGetResponseDataTypesDataGroups",
    "CompanyGetTimetableSettingsResponseDataFieldDataTypes",
    "CompanyGetTimetableSettingsResponseDataTypes",
    "CompanyGridDaysSettingsContainerItem",
    "CompanyGridSettingContainer",
    "CompanyGridWeekdaysContainer",
    "CompanyLoyaltyProgramsSearchDataTypes",
    "CompanyMinimal",
    "CompanyPutRequestDataTypes",
    "CompanyPutResponseDataTypes",
    "CompanySalonIdSaleDocumentidResponseDataTypesDataKkmStateTransactionsItem",
    "CompanySalonIdSaleDocumentidResponseDataTypesDataPaymentMethodsItem",
    "CompanySalonIdSaleDocumentidResponseDataTypesDataStateLoyaltyTransactionsItemDeposit",
    "CompanySalonIdSaleDocumentidResponseDataTypesDataStatePaymentTransactionsItem",
    "CompanySalonidSaleDocumentidPaymentAbonementsPayment",
    "CompanySalonidSaleDocumentidPaymentAccountPayment",
    "CompanySalonidSaleDocumentidPaymentCertificatePayment",
    "CompanySalonidSaleDocumentidPaymentDepositPayment",
    "CompanySalonidSaleDocumentidPaymentDepositPaymentMethod",
    "CompanySalonidSaleDocumentidPaymentLoyaltyCardPayment",
    "CompanySalonidSaleDocumentidPaymentLoyaltyCardPaymentMethod",
    "CompanySalonidSaleDocumentidPaymentLoyaltyProgramPaymentMethod",
    "CompanySalonidSaleDocumentidPaymentReferalPaymentMethod",
    "CompanyUpdateOnlineSettingsDataTypes",
    "CompanyUpdateTimetableSettingsDataTypes",
    "CompanyUsersDeprecatedResponseDataTypesDataItemAccess",
    "Consumables2",
    "ConsumablesConsumablesItem",
    "CountriesResponseDataTypes",
    "CountriesResponseDataTypesDataItem",
    "Currency2",
    "CustomFieldsRequestDataType",
    "CustomFieldsResponseDataTypesDataItemCustomFieldType"
]
