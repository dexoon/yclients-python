"""Модели YCLIENTS API (a: A).

Сгенерировано scripts/generate.py -- не редактируйте вручную.
"""

from __future__ import annotations

from datetime import date, datetime
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class AbonementTypeAvailabilityIntervalsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    from_: int | None = Field(default=None, alias="from", description="Начало интервала в секундах.")
    to: int | None = Field(default=None, description="Конец интервала в секундах.")


class AccountsResponseDataTypesDataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор кассы")
    title: str | None = Field(default=None, description="Название кассы")
    type_: float | None = Field(default=None, alias="type", description="1 - для безналичных платежей, 0 для наличных")
    comment: str | None = Field(default=None, description="Описание к кассе")


class ActivityCompanyidActivityidBookResponseDataTypesData(BaseModel):
    """Объект с данными
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор записи")
    hash: str | None = Field(default=None, description="Идентификатор записи, для ее удаления непосредственно сразу после создания")


class ActivityCompanyidResponseDataTypesDataDurationDetails(BaseModel):
    """Детали длительности события
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор деталей")
    services_duration: float | None = Field(default=None, description="Длительность услуг")
    technical_break_duration: float | None = Field(default=None, description="Длительность технического перерыва")


class ActivityCompanyidResponseDataTypesDataResourceInstancesItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор экземпляра ресурса")
    title: str | None = Field(default=None, description="Название экземпляра ресурса")
    resource_id: float | None = Field(default=None, description="Идентификатор ресурса")


class ActivityCompanyidResponseDataTypesDataServiceCategory(BaseModel):
    """Информация о категории услуги
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    title: str | None = Field(default=None, description="Название категории")
    id_: int | None = Field(default=None, alias="id", description="Идентификатор категории услуг")
    is_category: Any | None = Field(default=None, description="Элемент является категорией")
    salon_service_id: str | None = Field(default=None, description="Идентификатор категории для компании в сети")
    prepaid: str | None = Field(default=None, description="Доступна ли онлайн-оплата")
    abonement_restriction: int | None = Field(default=None, description="Онлайн-запись доступна только при наличии абонемента")


class ActivityCompanyidResponseDataTypesDataStaff(BaseModel):
    """Сотрудник
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор сотрудника")
    name: str | None = Field(default=None, description="Имя сотрудника")
    company_id: float | None = Field(default=None, description="Идентификатор филиала")
    specialization: str | None = Field(default=None, description="Специальность сотрудника")
    api_id: float | None = Field(default=None, description="Внешний идентификатор сотрудника")
    user_id: float | None = Field(default=None, description="Идентификатор связанного с сотрудником пользователя")
    rating: float | None = Field(default=None, description="Рейтинг сотрудника")
    prepaid: str | None = Field(default=None, description="Доступна ли онлайн-оплата для записи")
    show_rating: Any | None = Field(default=None, description="Показывать рейтиннг сотрудника")
    comments_count: float | None = Field(default=None, description="Кол-во комментариев к сотруднику")
    votes_count: float | None = Field(default=None, description="Кол-во голосов, оценивших сотрудника")
    average_score: Any | None = Field(default=None, description="Средняя оценка сотрудника")
    avatar: str | None = Field(default=None, description="Путь к файлу аватарки сотрудника")
    avatar_big: float | None = Field(default=None, description="Путь к файлу аватарки сотрудника в более высоком разрешении")
    position: list[Any] | None = Field(default=None, description="Должность сотрудника")


class ActivityCompanyidSearchResponseDataTypesDataItemResourceInstancesItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор экземпляра ресурса")
    title: str | None = Field(default=None, description="Название экземпляра ресурса")
    resource_id: float | None = Field(default=None, description="Идентификатор ресурса")


class ActivityCompanyidSearchResponseDataTypesDataItemServiceCategory(BaseModel):
    """Категория
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор категории")
    category_id: float | None = Field(default=None, description="Идентификатор товарной категории (0, если элемент - товар)")
    title: str | None = Field(default=None, description="Название категории")


class ActivityCompanyidSearchResponseDataTypesDataItemStaffPosition(BaseModel):
    """Должность сотрудника
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор должности")
    title: str | None = Field(default=None, description="Название должности")


class ActivityCompanyidSearchResponseDataTypesMeta(BaseModel):
    """Метаданные (содержит в себе количество найденных событий)
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    count_: int | None = Field(default=None, alias="count")


class ActivityCompanyidServicesResponseDataTypesDataItemCategory(BaseModel):
    """Категория услуги
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор категории")
    title: str | None = Field(default=None, description="Название категории услуги")


class ActivityCompanyidServicesResponseDataTypesDataItemResourcesItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор ресурса")
    title: str | None = Field(default=None, description="Название ресурса")
    salon_id: float | None = Field(default=None, description="Идентификатор филиала")


class ActivityCompanyidServicesResponseDataTypesDataItemStaffItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор сотрудника")
    name: str | None = Field(default=None, description="Имя сотрудника")
    length: float | None = Field(default=None, description="Длительность услуги")


class ActivityCompanyidServicesResponseDataTypesMeta(BaseModel):
    """Метаданные (содержит количество найденных услуг)
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    count_: int | None = Field(default=None, alias="count")


class ActivityFilterDataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор элемента фильтра.")
    title: str | None = Field(default=None, description="Название элемента фильтра.")
    is_disabled: bool | None = Field(default=None, description="Флаг, что элемент фильтра не доступен для выбора (зависит от ранее применённых фильтров, указанных в параметрах запроса).")


class ApiV2CompanyWaitingListCreateResponseDataAttributes(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    created_at: str | None = Field(default=None, description="Дата создания заявки")
    updated_at: str | None = Field(default=None, description="Дата обновления заявки")
    status: Literal["active", "expired", "finished"] | None = Field(default=None, description="Статус заявки")
    location_id: int | None = Field(default=None, description="Идентификатор филиала")
    client_id: int | None = Field(default=None, description="Идентификатор клиента")
    comment: str | None = Field(default=None, description="Комментарий к заявке")


class ApiV2CompanyWaitingListGetResponseDataAttributes(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    created_at: str | None = Field(default=None, description="Дата создания заявки")
    updated_at: str | None = Field(default=None, description="Дата обновления заявки")
    status: Literal["active", "expired", "finished"] | None = Field(default=None, description="Статус заявки")
    location_id: int | None = Field(default=None, description="Идентификатор филиала")
    client_id: int | None = Field(default=None, description="Идентификатор клиента")
    comment: str | None = Field(default=None, description="Комментарий к заявке")


class ApiV2CompanyWaitingListGetResponseMeta(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    count_: int | None = Field(default=None, alias="count", description="Количество заявок на странице")


class AuthRequest2faParam2fa(BaseModel):
    """Объект двухфакторной авторизации.
    ⚠️Если у пользователя включена 2fa сначала отправляется запрос только с параметрами login и password
    вторым запросом login, password и объект 2fa.
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    uuid: str | None = Field(default=None, description="Идентификатор запроса. Этот идентификатор может быть получен из ответа на запрос авторизации, когда переданы только параметры login и password.")
    secret: str | None = Field(default=None, description="Код подтверждения. После того, как был отправлен запрос авторизации только с параметрами login и password, пользователь получит код подтверждения на почту и push-уведомление в мобильном приложении ...")


class AuthResponse2faNeedDataTransport(BaseModel):
    """Объект с описанием канала по которому отправлен код подтверждения
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    type_: Literal["email"] | None = Field(default=None, alias="type", description="Указывает канал по которому будет доставлен код подтверждения.")
    recipient: str | None = Field(default=None, description="Адрес доставки кода подтверждения")


class AbonementTypeAvailability(BaseModel):
    """Схема спеки: Объект модели "Период доступности абонемента".
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    week_days: list[float] | None = Field(default=None, description="Дни недели, в которых действует условие.")
    intervals: list[AbonementTypeAvailabilityIntervalsItem] | None = Field(default=None, description="Интервалы доступности.")


class AccountsResponseDataTypes(BaseModel):
    """Получить кассы компании
    Схема спеки: Root Type for accounts_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: list[AccountsResponseDataTypesDataItem] | None = Field(default=None, alias="data", description="Массив объектов с данными")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")


class ActivityCompanyidActivityidBookResponseDataTypes(BaseModel):
    """Создать запись в групповом событии
    Схема спеки: Root Type for activity_company_id__activity_book_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: ActivityCompanyidActivityidBookResponseDataTypesData | None = Field(default=None, alias="data")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")


class ActivityCompanyidRequestDataTypes(BaseModel):
    """Создание группового события
    Схема спеки: Root Type for activity_companyid_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    date: str = Field(description="Дата и время")
    service_id: float = Field(description="Идентификатор услуги")
    staff_id: float = Field(description="Идентификатор сотрудника")
    capacity: float = Field(description="Вместимость")
    resource_instance_ids: list[float] | None = Field(default=None, description="Массив идентификаторов экземпляров ресурсов")
    force: bool = Field(description="Игнорировать ошибки (занятость мастера/ресурсов и т.п.)")
    length: float | None = Field(default=None, description="Длительность события в секундах")
    color: str | None = Field(default=None, description="Цвет события")
    label_ids: list[Any] | None = Field(default=None, description="Категории событий")
    comment: str | None = Field(default=None, description="Комментарий события")
    stream_link: str | None = Field(default=None, description="Ссылка на онлайн-событие")
    technical_break_duration: float | None = Field(default=None, description="Длительность технического перерыва - Если не передан. Значение по умолчанию null - Значение null, соответствует общей настройке филиала, и задается в разделе *Настройки → Журнал записи → Технически...")
    instructions: str | None = Field(default=None, description="Инструкции")


class ActivityCompanyidServicesRequestDataTypes(BaseModel):
    """Поиск групповых услуг
    Схема спеки: Root Type for activity_companyid_services_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    staff_id: float | None = Field(default=None, description="Идентификатор сотрудника для фильтрации")
    term: str | None = Field(default=None, description="Поиск по названию или части названия услуги")


class ActivityDatesRange(BaseModel):
    """Диапазон данных для поиска событий.
    Схема спеки: Объект "Диапазон данных для поиска событий"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    min_date: str | None = Field(default=None, description="Дата начала диапазона (ГГГГ-ММ-ДД).")
    max_date: str | None = Field(default=None, description="Дата окончания диапазона (ГГГГ-ММ-ДД).")


class ActivityFilter(BaseModel):
    """Фильтр для поиска событий.
    Схема спеки: Объект "Фильтр для поиска событий"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    code: Literal["staff", "resource", "service", "service_category"] | None = Field(default=None, description="Тип фильтра.")
    title: str | None = Field(default=None, description="Название фильтра.")
    data_: list[ActivityFilterDataItem] | None = Field(default=None, alias="data", description="Элементы фильтра.")


class AnalyticsReportOverallChartScalarItem2(BaseModel):
    """Данные для построения агрегирующей диаграммы в отчете Основные показатели
    Схема спеки: Root Type for AnalyticsReportOverallChartRow
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    label: str | None = Field(default=None, description="Название показателя")
    data_: int | None = Field(default=None, alias="data", description="Значение показателя")


class AnalyticsReportOverallClientStats2(BaseModel):
    """Сводные показатели по количеству клиентов
    Схема спеки: Root Type for AnalyticsReportOverallClientStats
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    total_count: int | None = Field(default=None, description="Общее количество клиентов")
    new_count: int | None = Field(default=None, description="Количество новых клиентов в анализируемом периоде")
    new_percent: int | None = Field(default=None, description="Процент новых клиентов относительно количества активных клиентов")
    return_count: int | None = Field(default=None, description="Количество клиентов, вернувшихся в анализируемом периоде")
    return_percent: int | None = Field(default=None, description="Процент вернувшихся клиентов относительно количества активных клиентов")
    active_count: int | None = Field(default=None, description="Количество активных клиентов в анализируемом периоде")
    lost_count: int | None = Field(default=None, description="Количество потерянных клиентов в анализируемом периоде")
    lost_percent: int | None = Field(default=None, description="Процент потерянных клиентов относительно общего количества клиентов")


class AnalyticsReportOverallFullnessStats2(BaseModel):
    """Сводные показатели заполненности рабочего времени сотрудников компании
    Схема спеки: Root Type for AnalyticsReportOverallFullnessStats
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    current_percent: float | None = Field(default=None, description="Процент заполненности в текущем периоде")
    previous_percent: float | None = Field(default=None, description="Процент заполненности в предыдущем периоде")
    change_percent: int | None = Field(default=None, description="Процент изменения текущего значения показателя относительно прошлого. Null, если прошлый показатель равен 0, а текущий отличен от 0.")


class AnalyticsReportOverallRecordStats2(BaseModel):
    """Сводные показатели по количеству записей
    Схема спеки: Root Type for AnalyticsReportOverallRecordStats
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    current_completed_count: int | None = Field(default=None, description="Количество завершенных записей")
    current_completed_percent: int | None = Field(default=None, description="Процент завершенных записей относительно общего количества. Null, если общее количество равно 0.")
    current_pending_count: int | None = Field(default=None, description="Количество незавершенных записей")
    current_pending_percent: int | None = Field(default=None, description="Процент незавершенных записей относительно общего количества. Null, если общее количество равно 0.")
    current_canceled_count: int | None = Field(default=None, description="Количество отмененных записей")
    current_canceled_percent: int | None = Field(default=None, description="Процент отмененных записей относительно общего количества. Null, если общее количество равно 0.")
    current_total_count: int | None = Field(default=None, description="Количество всех записей в текущем периоде")
    previous_total_count: int | None = Field(default=None, description="Количество всех записей в предыдущем периоде")
    change_percent: int | None = Field(default=None, description="Процент изменения текущего значения полного числа записей относительно прошлого. Null, если количество записей в предыдущем периоде равно 0, а текущее количество отлично от 0.")


class AuthRequest2(BaseModel):
    """Авторизация пользователя
    Схема спеки: Базовая авторизация
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    login: str = Field(description="Номер телефона или Email")
    password: str = Field(description="Пароль")


class AuthRequest2fa(BaseModel):
    """Авторизация пользователя
    Схема спеки: Передать код подтверждения 2FA
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    login: str = Field(description="Номер телефона или Email")
    password: str = Field(description="Пароль")
    param_2fa: AuthRequest2faParam2fa | None = Field(default=None, alias="2fa")


class AuthResponse2(BaseModel):
    """Авторизация пользователя
    Схема спеки: Пользователь авторизован
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор пользователя")
    user_token: str | None = Field(default=None, description="User_token пользователя")
    name: str | None = Field(default=None, description="Имя пользователя")
    phone: str | None = Field(default=None, description="Телефон пользователя")
    login: str | None = Field(default=None, description="Логин пользователя")
    email: str | None = Field(default=None, description="Почтовый адрес пользователя")
    avatar: str | None = Field(default=None, description="Путь к файлу аватарки пользователя")
    is_approved: bool | None = Field(default=None, description="Подтвержден ли пользователь в системе")
    is_email_confirmed: bool | None = Field(default=None, description="Подтвержден ли email у пользователя")


class AbonementTypeServiceLinksContainerLinksItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    count_: float | None = Field(default=None, alias="count", description="Количество применений.")
    service: dict[str, Any] | None = Field(default=None, description="Привязанная услуга.")
    category: dict[str, Any] | None = Field(default=None, description="Привязанная категория услуг.")


class ActivityCompanyidResponseDataTypesDataService(BaseModel):
    """Услуга
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор услуги")
    title: str | None = Field(default=None, description="Название услуги")
    image_url: str | None = Field(default=None, description="Путь к картинке с изображением услуги")
    category_id: float | None = Field(default=None, description="Идентификатор категории услуги")
    is_category: Any | None = Field(default=None, description="Элемент является категорией")
    salon_service_id: float | None = Field(default=None, description="Идентификатор услуги для компании в сети")
    comment: str | None = Field(default=None, description="Комментарий услуги")
    price_min: float | None = Field(default=None, description="Минимальная стоимость услуги")
    price_max: float | None = Field(default=None, description="Максимальная стоимость услуги")
    prepaid: str | None = Field(default=None, description="Доступна ли онлайн-оплата для записи")
    abonement_restriction: Any | None = Field(default=None, description="Онлайн-запись доступна только при наличии абонемента")
    category: ActivityCompanyidResponseDataTypesDataServiceCategory | None = Field(default=None)
    labels: list[Any] | None = Field(default=None, description="Категории услуги")
    resource_instances: list[Any] | None = Field(default=None, description="Ресурсы связанные с услугой")


class ActivityCompanyidSearchResponseDataTypesDataItemService(BaseModel):
    """Услуга
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор услуги")
    category_id: float | None = Field(default=None, description="Идентификатор категории услуги")
    title: str | None = Field(default=None, description="Название услуги")
    price_min: float | None = Field(default=None, description="Минимальная стоимость услуги")
    price_max: float | None = Field(default=None, description="Максимальная стоимость услуги")
    comment: str | None = Field(default=None, description="Комментарий")
    image_url: str | None = Field(default=None, description="Путь к картинке с изображением услуги")
    salon_service_id: float | None = Field(default=None, description="Идентификатор категории для компании в сети")
    prepaid: str | None = Field(default=None, description="Предоплата")
    category: ActivityCompanyidSearchResponseDataTypesDataItemServiceCategory | None = Field(default=None)


class ActivityCompanyidSearchResponseDataTypesDataItemStaff(BaseModel):
    """Сотрудник
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор сотрудника")
    api_id: str | None = Field(default=None, description="Внешний идентификатор сотрудника")
    name: str | None = Field(default=None, description="Имя сотрудника")
    company_id: float | None = Field(default=None, description="Идентификатор филиала")
    specialization: str | None = Field(default=None, description="Специализация сотрудника")
    rating: float | None = Field(default=None, description="Рейтинг")
    show_rating: float | None = Field(default=None, description="Показывать ли рейтинг сотрудника (1 - показывать, 0 - не показывать)")
    avatar: str | None = Field(default=None, description="Путь к файлу аватарки сотрудника")
    avatar_big: str | None = Field(default=None, description="Путь к файлу аватарки сотрудника в более высоком разрешении")
    comments_count: float | None = Field(default=None, description="Кол-во комментариев к сотруднику")
    votes_count: float | None = Field(default=None, description="Кол-во голосов, оценивших сотрудника")
    average_score: float | None = Field(default=None, description="Средний рейтинг")
    prepaid: str | None = Field(default=None, description="Доступна ли онлайн-оплата для записи")
    position: ActivityCompanyidSearchResponseDataTypesDataItemStaffPosition | None = Field(default=None)


class ActivityCompanyidServicesResponseDataTypesDataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор услуги")
    title: str | None = Field(default=None, description="Название услуги")
    capacity: float | None = Field(default=None, description="Вместимость")
    price_min: float | None = Field(default=None, description="Минимальная стоимость услуги")
    price_max: float | None = Field(default=None, description="Максимальная стоимость услуги")
    is_multi: bool | None = Field(default=None, description="Доступна ли услуга для группового события")
    category: ActivityCompanyidServicesResponseDataTypesDataItemCategory | None = Field(default=None)
    staff: list[ActivityCompanyidServicesResponseDataTypesDataItemStaffItem] | None = Field(default=None, description="Сотрудник")
    resources: list[ActivityCompanyidServicesResponseDataTypesDataItemResourcesItem] | None = Field(default=None, description="Ресурсы")


class ApiV2CompanyWaitingListCreateResponseData(BaseModel):
    """Объект описывающий созданную заявку в листе ожидания
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: str | None = Field(default=None, alias="id", description="Идентификатор записи в листе ожидания")
    type_: Literal["waiting_list_entry"] | None = Field(default=None, alias="type", description="Тип данных")
    attributes: ApiV2CompanyWaitingListCreateResponseDataAttributes | None = Field(default=None)


class ApiV2CompanyWaitingListGetResponseData(BaseModel):
    """Массив заявок в листе ожидания
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: str | None = Field(default=None, alias="id", description="Идентификатор записи в листе ожидания")
    type_: Literal["waiting_list_entry"] | None = Field(default=None, alias="type", description="Тип данных")
    attributes: ApiV2CompanyWaitingListGetResponseDataAttributes | None = Field(default=None)


class AuthResponse2faNeedData(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    uuid: str | None = Field(default=None, description="Идентификатор запроса авторизации. ⚠️ Данный идентификатор необходим при запросе авторизации с кодом подтверждения.")
    flow: Literal["login"] | None = Field(default=None)
    transport: AuthResponse2faNeedDataTransport | None = Field(default=None)
    refresh_ttl_sec: float | None = Field(default=None, description="Через сколько секунд можно запросить новый код")
    attempts_left: float | None = Field(default=None, description="Сколько попыток ввода кода подтверждения осталось.")


class AbonementTypeServiceLinksContainer(BaseModel):
    """Схема спеки: Объект модели "Баланс абонемента".
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    links: list[AbonementTypeServiceLinksContainerLinksItem] | None = Field(default=None, description="Массив услуг, на которые распространяется абонемент.")


class ActivityCompanyidServicesResponseDataTypes(BaseModel):
    """Поиск групповых услуг
    Схема спеки: Root Type for activity_companyid_services_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: list[ActivityCompanyidServicesResponseDataTypesDataItem] | None = Field(default=None, alias="data", description="Массив объектов с данными")
    meta: ActivityCompanyidServicesResponseDataTypesMeta | None = Field(default=None)


class AnalyticsReportOverallChartDailyRow2(BaseModel):
    """Данные для построения диаграммы в разрезе по дням в отчете Основные показатели
    Схема спеки: Root Type for AnalyticsReportOverallChartRow
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    label: str | None = Field(default=None, description="Название ряда данных")
    data_: list[list[int]] | None = Field(default=None, alias="data", description="Данные за каждый день. Каждый день - это массив из двух чисел. Первое число - timestamp начала дня в зоне UTC, второе число - значение показателя в этот день.")


class AnalyticsReportOverallSumStats2(BaseModel):
    """Схема спеки: Root Type for AnalyticsReportOverallSumStats
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    current_sum: str | None = Field(default=None, description="Текущее значение показателя")
    previous_sum: str | None = Field(default=None, description="Значение показателя в предыдущем периоде")
    change_percent: int | None = Field(default=None, description="Процент изменения текущего значения показателя относительно прошлого. Null, если прошлый показатель равен 0, а текущий отличен от 0.")
    currency: Currency2 | None = Field(default=None)


class ApiV2CompanyWaitingListCreateResponse(BaseModel):
    """Схема спеки: Создание заявки в листе ожидания
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data_: ApiV2CompanyWaitingListCreateResponseData | None = Field(default=None, alias="data")


class ApiV2CompanyWaitingListGetResponse(BaseModel):
    """Схема спеки: Получение заявок в листе ожидания
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data_: ApiV2CompanyWaitingListGetResponseData | None = Field(default=None, alias="data")
    meta: ApiV2CompanyWaitingListGetResponseMeta | None = Field(default=None)


class AuthResponse2faNeed(BaseModel):
    """Авторизация пользователя с включенной двухфакторной авторизацией
    Схема спеки: Нужна авторизация 2fa
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Успешность запроса")
    data_: AuthResponse2faNeedData | None = Field(default=None, alias="data")
    meta: list[Any] | None = Field(default=None)


class ActivityCompanyidResponseDataTypesData(BaseModel):
    """Объект с данными
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор группового события")
    salon_id: float | None = Field(default=None, description="Идентификатор филиала")
    service_id: float | None = Field(default=None, description="Идентификатор услуги")
    staff_id: float | None = Field(default=None, description="Идентификатор сотрудника")
    date: str | None = Field(default=None, description="Дата группового события")
    length: float | None = Field(default=None, description="Длительность группового события")
    capacity: float | None = Field(default=None, description="Вместимость")
    records_count: float | None = Field(default=None, description="Количество записей в групповом событии")
    color: str | None = Field(default=None, description="Цвет")
    font_color: str | None = Field(default=None, description="Цвет шрифта")
    instructions: str | None = Field(default=None, description="Инструкции")
    stream_link: str | None = Field(default=None, description="Ссылка на онлайн-событие")
    duration_details: ActivityCompanyidResponseDataTypesDataDurationDetails | None = Field(default=None)
    notified: Any | None = Field(default=None, description="Отправлено уведомление подтверждения всех записей")
    comment: str | None = Field(default=None, description="Комментарий к событию")
    service: ActivityCompanyidResponseDataTypesDataService | None = Field(default=None)
    staff: ActivityCompanyidResponseDataTypesDataStaff | None = Field(default=None)
    resource_instances: list[ActivityCompanyidResponseDataTypesDataResourceInstancesItem] | None = Field(default=None, description="Ресурс")


class ActivityCompanyidSearchResponseDataTypesDataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор группового события")
    service_id: float | None = Field(default=None, description="Идентификатор услуги")
    company_id: float | None = Field(default=None, description="Идентификатор филиала")
    staff_id: float | None = Field(default=None, description="Идентификатор сотрудника")
    date: str | None = Field(default=None, description="Дата сеанса")
    length: float | None = Field(default=None, description="Длительность")
    capacity: float | None = Field(default=None, description="Вместимость")
    records_count: float | None = Field(default=None, description="Количество записей")
    color: str | None = Field(default=None, description="Цвет")
    instructions: str | None = Field(default=None, description="Инструкции")
    stream_link: str | None = Field(default=None, description="Ссылка на инструкцию")
    font_color: str | None = Field(default=None, description="Цвет шрифта")
    notified: bool | None = Field(default=None, description="Уведомления")
    prepaid: str | None = Field(default=None, description="Предоплата")
    service: ActivityCompanyidSearchResponseDataTypesDataItemService | None = Field(default=None)
    staff: ActivityCompanyidSearchResponseDataTypesDataItemStaff | None = Field(default=None)
    resource_instances: list[ActivityCompanyidSearchResponseDataTypesDataItemResourceInstancesItem] | None = Field(default=None, description="Эксемпляр ресурса")
    labels: list[dict[str, Any]] | None = Field(default=None, description="Категория записи")


class ActivityCompanyidResponseDataTypes(BaseModel):
    """Создание группового события
    Схема спеки: Root Type for activity_companyid_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: ActivityCompanyidResponseDataTypesData | None = Field(default=None, alias="data")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")


class ActivityCompanyidSearchResponseDataTypes(BaseModel):
    """Поиск групповых событий
    Схема спеки: Root Type for activity_companyid_search_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: list[ActivityCompanyidSearchResponseDataTypesDataItem] | None = Field(default=None, alias="data", description="Массив объектов с данными")
    meta: ActivityCompanyidSearchResponseDataTypesMeta | None = Field(default=None)


class AnalyticsReportOverallStats2(BaseModel):
    """Сводные показатели
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    income_total_stats: AnalyticsReportOverallSumStats2 | None = Field(default=None)
    income_services_stats: AnalyticsReportOverallSumStats2 | None = Field(default=None)
    income_goods_stats: AnalyticsReportOverallSumStats2 | None = Field(default=None)
    income_average_stats: AnalyticsReportOverallSumStats2 | None = Field(default=None)
    income_average_services_stats: AnalyticsReportOverallSumStats2 | None = Field(default=None)
    fullness_stats: AnalyticsReportOverallFullnessStats2 | None = Field(default=None)
    record_stats: AnalyticsReportOverallRecordStats2 | None = Field(default=None)
    client_stats: AnalyticsReportOverallClientStats2 | None = Field(default=None)

__all__ = [
    "AbonementTypeAvailability",
    "AbonementTypeAvailabilityIntervalsItem",
    "AbonementTypeServiceLinksContainer",
    "AbonementTypeServiceLinksContainerLinksItem",
    "AccountsResponseDataTypes",
    "AccountsResponseDataTypesDataItem",
    "ActivityCompanyidActivityidBookResponseDataTypes",
    "ActivityCompanyidActivityidBookResponseDataTypesData",
    "ActivityCompanyidRequestDataTypes",
    "ActivityCompanyidResponseDataTypes",
    "ActivityCompanyidResponseDataTypesData",
    "ActivityCompanyidResponseDataTypesDataDurationDetails",
    "ActivityCompanyidResponseDataTypesDataResourceInstancesItem",
    "ActivityCompanyidResponseDataTypesDataService",
    "ActivityCompanyidResponseDataTypesDataServiceCategory",
    "ActivityCompanyidResponseDataTypesDataStaff",
    "ActivityCompanyidSearchResponseDataTypes",
    "ActivityCompanyidSearchResponseDataTypesDataItem",
    "ActivityCompanyidSearchResponseDataTypesDataItemResourceInstancesItem",
    "ActivityCompanyidSearchResponseDataTypesDataItemService",
    "ActivityCompanyidSearchResponseDataTypesDataItemServiceCategory",
    "ActivityCompanyidSearchResponseDataTypesDataItemStaff",
    "ActivityCompanyidSearchResponseDataTypesDataItemStaffPosition",
    "ActivityCompanyidSearchResponseDataTypesMeta",
    "ActivityCompanyidServicesRequestDataTypes",
    "ActivityCompanyidServicesResponseDataTypes",
    "ActivityCompanyidServicesResponseDataTypesDataItem",
    "ActivityCompanyidServicesResponseDataTypesDataItemCategory",
    "ActivityCompanyidServicesResponseDataTypesDataItemResourcesItem",
    "ActivityCompanyidServicesResponseDataTypesDataItemStaffItem",
    "ActivityCompanyidServicesResponseDataTypesMeta",
    "ActivityDatesRange",
    "ActivityFilter",
    "ActivityFilterDataItem",
    "AnalyticsReportOverallChartDailyRow2",
    "AnalyticsReportOverallChartScalarItem2",
    "AnalyticsReportOverallClientStats2",
    "AnalyticsReportOverallFullnessStats2",
    "AnalyticsReportOverallRecordStats2",
    "AnalyticsReportOverallStats2",
    "AnalyticsReportOverallSumStats2",
    "ApiV2CompanyWaitingListCreateResponse",
    "ApiV2CompanyWaitingListCreateResponseData",
    "ApiV2CompanyWaitingListCreateResponseDataAttributes",
    "ApiV2CompanyWaitingListGetResponse",
    "ApiV2CompanyWaitingListGetResponseData",
    "ApiV2CompanyWaitingListGetResponseDataAttributes",
    "ApiV2CompanyWaitingListGetResponseMeta",
    "AuthRequest2",
    "AuthRequest2fa",
    "AuthRequest2faParam2fa",
    "AuthResponse2",
    "AuthResponse2faNeed",
    "AuthResponse2faNeedData",
    "AuthResponse2faNeedDataTransport"
]
