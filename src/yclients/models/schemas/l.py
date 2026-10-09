"""Модели YCLIENTS API (l: L).

Сгенерировано scripts/generate.py -- не редактируйте вручную.
"""

from __future__ import annotations

from datetime import date, datetime
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class LabelsClientsResponse200DataTypesDataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор категории")
    salon_id: float | None = Field(default=None, description="Идентификатор филиала")
    title: str | None = Field(default=None, description="Название категории")
    color: str | None = Field(default=None, description="Цвет метки в формате #RRGGBB")
    icon: str | None = Field(default=None, description="Название иконки")
    entity: float | None = Field(default=None, description="Объект категории (1 - категория для клиентов, 2 - категория для записей)")
    deleted: float | None = Field(default=None, description="Метка удаления")
    not_editable: float | None = Field(default=None, description="Разрешены ли изменения категории (1 - разрешены, 0 - не разрешены)")


class LabelsClientsResponse200DataTypesMeta(BaseModel):
    """Метаданные (содержит номер страницы и количество найденных категорий)
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    page_: int | None = Field(default=None, alias="page", description="Номер страницы")
    total_count: int | None = Field(default=None, description="Количество категорий")


class LabelsCompanyEntityResponse200DataTypesItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор категории")
    salon_id: float | None = Field(default=None, description="Идентификатор филиала")
    title: str | None = Field(default=None, description="Название категории")
    color: str | None = Field(default=None, description="Цвет метки в формате #RRGGBB")
    icon: str | None = Field(default=None, description="Название иконки")
    entity: float | None = Field(default=None, description="Объект категории (1 - категория для клиентов, 2 - категория для записей)")
    deleted: float | None = Field(default=None, description="Метка удаления")
    not_editable: float | None = Field(default=None, description="Разрешены ли изменения категории (1 - разрешены, 0 - не разрешены)")


class LabelsCreateResponse200DataTypesData(BaseModel):
    """Объект с данными
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    title: str | None = Field(default=None, description="Название категории")
    salon_id: float | None = Field(default=None, description="Идентификатор филиала, которому принадлежит категория")
    color: str | None = Field(default=None, description="Цвет метки в формате #RRGGBB")
    entity: float | None = Field(default=None, description="Объект категории (1 - категория для клиентов, 2 - категория для записей)")
    id_: str | None = Field(default=None, alias="id", description="Идентификатор категории")


class LoyaltyAbonementsResponseDataTypesDataItemBalanceContainerLinksItemCategory(BaseModel):
    """Категория услуг
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор услуги")
    category_id: int | None = Field(default=None, description="Идентификатор категории услуг")
    title: str | None = Field(default=None, description="Название услуги")


class LoyaltyAbonementsResponseDataTypesDataItemStatus(BaseModel):
    """Текущий статус абонемента
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор статуса")
    title: str | None = Field(default=None, description="Название статуса")
    extended_title: str | None = Field(default=None, description="Полное название статуса")


class LoyaltyAbonementsResponseDataTypesDataItemTypeBalanceContainerLinksItemCategory(BaseModel):
    """Категория услуг
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор услуги")
    category_id: int | None = Field(default=None, description="Идентификатор категории услуг")
    title: str | None = Field(default=None, description="Название услуги")


class LoyaltyAbonementsResponseDataTypesMeta(BaseModel):
    """Метаданные (содержит количество найденных абонементов)
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    count_: int | None = Field(default=None, alias="count")


class LoyaltyAbonementsTypeSearchResponseDataTypesDataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор типа абонемента")
    salon_group_id: float | None = Field(default=None, description="Идентификатор сети, в которой действует тип абонемента")
    title: str | None = Field(default=None, description="Название типа абонемента")
    period: float | None = Field(default=None, description="Срок действия абонемента (0, если не задан)")
    period_unit_id: float | None = Field(default=None, description="Единица измерения срока действия абонемента (список возможных значений, если не задан - 0)")
    allow_freeze: bool | None = Field(default=None, description="Допускается ли заморозка абонементов? true - допускается, false - не допускается")
    freeze_limit: float | None = Field(default=None, description="Максимальный общий период заморозки (дни)")
    is_allow_empty_code: bool | None = Field(default=None, description="Разрешить продажу абонемента без кода? true - разрешить, false - не разрешать")
    is_united_balance: bool | None = Field(default=None, description="Общий или раздельный баланс абонемента: true - общий, false - раздельный")
    united_balance_services_count: float | None = Field(default=None, description="Количество посещений для общего баланса")


class LoyaltyAbonementsTypeSearchResponseDataTypesMeta(BaseModel):
    """Метаданные (содержит количество найденных типов абонементов)
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    count_: int | None = Field(default=None, alias="count")


class LoyaltyCardTypesResponseDataTypesItemSalonGroup(BaseModel):
    """Объект, содержащий в себе поля "id" и "title": идентификатор сети, где создан тип карты и название этой сети
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор сети, где создан тип карты")
    title: str | None = Field(default=None, description="Название сети, где создан тип карты")


class LoyaltyCardsResponseDataTypesProgramsItemLoyaltyType(BaseModel):
    """Объект с информацией о акции
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор типа акции")
    title: str | None = Field(default=None, description="Название типа акции")
    is_discount: bool | None = Field(default=None, description="Скидка")
    is_cashback: bool | None = Field(default=None, description="Кэшбэк")
    is_static: bool | None = Field(default=None, description="Фиксированная скидка")
    is_accumulative: bool | None = Field(default=None, description="Накопительная скидка")


class LoyaltyCardsResponseDataTypesProgramsItemRulesItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор правила")
    loyalty_program_id: int | None = Field(default=None, description="Идентификатор акции, к которой привязано правило")
    loyalty_type_id: int | None = Field(default=None, description="Идентификатор типа акции")
    value: int | None = Field(default=None, description="Значение от которого сработает правило")
    parameter: int | None = Field(default=None)


class LoyaltyCardsResponseDataTypesSalonGroup(BaseModel):
    """Объект, содержащий в себе поля "id" и "title": идентификатор сети, где создан тип карты и название этой сети
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id")
    title: str | None = Field(default=None)


class LoyaltyCardsResponseDataTypesType(BaseModel):
    """Объект, содержащий в себе поля "id" и "title": идентификатор типа карты и название типа карты, соотвественно
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id")
    title: str | None = Field(default=None)
    salon_group_id: int | None = Field(default=None)


class LoyaltyCertificateTypeSearchResponseDataTypesDataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор типа сертификата")
    title: str | None = Field(default=None, description="Название типа сертификата")
    balance: float | None = Field(default=None, description="Номинал сертификата")
    is_multi: bool | None = Field(default=None, description="Тип списания: true - многократное списание, false - однократное списание")
    company_group_id: float | None = Field(default=None, description="Идентификатор сети, в которой действует тип сертификата")
    item_type_id: float | None = Field(default=None, description="Ограничение применения (список возможных значений)")
    expiration_type_id: float | None = Field(default=None, description="Ограничение срока действия (список возможных значений)")
    expiration_date: str | None = Field(default=None, description="Фиксированная дата сгорания в формате ISO8601 (null, если не задана)")
    expiration_timeout: float | None = Field(default=None, description="Срок действия сертификата с момента продажи (0, если не задан)")
    expiration_timeout_unit_id: float | None = Field(default=None, description="Единица измерения срока действия сертификата с момента продажи (список возможных значений, если не задан - 0)")
    is_allow_empty_code: bool | None = Field(default=None, description="Разрешить продажу сертификата без кода? true - разрешить, false - не разрешать")


class LoyaltyCertificateTypeSearchResponseDataTypesMeta(BaseModel):
    """Метаданные (содержит количество найденных типов сертификатов)
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    count_: int | None = Field(default=None, alias="count")


class LoyaltyCertificatesResponseDataTypesDataItemStatus(BaseModel):
    """Объект с информацией о текущем статусе сертификата
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор статуса")
    title: str | None = Field(default=None, description="Название статуса")


class LoyaltyCertificatesResponseDataTypesDataItemTypeItemType(BaseModel):
    """Объект с item_type_id и его названием
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор ограничения срока действия")
    title: str | None = Field(default=None, description="Название ограничения")


class LoyaltyCertificatesResponseDataTypesMeta(BaseModel):
    """Метаданные (содержит количество найденных сертификатов)
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    count_: int | None = Field(default=None, alias="count")


class LoyaltyTransactionDataItemType(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id")
    title: str | None = Field(default=None)


class LoyaltyTransactionMeta(BaseModel):
    """Метаданные (содержит количество элементов в ответе)
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    count_: int | None = Field(default=None, alias="count")


class Label(BaseModel):
    """Схема спеки: Объект модели "Категория"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор категории.")
    title: str | None = Field(default=None, description="Наименование категории.")
    color: str | None = Field(default=None, description="Цвет категории (#rrggbb).")


class LabelsClientsResponse200DataTypes(BaseModel):
    """Клиентские категории филиала
    Схема спеки: Root Type for labels_clients_response200_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: list[LabelsClientsResponse200DataTypesDataItem] | None = Field(default=None, alias="data", description="Массив с объектами данных")
    meta: LabelsClientsResponse200DataTypesMeta | None = Field(default=None)


class LabelsCreateResponse200DataTypes(BaseModel):
    """Создание категории
    Схема спеки: Root Type for labels_create_response200_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: LabelsCreateResponse200DataTypesData | None = Field(default=None, alias="data")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")


class LabelsUpdateRequestDataTypes(BaseModel):
    """Обновить категорию
    Схема спеки: Root Type for labels_update_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    title: str | None = Field(default=None, description="Название категории")
    color: str | None = Field(default=None, description="Цвет метки в формате #RRGGBB")
    entity: float | None = Field(default=None, description="Объект категории (1 - категория для клиентов, 2 - категория для записей)")
    icon: str | None = Field(default=None, description="Название иконки")


class LicenseOption2(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float = Field(alias="id", description="id опции")
    title: str = Field(description="Название опции")


class LoyaltyAbonementsTypeSearchResponseDataTypes(BaseModel):
    """Получить список доступных типов абонементов
    Схема спеки: Root Type for loyalty_abonements_type_search_reaponse_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: list[LoyaltyAbonementsTypeSearchResponseDataTypesDataItem] | None = Field(default=None, alias="data", description="Массив с объектами данных")
    meta: LoyaltyAbonementsTypeSearchResponseDataTypesMeta | None = Field(default=None)


class LoyaltyCard2(BaseModel):
    """Карта лояльности
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор карты")
    balance: float | None = Field(default=None, description="Баланс карты")
    points: float | None = Field(default=None, description="Очки")
    paid_amount: float | None = Field(default=None, description="Сумма \\\"Оплачено\\\"")
    sold_amount: float | None = Field(default=None, description="Сумма \\\"Продано\\\"")
    visits_count: float | None = Field(default=None, description="Количество визитов")
    number: str | None = Field(default=None, description="Номер карты")
    type_id: float | None = Field(default=None, description="Идентификатор типа карты")
    salon_group_id: float | None = Field(default=None, description="Идентификатор сети")
    max_discount_percent: float | None = Field(default=None, description="Максимальный процент скидки")
    max_discount_amount: float | None = Field(default=None, description="Максимальная фиксированная скидка")


class LoyaltyCardType2(BaseModel):
    """Тип карты лояльности
    Схема спеки: Root Type for LoyaltyCardType
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор типа карты")
    title: str | None = Field(default=None, description="Название типа карты")


class LoyaltyCardsRequestDataTypes(BaseModel):
    """Выдать карту лояльности
    Схема спеки: Root Type for loyalty_cards_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    loyalty_card_number: str | None = Field(default=None, description="Номер карты лояльности")
    loyalty_card_type_id: str | None = Field(default=None, description="Идентификатор типа карты лояльности")
    phone: float | None = Field(default=None, description="Номер телефона клиента в формате 70001234567")


class LoyaltyCertificateTypeSearchResponseDataTypes(BaseModel):
    """Получить список доступных типов сертификатов
    Схема спеки: Root Type for loyalty_certificate_type_search_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: list[LoyaltyCertificateTypeSearchResponseDataTypesDataItem] | None = Field(default=None, alias="data", description="Массив объектов с данными")
    meta: LoyaltyCertificateTypeSearchResponseDataTypesMeta | None = Field(default=None)


class LoyaltyEntityAttendanceItem2(BaseModel):
    """Сущность, к которой применяется акция (при выборочном применении)
    Схема спеки: Root Type for LoyaltyEntityAttendanceItem
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор связанной сущности")
    title: str | None = Field(default=None, description="Название связанной сущности")
    is_service: bool | None = Field(default=None, description="Флаг: true - услуга/категория услуг, false - товар/категория товаров")
    is_category: bool | None = Field(default=None, description="Флаг: true - категория услуг/товаров, false - услуга/товар")


class LoyaltyGenerateCode200DataOption2(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    code: str = Field(description="Сгенерированный код")


class LoyaltyNotificationMessageTemplate2(BaseModel):
    """Шаблон уведомлений лояльности
    Схема спеки: Root Type for LoyaltyNotificationMessageTemplate
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор шаблона")
    type_: Literal["big", "mid", "small", "custom"] | None = Field(default=None, alias="type", description="Вариант шаблона")
    body: str | None = Field(default=None, description="Текст шаблона")
    message_type: Literal["loyalty_discount_expiration", "loyalty_cashback_expiration", "loyalty_discount_increased", "loyalty_discount_decreased", "loyalty_card_created", "loyalty_card_withdraw", "loyalty_withdraw_cancelled", "loyalty_card_manual", "loyalty_card_manual_withdraw", "loyalty_card_cashback", "loyalty_card_cashback_cancelled", "loyalty_card_income", "loyalty_discount_changed", "loyalty_cashback_changed", "loyalty_settings_abonement_notification"] | None = Field(default=None, description="Тип сообщения")


class LoyaltyNotificationMessageTemplateRequest2(BaseModel):
    """Тело запроса на привязку шаблона уведомления лояльности
    Схема спеки: Root Type for LoyaltyNotificationMessageTemplateRequest
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    type_: Literal["none", "big", "mid", "small", "custom"] | None = Field(default=None, alias="type", description="Вариант шаблона")
    body: str | None = Field(default=None, description="Текст шаблона (только для варианта \"пользовательский\")")


class LoyaltyProgramRule2(BaseModel):
    """Правило для акции лояльности
    Схема спеки: Root Type for LoyaltyProgramRule
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор правила")
    parameter: int | None = Field(default=None, description="Пороговое значение правила (0 для фиксированных типов акций)")
    value: float | None = Field(default=None, description="Значение скидкии или бонуса")
    loyalty_program_id: int | None = Field(default=None, description="Идентификатор акции лояльности")
    loyalty_type_id: int | None = Field(default=None, description="Идентификатор типа акции лояльности")
    service_id: int | None = Field(default=None, description="Идентификатор услуги (только для акции \"Скидка по условию\")")


class LoyaltyProgramRuleRequest2(BaseModel):
    """Тело запроса на изменение правила для акции лояльности
    Схема спеки: Root Type for LoyaltyProgramRuleRequest
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    parameter: int | None = Field(default=None, description="Пороговое значение правила (0 для фиксированных типов акций)")
    value: float | None = Field(default=None, description="Значение скидкии или бонуса")
    service_id: int | None = Field(default=None, description="Идентификатор услуги (только для акции \"Скидка по условию\")")


class LoyaltyAbonementsResponseDataTypesDataItemBalanceContainerLinksItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    count_: int | None = Field(default=None, alias="count", description="Количество применений")
    category: LoyaltyAbonementsResponseDataTypesDataItemBalanceContainerLinksItemCategory | None = Field(default=None)


class LoyaltyAbonementsResponseDataTypesDataItemTypeBalanceContainerLinksItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    count_: int | None = Field(default=None, alias="count", description="Количество применений")
    category: LoyaltyAbonementsResponseDataTypesDataItemTypeBalanceContainerLinksItemCategory | None = Field(default=None)


class LoyaltyCardTypesResponseDataTypesItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор типа карты")
    title: str | None = Field(default=None, description="Название типа карты")
    salon_group_id: int | None = Field(default=None, description="Идентификатор сети, где создан тип карты")
    salon_group: LoyaltyCardTypesResponseDataTypesItemSalonGroup | None = Field(default=None)


class LoyaltyCardsResponseDataTypesProgramsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор акции")
    title: str | None = Field(default=None, description="Название акции")
    value: int | None = Field(default=None, description="Значение, от которого сработает правило")
    loyalty_type_id: int | None = Field(default=None, description="Идентификатор типа акции")
    item_type_id: int | None = Field(default=None, description="Начисляется ли кэшбек от товаров")
    value_unit_id: int | None = Field(default=None, description="Поле \"Бонус\". Скидка % или Фикс. сумма")
    group_id: int | None = Field(default=None, description="Идентификатор сети, где создана акция")
    loyalty_type: LoyaltyCardsResponseDataTypesProgramsItemLoyaltyType | None = Field(default=None)
    rules: list[LoyaltyCardsResponseDataTypesProgramsItemRulesItem] | None = Field(default=None, description="Массив с информацией о правилах, настроенных в акции")


class LoyaltyCertificatesResponseDataTypesDataItemType(BaseModel):
    """Объект с информацией о типе сертификата
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор типа сертификата")
    title: str | None = Field(default=None, description="Название типа сертификата")
    balance: int | None = Field(default=None, description="Номинал сертификата")
    is_multi: bool | None = Field(default=None, description="Доступен ли для многократрного списания")
    company_group_id: int | None = Field(default=None, description="Идентификатор сети, где создан тип сертификата")
    item_type_id: int | None = Field(default=None, description="Ограничение применения списания баллов. 0 - без ограничений, 1 - Только услуги, 2 - Некоторые услуги + все товары, 3 - Некоторые услуги, 4 - Только товары")
    expiration_type_id: int | None = Field(default=None, description="Идентификатор ограничения срока действия. 0 - без ограничения, 1 - фиксированная дата, 2 - фиксированный срок")
    expiration_date: str | None = Field(default=None, description="Дата сгорания всех сертифкатов. Заполняется с expiration_type_id = 1")
    expiration_timeout: int | None = Field(default=None, description="Срок действия сертифкатов. Заполняется с expiration_type_id = 2")
    expiration_timeout_unit_id: int | None = Field(default=None, description="Единицы измерения времени. 1 - День, 2 - Неделя, 3 - месяц, 4 - год")
    is_allow_empty_code: bool | None = Field(default=None, description="Продажа без кода")
    item_type: LoyaltyCertificatesResponseDataTypesDataItemTypeItemType | None = Field(default=None)


class LoyaltyTransactionDataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор транзакции")
    visit_id: float | None = Field(default=None, description="Идентификатор визита")
    status_id: float | None = Field(default=None, description="Идентификатор статуса транзакции")
    amount: float | None = Field(default=None, description="Сумма оплаты лояльностью")
    type_id: float | None = Field(default=None, description="Тип транзакции лояльности")
    card_id: float | None = Field(default=None, description="Идентификатор карты лояльности")
    program_id: float | None = Field(default=None, description="Идентификатор программы лояльности")
    certificate_id: float | None = Field(default=None, description="Идентификатор сертификата")
    abonement_id: float | None = Field(default=None, description="Идентификатор абонемента")
    salon_group_id: float | None = Field(default=None, description="ID сети салонов, в рамках лояльности которой была создана данная транзакция")
    item_id: float | None = Field(default=None, description="Идентификатор позиции в заказе, если транзакция связана с продажей товара или услуги")
    item_type_id: float | None = Field(default=None, description="Тип позиции в заказе, к которой относится данная транзакция (1 Оказание услуги, 7 Продажа товара), если применимо")
    item_record_id: float | None = Field(default=None, description="ID записи к которой относится позиция в заказе, если применимо")
    goods_transaction_id: float | None = Field(default=None, description="ID транзакции продажи товара")
    services_transaction_id: float | None = Field(default=None, description="ID транзакции оказания услуг")
    is_discount: bool | None = Field(default=None)
    is_loyalty_withdraw: bool | None = Field(default=None)
    type_: LoyaltyTransactionDataItemType | None = Field(default=None, alias="type")


class LoyaltyAbonementTypeWithSalons(BaseModel):
    """Схема спеки: Объект модели "Тип абонемента"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор типа абонемента.")
    salon_group_id: float | None = Field(default=None, description="Идентификатор сети, в которой действует тип абонемента.")
    title: str | None = Field(default=None, description="Название типа абонементы.")
    period: float | None = Field(default=None, description="Срок действия абонемента (0, если не задан).")
    period_unit_id: float | None = Field(default=None, description="Единица измерения срока действия абонемента (1 - день, 2 - неделя, 3 - месяц, 4 - год, если не задан - 0).")
    allow_freeze: bool | None = Field(default=None, description="Допускается ли заморозка абонементов: true - допускается, false - не допускается.")
    freeze_limit: float | None = Field(default=None, description="Максимальный общий период заморозки.")
    freeze_limit_unit_id: float | None = Field(default=None, description="Единица измерения срока заморозки абонемента (1 - день, 2 - неделя, 3 - месяц, 4 - год).")
    is_allow_empty_code: bool | None = Field(default=None, description="Разрешить продажу абонемента без кода: true - разрешить, false - не разрешать.")
    is_united_balance: bool | None = Field(default=None, description="Общий или раздельный баланс абонемента: true - общий, false - раздельный.")
    cost: float | None = Field(default=None, description="Цена абонемента.")
    expiration_type_id: float | None = Field(default=None, description="Тип активации абонемента (1 - при продаже, 2 - при первом использовании, 3 - с конкретной даты).")
    is_online_sale_enabled: bool | None = Field(default=None, description="Онлайн продажа (true - разрешена, false - запрещена).")
    online_sale_title: str | None = Field(default=None, description="Название абонемента при онлайн продаже.")
    online_sale_description: str | None = Field(default=None, description="Описание абонемента при онлайн продаже.")
    online_sale_price: float | None = Field(default=None, description="Цена абонемента при продаже онлайн.")
    service_price_correction: bool | None = Field(default=None, description="Возможность корректировки цены услуги при применении абонемента.")
    united_balance_services_count: float | None = Field(default=None, description="Количество посещений для общего баланса.")
    autoactivation_time: float | None = Field(default=None, description="Кол-во единиц времени для автоактивации абонемента.")
    autoactivation_time_unit_id: int | None = Field(default=None, description="Единицы измерения для автоактивации (1 - дни, 2 - недели, 3 - месяцы, 4 - годы).")
    attached_salon_ids: list[float] | None = Field(default=None, description="Список ID прикреплённых к типу абонемента филиалов.")
    online_sale_image: str | None = Field(default=None, description="Ссылка на изображение при онлайн продаже.")
    availability: list[dict[str, Any]] | None = Field(default=None, description="Список условий доступности абонемента.")
    balance_container: dict[str, Any] | None = Field(default=None, description="Объект с массивом прикрепленных услуг и/или категорий и их балансом.")


class LoyaltyCardsResponseDataTypes(BaseModel):
    """Получить список карт клиента
    Схема спеки: Root Type for loyalty_cards_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор карты лояльности")
    balance: float | None = Field(default=None, description="Баланс карты лояльности")
    points: int | None = Field(default=None)
    paid_amount: float | None = Field(default=None, description="Сумма \"Оплачено\"")
    sold_amount: float | None = Field(default=None, description="Сумма \"Продано\"")
    visits_count: int | None = Field(default=None, description="Количество визитов")
    number: str | None = Field(default=None, description="Номер карты")
    type_id: int | None = Field(default=None, description="Идентификатор типа карты лояльности")
    salon_group_id: int | None = Field(default=None, description="Идентификатор сети, где создана карта")
    type_: LoyaltyCardsResponseDataTypesType | None = Field(default=None, alias="type")
    salon_group: LoyaltyCardsResponseDataTypesSalonGroup | None = Field(default=None)
    programs: list[LoyaltyCardsResponseDataTypesProgramsItem] | None = Field(default=None, description="Массив с информацией об акциях, привязанных к карте лояльности")


class LoyaltyGenerateCode200Option2(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool = Field(description="флаг показывающий, что ответ выполнен без ошибок (true)")
    data_: LoyaltyGenerateCode200DataOption2 = Field(alias="data")
    meta: list[dict[str, Any]] = Field(description="метаданные (пустой массив)")


class LoyaltyProgram2(BaseModel):
    """Акция лояльности
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идетификатор акции")
    title: str | None = Field(default=None, description="Название акции")
    type_: Literal["discount_static", "discount_accumulative_visits", "discount_accumulative_sold", "discount_accumulative_paid", "cashback_static_sold", "cashback_static_paid", "cashback_accumulative_paid", "cashback_accumulative_sold", "cashback_accumulative_paid_visits", "cashback_accumulative_sold_visits", "cashback_sold_visits", "cashback_paid_visits", "package_discount"] | None = Field(default=None, alias="type", description="Тип акции")
    service_item_type: Literal["any_allowed", "not_allowed", "custom_allowed"] | None = Field(default=None, description="Тип применения к услугам")
    good_item_type: Literal["any_allowed", "not_allowed", "custom_allowed"] | None = Field(default=None, description="Тип применения к товарам")
    value_unit: Literal["percent", "amount"] | None = Field(default=None, description="Единица измерения бонуса или скидки (процент, фиксированная сумма)")
    usage_limit: int | None = Field(default=None, description="Ограничение по количеству применений (только для кэшбека)")
    visit_multiplicity: int | None = Field(default=None, description="Кратность применения по визитам (только для кэшбека)")
    sold_items_multiplicity: int | None = Field(default=None, description="Сколько услуг нужно оплатить, чтобы получить скидку на акционные услуги (только для типа акции \"Скидка по условию\")")
    expiration_timeout: int | None = Field(default=None, description="Срок сгорания бонусов или скидки")
    expiration_timeout_unit: Literal["day", "week", "month", "year"] | None = Field(default=None, description="Единица измерения срока сгорания бонусов или скидки")
    expiration_notification_timeout: int | None = Field(default=None, description="За сколько дней до наступления срока сгорания бонуса или скидки необходимо отправить клиенту уведомление")
    params_source_type: Literal["loyalty_card", "active_companies", "chain"] | None = Field(default=None, description="Откуда брать историю клиента для расчета размера бонуса или скидки (для накпоительных акций или скидки по условию)")
    history_start_date: str | None = Field(default=None, description="С какой даты учитывать историю клиента для расчета размера бонуса или скидки (для накопительных акций или скидки по условию)")
    on_changed_notification_template_id: int | None = Field(default=None, description="Идентификатор шаблона уведомления при изменении бонуса или скидки")
    on_expiration_notification_template_id: int | None = Field(default=None, description="Идентификатор шаблона уведомления при сгорании бонуса или скидки")
    loyalty_card_types: list[LoyaltyCardType2] | None = Field(default=None, description="Тип карт, для которых действует акция (по запросу)")
    on_changed_notification_template: LoyaltyNotificationMessageTemplate2 | None = Field(default=None)
    on_expiration_notification_template: LoyaltyNotificationMessageTemplate2 | None = Field(default=None)
    rules: list[LoyaltyProgramRule2] | None = Field(default=None, description="Правила для определения значения бонуса или скидки (допустимо только одно правило для фиксированных акций) (по запросу)")
    companies: list[Company2] | None = Field(default=None, description="Филиалы, в которых действует акция (по запросу)")
    applicable_items: list[LoyaltyEntityAttendanceItem2] | None = Field(default=None, description="Связанные сущности для выборочного применения акции (по запросу)")


class LoyaltyProgramCreateRequest2(BaseModel):
    """Тело запроса на создание акции лояльности
    Схема спеки: Root Type for LoyaltyProgramCreateRequest
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    title: str = Field(description="Название акции")
    type_: Literal["discount_static", "discount_accumulative_visits", "discount_accumulative_sold", "discount_accumulative_paid", "cashback_static_sold", "cashback_static_paid", "cashback_accumulative_paid", "cashback_accumulative_sold", "cashback_accumulative_paid_visits", "cashback_accumulative_sold_visits", "cashback_sold_visits", "cashback_paid_visits", "package_discount"] = Field(alias="type", description="Тип акции")
    service_item_type: Literal["any_allowed", "not_allowed", "custom_allowed"] = Field(description="Тип применения к услугам")
    good_item_type: Literal["any_allowed", "not_allowed", "custom_allowed"] = Field(description="Тип применения к товарам")
    value_unit: Literal["percent", "amount"] = Field(description="Единица измерения бонуса или скидки (процент, фиксированная сумма)")
    usage_limit: int | None = Field(default=None, description="Ограничение по количеству применений (только для кэшбека)")
    visit_multiplicity: int | None = Field(default=None, description="Кратность применения по визитам (только для кэшбека)")
    sold_items_multiplicity: int | None = Field(default=None, description="Сколько услуг нужно оплатить, чтобы получить скидку на акционные услуги (только для типа акции \"Скидка по условию\")")
    expiration_timeout: int | None = Field(default=None, description="Срок сгорания бонусов или скидки")
    expiration_timeout_unit: Literal["day", "week", "month", "year"] | None = Field(default=None, description="Единица измерения срока сгорания бонусов или скидки")
    expiration_notification_timeout: int | None = Field(default=None, description="За сколько дней до наступления срока сгорания бонуса или скидки необходимо отправить клиенту уведомление")
    params_source_type: Literal["loyalty_card", "active_companies", "chain"] | None = Field(default=None, description="Откуда брать историю клиента для расчета размера бонуса или скидки (для накпоительных акций или скидки по условию)")
    history_start_date: str | None = Field(default=None, description="С какой даты учитывать историю клиента для расчета размера бонуса или скидки (для накопительных акций или скидки по условию)")
    loyalty_card_type_ids: list[int] | None = Field(default=None, description="Идентификаторы типов карт, для которых действует акция")
    on_changed_notification_template: LoyaltyNotificationMessageTemplateRequest2 | None = Field(default=None)
    on_expiration_notification_template: LoyaltyNotificationMessageTemplateRequest2 | None = Field(default=None)
    rules: list[LoyaltyProgramRuleRequest2] = Field(description="Правила для определения значения бонуса или скидки (допустимо только одно правило для фиксированных акций)")
    company_ids: list[int] = Field(description="Идентификаторы филиалов, в которых действует акция")
    allowed_service_ids: list[int] | None = Field(default=None, description="Идентификаторы услуг и категорий услуг (если задан тип применения для некоторых услуг)")
    allowed_good_ids: list[int] | None = Field(default=None, description="Идентификаторы товаров (если задан тип применения для некоторых товаров)")
    allowed_good_category_ids: list[int] | None = Field(default=None, description="Идентификаторы категорий товаров (если задан тип применения для некоторых товаров)")


class LoyaltyProgramUpdateRequest2(BaseModel):
    """Тело запроса на изменение акции лояльности
    Схема спеки: Root Type for LoyaltyProgramUpdateRequest
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    title: str | None = Field(default=None, description="Название акции")
    usage_limit: int | None = Field(default=None, description="Ограничение по количеству применений (только для кэшбека)")
    expiration_timeout: int | None = Field(default=None, description="Срок сгорания бонусов или скидки")
    expiration_timeout_unit: Literal["day", "week", "month", "year"] | None = Field(default=None, description="Единица измерения срока сгорания бонусов или скидки")
    expiration_notification_timeout: int | None = Field(default=None, description="За сколько дней до наступления срока сгорания бонуса или скидки необходимо отправить клиенту уведомление")
    loyalty_card_type_ids: list[int] | None = Field(default=None, description="Идентификаторы типов карт, для которых действует акция")
    on_changed_notification_template: LoyaltyNotificationMessageTemplateRequest2 | None = Field(default=None)
    on_expiration_notification_template: LoyaltyNotificationMessageTemplateRequest2 | None = Field(default=None)
    rules: list[LoyaltyProgramRuleRequest2] | None = Field(default=None, description="Правила для определения значения бонуса или скидки (допустимо только одно правило для фиксированных акций)")
    company_ids: list[int] | None = Field(default=None, description="Идентификаторы филиалов, в которых действует акция")
    allowed_service_ids: list[int] | None = Field(default=None, description="Идентификаторы услуг и категорий услуг (если задан тип применения для некоторых услуг)")
    allowed_good_ids: list[int] | None = Field(default=None, description="Идентификаторы товаров (если задан тип применения для некоторых товаров)")
    allowed_good_category_ids: list[int] | None = Field(default=None, description="Идентификаторы категорий товаров (если задан тип применения для некоторых товаров)")


class LoyaltyTransaction2(BaseModel):
    """Транзакция лояльности
    Схема спеки: Root Type for LoyaltyTransaction
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: list[LoyaltyTransactionDataItem] | None = Field(default=None, alias="data", description="Массив объектов с данными")
    meta: LoyaltyTransactionMeta | None = Field(default=None)


class LoyaltyAbonementsResponseDataTypesDataItemBalanceContainer(BaseModel):
    """Объект включающий в себя массив links с информацией о балансе абонемента
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    links: list[LoyaltyAbonementsResponseDataTypesDataItemBalanceContainerLinksItem] | None = Field(default=None, description="Массив услуг, на которые распространяется абонемент")


class LoyaltyAbonementsResponseDataTypesDataItemTypeBalanceContainer(BaseModel):
    """Объект включающий в себя массив links с информацией о балансе абонемента
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    links: list[LoyaltyAbonementsResponseDataTypesDataItemTypeBalanceContainerLinksItem] | None = Field(default=None, description="Массив услуг, на которые распространяется абонемент")


class LoyaltyCertificatesResponseDataTypesDataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор сертификата")
    number: str | None = Field(default=None, description="Номер сертификата")
    balance: float | None = Field(default=None, description="Текущий баланс")
    default_balance: float | None = Field(default=None, description="Начальный баланс")
    type_id: int | None = Field(default=None, description="Идентификатор типа сертификата")
    status_id: int | None = Field(default=None, description="Идентификатор статуса")
    created_date: str | None = Field(default=None, description="Дата продажи")
    expiration_date: str | None = Field(default=None, description="Дата сгорания")
    type_: LoyaltyCertificatesResponseDataTypesDataItemType | None = Field(default=None, alias="type")
    status: LoyaltyCertificatesResponseDataTypesDataItemStatus | None = Field(default=None)


class LoyaltyCertificatesResponseDataTypes(BaseModel):
    """Получить сертификаты
    Схема спеки: Root Type for loyalty_certificates_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: list[LoyaltyCertificatesResponseDataTypesDataItem] | None = Field(default=None, alias="data", description="Массив объектов с данными")
    meta: LoyaltyCertificatesResponseDataTypesMeta | None = Field(default=None)


class LoyaltyAbonementsResponseDataTypesDataItemType(BaseModel):
    """Объект с информацией о типе абонемента
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор типа абонемента")
    salon_group_id: int | None = Field(default=None, description="Идентификатор сети, в которой действует тип абонемента")
    title: str | None = Field(default=None, description="Название типа абонементы")
    period: int | None = Field(default=None, description="Срок действия абонемента (0, если не задан)")
    period_unit_id: int | None = Field(default=None, description="Единица измерения срока действия абонемента (список возможных значений, если не задан - 0)")
    allow_freeze: bool | None = Field(default=None, description="Допускается ли заморозка абонементов? true - допускается, false - не допускается")
    freeze_limit: int | None = Field(default=None, description="Максимальный общий период заморозки (дни)")
    is_allow_empty_code: bool | None = Field(default=None, description="Разрешить продажу абонемента без кода? true - разрешить, false - не разрешать")
    is_united_balance: bool | None = Field(default=None, description="Общий или раздельный баланс абонемента: true - общий, false - раздельный")
    united_balance_services_count: int | None = Field(default=None, description="Количество посещений для общего баланса")
    balance_container: LoyaltyAbonementsResponseDataTypesDataItemTypeBalanceContainer | None = Field(default=None)


class LoyaltyAbonementsResponseDataTypesDataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор абонемента")
    number: str | None = Field(default=None, description="Код абонемента")
    balance_string: str | None = Field(default=None, description="Название услуги, с количеством использований")
    is_frozen: bool | None = Field(default=None, description="Заморожен ли абонемент")
    freeze_period: int | None = Field(default=None, description="Период, который абонемент был заморожен")
    period: int | None = Field(default=None, description="Значение срока действия абонемента")
    period_unit_id: int | None = Field(default=None, description="Идентификатор единиц измерения срока действия. 1 - день, 2 - неделя, 3 - месяц, 4 - год")
    expiration_date: str | None = Field(default=None, description="Дата сгорания абонемента")
    status: LoyaltyAbonementsResponseDataTypesDataItemStatus | None = Field(default=None)
    balance_container: LoyaltyAbonementsResponseDataTypesDataItemBalanceContainer | None = Field(default=None)
    type_: LoyaltyAbonementsResponseDataTypesDataItemType | None = Field(default=None, alias="type")


class LoyaltyAbonementsResponseDataTypes(BaseModel):
    """Получить список абонементов клиента
    Схема спеки: Root Type for loyalty_abonements_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: list[LoyaltyAbonementsResponseDataTypesDataItem] | None = Field(default=None, alias="data", description="Массив объектов с данными")
    meta: LoyaltyAbonementsResponseDataTypesMeta | None = Field(default=None)

__all__ = [
    "Label",
    "LabelsClientsResponse200DataTypes",
    "LabelsClientsResponse200DataTypesDataItem",
    "LabelsClientsResponse200DataTypesMeta",
    "LabelsCompanyEntityResponse200DataTypesItem",
    "LabelsCreateResponse200DataTypes",
    "LabelsCreateResponse200DataTypesData",
    "LabelsUpdateRequestDataTypes",
    "LicenseOption2",
    "LoyaltyAbonementTypeWithSalons",
    "LoyaltyAbonementsResponseDataTypes",
    "LoyaltyAbonementsResponseDataTypesDataItem",
    "LoyaltyAbonementsResponseDataTypesDataItemBalanceContainer",
    "LoyaltyAbonementsResponseDataTypesDataItemBalanceContainerLinksItem",
    "LoyaltyAbonementsResponseDataTypesDataItemBalanceContainerLinksItemCategory",
    "LoyaltyAbonementsResponseDataTypesDataItemStatus",
    "LoyaltyAbonementsResponseDataTypesDataItemType",
    "LoyaltyAbonementsResponseDataTypesDataItemTypeBalanceContainer",
    "LoyaltyAbonementsResponseDataTypesDataItemTypeBalanceContainerLinksItem",
    "LoyaltyAbonementsResponseDataTypesDataItemTypeBalanceContainerLinksItemCategory",
    "LoyaltyAbonementsResponseDataTypesMeta",
    "LoyaltyAbonementsTypeSearchResponseDataTypes",
    "LoyaltyAbonementsTypeSearchResponseDataTypesDataItem",
    "LoyaltyAbonementsTypeSearchResponseDataTypesMeta",
    "LoyaltyCard2",
    "LoyaltyCardType2",
    "LoyaltyCardTypesResponseDataTypesItem",
    "LoyaltyCardTypesResponseDataTypesItemSalonGroup",
    "LoyaltyCardsRequestDataTypes",
    "LoyaltyCardsResponseDataTypes",
    "LoyaltyCardsResponseDataTypesProgramsItem",
    "LoyaltyCardsResponseDataTypesProgramsItemLoyaltyType",
    "LoyaltyCardsResponseDataTypesProgramsItemRulesItem",
    "LoyaltyCardsResponseDataTypesSalonGroup",
    "LoyaltyCardsResponseDataTypesType",
    "LoyaltyCertificateTypeSearchResponseDataTypes",
    "LoyaltyCertificateTypeSearchResponseDataTypesDataItem",
    "LoyaltyCertificateTypeSearchResponseDataTypesMeta",
    "LoyaltyCertificatesResponseDataTypes",
    "LoyaltyCertificatesResponseDataTypesDataItem",
    "LoyaltyCertificatesResponseDataTypesDataItemStatus",
    "LoyaltyCertificatesResponseDataTypesDataItemType",
    "LoyaltyCertificatesResponseDataTypesDataItemTypeItemType",
    "LoyaltyCertificatesResponseDataTypesMeta",
    "LoyaltyEntityAttendanceItem2",
    "LoyaltyGenerateCode200DataOption2",
    "LoyaltyGenerateCode200Option2",
    "LoyaltyNotificationMessageTemplate2",
    "LoyaltyNotificationMessageTemplateRequest2",
    "LoyaltyProgram2",
    "LoyaltyProgramCreateRequest2",
    "LoyaltyProgramRule2",
    "LoyaltyProgramRuleRequest2",
    "LoyaltyProgramUpdateRequest2",
    "LoyaltyTransaction2",
    "LoyaltyTransactionDataItem",
    "LoyaltyTransactionDataItemType",
    "LoyaltyTransactionMeta"
]
