"""Pydantic-модели webhook-уведомлений YCLIENTS.

Webhook -- это HTTP POST-запрос, который YCLIENTS отправляет на указанный в
настройках филиала URL при наступлении события (создание/изменение/удаление
сотрудника, записи, клиента и т.д.). Документация:
https://support.yclients.ru/67-69-993--webhooks-v-yclients/

Каждое уведомление -- JSON-объект с полями верхнего уровня
(``company_id``, ``resource``, ``resource_id``, ``status``) и объектом ``data``
с данными сущности на момент события. YCLIENTS отправляет запрос один раз,
без повторных попыток, порядок доставки не гарантируется, поэтому
рекомендуется логировать события и обрабатывать их идемпотентно.

Использование::

    from yclients import parse_webhook

    def handle(body: bytes) -> None:
        event = parse_webhook(body)
        match event.resource:
            case "record":
                print("запись", event.resource_id)
            case _:
                print(event.resource, event.status)

Особенности формата, учтённые в моделях:

- payload частичный: в ``data`` могут прийти только изменившиеся поля
  (например ``{"id": ..., "comment": "test"}``), поэтому все поля моделей
  необязательны;
- YCLIENTS может добавить новые поля -- включён режим ``extra="allow"``,
  незнакомые поля доступны через ``model_extra`` и не теряются;
- поля ``client``/``master``/``service`` в товарных операциях приходят то
  объектом, то массивом в зависимости от типа операции -- поэтому они
  типизированы как union.
"""

from typing import Annotated, Any, Literal

from pydantic import BaseModel, ConfigDict, Field, TypeAdapter, ValidationError

__all__ = [
    "ClientWebhook",
    "ClientWebhookData",
    "FinancesOperationWebhook",
    "FinancesOperationWebhookData",
    "GoodWebhook",
    "GoodWebhookData",
    "GoodsOperationsWebhook",
    "GoodsOperationsWebhookData",
    "RecordWebhook",
    "RecordWebhookData",
    "ServiceCategoryWebhook",
    "ServiceCategoryWebhookData",
    "ServiceWebhook",
    "ServiceWebhookData",
    "StaffWebhook",
    "StaffWebhookData",
    "UnknownWebhook",
    "WebhookAccount",
    "WebhookClientShort",
    "WebhookExpense",
    "WebhookFinanceClient",
    "WebhookFinanceRecord",
    "WebhookNamedEntity",
    "WebhookRecordClient",
    "WebhookRecordService",
    "WebhookRecordStaff",
    "WebhookServiceStaffItem",
    "WebhookStatus",
    "WebhookUnit",
    "YclientsWebhook",
    "parse_webhook",
]

WebhookStatus = Literal["create", "update", "delete"]

WebhookResource = Literal[
    "staff",
    "good",
    "service",
    "service_category",
    "client",
    "record",
    "goods_operations_sale",
    "goods_operations_receipt",
    "goods_operations_consumable",
    "goods_operations_stolen",
    "goods_operations_move",
    "finances_operation",
]


class _WebhookModel(BaseModel):
    """Общая настройка моделей webhook: частичные payload, extra-поля не теряются."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")


# --- Вложенные структуры ---------------------------------------------------


class WebhookNamedEntity(_WebhookModel):
    """Объект вида ``{id, title}`` (товар, склад, статья платежа и т.п.)."""

    id_: int | None = Field(default=None, alias="id", description="Идентификатор")
    title: str | None = Field(default=None, description="Название")


class WebhookUnit(_WebhookModel):
    """Единица измерения."""

    id_: int | None = Field(default=None, alias="id", description="ID единицы измерения")
    title: str | None = Field(default=None, description="Название единицы")
    short_title: str | None = Field(default=None, description="Краткое название")


class WebhookServiceStaffItem(_WebhookModel):
    """Элемент массива ``staff`` у услуги/категории услуг."""

    id_: int | None = Field(default=None, alias="id", description="ID сотрудника")
    seance_length: int | None = Field(
        default=None, description="Длительность оказания услуги сотрудником, секунды"
    )


class WebhookClientShort(_WebhookModel):
    """Клиент в товарных операциях: ``{id, name, phone}``."""

    id_: int | None = Field(default=None, alias="id", description="ID клиента")
    name: str | None = Field(default=None, description="Имя клиента")
    phone: str | None = Field(default=None, description="Телефон клиента")


class WebhookFinanceClient(_WebhookModel):
    """Клиент в финансовой операции."""

    id_: int | None = Field(default=None, alias="id", description="ID клиента")
    name: str | None = Field(default=None, description="Имя клиента")
    surname: str | None = Field(default=None, description="Фамилия")
    patronymic: str | None = Field(default=None, description="Отчество")
    phone: str | None = Field(default=None, description="Телефон")
    email: str | None = Field(default=None, description="Email")


class WebhookExpense(_WebhookModel):
    """Статья платежа."""

    id_: int | None = Field(default=None, alias="id", description="ID статьи платежа")
    title: str | None = Field(default=None, description="Название статьи")
    type: int | None = Field(default=None, description="Тип статьи")


class WebhookAccount(_WebhookModel):
    """Касса."""

    id_: int | None = Field(default=None, alias="id", description="ID кассы")
    title: str | None = Field(default=None, description="Название кассы")
    is_cash: bool | None = Field(default=None, description="Является ли касса наличной")
    is_default: bool | None = Field(default=None, description="Касса по умолчанию")


class WebhookFinanceRecord(_WebhookModel):
    """Связанная запись в финансовой операции."""

    id_: int | None = Field(default=None, alias="id", description="ID записи")
    location_id: int | None = Field(default=None, description="ID филиала")
    staff_id: int | None = Field(default=None, description="ID сотрудника")
    date: str | None = Field(default=None, description="Дата записи")
    visit_id: int | None = Field(default=None, description="ID визита")
    attendance_status: int | None = Field(default=None, description="Статус визита")
    paid_full: bool | None = Field(default=None, description="Полностью ли оплачена запись")
    is_online: bool | None = Field(default=None, description="Онлайн-запись")
    prepaid: bool | None = Field(default=None, description="Используется ли предоплата")
    clients_count: int | None = Field(default=None, description="Количество клиентов")
    deleted: bool | None = Field(default=None, description="Признак удаления записи")


class WebhookRecordStaff(_WebhookModel):
    """Сотрудник в записи."""

    id_: int | None = Field(default=None, alias="id", description="ID сотрудника")
    api_id: int | None = Field(default=None, description="Внешний идентификатор")
    name: str | None = Field(default=None, description="Имя сотрудника")
    specialization: str | None = Field(default=None, description="Специализация")
    position: dict[str, Any] | None = Field(default=None, description="Должность сотрудника")
    avatar: str | None = Field(default=None, description="URL маленького аватара")
    avatar_big: str | None = Field(default=None, description="URL большого аватара")
    rating: float | None = Field(default=None, description="Рейтинг сотрудника")
    votes_count: int | None = Field(default=None, description="Количество голосов")


class WebhookRecordService(_WebhookModel):
    """Услуга в записи."""

    id_: int | None = Field(default=None, alias="id", description="ID услуги")
    title: str | None = Field(default=None, description="Название услуги")
    cost: float | None = Field(default=None, description="Стоимость услуги")
    cost_to_pay: float | None = Field(default=None, description="Итоговая стоимость к оплате")
    manual_cost: float | None = Field(default=None, description="Стоимость, установленная вручную")
    cost_per_unit: float | None = Field(default=None, description="Стоимость за единицу")
    discount: float | None = Field(default=None, description="Скидка")
    first_cost: float | None = Field(default=None, description="Начальная стоимость")
    amount: float | None = Field(default=None, description="Количество")


class WebhookRecordClient(_WebhookModel):
    """Клиент в записи."""

    id_: int | None = Field(default=None, alias="id", description="ID клиента")
    name: str | None = Field(default=None, description="Имя клиента")
    surname: str | None = Field(default=None, description="Фамилия")
    patronymic: str | None = Field(default=None, description="Отчество")
    display_name: str | None = Field(default=None, description="Отображаемое имя")
    phone: str | None = Field(default=None, description="Телефон")
    email: str | None = Field(default=None, description="Email")
    card: str | None = Field(default=None, description="Номер карты")
    comment: str | None = Field(default=None, description="Комментарий")
    success_visits_count: int | None = Field(default=None, description="Количество успешных визитов")
    fail_visits_count: int | None = Field(default=None, description="Количество пропущенных визитов")
    discount: float | None = Field(default=None, description="Скидка клиента")
    custom_fields: list[Any] | None = Field(default=None, description="Дополнительные поля клиента")
    sex: int | None = Field(default=None, description="Пол")
    birthday: str | None = Field(default=None, description="Дата рождения")
    client_tags: list[Any] | None = Field(default=None, description="Теги клиента")


# --- Данные событий (объект data) ------------------------------------------


class StaffWebhookData(_WebhookModel):
    """Сотрудник на момент события."""

    id_: int | None = Field(default=None, alias="id", description="ID сотрудника")
    api_id: str | None = Field(default=None, description="Внешний идентификатор")
    name: str | None = Field(default=None, description="Имя сотрудника")
    specialization: str | None = Field(default=None, description="Специализация")
    position: list[Any] | None = Field(default=None, description="Должность сотрудника")
    position_id: int | None = Field(default=None, description="ID основной должности")
    show_rating: int | None = Field(
        default=None, description="Флаг отображения рейтинга (1 -- отображается, 0 -- скрыт)"
    )
    rating: float | None = Field(default=None, description="Рейтинг сотрудника")
    votes_count: float | None = Field(
        default=None, description="Количество голосов в расчёте рейтинга"
    )
    avatar: str | None = Field(default=None, description="URL изображения (малый размер)")
    avatar_big: str | None = Field(default=None, description="URL изображения (большой размер)")
    comments_count: int | None = Field(default=None, description="Количество отзывов")
    weight: int | None = Field(default=None, description="Порядок отображения в списке")
    information: str | None = Field(default=None, description="Дополнительная информация")
    hidden: int | None = Field(
        default=None, description="Признак скрытия для онлайн-записи (1 -- скрыт)"
    )
    fired: float | None = Field(default=None, description="Признак увольнения (1 -- уволен)")
    status: float | None = Field(
        default=None, description="Статус удаления сотрудника (1 -- удалён)"
    )
    schedule_till: str | None = Field(
        default=None, description="Дата, до которой сформировано расписание"
    )
    image_group: list[Any] | None = Field(default=None, description="Дополнительные изображения")
    prepaid: str | None = Field(default=None, description="Настройки предоплаты")
    user_id: int | None = Field(default=None, description="ID связанного пользователя системы")
    user: dict[str, Any] | None = Field(default=None, description="Связанный пользователь")


class GoodWebhookData(_WebhookModel):
    """Товар на момент события."""

    title: str | None = Field(default=None, description="Наименование товара")
    value: str | None = Field(default=None, description="Наименование товара")
    label: str | None = Field(
        default=None, description="Наименование с артикулом, если он указан"
    )
    article: str | None = Field(default=None, description="Артикул")
    category: str | None = Field(default=None, description="Название категории")
    category_id: int | None = Field(default=None, description="ID категории")
    salon_id: int | None = Field(default=None, description="ID филиала")
    good_id: int | None = Field(default=None, description="ID товара")
    cost: float | None = Field(default=None, description="Цена продажи")
    unit_id: int | None = Field(default=None, description="ID единицы измерения для продажи")
    unit_short_title: str | None = Field(
        default=None, description="Краткое название единицы для продажи"
    )
    service_unit_id: int | None = Field(default=None, description="ID единицы для списания")
    service_unit_short_title: str | None = Field(
        default=None, description="Краткое название единицы для списания"
    )
    actual_cost: float | None = Field(default=None, description="Себестоимость товара")
    unit_actual_cost: float | None = Field(default=None, description="Себестоимость единицы")
    unit_actual_cost_format: str | None = Field(
        default=None, description="Себестоимость единицы в отформатированном виде"
    )
    unit_equals: float | None = Field(
        default=None, description="Соотношение единицы продажи к единице списания"
    )
    barcode: str | None = Field(default=None, description="Штрих-код")
    is_chain: bool | None = Field(default=None, description="Признак сетевого товара")
    comment: str | None = Field(default=None, description="Комментарий")
    loyalty_abonement_type_id: int | None = Field(
        default=None, description="ID типа абонемента, если товар -- абонемент"
    )
    loyalty_certificate_type_id: int | None = Field(
        default=None, description="ID типа сертификата, если товар -- сертификат"
    )
    loyalty_certificate_type: dict[str, Any] | None = Field(
        default=None, description="Тип сертификата"
    )
    loyalty_allow_empty_code: bool | int | None = Field(
        default=None, description="Разрешена ли продажа без кода"
    )
    actual_amounts: list[Any] | None = Field(default=None, description="Остатки по складам")
    critical_amount: float | None = Field(default=None, description="Критичный остаток")
    desired_amount: float | None = Field(default=None, description="Желаемый остаток")
    last_change_date: str | None = Field(default=None, description="Дата последнего изменения")
    is_goods_mark_enabled: bool | None = Field(
        default=None, description="Используется ли маркировка товара"
    )


class ServiceWebhookData(_WebhookModel):
    """Услуга на момент события."""

    id_: int | None = Field(default=None, alias="id", description="ID услуги")
    salon_service_id: int | None = Field(default=None, description="ID связи услуги с филиалом")
    title: str | None = Field(default=None, description="Название услуги")
    booking_title: str | None = Field(
        default=None, description="Название услуги при онлайн-записи"
    )
    category_id: int | None = Field(default=None, description="ID категории услуги")
    price_min: float | None = Field(default=None, description="Минимальная цена")
    price_max: float | None = Field(default=None, description="Максимальная цена")
    duration: int | None = Field(default=None, description="Длительность, секунды")
    discount: float | None = Field(default=None, description="Скидка")
    comment: str | None = Field(default=None, description="Комментарий")
    weight: int | None = Field(default=None, description="Вес (для сортировки)")
    active: int | None = Field(
        default=None, description="Активна ли в онлайн-записи (1 -- активна)"
    )
    api_id: str | int | None = Field(default=None, description="Внешний идентификатор")
    staff: list[WebhookServiceStaffItem] | None = Field(
        default=None, description="Сотрудники, оказывающие услугу"
    )
    image_group: list[Any] | None = Field(default=None, description="Изображения услуги")
    prepaid: str | None = Field(default=None, description="Настройки предоплаты")
    is_multi: bool | None = Field(default=None, description="Признак групповой услуги")
    capacity: int | None = Field(
        default=None, description="Максимум клиентов на одну запись"
    )
    is_price_managed_only_in_chain: bool | None = Field(
        default=None, description="Цена управляется только на уровне сети"
    )
    is_comment_managed_only_in_chain: bool | None = Field(
        default=None, description="Комментарий управляется только на уровне сети"
    )


class ServiceCategoryWebhookData(_WebhookModel):
    """Категория услуг на момент события."""

    id_: int | None = Field(default=None, alias="id", description="ID категории")
    salon_service_id: int | None = Field(
        default=None, description="ID связи категории с филиалом"
    )
    title: str | None = Field(default=None, description="Название категории")
    weight: int | None = Field(default=None, description="Вес (для сортировки)")
    api_id: str | int | None = Field(default=None, description="Внешний идентификатор")
    staff: list[WebhookServiceStaffItem] | None = Field(
        default=None, description="Связанные сотрудники"
    )
    is_chain: bool | None = Field(default=None, description="Признак сетевой категории")


class ClientWebhookData(_WebhookModel):
    """Клиент на момент события."""

    id_: int | None = Field(default=None, alias="id", description="ID клиента")
    name: str | None = Field(default=None, description="Имя")
    surname: str | None = Field(default=None, description="Фамилия")
    patronymic: str | None = Field(default=None, description="Отчество")
    display_name: str | None = Field(default=None, description="Отображаемое имя")
    phone: str | None = Field(default=None, description="Телефон")
    email: str | None = Field(default=None, description="Email")
    card: str | None = Field(default=None, description="Номер карты")
    birth_date: str | None = Field(default=None, description="Дата рождения")
    comment: str | None = Field(default=None, description="Комментарий")
    discount: float | None = Field(default=None, description="Скидка клиента")
    visits: int | None = Field(default=None, description="Количество визитов")
    sex_id: int | None = Field(default=None, description="Пол клиента")
    sex: str | None = Field(default=None, description="Текстовое значение пола")
    sms_check: int | None = Field(
        default=None, description="Отправлять поздравления с днём рождения по СМС"
    )
    sms_bot: int | None = Field(
        default=None, description="Дублирует sms_not, некорректное поле"
    )
    sms_not: int | None = Field(default=None, description="Исключить из СМС-рассылок")
    spent: float | None = Field(default=None, description="Сумма, потраченная клиентом")
    paid: float | None = Field(default=None, description="Сумма оплаченных услуг")
    balance: float | None = Field(default=None, description="Баланс клиента")
    importance_id: int | None = Field(default=None, description="Класс важности клиента")
    importance: str | None = Field(default=None, description="Название класса важности")
    categories: list[Any] | None = Field(default=None, description="Категории клиента")
    last_change_date: str | None = Field(default=None, description="Дата последнего изменения")
    custom_fields: dict[str, Any] | None = Field(
        default=None, description="Пользовательские поля: ``{api_key: value}``"
    )


class RecordWebhookData(_WebhookModel):
    """Запись на момент события."""

    # Основные поля
    id_: int | None = Field(default=None, alias="id", description="ID записи")
    company_id: int | None = Field(default=None, description="ID филиала")
    staff_id: int | None = Field(default=None, description="ID сотрудника")
    clients_count: int | None = Field(default=None, description="Количество клиентов в записи")
    date: str | None = Field(default=None, description="Дата и время записи")
    datetime: str | None = Field(default=None, description="Дата и время в ISO-формате")
    seance_length: int | None = Field(default=None, description="Длительность записи, секунды")
    length: int | None = Field(default=None, description="Общая длительность записи")
    comment: str | None = Field(default=None, description="Комментарий к записи")
    online: bool | None = Field(default=None, description="Признак онлайн-записи")
    attendance: int | None = Field(default=None, description="Статус записи")
    visit_id: int | None = Field(default=None, description="ID визита")
    visit_attendance: int | None = Field(default=None, description="Статус визита")
    confirmed: int | None = Field(default=None, description="Подтверждена ли запись")
    deleted: bool | None = Field(default=None, description="Признак удаления записи")
    created_user_id: int | None = Field(
        default=None, description="ID пользователя, создавшего запись"
    )
    create_date: str | None = Field(default=None, description="Дата создания записи")
    last_change_date: str | None = Field(default=None, description="Дата последнего изменения")
    api_id: str | None = Field(default=None, description="Внешний идентификатор записи")
    activity_id: int | None = Field(default=None, description="ID группового события")
    bookform_id: int | None = Field(default=None, description="ID формы онлайн-записи")
    record_from: str | None = Field(default=None, description="Источник записи")
    is_mobile: int | None = Field(
        default=None, description="Создана ли запись с мобильного устройства"
    )
    # Уведомления и напоминания
    sms_before: int | None = Field(default=None, description="Отправлено ли СМС-напоминание")
    sms_now: int | None = Field(default=None, description="Отправить СМС после создания")
    sms_now_text: str | None = Field(default=None, description="Текст СМС")
    email_now: int | None = Field(default=None, description="Отправить email")
    sms_remain_hours: int | None = Field(
        default=None, description="За сколько часов отправлять СМС-напоминание"
    )
    email_remain_hours: int | None = Field(
        default=None, description="За сколько часов отправлять email-напоминание"
    )
    notified: int | None = Field(default=None, description="Был ли клиент уведомлён")
    # Финансовые параметры
    paid_full: int | None = Field(
        default=None, description="Полностью ли оплачена запись (0/1)"
    )
    prepaid: bool | None = Field(default=None, description="Используется ли предоплата")
    prepaid_confirmed: bool | None = Field(default=None, description="Подтверждена ли предоплата")
    # Услуги и связанные сущности
    services: list[WebhookRecordService] | None = Field(
        default=None, description="Услуги записи"
    )
    staff: WebhookRecordStaff | None = Field(default=None, description="Сотрудник записи")
    client: WebhookRecordClient | None = Field(default=None, description="Клиент записи")
    # Дополнительные данные
    goods_transactions: list[Any] | None = Field(
        default=None, description="Товары, добавленные в запись"
    )
    custom_fields: list[Any] | None = Field(default=None, description="Дополнительные поля записи")
    custom_color: str | None = Field(default=None, description="Цвет записи")
    custom_font_color: str | None = Field(default=None, description="Цвет текста записи")
    record_labels: list[Any] | None = Field(default=None, description="Категории записи")
    documents: list[Any] | None = Field(default=None, description="Связанные документы")
    short_link: str | None = Field(default=None, description="Короткая ссылка на запись")
    review_link: str | None = Field(default=None, description="Ссылка для отзыва")
    composite: list[Any] | None = Field(default=None, description="Комплексная запись")


class GoodsOperationsWebhookData(_WebhookModel):
    """Товарная операция (продажа, приход, списание, перемещение, расходники).

    Структура одна для всех пяти типов операций. Поля ``client``/``master``/
    ``service`` в зависимости от типа операции приходят объектом или массивом,
    поэтому типизированы как union. При перемещении формируются две операции
    (списание со склада-источника и приход на склад-получатель) с одинаковым
    ``document_id``; amount отрицательный при списании.
    """

    id_: int | None = Field(default=None, alias="id", description="ID операции")
    document_id: int | None = Field(default=None, description="ID связанного документа")
    type_id: int | None = Field(default=None, description="ID типа операции")
    type: str | None = Field(default=None, description="Название типа операции")
    operation_unit_type: int | None = Field(default=None, description="Тип единицы операции")
    amount: float | None = Field(default=None, description="Количество товара")
    create_date: str | None = Field(default=None, description="Дата создания операции")
    cost_per_unit: float | None = Field(default=None, description="Себестоимость единицы")
    cost: float | None = Field(default=None, description="Общая стоимость операции")
    discount: float | None = Field(default=None, description="Скидка")
    comment: str | None = Field(default=None, description="Комментарий")
    record_id: int | None = Field(
        default=None, description="ID записи, если операция связана с визитом"
    )
    last_change_date: str | None = Field(default=None, description="Дата последнего изменения")
    loyalty_abonement_id: int | None = Field(default=None, description="ID абонемента")
    loyalty_certificate_id: int | None = Field(default=None, description="ID сертификата")
    good: WebhookNamedEntity | None = Field(default=None, description="Товар")
    unit: WebhookUnit | None = Field(default=None, description="Единица измерения")
    storage: WebhookNamedEntity | None = Field(default=None, description="Склад")
    client: WebhookClientShort | list[Any] | None = Field(
        default=None, description="Клиент (объект или массив)"
    )
    master: WebhookNamedEntity | list[Any] | None = Field(
        default=None, description="Сотрудник (объект или массив)"
    )
    service: WebhookNamedEntity | list[Any] | None = Field(
        default=None, description="Связанная услуга (объект или массив)"
    )
    supplier: list[Any] | None = Field(default=None, description="Контрагент")


class FinancesOperationWebhookData(_WebhookModel):
    """Финансовая операция на момент события."""

    id_: int | None = Field(default=None, alias="id", description="ID транзакции")
    document_id: int | None = Field(default=None, description="ID документа")
    date: str | None = Field(default=None, description="Дата создания транзакции")
    amount: float | None = Field(default=None, description="Сумма операции")
    comment: str | None = Field(default=None, description="Комментарий")
    last_change_date: str | None = Field(default=None, description="Дата последнего изменения")
    record_id: int | None = Field(default=None, description="ID записи")
    visit_id: int | None = Field(default=None, description="ID визита")
    sold_item_id: int | None = Field(default=None, description="ID проданного элемента")
    sold_item_type: str | None = Field(
        default=None, description="Тип проданного элемента (service, good и др.)"
    )
    expense: WebhookExpense | None = Field(default=None, description="Статья платежа")
    master: list[Any] | None = Field(default=None, description="Сотрудник")
    supplier: list[Any] | None = Field(default=None, description="Контрагент")
    account: WebhookAccount | None = Field(default=None, description="Касса")
    client: WebhookFinanceClient | None = Field(default=None, description="Клиент")
    record: WebhookFinanceRecord | None = Field(default=None, description="Связанная запись")


# --- Конверт уведомления ----------------------------------------------------


class _WebhookBase(_WebhookModel):
    """Базовые поля webhook-уведомления (верхний уровень)."""

    company_id: int = Field(description="ID филиала")
    resource_id: int = Field(description="ID сущности, по которой произошло событие")
    status: WebhookStatus = Field(description="Тип события: create, update или delete")


class StaffWebhook(_WebhookBase):
    """Webhook по сотрудникам."""

    resource: Literal["staff"] = Field(description="Тип ресурса")
    data: StaffWebhookData | None = Field(default=None, description="Данные сотрудника")


class GoodWebhook(_WebhookBase):
    """Webhook по товарам."""

    resource: Literal["good"] = Field(description="Тип ресурса")
    data: GoodWebhookData | None = Field(default=None, description="Данные товара")


class ServiceWebhook(_WebhookBase):
    """Webhook по услугам."""

    resource: Literal["service"] = Field(description="Тип ресурса")
    data: ServiceWebhookData | None = Field(default=None, description="Данные услуги")


class ServiceCategoryWebhook(_WebhookBase):
    """Webhook по категориям услуг."""

    resource: Literal["service_category"] = Field(description="Тип ресурса")
    data: ServiceCategoryWebhookData | None = Field(
        default=None, description="Данные категории услуг"
    )


class ClientWebhook(_WebhookBase):
    """Webhook по клиентам."""

    resource: Literal["client"] = Field(description="Тип ресурса")
    data: ClientWebhookData | None = Field(default=None, description="Данные клиента")


class RecordWebhook(_WebhookBase):
    """Webhook по записям в журнале."""

    resource: Literal["record"] = Field(description="Тип ресурса")
    data: RecordWebhookData | None = Field(default=None, description="Данные записи")


class GoodsOperationsWebhook(_WebhookBase):
    """Webhook по товарным операциям (все пять типов).

    ``resource`` принимает значения ``goods_operations_sale`` (продажа),
    ``goods_operations_receipt`` (приход), ``goods_operations_consumable``
    (списание расходников), ``goods_operations_stolen`` (списание товара)
    и ``goods_operations_move`` (перемещение; для него формируется только
    событие ``create``).
    """

    resource: Literal[
        "goods_operations_sale",
        "goods_operations_receipt",
        "goods_operations_consumable",
        "goods_operations_stolen",
        "goods_operations_move",
    ] = Field(description="Тип ресурса")
    data: GoodsOperationsWebhookData | None = Field(
        default=None, description="Данные операции"
    )


class FinancesOperationWebhook(_WebhookBase):
    """Webhook по финансовым операциям."""

    resource: Literal["finances_operation"] = Field(description="Тип ресурса")
    data: FinancesOperationWebhookData | None = Field(
        default=None, description="Данные финансовой операции"
    )


class UnknownWebhook(_WebhookBase):
    """Webhook с неизвестным типом ресурса.

    Используется как запасной вариант в :func:`parse_webhook`, если YCLIENTS
    пришлёт ресурс, которого нет в текущих моделях. Исходное значение
    ``resource`` доступно как обычное поле, остальное -- в ``model_extra``.
    """

    resource: str = Field(description="Тип ресурса")
    data: dict[str, Any] | None = Field(default=None, description="Данные события")


# Дискриминированное объединение: pydantic сам выберет нужный класс по полю
# resource, а статически по event.resource сужается тип в match/case.
YclientsWebhook = Annotated[
    StaffWebhook | GoodWebhook | ServiceWebhook | ServiceCategoryWebhook | ClientWebhook | RecordWebhook | GoodsOperationsWebhook | FinancesOperationWebhook,
    Field(discriminator="resource"),
]

_webhook_adapter: TypeAdapter[YclientsWebhook] = TypeAdapter(YclientsWebhook)


def parse_webhook(payload: str | bytes | dict[str, Any]) -> YclientsWebhook | UnknownWebhook:
    """Разобрать тело webhook-уведомления YCLIENTS.

    Принимает сырое тело запроса (``str``/``bytes``) или уже разобранный
    ``dict`` и возвращает типизированное событие; нужный класс выбирается
    по полю ``resource``::

        event = parse_webhook(body)
        match event.resource:
            case "record":
                ...  # event: RecordWebhook
            case "client":
                ...  # event: ClientWebhook
            case _:
                ...  # неизвестный ресурс -> UnknownWebhook

    Для неизвестного типа ресурса возвращается :class:`UnknownWebhook`
    (чтобы обработчик не падал на новых событиях YCLIENTS). Совсем
    некорректное тело (не JSON, нет ``company_id`` и т.п.) приводит
    к ``pydantic.ValidationError``.
    """
    try:
        if isinstance(payload, str | bytes):
            return _webhook_adapter.validate_json(payload)
        return _webhook_adapter.validate_python(payload)
    except ValidationError:
        return UnknownWebhook.model_validate(payload)
