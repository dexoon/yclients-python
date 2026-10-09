"""Модели YCLIENTS API (c1: C).

Сгенерировано scripts/generate.py -- не редактируйте вручную.
"""

from __future__ import annotations

from datetime import date, datetime
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class CheckForActivityAttributes(BaseModel):
    """Параметры обьекта указывающие дату последней возможной записи и количество записей в расписании события
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    possible_visits: int | None = Field(default=None, description="Количество возможных записей в расписании события по выбранному абонементу")
    possible_datetime: str | None = Field(default=None, description="Дата и время последней записи в расписании события")


class CitiesResponseDataTypesDataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор города")
    country_id: float | None = Field(default=None, description="Идентификатор страны")
    title: str | None = Field(default=None, description="Название города")


class ClientsCompanyidResponseDeprecatedDataTypesDataItemCategoriesItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор категории")
    title: str | None = Field(default=None, description="Название категории")
    color: str | None = Field(default=None, description="Цвет категории")


class ClientsCompanyidResponseDeprecatedDataTypesMeta(BaseModel):
    """Метаданные (содержит номер страницы и количество клиентов на странице)
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    page_: int | None = Field(default=None, alias="page")
    total_count: int | None = Field(default=None)


class ClientsFilesClientidReaponseDataTypesDataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор файла")
    client_id: float | None = Field(default=None, description="Идентификатор клиента")
    name: str | None = Field(default=None, description="Имя файла с расширением")
    description: str | None = Field(default=None, description="Описание файла")
    date_create: str | None = Field(default=None, description="Дата загрузки файла в формате ISO8601")
    extension: str | None = Field(default=None, description="Расширение имени файла")
    mime: str | None = Field(default=None, description="MIME-тип файла")
    link: str | None = Field(default=None, description="Ссылка на скачивание файла")
    user_name: str | None = Field(default=None, description="Имя пользователя, загрузившего файл")
    user_avatar: str | None = Field(default=None, description="Аватар пользователя, загрузившего файл")
    size: str | None = Field(default=None, description="Форматированная строка размера файла")
    can_edit: bool | None = Field(default=None, description="Есть ли право изменять и удалять файл? true - право есть, false - права нет")


class ClientsFilesClientidReaponseDataTypesMeta(BaseModel):
    """Метаданные (содержит количество файлов)
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    count_: int | None = Field(default=None, alias="count")


class CommentsCompanyidRessponse200DataTypesDataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор комментария")
    salon_id: float | None = Field(default=None, description="Идентификатор компании")
    type_: float | None = Field(default=None, alias="type", description="1 - комментарий к мастеру, 0 - к салону")
    master_id: float | None = Field(default=None, description="Идентификатор мастера, если type = 1")
    text: str | None = Field(default=None, description="Текст комментария")
    date: str | None = Field(default=None, description="Дата, когда был оставлен комментарий")
    rating: str | None = Field(default=None, description="Оценка (от 1 до 5)")
    user_id: float | None = Field(default=None, description="Идентификатор пользователя, оставившего комментарий")
    user_name: str | None = Field(default=None, description="Имя пользователя, оставившего комментарий")
    user_avatar: str | None = Field(default=None, description="Аватар пользователя, оставившего комментарий")
    record_id: float | None = Field(default=None, description="Идентификатор записи, после которой оставлен отзыв")


class CompaniesDataTypes2DataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор компании")
    title: str | None = Field(default=None, description="Название компании")
    short_descr: str | None = Field(default=None, description="Категория компании")
    logo: str | None = Field(default=None, description="Адрес изображения логотипа компании")
    active: str | None = Field(default=None, description="Активна ли компания (наличие оплаченной лицензии)")
    phone: str | None = Field(default=None, description="Номер телефона компании")
    country_id: float | None = Field(default=None, description="Идентификатор страны, в которой расположена компания")
    schedule: str | None = Field(default=None, description="Расписание работы компании")
    country: str | None = Field(default=None, description="Название страны компании")
    city_id: float | None = Field(default=None, description="Идентификатор города, в котором расположена компания")
    city: str | None = Field(default=None, description="Название города компании")
    timezone_name: str | None = Field(default=None, description="Наименование временной зоны, в которой расположена компания")
    address: str | None = Field(default=None, description="Адрес, по которому расположена компания")
    coordinate_lat: float | None = Field(default=None, description="Широта")
    coordinate_lon: float | None = Field(default=None, description="Долгота")
    phone_confirmation: bool | None = Field(default=None, description="Нужно ли подтверждать номер телефона по смс, при бронировании")
    active_staff_count: float | None = Field(default=None, description="Количество сотрудников, доступных для бронирования")
    next_slot: str | None = Field(default=None, description="Дата и время ближайшего свободного сеанса в компании (ISO8601). Поле будет присутствовать только если передан GET параметр forBooking=1")
    app_ios: str | None = Field(default=None, description="Ссылка на приложение под iOS")
    app_android: str | None = Field(default=None, description="Ссылка на приложение под Andriod")
    currency_short_title: str | None = Field(default=None, description="Сокращенное название валюты")
    group_priority: float | None = Field(default=None, description="Чем больше приоритет, тем выше компания при выводе в списке филиалов сети")


class CompaniesDataTypesDataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор компании")
    title: str | None = Field(default=None, description="Название компании")
    short_descr: str | None = Field(default=None, description="Категория компании")
    logo: str | None = Field(default=None, description="Адрес изображения логотипа компании")
    active: str | None = Field(default=None, description="Активна ли компания (наличие оплаченной лицензии)")
    phone: str | None = Field(default=None, description="Номер телефона компании")
    country_id: float | None = Field(default=None, description="Идентификатор страны, в которой расположена компания")
    schedule: str | None = Field(default=None, description="Расписание работы компании")
    country: str | None = Field(default=None, description="Название страны компании")
    city_id: float | None = Field(default=None, description="Идентификатор города, в котором расположена компания")
    city: str | None = Field(default=None, description="Название города компании")
    timezone_name: str | None = Field(default=None, description="Наименование временной зоны, в которой расположена компания")
    address: str | None = Field(default=None, description="Адрес, по которому расположена компания")
    coordinate_lat: float | None = Field(default=None, description="Широта")
    coordinate_lon: float | None = Field(default=None, description="Долгота")
    phone_confirmation: bool | None = Field(default=None, description="Нужно ли подтверждать номер телефона по смс, при бронировании")
    active_staff_count: float | None = Field(default=None, description="Количество сотрудников, доступных для бронирования")
    next_slot: str | None = Field(default=None, description="Дата и время ближайшего свободного сеанса в компании (ISO8601). Поле будет присутствовать только если передан GET параметр forBooking=1")
    app_ios: str | None = Field(default=None, description="Ссылка на приложение под iOS")
    app_android: str | None = Field(default=None, description="Ссылка на приложение под Andriod")
    currency_short_title: str | None = Field(default=None, description="Сокращенное название валюты")
    group_priority: float | None = Field(default=None, description="Чем больше приоритет, тем выше компания при выводе в списке филиалов сети")


class CompanyAnalyticsLoyaltyProgramsIncomeDataTypesDataCurrency(BaseModel):
    """Валюта
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор валюты")
    iso: str | None = Field(default=None, description="Название в системе ISO")
    name: str | None = Field(default=None, description="Полное название")
    symbol: str | None = Field(default=None, description="Символ валюты")
    is_symbol_after_amount: bool | None = Field(default=None)


class CompanyAnalyticsLoyaltyProgramsIncomeDataTypesDataIncomeStatsByDayItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    date: str | None = Field(default=None, description="Дата")
    new_sum: int | None = Field(default=None, description="Выручка по новым клиентам")
    old_sum: int | None = Field(default=None, description="Выручка по старым клиентам")


class CompanyAnalyticsLoyaltyProgramsIncomeDataTypesDataIncomeStatsNew(BaseModel):
    """Новые клиенты
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    all_sum: int | None = Field(default=None, description="Выручка по новым клиентам")
    returned_sum: int | None = Field(default=None, description="Выручка по вернувшимся клиентам")


class CompanyAnalyticsLoyaltyProgramsIncomeDataTypesDataIncomeStatsOld(BaseModel):
    """Старые клиенты
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    all_sum: int | None = Field(default=None, description="Выручка по старым клиентам")
    returned_sum: int | None = Field(default=None, description="Выручка по вернувшимся клиентам")


class CompanyAnalyticsLoyaltyProgramsIncomeDataTypesDataIncomeStatsTotal(BaseModel):
    """Итоговая сумма
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    all_sum: int | None = Field(default=None, description="Выручка по всем клиентам")
    returned_sum: int | None = Field(default=None, description="Выручка по вернувшимся клиентам")


class CompanyAnalyticsLoyaltyProgramsStaffDataTypesDataItemClientStats(BaseModel):
    """Статистика по клиентам
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    all_count: int | None = Field(default=None, description="Количество всех клиентов")
    lost_count: int | None = Field(default=None, description="Количнство потерянных клиентов")
    returned_count: int | None = Field(default=None, description="Количество вернувшихся клиентов")
    returned_percent: float | None = Field(default=None, description="Процент вернувшихся клиентов")


class CompanyAnalyticsLoyaltyProgramsStaffDataTypesDataItemStaff(BaseModel):
    """Сотрудник
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор сотрудника")
    name: str | None = Field(default=None, description="Имя сотрудника")


class CompanyAnalyticsLoyaltyProgramsStaffDataTypesMeta(BaseModel):
    """Метаданные (содержит количество найденных объектов)
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    count_: int | None = Field(default=None, alias="count")


class CompanyAnalyticsLoyaltyProgramsVisitsDataTypesDataClientStatsNew(BaseModel):
    """Новые клиенты
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    all_count: int | None = Field(default=None, description="Общее количество")
    lost_count: int | None = Field(default=None, description="Потерянные клиенты")
    returned_count: int | None = Field(default=None, description="Вернувшиеся клиенты")
    returned_percent: float | None = Field(default=None, description="Процент вернувшихся клиентов")


class CompanyAnalyticsLoyaltyProgramsVisitsDataTypesDataClientStatsOld(BaseModel):
    """Старые клиенты
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    all_count: int | None = Field(default=None, description="Общее количество")
    lost_count: int | None = Field(default=None, description="Потерянные клиенты")
    returned_count: int | None = Field(default=None, description="Вернувшиеся клиенты")
    returned_percent: float | None = Field(default=None, description="Процент вернувшихся клиентов")


class CompanyAnalyticsLoyaltyProgramsVisitsDataTypesDataClientStatsTotal(BaseModel):
    """Итоговое количество
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    all_count: int | None = Field(default=None, description="Общее количество")
    lost_count: int | None = Field(default=None, description="Потерянные клиенты")
    returned_count: int | None = Field(default=None, description="Вернувшиеся клиенты")
    returned_percent: float | None = Field(default=None, description="Процент вернувшихся клиентов")


class CompanyAnalyticsLoyaltyProgramsVisitsDataTypesDataVisitsStatsByDayItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    date: str | None = Field(default=None, description="Дата")
    new_count: int | None = Field(default=None, description="Количество новых клиентов")
    old_count: int | None = Field(default=None, description="Количество старых клиентов")


class CompanyCompanyIdUsersResponseDataTypesDataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор пользователя")
    name: str | None = Field(default=None, description="Имя пользователя")
    phone: str | None = Field(default=None, description="Телефон пользователя")
    email: str | None = Field(default=None, description="Почтовый адрес пользователя")
    information: str | None = Field(default=None, description="Информация о пользователе")
    is_approved: bool | None = Field(default=None, description="Принял ли пользователь приглашение к управлению филиалом")
    is_non_deletable: bool | None = Field(default=None, description="Является ли пользователь неудаляемым")
    user_role_slug: str | None = Field(default=None, description="Роль пользователя в филиале (доступно только для типа бизнеса \\\"Красота\\\")")


class CompanyCompanyIdUsersResponseDataTypesMeta(BaseModel):
    """Метаданные (содержит количество найденных пользователей)
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    count_: float | None = Field(default=None, alias="count", description="Количество найденных пользователей")


class CompanyCompanyidClientsSearchRequestDataTypesFiltersItemState(BaseModel):
    """Тип фильтра
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    value: list[float] | None = Field(default=None)


class CompanyCompanyidClientsSearchResponseDataTypesDataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    name: str | None = Field(default=None, description="Имя клиента")
    id_: float | None = Field(default=None, alias="id", description="Идентификатор клиента")


class CompanyCompanyidClientsSearchResponseDataTypesMeta(BaseModel):
    """Метаданные (содержит количество найденных клиентов)
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    total_count: int | None = Field(default=None)


class CompanyCompanyidServiceCategoriesResponse200DataTypesDataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор категории")
    salon_service_id: float | None = Field(default=None, description="Идентификатор категории для компании в сети")
    title: str | None = Field(default=None, description="Название категории")
    api_id: str | None = Field(default=None, description="Внешний идентификатор категории")
    weight: float | None = Field(default=None, description="Вес категории (используется для сортировки категорий при отображении)")
    staff: list[float] | None = Field(default=None, description="Список ID сотрудников, оказывающих услугу")


class CompanyCompanyidServiceCategoriesResponse200DataTypesMeta(BaseModel):
    """Метаданные (количество категорий)
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    total_count: float | None = Field(default=None, description="Количество найденных категорий")


class CompanyCompanyidServicesServiceidResponse200DataTypesDataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор услуги")
    salon_service_id: float | None = Field(default=None, description="Идентификатор услуги для компании в сети")
    title: str | None = Field(default=None, description="Название услуги")
    category_id: float | None = Field(default=None, description="Идентификатор категории, в которой состоит услуги")
    price_min: float | None = Field(default=None, description="Минимальная цена на услугу")
    price_max: float | None = Field(default=None, description="Максимальная цена на услугу")
    discount: str | None = Field(default=None, description="Скидка")
    comment: str | None = Field(default=None, description="Комментарий к услуге")
    weight: float | None = Field(default=None, description="Вес услуги (используется для сортировки категорий при отображении)")
    active: float | None = Field(default=None, description="1 - доступна для онлайн записи, 0 - не доступна")
    api_id: str | None = Field(default=None, description="Внешний идентификатор услуги")
    staff: list[dict[str, Any]] | None = Field(default=None, description="Список сотрудников, оказывающих услугу и длительность сеанса")


class CompanyCompanyidServicesServiceidResponse200DataTypesMeta(BaseModel):
    """Метаданные (содержит количество найденных услуг)
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    total_count: int | None = Field(default=None)


class CompanyCompanyidStaffStaffidResponseDataTypesDataItemPosition(BaseModel):
    """Должность сотрудника
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор должности")
    title: str | None = Field(default=None, description="Название должности")


class CompanyCompanyidStaffStaffidResponseDataTypesDeprecatedDataItemImageGroupImagesNorm(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: str | None = Field(default=None, alias="id")
    path: str | None = Field(default=None)
    width: str | None = Field(default=None)
    height: str | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    image_group_id: int | None = Field(default=None)
    version: str | None = Field(default=None)


class CompanyCompanyidStaffStaffidResponseDataTypesDeprecatedDataItemImageGroupImagesOrigin(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: str | None = Field(default=None, alias="id")
    path: str | None = Field(default=None)
    width: str | None = Field(default=None)
    height: str | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    image_group_id: int | None = Field(default=None)
    version: str | None = Field(default=None)


class CompanyCompanyidStaffStaffidResponseDataTypesDeprecatedDataItemImageGroupImagesSm(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: str | None = Field(default=None, alias="id")
    path: str | None = Field(default=None)
    width: str | None = Field(default=None)
    height: str | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    image_group_id: int | None = Field(default=None)
    version: str | None = Field(default=None)


class CompanyCompanyidStaffStaffidResponseDataTypesDeprecatedDataItemPosition(BaseModel):
    """Должность сотрудника
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор должности")
    title: str | None = Field(default=None, description="Название должности")


class CompanyCompanyidStaffStaffidResponseDataTypesMeta(BaseModel):
    """Метаданные (содержат количество найденных сотрудников)
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    total_count: int | None = Field(default=None)


class CompanyCreateResponseDataTypesData(BaseModel):
    """Объект данных
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор компании")
    title: str | None = Field(default=None, description="Название компании")
    short_descr: str | None = Field(default=None, description="Категория компании")
    logo: str | None = Field(default=None, description="Путь к изображению логотипа компании")
    active: str | None = Field(default=None, description="Активна ли компания (наличие оплаченной лицензии)")
    phone: str | None = Field(default=None, description="Номер телефона компании")
    country_id: float | None = Field(default=None, description="Идентификатор страны, в которой расположена компания")
    schedule: str | None = Field(default=None, description="Расписание работы компании")
    country: str | None = Field(default=None, description="Название страны, в которой расположена компания")
    city_id: float | None = Field(default=None, description="Идентификатор города, в котором расположена компания")
    city: str | None = Field(default=None, description="Название города, в котором расположена компания")
    timezone_name: str | None = Field(default=None, description="Timezone компании")
    address: str | None = Field(default=None, description="Адрес, по которому расположена компания")
    coordinate_lat: float | None = Field(default=None, description="Широта")
    coordinate_lon: float | None = Field(default=None, description="Долгота")
    phone_confirmation: bool | None = Field(default=None, description="Нужно ли подтверждать номер телефона по смс, при бронировании")
    active_staff_count: float | None = Field(default=None, description="Количество сотрудников, доступных для бронирования")
    app_ios: str | None = Field(default=None, description="Ссылка на приложение под iOS")
    app_android: str | None = Field(default=None, description="Ссылка на приложение под Android")
    currency_short_title: str | None = Field(default=None, description="Сокращенное название валюты")


class CompanyGetResponseDataTypesDataBookformsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор виджета")
    title: str | None = Field(default=None, description="Наименование виджета")
    is_default: float | None = Field(default=None, description="Признак виджета по-умолчанию")
    url: str | None = Field(default=None, description="Ссылка на виджет")


class CompanyGetResponseDataTypesDataGroupsId1(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор сети _ID-1_")
    title: str | None = Field(default=None, description="Наименование сети _ID-1_")


class CompanyGetResponseDataTypesDataGroupsId2(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор сети _ID-2_")
    title: str | None = Field(default=None, description="Наименование сети _ID-2_")


class CompanyGetResponseDataTypesDataMainGroupItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор сети")
    title: str | None = Field(default=None, description="Наименование сети")


class CompanyGetResponseDataTypesDataSocial(BaseModel):
    """Социальные сети компании
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    telegram: str | None = Field(default=None, description="Telegram")
    instagram: str | None = Field(default=None, description="Instagram")
    vk: str | None = Field(default=None, description="Вконтакте")
    facebook: str | None = Field(default=None, description="Facebook")
    viber: str | None = Field(default=None, description="Viber")
    whatsapp: str | None = Field(default=None, description="WhatsApp")


class CompanyLoyaltyProgramsSearchDataTypesDataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор акции")
    title: str | None = Field(default=None, description="Название акции")
    type_: Literal["discount_static", "discount_accumulative_visits", "discount_accumulative_sold", "discount_accumulative_paid", "cashback_static_sold", "cashback_static_paid", "cashback_accumulative_paid", "cashback_accumulative_sold", "cashback_accumulative_paid_visits", "cashback_accumulative_sold_visits", "cashback_sold_visits", "cashback_paid_visits", "package_discount"] | None = Field(default=None, alias="type", description="Тип акции")
    loyalty_type_id: int | None = Field(default=None, description="Идентификатор типа акции")
    item_type_id: int | None = Field(default=None, description="Идентификатор типа применения скидки")
    service_item_type: Literal["any_allowed", "not_allowed", "custom_allowed"] | None = Field(default=None, description="Тип применения к услугам")
    good_item_type: Literal["any_allowed", "not_allowed", "custom_allowed"] | None = Field(default=None, description="Тип применения к товарам")
    value_unit_id: int | None = Field(default=None, description="Идентификатор единицы измерения бонуса или скидки")
    value_unit: Literal["percent", "amount"] | None = Field(default=None, description="Единица измерения бонуса или скидки (процент, фиксированная сумма)")
    group_id: int | None = Field(default=None, description="Идентификатор сети")
    usage_limit: int | None = Field(default=None, description="Ограничение по количеству применений (только для кэшбека)")
    visit_multiplicity: int | None = Field(default=None, description="Кратность применения по визитам (только для кэшбека)")
    sold_items_multiplicity: int | None = Field(default=None, description="Сколько услуг нужно оплатить, чтобы получить скидку на акционные услуги (только для типа акции \"Скидка по условию\")")
    current_package_progress: int | None = Field(default=None, description="Текущее количество применений акции")
    allowed_usages_amount: int | None = Field(default=None, description="Ограничение количества допустимых применений")
    expiration_timeout: int | None = Field(default=None, description="Срок сгорания бонусов или скидки")
    expiration_timeout_unit: Literal["day", "week", "month", "year"] | None = Field(default=None, description="Единица измерения срока сгорания бонусов или скидки")
    expiration_notification_timeout: int | None = Field(default=None, description="За сколько дней до наступления срока сгорания бонуса или скидки необходимо отправить клиенту уведомление")
    params_source_type: Literal["loyalty_card", "active_companies", "chain"] | None = Field(default=None, description="Откуда брать историю клиента для расчета размера бонуса или скидки (для накпоительных акций или скидки по условию)")
    history_start_date: str | None = Field(default=None, description="С какой даты учитывать историю клиента для расчета размера бонуса или скидки (для накопительных акций или скидки по условию)")
    on_changed_notification_template_id: int | None = Field(default=None, description="Идентификатор шаблона уведомления при изменении бонуса или скидки")
    on_expiration_notification_template_id: int | None = Field(default=None, description="Идентификатор шаблона уведомления при сгорании бонуса или скидки")
    first_transaction_date: str | None = Field(default=None, description="Дата первой транзакции по акции")


class CompanyLoyaltyProgramsSearchDataTypesMeta(BaseModel):
    """Метаданные (содержит количество найденных объектов)
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    count_: int | None = Field(default=None, alias="count", description="Количество найденных объектов")


class CompanyPutRequestDataTypesSocial(BaseModel):
    """Социальные сети компании
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    telegram: str | None = Field(default=None, description="Telegram")
    instagram: str | None = Field(default=None, description="Instagram")
    vk: str | None = Field(default=None, description="Вконтакте")
    facebook: str | None = Field(default=None, description="Facebook")
    viber: str | None = Field(default=None, description="Viber")
    whatsapp: str | None = Field(default=None, description="WhatsApp")


class CompanyPutResponseDataTypesSocial(BaseModel):
    """Социальные сети компании
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    telegram: str | None = Field(default=None, description="Telegram")
    instagram: str | None = Field(default=None, description="Instagram")
    vk: str | None = Field(default=None, description="Вконтакте")
    facebook: str | None = Field(default=None, description="Facebook")
    viber: str | None = Field(default=None, description="Viber")
    whatsapp: str | None = Field(default=None, description="WhatsApp")


class CompanySalonIdSaleDocumentidResponseDataTypesDataKkmStateTransactionsItemCashier(BaseModel):
    """Кассир
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор сотрудника")
    name: str | None = Field(default=None, description="Имя сотрудника")


class CompanySalonIdSaleDocumentidResponseDataTypesDataKkmStateTransactionsItemDocument(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор документа")
    type_: int | None = Field(default=None, alias="type", description="Тип документа")
    type_title: str | None = Field(default=None, description="Название типа документа")


class CompanySalonIdSaleDocumentidResponseDataTypesDataKkmStateTransactionsItemStatus(BaseModel):
    """Статус печати чека
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор статуса")
    title: str | None = Field(default=None, description="Название статуса")


class CompanySalonIdSaleDocumentidResponseDataTypesDataKkmStateTransactionsItemType(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id")
    title: str | None = Field(default=None)


class CompanySalonIdSaleDocumentidResponseDataTypesDataPaymentMethodsItemAccount(BaseModel):
    """Касса
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор кассы")
    title: str | None = Field(default=None, description="Название кассы")
    is_cash: bool | None = Field(default=None, description="Является ли касса наличной")


class CompanySalonIdSaleDocumentidResponseDataTypesDataStateItemsItem(BaseModel):
    """Продаваемая единица
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор продаваемой единицы")
    type_: str | None = Field(default=None, alias="type", description="Тип (service/good)")
    title: str | None = Field(default=None, description="Название")
    amount: float | None = Field(default=None, description="Количество")
    default_cost_per_unit: float | None = Field(default=None, description="Цена за единицу")
    default_cost_total: float | None = Field(default=None, description="Общая цена по умолчанию")
    client_discount_percent: float | None = Field(default=None, description="Процент скидки")
    cost_to_pay_total: float | None = Field(default=None, description="Цена к оплате")


class CompanySalonIdSaleDocumentidResponseDataTypesDataStateLoyaltyTransactionsItemChain(BaseModel):
    """Сеть филиалов
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор сети филиалов")
    title: str | None = Field(default=None, description="Название сети филиалов")


class CompanySalonIdSaleDocumentidResponseDataTypesDataStateLoyaltyTransactionsItemDepositType(BaseModel):
    """Тип депозита
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор типа депозита")
    title: str | None = Field(default=None, description="Название депозита")


class CompanySalonIdSaleDocumentidResponseDataTypesDataStateLoyaltyTransactionsItemType(BaseModel):
    """Тип транзакции
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор типа транзакции")
    title: str | None = Field(default=None, description="Название типа транзакции")


class CompanySalonIdSaleDocumentidResponseDataTypesDataStatePaymentTransactionsItemAccount(BaseModel):
    """Касса
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор кассы")
    title: str | None = Field(default=None, description="Название кассы")
    is_cash: bool | None = Field(default=None, description="Является ли оплата наличной")
    is_default: bool | None = Field(default=None, description="Является ли кассой по умолчанию")


class CompanySalonIdSaleDocumentidResponseDataTypesDataStatePaymentTransactionsItemExpense(BaseModel):
    """Статья плаитежа
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор статьи платежа")
    title: str | None = Field(default=None, description="Название статьи платежа")


class CompanySalonidSaleDocumentidPaymentAbonementsPaymentMethod(BaseModel):
    """Метод оплаты
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    slug: str | None = Field(default=None, description="Тип метода оплаты")
    loyalty_abonement_id: int | None = Field(default=None, description="Идентификатор абонемента")


class CompanySalonidSaleDocumentidPaymentAccountPaymentMethod(BaseModel):
    """Метод оплаты
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    slug: str | None = Field(default=None, description="Тип метода оплаты")
    account_id: int | None = Field(default=None, description="Идентификатор кассы")


class CompanySalonidSaleDocumentidPaymentCertificatePaymentMethod(BaseModel):
    """Метод оплаты
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    slug: str | None = Field(default=None, description="Тип метода оплаты")
    loyalty_certificate_id: int | None = Field(default=None, description="Идентификатор сертификата")

__all__ = [
    "CheckForActivityAttributes",
    "CitiesResponseDataTypesDataItem",
    "ClientsCompanyidResponseDeprecatedDataTypesDataItemCategoriesItem",
    "ClientsCompanyidResponseDeprecatedDataTypesMeta",
    "ClientsFilesClientidReaponseDataTypesDataItem",
    "ClientsFilesClientidReaponseDataTypesMeta",
    "CommentsCompanyidRessponse200DataTypesDataItem",
    "CompaniesDataTypes2DataItem",
    "CompaniesDataTypesDataItem",
    "CompanyAnalyticsLoyaltyProgramsIncomeDataTypesDataCurrency",
    "CompanyAnalyticsLoyaltyProgramsIncomeDataTypesDataIncomeStatsByDayItem",
    "CompanyAnalyticsLoyaltyProgramsIncomeDataTypesDataIncomeStatsNew",
    "CompanyAnalyticsLoyaltyProgramsIncomeDataTypesDataIncomeStatsOld",
    "CompanyAnalyticsLoyaltyProgramsIncomeDataTypesDataIncomeStatsTotal",
    "CompanyAnalyticsLoyaltyProgramsStaffDataTypesDataItemClientStats",
    "CompanyAnalyticsLoyaltyProgramsStaffDataTypesDataItemStaff",
    "CompanyAnalyticsLoyaltyProgramsStaffDataTypesMeta",
    "CompanyAnalyticsLoyaltyProgramsVisitsDataTypesDataClientStatsNew",
    "CompanyAnalyticsLoyaltyProgramsVisitsDataTypesDataClientStatsOld",
    "CompanyAnalyticsLoyaltyProgramsVisitsDataTypesDataClientStatsTotal",
    "CompanyAnalyticsLoyaltyProgramsVisitsDataTypesDataVisitsStatsByDayItem",
    "CompanyCompanyIdUsersResponseDataTypesDataItem",
    "CompanyCompanyIdUsersResponseDataTypesMeta",
    "CompanyCompanyidClientsSearchRequestDataTypesFiltersItemState",
    "CompanyCompanyidClientsSearchResponseDataTypesDataItem",
    "CompanyCompanyidClientsSearchResponseDataTypesMeta",
    "CompanyCompanyidServiceCategoriesResponse200DataTypesDataItem",
    "CompanyCompanyidServiceCategoriesResponse200DataTypesMeta",
    "CompanyCompanyidServicesServiceidResponse200DataTypesDataItem",
    "CompanyCompanyidServicesServiceidResponse200DataTypesMeta",
    "CompanyCompanyidStaffStaffidResponseDataTypesDataItemPosition",
    "CompanyCompanyidStaffStaffidResponseDataTypesDeprecatedDataItemImageGroupImagesNorm",
    "CompanyCompanyidStaffStaffidResponseDataTypesDeprecatedDataItemImageGroupImagesOrigin",
    "CompanyCompanyidStaffStaffidResponseDataTypesDeprecatedDataItemImageGroupImagesSm",
    "CompanyCompanyidStaffStaffidResponseDataTypesDeprecatedDataItemPosition",
    "CompanyCompanyidStaffStaffidResponseDataTypesMeta",
    "CompanyCreateResponseDataTypesData",
    "CompanyGetResponseDataTypesDataBookformsItem",
    "CompanyGetResponseDataTypesDataGroupsId1",
    "CompanyGetResponseDataTypesDataGroupsId2",
    "CompanyGetResponseDataTypesDataMainGroupItem",
    "CompanyGetResponseDataTypesDataSocial",
    "CompanyLoyaltyProgramsSearchDataTypesDataItem",
    "CompanyLoyaltyProgramsSearchDataTypesMeta",
    "CompanyPutRequestDataTypesSocial",
    "CompanyPutResponseDataTypesSocial",
    "CompanySalonIdSaleDocumentidResponseDataTypesDataKkmStateTransactionsItemCashier",
    "CompanySalonIdSaleDocumentidResponseDataTypesDataKkmStateTransactionsItemDocument",
    "CompanySalonIdSaleDocumentidResponseDataTypesDataKkmStateTransactionsItemStatus",
    "CompanySalonIdSaleDocumentidResponseDataTypesDataKkmStateTransactionsItemType",
    "CompanySalonIdSaleDocumentidResponseDataTypesDataPaymentMethodsItemAccount",
    "CompanySalonIdSaleDocumentidResponseDataTypesDataStateItemsItem",
    "CompanySalonIdSaleDocumentidResponseDataTypesDataStateLoyaltyTransactionsItemChain",
    "CompanySalonIdSaleDocumentidResponseDataTypesDataStateLoyaltyTransactionsItemDepositType",
    "CompanySalonIdSaleDocumentidResponseDataTypesDataStateLoyaltyTransactionsItemType",
    "CompanySalonIdSaleDocumentidResponseDataTypesDataStatePaymentTransactionsItemAccount",
    "CompanySalonIdSaleDocumentidResponseDataTypesDataStatePaymentTransactionsItemExpense",
    "CompanySalonidSaleDocumentidPaymentAbonementsPaymentMethod",
    "CompanySalonidSaleDocumentidPaymentAccountPaymentMethod",
    "CompanySalonidSaleDocumentidPaymentCertificatePaymentMethod"
]
