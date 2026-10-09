"""Модели YCLIENTS API (b: B).

Сгенерировано scripts/generate.py -- не редактируйте вручную.
"""

from __future__ import annotations

from datetime import date, datetime
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class BookCheckCompanyidResponse201DataTypesMeta(BaseModel):
    """Метаданные
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    message: str | None = Field(default=None)


class BookCodeCompanyidDataTypeResponseMeta(BaseModel):
    """Метаданные
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    message: str | None = Field(default=None)


class BookDatesCompanyidDataTypesDataBookingDays(BaseModel):
    """Массив дней, которые доступны для бронирования на указанные услуги
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    param_9: list[str] | None = Field(default=None, alias="9")
    param_10: list[str] | None = Field(default=None, alias="10")


class BookDatesCompanyidDataTypesDataWorkingDays(BaseModel):
    """Рабочие дни сотрудника/организации
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    param_9: list[str] | None = Field(default=None, alias="9")
    param_10: list[str] | None = Field(default=None, alias="10")


class BookRecordCompanyidRecordResponseDataTypesDataCompany(BaseModel):
    """Параметры компании
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="ID компании")
    title: str | None = Field(default=None, description="Название организации")
    country_id: float | None = Field(default=None, description="ID страны")
    country: str | None = Field(default=None, description="Название страны, в которой расположена организация")
    city_id: float | None = Field(default=None, description="ID города")
    city: str | None = Field(default=None, description="Название города, в котором расположена организация")
    phone: str | None = Field(default=None, description="Телефон компании")
    timezone: str | None = Field(default=None, description="Временная зона компании")
    address: str | None = Field(default=None, description="Адрес компании")
    coordinate_lat: float | None = Field(default=None, description="Широта")
    coordinate_lon: float | None = Field(default=None, description="Долгота")


class BookRecordCompanyidRecordResponseDataTypesDataServicesItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id")
    title: str | None = Field(default=None)
    cost: int | None = Field(default=None)
    discount: int | None = Field(default=None)


class BookRecordCompanyidRecordResponseDataTypesDataStaff(BaseModel):
    """Параметры сотрудника
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="ID сотрудника")
    name: str | None = Field(default=None, description="Имя сотрудника")
    spec: str | None = Field(default=None, description="Специализация сотрудника")
    show_rating: bool | None = Field(default=None, description="Показывать ли рейтинг сотрудника")
    rating: float | None = Field(default=None, description="Рейтинг сотрудника (от 0 до 5)")
    votes_count: float | None = Field(default=None, description="Кол-во голосов, поставивших сотруднику оценку")
    avatar: str | None = Field(default=None, description="Путь к аватарке сотрудника")
    comments_count: float | None = Field(default=None, description="Кол-во комментариев сотруднику")


class BookRecordCompanyidRecordidRecordhashResponseDataTypesCompany(BaseModel):
    """Параметры компании
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="ID копаниии")
    title: str | None = Field(default=None, description="Название компании")
    country_id: float | None = Field(default=None, description="ID страны")
    country: str | None = Field(default=None, description="Название страны, в которой расположены организация")
    city_id: float | None = Field(default=None, description="ID города")
    city: str | None = Field(default=None, description="Название города, в котором расположена организация")
    phone: str | None = Field(default=None, description="Телефон компании")
    phones: list[str] | None = Field(default=None)
    timezone: str | None = Field(default=None, description="Временная зона компании")
    address: str | None = Field(default=None, description="Адрес компании")
    coordinate_lat: float | None = Field(default=None, description="Широта")
    coordinate_lon: float | None = Field(default=None, description="Долгота")
    allow_delete_record: bool | None = Field(default=None)
    allow_change_record: bool | None = Field(default=None)
    site: str | None = Field(default=None)
    currency_short_title: str | None = Field(default=None)
    allow_change_record_delay_step: int | None = Field(default=None)
    allow_delete_record_delay_step: int | None = Field(default=None)


class BookRecordCompanyidRecordidRecordhashResponseDataTypesServicesItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор услуги")
    title: str | None = Field(default=None, description="Название услуги")
    amount: int | None = Field(default=None, description="Количество заказанных услуг")
    seance_length: int | None = Field(default=None, description="Длительность оказания услуги в секундах (только если задан фильтр по сотруднику)")


class BookRecordCompanyidRecordidRecordhashResponseDataTypesStaffPosition(BaseModel):
    """Должность сотрудника
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="ID должности")
    title: str | None = Field(default=None, description="Название должности")


class BookRecordCompanyidRequestDataTypesAppointmentsItemCustomFields(BaseModel):
    """Дополнительные поля записи
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    my_custom_field: float | None = Field(default=None)
    some_another_field: list[float] | None = Field(default=None)


class BookRecordCompanyidResponseDataTypesDataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="ID записи переданный в запросе в appontments")
    record_id: float | None = Field(default=None, description="ID записи в системе yclients. Используется для удаления записи")
    record_hash: str | None = Field(default=None, description="HASH записи в системе yclients. Используется для удаления записи неавторизованным пользователем сразу после бронирования")


class BookServicesCompanyidDataTypesDataCategoryItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="ID категории")
    title: str | None = Field(default=None, description="Название категории услуг")
    sex: float | None = Field(default=None, description="Пол, для которого оказывается услуга")
    api_id: str | None = Field(default=None, description="Внешний идентификатор категории")
    weight: float | None = Field(default=None, description="Вес категории услуг. При выводе услуги сортируются по весу, сначала более тяжелые")


class BookServicesCompanyidDataTypesDataServicesItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="ID услуги")
    title: str | None = Field(default=None, description="Название услуги")
    category_id: float | None = Field(default=None, description="ID категории, которой принадлежит услуга")
    price_min: float | None = Field(default=None, description="Минимальная стоимость услуги")
    price_max: float | None = Field(default=None, description="Максимальная стоимость услуги")
    discount: float | None = Field(default=None, description="Скидка по услуге")
    comment: str | None = Field(default=None, description="Комментарий к услуге")
    weight: float | None = Field(default=None, description="Вес услуги. При выводе услуги сортируются по весу, сначала более тяжелые")
    active: float | None = Field(default=None, description="Активная ли услуга")
    sex: float | None = Field(default=None, description="Пол, для которого оказывается услуга")
    image: str | None = Field(default=None, description="Изображение услуги")
    prepaid: str | None = Field(default=None, description="Статус онлайн-оплат")
    seance_length: float | None = Field(default=None, description="Длительность оказания услуги в секундах (только если задан фильтр по сотруднику)")


class BookStaffCompanyidDataTypesDataItemPosition(BaseModel):
    """Должность сотрудника
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="ID должности")
    title: str | None = Field(default=None, description="Название должности")


class BookStaffSeancesCompanyidStaffidDataTypesDataSeancesItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    time: str | None = Field(default=None, description="Время сеанса")
    seance_length: float | None = Field(default=None, description="Длительность сеанса")
    datetime: str | None = Field(default=None, description="10-01T17:00:00Z\\' (required, string) - Дата и время сеанса")


class BookTimesCompanyidDataTypesDataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    time: str | None = Field(default=None, description="Время сеанса")
    seance_length: float | None = Field(default=None, description="Длительность сеанса")
    datetime: str | None = Field(default=None, description="10-01T17:00:00Z\\' (required, string) - Дата и время сеанса")


class BookformIdInfoDataTypesDataLangsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id")
    code: str | None = Field(default=None)
    title: str | None = Field(default=None)


class BookformIdInfoDataTypesDataStepsItem(BaseModel):
    """Настройки дизайна формы бронирования
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    step: str | None = Field(default=None, description="Шаг выбора услуги\\мастера\\даты")
    title: str | None = Field(default=None, description="Название шага для вывода в интерфейсе")
    num: float | None = Field(default=None, description="Каким по счету должен выводиться данный шаг (начиная с 1)")
    hidden: bool | None = Field(default=None, description="Скрыть данный шаг при бронировании или нет")


class BookformIdInfoDataTypesDataStyle(BaseModel):
    """Настройки дизайна формы бронирования
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    show_header: bool | None = Field(default=None, description="Выводить шапку и меню или нет")
    logo: str | None = Field(default=None, description="Путь до картинки логотипа")
    header_background: str | None = Field(default=None, description="Путь до картинки фона подзаголовка")
    menu_background: str | None = Field(default=None, description="Путь до картинки фона меню")
    main_color: str | None = Field(default=None, description="Главный цвет формы (все цвета из списка: red, pink, purple, deep-purple, indigo, blue, light-blue, cyan, teal, green, light-green, lime, yellow, amber, orange, deep-orange, brown, grey, blue-grey, ...")
    secondary_color: str | None = Field(default=None, description="Второстепенный цвет формы (полупрозрачный cover подзаголовка)")
    buttons_color: str | None = Field(default=None, description="Цвет кнопок")


class BookingUserUpdatePasswordResponseDataTypesData(BaseModel):
    """Объект с данными
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    user_token: str | None = Field(default=None, description="Новый User-token пользователя")


class BookCheckCompanyidRequestDataTypes(BaseModel):
    """Проверить параметры записи
    Схема спеки: Root Type for book_check_companyid_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    appointments: list[dict[str, Any]] = Field(description="Параметры записи (услуги, специалисты...)")


class BookCheckCompanyidResponse201DataTypes(BaseModel):
    """Проверить параметры записи
    Схема спеки: Root Type for book_check_companyid_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    meta: BookCheckCompanyidResponse201DataTypesMeta | None = Field(default=None)


class BookCodeCompanyidDataTypeResponse(BaseModel):
    """Схема спеки: Root Type for book_code_companyid_resp
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    meta: BookCodeCompanyidDataTypeResponseMeta | None = Field(default=None)


class BookCodeCompanyidDataTypesRequest(BaseModel):
    """Отправить СМС код подтверждения номера телефона
    Схема спеки: Root Type for book_code_companyid_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    phone: str = Field(description="Номер телефона клиента")
    fulname: str | None = Field(default=None, description="Имя клиента")


class BookRecordCompanyidRecordRequestDataTypes(BaseModel):
    """Перенести запись на сеанс
    Схема спеки: Root Type for book_record_companyid_record_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    datetime: str | None = Field(default=None, description="Дата и время на которое мы хотим перенести запись")
    comment: str | None = Field(default=None, description="Комментарий к записи")


class BookRecordCompanyidResponseDataTypes(BaseModel):
    """Перенести запись на сеанс
    Схема спеки: Root Type for book_record_companyid_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: list[BookRecordCompanyidResponseDataTypesDataItem] | None = Field(default=None, alias="data", description="Данные (массив объектов)")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")


class BookTimesCompanyidDataTypes(BaseModel):
    """Получить список сеансов доступных для бронирования
    Схема спеки: Root Type for book_times_company_id_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: list[BookTimesCompanyidDataTypesDataItem] | None = Field(default=None, alias="data", description="Массив объектов с данными")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")


class BookformCreateRequest2(BaseModel):
    """Запрос для создания букформы
    Схема спеки: Root Type BookformCreateRequest
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    title: str = Field(description="Название букформы")
    description: str | None = Field(default=None, description="Описание букформы")
    is_default: bool | None = Field(default=None, description="Флаг дефолтной букформы")
    without_menu: bool | None = Field(default=None, description="Флаг пошагового режима")
    service_step_default: float | None = Field(default=None, description="ID услуги")
    service_step_hide: bool | None = Field(default=None, description="Флаг скрытия услуги")
    master_step_default: float | None = Field(default=None, description="ID мастера")
    master_step_hide: bool | None = Field(default=None, description="Флаг скрытия мастера")
    service_step_num: float | None = Field(default=None, description="Порядковый номер шага услуги")
    master_step_num: float | None = Field(default=None, description="Порядковый номер шага мастера")
    datetime_step_num: float | None = Field(default=None, description="Порядковый номер шага даты и времени")
    show_button: bool | None = Field(default=None, description="Флаг включения видимости кнопки")
    button_position: Literal["bottom right", "bottom left", "top right", "top left "] | None = Field(default=None, description="Расположение кнопки на странице")
    form_position: Literal["right", "left"] | None = Field(default=None, description="Расположение панели на странице")
    button_color: str | None = Field(default=None, description="Цвет кнопки")
    button_animation: bool | None = Field(default=None, description="Флаг включения анимации кнопки")


class BookformSettingsResponse2(BaseModel):
    """Настройки букформы
    Схема спеки: Root Type BookformSettingsResponse
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float = Field(alias="id", description="ID букформы")
    title: str = Field(description="Название букформы")
    description: str = Field(description="Описание букформы")
    is_default: bool = Field(description="Флаг дефолтной букформы")
    without_menu: bool = Field(description="Флаг пошагового режима")
    service_step_default: float = Field(description="ID услуги")
    service_step_hide: bool = Field(description="Флаг скрытия услуги")
    master_step_default: float = Field(description="ID мастера")
    master_step_hide: bool = Field(description="Флаг скрытия мастера")
    service_step_num: float = Field(description="Порядковый номер услуги")
    master_step_num: float = Field(description="Порядковый номер мастера")
    datetime_step_num: float = Field(description="Порядковый номер даты и времени")
    show_button: bool = Field(description="Шаг включения видимости кнопки")
    button_position: str = Field(description="Расположение кнопки на странице")
    form_position: str = Field(description="Расположение панели на странице")
    button_color: str = Field(description="Цвет кнопки")
    button_animation: bool = Field(description="Флаг включения анимации кнопки")
    html_code: str = Field(description="Код для вставки кнопки на сайт")
    ab_test_enabled: bool = Field(description="Флаг включения аб-теста букформы")


class BookformUpdateRequest2(BaseModel):
    """Запрос для изменения букформы
    Схема спеки: Root Type for BookformUpdateRequest
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    title: str = Field(description="Название букформы")
    description: str = Field(description="Описание букформы")
    is_default: bool = Field(description="Флаг дефолтной букформы")
    without_menu: bool = Field(description="Флаг пошагового режима")
    service_step_default: float = Field(description="ID услуги")
    service_step_hide: bool = Field(description="Флаг скрытия услуги")
    master_step_default: float = Field(description="ID мастера")
    master_step_hide: bool = Field(description="Флаг скрытия мастера")
    service_step_num: float = Field(description="Порядковый номер шага услуги")
    master_step_num: float = Field(description="Порядковый номер шага мастера")
    datetime_step_num: float = Field(description="Порядковый номер шага даты и времени")
    show_button: bool = Field(description="Шаг включения видимости кнопки")
    button_position: Literal["bottom right", "bottom left", "top right", "top left"] = Field(description="Расположение кнопки на странице")
    form_position: Literal["right", "left"] = Field(description="Расположение панели на странице")
    button_color: str = Field(description="Цвет кнопки")
    button_animation: bool = Field(description="Флаг включения анимации кнопки")


class BookingAuthResponse(BaseModel):
    """Авторизация пользователя
    Схема спеки: Root Type for auth_response
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор пользователя")
    user_token: str | None = Field(default=None, description="User_token пользователя")
    name: str | None = Field(default=None, description="Имя пользователя")
    phone: str | None = Field(default=None, description="Телефон пользователя")
    login: str | None = Field(default=None, description="Логин пользователя")
    email: str | None = Field(default=None, description="Почтовый адрес пользователя")
    avatar: str | None = Field(default=None, description="Путь к файлу аватарки пользователя")


class BookingAuthResponse2(BaseModel):
    """Авторизация пользователя
    Схема спеки: Root Type for auth_response
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор пользователя")
    user_token: str | None = Field(default=None, description="User_token пользователя")
    name: str | None = Field(default=None, description="Имя пользователя")
    phone: str | None = Field(default=None, description="Телефон пользователя")
    login: str | None = Field(default=None, description="Логин пользователя")
    email: str | None = Field(default=None, description="Почтовый адрес пользователя")
    avatar: str | None = Field(default=None, description="Путь к файлу аватарки пользователя")


class BookingAuthWithCode(BaseModel):
    """Авторизация пользователя
    Схема спеки: Авторизация по коду подтверждения
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    phone: str = Field(description="Номер телефона")
    code: str = Field(description="Код подтверждения")


class BookingUserGetDataResponseDataTypes(BaseModel):
    """Получение данных пользователя онлайн-записи
    Схема спеки: Root Type for booking_user_get_data_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    param_0: str | None = Field(default=None, alias="0", description="Токен пользователя")
    id_: int | None = Field(default=None, alias="id", description="Идентификатор пользователя")
    user_token: str | None = Field(default=None, description="Токен пользователя")
    name: str | None = Field(default=None, description="Имя пользователя")
    phone: str | None = Field(default=None, description="Телефон пользователя")
    login: str | None = Field(default=None, description="Логин пользователя")
    email: str | None = Field(default=None, description="Почта пользователя")
    avatar: str | None = Field(default=None, description="Аватар пользователя")


class BookingUserUpdateInfoRequestDataTypes(BaseModel):
    """Обновление данных пользователя онлайн-записи
    Схема спеки: Root Type for booking_user_update_info_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    name: str | None = Field(default=None, description="Имя")
    email: str | None = Field(default=None, description="Почта")
    phone: str | None = Field(default=None, description="Номер телефона")
    confirmation_code: str | None = Field(default=None, description="Код подтверждения из смс (при смене номера телефона)")


class BookingUserUpdatePasswordRequestDataTypes(BaseModel):
    """Обновление пароля пользователя онлайн-записи
    Схема спеки: Root Type for booking_user_update_password_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    old_password: str | None = Field(default=None, description="Текущий пароль")
    new_password: str | None = Field(default=None, description="Новый пароль")


class BookingUserUpdatePasswordResponseDataTypes(BaseModel):
    """Обновление пароля пользователя онлайн-записи
    Схема спеки: Root Type for booking_user_update_password_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: BookingUserUpdatePasswordResponseDataTypesData | None = Field(default=None, alias="data")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")


class BookDatesCompanyidDataTypesData(BaseModel):
    """Данные (объект)
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    booking_days: BookDatesCompanyidDataTypesDataBookingDays | None = Field(default=None)
    booking_dates: list[str] | None = Field(default=None, description="Массив дат, когда есть свободные сеансы на услугу к выбранному сотруднику/организации")
    working_days: BookDatesCompanyidDataTypesDataWorkingDays | None = Field(default=None)
    working_dates: list[str] | None = Field(default=None, description="Массив дат, когда работает сотрудник/организация")


class BookRecordCompanyidRecordResponseDataTypesData(BaseModel):
    """Данные (объект)
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="ID записи")
    services: list[BookRecordCompanyidRecordResponseDataTypesDataServicesItem] | None = Field(default=None, description="Список ID услуг")
    company: BookRecordCompanyidRecordResponseDataTypesDataCompany | None = Field(default=None)
    staff: BookRecordCompanyidRecordResponseDataTypesDataStaff | None = Field(default=None)
    date: str | None = Field(default=None, description="\"2025-01-01 12:00:00\" (required, string) - Дата сеанса")
    create_date: str | None = Field(default=None, description="\"2025-01-01 12:00:00\" (required, string) - Дата создания записи")
    comment: str | None = Field(default=None, description="Комментарий к записи")
    deleted: bool | None = Field(default=None, description="Удалена ли запись (true если удалена)")
    length: float | None = Field(default=None, description="Длительность сеанса")
    notify_by_sms: float | None = Field(default=None, description="За сколько часов до визита следует выслать смс напоминание клиенту (0 - если не нужно)")
    notify_by_email: float | None = Field(default=None, description="За сколько часов до визита следует выслать email напоминание клиенту (0 - если не нужно)")
    master_requested: bool | None = Field(default=None, description="Был ли указан определенный специалист при записи (false если был указан \"не имеет значения\")")
    online: bool | None = Field(default=None, description="Запись онлайновая или нет (false если запись внес администратор)")
    api_id: float | None = Field(default=None, description="ID записи из внешней системы")


class BookRecordCompanyidRecordidRecordhashResponseDataTypesStaff(BaseModel):
    """Параметры сотрудника
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="ID сотрудника")
    name: str | None = Field(default=None, description="Имя сотрудника")
    specialization: str | None = Field(default=None, description="Специализация сотрудника")
    position: BookRecordCompanyidRecordidRecordhashResponseDataTypesStaffPosition | None = Field(default=None)
    show_rating: bool | None = Field(default=None, description="Показывать ли рейтинг сотрудника")
    rating: float | None = Field(default=None, description="Рейтинг сотрудника (от 0 до 5)")
    votes_count: float | None = Field(default=None, description="Кол-во голосов, поставивших сотруднику оценку")
    avatar: str | None = Field(default=None, description="Путь к аватарке сотрудника")
    comments_count: float | None = Field(default=None, description="Кол-во комментариев сотруднику")


class BookRecordCompanyidRequestDataTypesAppointmentsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="ID записи по которому будет возвращаться ее хеш в ответет")
    services: list[float] | None = Field(default=None, description="Список ID услуг для записи")
    staff_id: float | None = Field(default=None, description="ID сотрудника")
    datetime: str | None = Field(default=None, description="\"2025-01-01 12:00:00\" (required, string) - Дата и время сеанса")
    custom_fields: BookRecordCompanyidRequestDataTypesAppointmentsItemCustomFields | None = Field(default=None)


class BookServicesCompanyidDataTypesData(BaseModel):
    """Объект с данными
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    events: list[dict[str, Any]] | None = Field(default=None)
    services: list[BookServicesCompanyidDataTypesDataServicesItem] | None = Field(default=None, description="Услуги")
    category: list[BookServicesCompanyidDataTypesDataCategoryItem] | None = Field(default=None, description="Категории услуг")


class BookStaffCompanyidDataTypesDataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="ID сотрудника")
    name: str | None = Field(default=None, description="Имя сотрудника")
    bookable: bool | None = Field(default=None, description="Есть ли у сотрудника сеансы, доступные для бронирования")
    specialization: str | None = Field(default=None, description="Специализация сотрудника")
    position: BookStaffCompanyidDataTypesDataItemPosition | None = Field(default=None)
    show_rating: float | None = Field(default=None, description="Показывать ли рейтинг сотрудника (1 - показывать, 0 - не показывать)")
    rating: float | None = Field(default=None, description="Рейтинг сотрудника")
    votes_count: float | None = Field(default=None, description="Кол-во голосов, оценивших сотрудника")
    avatar: str | None = Field(default=None, description="Путь к файлу аватарки сотрудника")
    comments_count: float | None = Field(default=None, description="Кол-во комментариев к сотруднику")
    weight: str | None = Field(default=None, description="Вес сотрудника. При выводе сотрудники сортируются по весу, сначала более тяжелые")
    information: str | None = Field(default=None, description="Дополнительная информация о сотруднике (HTML формат)")
    seance_date: str | None = Field(default=None, description="Дата ближайшего дня, на который есть доступные сеансы (только для bookable = true)")
    seances: list[dict[str, Any]] | None = Field(default=None, description="Доступные сеансы")


class BookStaffSeancesCompanyidStaffidDataTypesData(BaseModel):
    """Объект с данными
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    seance_date: str | None = Field(default=None, description="Ближайшая дата с доступными сеансами")
    seances: list[BookStaffSeancesCompanyidStaffidDataTypesDataSeancesItem] | None = Field(default=None, description="Список доступных сеансов")


class BookformIdInfoDataTypesData(BaseModel):
    """Объект с данными
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    steps: list[BookformIdInfoDataTypesDataStepsItem] | None = Field(default=None, description="Шаги формы бронирования со своими настройками")
    style: BookformIdInfoDataTypesDataStyle | None = Field(default=None)
    group_id: float | None = Field(default=None, description="Идентификатор сети компаний (0 - если форма записи для несетевой компании")
    company_id: float | None = Field(default=None, description="Идентификатор компании (возвращается всегда, используется для получения дополнительных настроек)")
    phone_confirmation: bool | None = Field(default=None, description="Нужно ли подтверждать телефон по смс (если groupid = 0 (не групповая форма), иначе смотреть в настройки каждой компании отдельно)")
    lang: str | None = Field(default=None, description="Язык формы бронирования (код из массива langs)")
    langs: list[BookformIdInfoDataTypesDataLangsItem] | None = Field(default=None, description="Список языков виджета")
    comment_required: bool | None = Field(default=None, description="Является ли поле с комментарием к записи обязательным для заполнения")
    metrika_counter_id: str | None = Field(default=None, description="Идентификатор Яндекс.Метрики")
    google_analytics_id: str | None = Field(default=None, description="Идентификатор Google Analytics")
    facebook_pixel_id: str | None = Field(default=None, description="Идентификатор Facebook Pixel")
    vkontakte_pixel_id: str | None = Field(default=None, description="Идентификатор Вконтакте Пиксель")
    app_metrika_id: str | None = Field(default=None, description="Идентификатор Yandex AppMetrika")
    sms_enabled: bool | None = Field(default=None, description="Доступна ли отправка смс")


class BookDatesCompanyidDataTypes(BaseModel):
    """Получить список дат доступных для бронирования
    Схема спеки: Root Type for book_dates_company_id_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: BookDatesCompanyidDataTypesData | None = Field(default=None, alias="data")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")


class BookRecordCompanyidRecordResponseDataTypes(BaseModel):
    """Перенести запись на сеанс
    Схема спеки: Root Type for book_record_companyid_record_respnse_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: BookRecordCompanyidRecordResponseDataTypesData | None = Field(default=None, alias="data")


class BookRecordCompanyidRecordidRecordhashResponseDataTypes(BaseModel):
    """Получить запись
    Схема спеки: Root Type for book_record_companyid_recordid_recordhash_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="ID записи")
    services: list[BookRecordCompanyidRecordidRecordhashResponseDataTypesServicesItem] | None = Field(default=None, description="Список ID услуг")
    company: BookRecordCompanyidRecordidRecordhashResponseDataTypesCompany | None = Field(default=None)
    staff: BookRecordCompanyidRecordidRecordhashResponseDataTypesStaff | None = Field(default=None)
    clients_count: int | None = Field(default=None)
    date: str | None = Field(default=None, description="\"2025-01-01 12:00:00\" (required, string) - Дата сеанса")
    datetime: str | None = Field(default=None, description="Дата сеанса в ISO")
    create_date: str | None = Field(default=None, description="\"2025-01-01 12:00:00\" (required, string) - Дата создания записи")
    comment: str | None = Field(default=None, description="Комментарий к записи")
    deleted: bool | None = Field(default=None, description="Удалена ли запись (true если удалена)")
    attendance: float | None = Field(default=None, description="2 - Пользователь подтвердил запись, 1 - Пользователь пришел, услуги оказаны, 0 - ожидание пользователя, -1 - пользователь не пришел на визит")
    length: float | None = Field(default=None, description="Длительность сеанса")
    notify_by_sms: float | None = Field(default=None, description="За какое кол-во часов отправить смс напоминание о записи (0 если не нужно напоминать)")
    notify_by_email: float | None = Field(default=None, description="За какое кол-во часов отправить email напоминание о записи (0 если не нужно напоминать)")
    master_requested: bool | None = Field(default=None, description="Был ли указан определенный специалист при записи (false если был указан \"не имеет значения\")")
    online: bool | None = Field(default=None, description="Запись онлайновая или нет (false если запись внес администратор)")
    api_id: str | None = Field(default=None, description="Внешний идентификатор записи")
    last_change_date: str | None = Field(default=None, description="Дата последнего редактирования записи")
    prepaid: bool | None = Field(default=None, description="Доступна ли онлайн-оплата для записи")
    prepaid_confirmed: bool | None = Field(default=None, description="Статус online-оплаты")
    activity_id: float | None = Field(default=None, description="ID групповой записи")


class BookRecordCompanyidRequestDataTypes(BaseModel):
    """Создать запись на сеанс
    Схема спеки: Root Type for book_record_companyid_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    phone: str = Field(description="Телефон клиента")
    fullname: str = Field(description="Имя клиента")
    surname: str | None = Field(default=None, description="Фамилия клиента")
    patronymic: str | None = Field(default=None, description="Отчество клиента")
    email: str = Field(description="Почтовый адрес клиента")
    code: float | None = Field(default=None, description="Код подтверждения телефона, высланный по смс (обязателен если у компании выставлен phone_conformation = true)")
    comment: str | None = Field(default=None, description="Коммаентарий к записи")
    notify_by_sms: float | None = Field(default=None, description="За сколько часов до визита следует выслать смс напоминание клиенту (0 - если не нужно)")
    notify_by_email: float | None = Field(default=None, description="За сколько часов до визита следует выслать email напоминание клиенту (0 - если не нужно)")
    api_id: float | None = Field(default=None, description="ID записи из внешней системы")
    is_newsletter_allowed: bool | None = Field(default=None, description="Отправка информационно-рекламной рассылки")
    is_personal_data_processing_allowed: bool | None = Field(default=None, description="Обработка персональных данных")
    appointments: list[BookRecordCompanyidRequestDataTypesAppointmentsItem] | None = Field(default=None, description="Параметры записей (сеанс, услуги, мастер)")


class BookServicesCompanyidDataTypes(BaseModel):
    """Получить списокуслуг доступных для бронирования
    Схема спеки: Root Type for get_book_services_type
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успшности выполнения (true)")
    data_: BookServicesCompanyidDataTypesData | None = Field(default=None, alias="data")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")


class BookStaffCompanyidDataTypes(BaseModel):
    """Получить список сотрудников доступных для бронирования
    Схема спеки: Root Type for book_staff_company_id_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: list[BookStaffCompanyidDataTypesDataItem] | None = Field(default=None, alias="data", description="Массив объектов с данными")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")


class BookStaffSeancesCompanyidStaffidDataTypes(BaseModel):
    """Получить список ближайших доступных сеансов
    Схема спеки: Root Type for book_staff_seances_companyid_staffid
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: BookStaffSeancesCompanyidStaffidDataTypesData | None = Field(default=None, alias="data")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")


class BookformIdInfoDataTypes(BaseModel):
    """Настройки формы бронирования записи
    Схема спеки: Root Type for bookform_info_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: BookformIdInfoDataTypesData | None = Field(default=None, alias="data")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")


class BookingFormListResponseDataType(BaseModel):
    """Список букформ
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data_: list[BookformSettingsResponse2] = Field(alias="data", description="Array of data")
    meta: list[dict[str, Any]] = Field(description="Metadata (contains the total count of bookforms)")
    success: bool = Field(description="Success status (true)")


class BookingFormResponseDataType(BaseModel):
    """Настройки букформы
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data_: BookformSettingsResponse2 = Field(alias="data")
    meta: list[dict[str, Any]] = Field(description="Metadata")
    success: bool = Field(description="Success status (true)")

__all__ = [
    "BookCheckCompanyidRequestDataTypes",
    "BookCheckCompanyidResponse201DataTypes",
    "BookCheckCompanyidResponse201DataTypesMeta",
    "BookCodeCompanyidDataTypeResponse",
    "BookCodeCompanyidDataTypeResponseMeta",
    "BookCodeCompanyidDataTypesRequest",
    "BookDatesCompanyidDataTypes",
    "BookDatesCompanyidDataTypesData",
    "BookDatesCompanyidDataTypesDataBookingDays",
    "BookDatesCompanyidDataTypesDataWorkingDays",
    "BookRecordCompanyidRecordRequestDataTypes",
    "BookRecordCompanyidRecordResponseDataTypes",
    "BookRecordCompanyidRecordResponseDataTypesData",
    "BookRecordCompanyidRecordResponseDataTypesDataCompany",
    "BookRecordCompanyidRecordResponseDataTypesDataServicesItem",
    "BookRecordCompanyidRecordResponseDataTypesDataStaff",
    "BookRecordCompanyidRecordidRecordhashResponseDataTypes",
    "BookRecordCompanyidRecordidRecordhashResponseDataTypesCompany",
    "BookRecordCompanyidRecordidRecordhashResponseDataTypesServicesItem",
    "BookRecordCompanyidRecordidRecordhashResponseDataTypesStaff",
    "BookRecordCompanyidRecordidRecordhashResponseDataTypesStaffPosition",
    "BookRecordCompanyidRequestDataTypes",
    "BookRecordCompanyidRequestDataTypesAppointmentsItem",
    "BookRecordCompanyidRequestDataTypesAppointmentsItemCustomFields",
    "BookRecordCompanyidResponseDataTypes",
    "BookRecordCompanyidResponseDataTypesDataItem",
    "BookServicesCompanyidDataTypes",
    "BookServicesCompanyidDataTypesData",
    "BookServicesCompanyidDataTypesDataCategoryItem",
    "BookServicesCompanyidDataTypesDataServicesItem",
    "BookStaffCompanyidDataTypes",
    "BookStaffCompanyidDataTypesDataItem",
    "BookStaffCompanyidDataTypesDataItemPosition",
    "BookStaffSeancesCompanyidStaffidDataTypes",
    "BookStaffSeancesCompanyidStaffidDataTypesData",
    "BookStaffSeancesCompanyidStaffidDataTypesDataSeancesItem",
    "BookTimesCompanyidDataTypes",
    "BookTimesCompanyidDataTypesDataItem",
    "BookformCreateRequest2",
    "BookformIdInfoDataTypes",
    "BookformIdInfoDataTypesData",
    "BookformIdInfoDataTypesDataLangsItem",
    "BookformIdInfoDataTypesDataStepsItem",
    "BookformIdInfoDataTypesDataStyle",
    "BookformSettingsResponse2",
    "BookformUpdateRequest2",
    "BookingAuthResponse",
    "BookingAuthResponse2",
    "BookingAuthWithCode",
    "BookingFormListResponseDataType",
    "BookingFormResponseDataType",
    "BookingUserGetDataResponseDataTypes",
    "BookingUserUpdateInfoRequestDataTypes",
    "BookingUserUpdatePasswordRequestDataTypes",
    "BookingUserUpdatePasswordResponseDataTypes",
    "BookingUserUpdatePasswordResponseDataTypesData"
]
