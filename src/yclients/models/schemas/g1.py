"""Модели YCLIENTS API (g1: G).

Сгенерировано scripts/generate.py -- не редактируйте вручную.
"""

from __future__ import annotations

from datetime import date, datetime
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class GetApplicationApplicationIdResponse200DataConnectionStatus(BaseModel):
    """Модель статуса установки приложения в салоне
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    status: Literal["pending", "freezed", "active"] | None = Field(default=None, description="Статус установки приложения в салоне. Pending - ждет активации от партнера, Freezed - заморожено по причине неуплаты, Active - активно")
    created_at: str | None = Field(default=None, description="Дата создания связки Приложение-Салон")


class GetApplicationApplicationIdResponse200DataLogsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    changed_at: str | None = Field(default=None, description="Дата смены статуса")
    status_from: str | None = Field(default=None, description="Предыдущий статус приложения в салоне")
    status_to: str | None = Field(default=None, description="Новый статус приложения в салоне")
    source: str | None = Field(default=None, description="Источник изменения статуса")


class GetApplicationApplicationIdResponse200DataPaymentsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="ID платежа.")
    payment_sum: float | None = Field(default=None, description="Сумма оплаты за период.")
    payment_date: str | None = Field(default=None, description="Дата оплаты.")
    is_refunded: bool | None = Field(default=None, description="Был ли возврат платежа.")
    currency_iso: str | None = Field(default=None, description="ISO валюты платежа")
    period_from: str | None = Field(default=None, description="Дата начала подписки")
    period_to: str | None = Field(default=None, description="Дата окончания подписки")


class GetApplicationIdTariffsResponse200DataItemOptionsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="ID Опции тарифа.")
    title: str | None = Field(default=None, description="Название опции тарифа.")
    overall_price: float | None = Field(default=None, description="Общая стоимость опции тарифа.")
    duration_in_months: bool | None = Field(default=None, description="Длина в месяцах основного тела тарифа.")
    currency_iso: str | None = Field(default=None, description="ISO валюты тарифа")
    staff_amount: float | None = Field(default=None, description="Максимальное количество сотрудников тарифа YCLIENTS, доступные для приобретения данной опции")
    free_period_in_months: float | None = Field(default=None, description="Длина в месяцах подарочного периода")


class GetApplicationPaymentLinkResponse200Data(BaseModel):
    """Объект со ссылкой на оплату
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    url: str | None = Field(default=None, description="Адрес страницы оплаты.")


class GetIntegrationCallsRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    salon_id: float = Field(description="Идентификатор салона.")
    date_from: str = Field(description="Дата начала выборки.")
    date_to: str = Field(description="Дата окончания выборки.")
    phone: str | None = Field(default=None, description="Номер телефона.")
    types: list[Literal["incoming", "outgoing", "internal"]] | None = Field(default=None, description="Набор типов звонка")
    statuses: list[Literal["success", "missed", "cancel", "busy", "notallowed", "notavailable", "notfound"]] | None = Field(default=None, description="Набор статусов")
    page_: float | None = Field(default=None, alias="page", description="Номер страницы")
    limit: float | None = Field(default=None, description="Количество элементов на странице")


class GetIntegrationCallsResponse200DataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="ID звонка")
    client_id: int | None = Field(default=None, description="ID клиента (при наличии клиента в КБ)")
    caller_phone: str | None = Field(default=None, description="Номер телефона")
    record_link: str | None = Field(default=None, description="Ссылка на запись звонка (при наличии)")
    duration: int | None = Field(default=None, description="Продолжительность звонка в секундах")
    status: Literal["success", "missed", "cancel", "busy", "notallowed", "notavailable", "notfound"] | None = Field(default=None, description="Статус дозвона")
    type_: Literal["incoming", "outgoing", "internal"] | None = Field(default=None, alias="type", description="Тип звонка")
    call_date: str | None = Field(default=None, description="Дата и время звонка")


class GetStaffIdDateResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    time: str = Field(description="Время сеанса")
    is_free: bool = Field(description="Свободно время или нет")


class GetStartDateEndDateResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    date: str = Field(description="дата в формате iso8601.")
    is_working: bool = Field(description="Свободно время или нет.")
    slots: list[dict[str, Any]] | None = Field(default=None, description="Массив (from, to) промежутков рабочего времени.")


class GoodsCategoriesPostPutResponseDataTypesData(BaseModel):
    """Объект с данными
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор категории товара")
    title: str | None = Field(default=None, description="Название категории товара")
    parent_category_id: int | None = Field(default=None, description="Идентификатор родительской категории товара (может содержать значение null, в случае, если родительская категория товаров отсутствует)")


class GoodsCategoriesResponse200DataTypesDataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: str | None = Field(default=None, alias="id", description="Идентификатор категории товаров")
    title: str | None = Field(default=None, description="Название категории товаров")


class GoodsCategoryNodeResponse200DataTypesDataChildrenItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    parent_id: float | None = Field(default=None, description="Идентификатор родительского элемента (0 для корневых элементов)")
    item_id: float | None = Field(default=None, description="Идентификатор товара (0, если элемент - категория)")
    category_id: float | None = Field(default=None, description="Идентификатор товарной категории (0, если элемент - товар)")
    title: str | None = Field(default=None, description="Название товара или товарной категории")
    is_chain: bool | None = Field(default=None, description="Является ли элемент привязанным к сети? true - элемент привязан к сети, false - не привязан")
    is_category: bool | None = Field(default=None, description="Является ли элемент категорией? true - категория, false - товар")
    is_item: bool | None = Field(default=None, description="Является ли элемент товаром? true - товар, false - категория")


class GoodsCompanyGoodsIdResponse200DataTypesDataItemActualAmountsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    storage_id: str | None = Field(default=None, description="ID склада")
    amount: str | None = Field(default=None, description="Количество")


class GoodsCompanyRequestWithRulesDataTypeCorrectionRulesItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    type_: int | None = Field(default=None, alias="type", description="Тип операции")
    base_unit: str | None = Field(default=None, description="Основные единицы при корректировке")


class GoodsSearchResponse200DataTypesDataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    parent_id: float | None = Field(default=None, description="Идентификатор родительского элемента (0 для корневых элементов)")
    item_id: float | None = Field(default=None, description="Идентификатор товара (0, если элемент - категория)")
    category_id: float | None = Field(default=None, description="Идентификатор товарной категории (0, если элемент - товар)")
    title: str | None = Field(default=None, description="Название товара или товарной категории")
    is_chain: bool | None = Field(default=None, description="Является ли элемент привязанным к сети? true - элемент привязан к сети, false - не привязан")
    is_category: bool | None = Field(default=None, description="Является ли элемент категорией? true - категория, false - товар")
    is_item: bool | None = Field(default=None, description="Является ли элемент товаром? true - товар, false - категория")


class GoodsSearchResponse200DataTypesMeta(BaseModel):
    """Метаданные (содержит количество найденных категорий)
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    count_: int | None = Field(default=None, alias="count")


class GroupGroupidClientsResponseDataTypesDataClientsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор клиента")
    company_id: float | None = Field(default=None, description="Идентификатор филиала")
    name: str | None = Field(default=None, description="Имя клиента")
    email: str | None = Field(default=None, description="Email клиента")


class GroupsResponseDataTypesDataItemAccess(BaseModel):
    """Права доступа пользователя в сети
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    settings_access: str | None = Field(default=None, description="true - есть доступ к разделу настройки, false - нет доступа")
    clients_access: str | None = Field(default=None, description="true - есть доступ к клиентской базе, false - нет доступа")
    users_access: str | None = Field(default=None, description="true - есть доступ к управлению пользователями, false - нет доступа")
    loyalty_access: str | None = Field(default=None, description="true - есть доступ к лояльности, false - нет доступа")
    loyalty_cards_manual_transactions_access: str | None = Field(default=None, description="true - есть доступ к ручному пополнению/списанию с карт лояльности, false - нет доступа")
    network_services_access: str | None = Field(default=None, description="true - есть доступ к управлению сетевыми услугами, false - нет доступа")


class GroupsResponseDataTypesDataItemCompaniesItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор компании")
    title: str | None = Field(default=None, description="Название компании")


class GoodsCategoriesPostPutResponseDataTypes(BaseModel):
    """Создать категорию товаров
    Схема спеки: Root Type for goods_categories_response201_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения")
    data_: GoodsCategoriesPostPutResponseDataTypesData | None = Field(default=None, alias="data")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")


class GoodsCategoriesRequestDataTypes(BaseModel):
    """Создать категорию товаров
    Схема спеки: Root Type for goods_categories_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    title: str = Field(description="Название категории товаров")
    parent_category_id: int | None = Field(default=None, description="Инедтификатор родительской категории (параметр необязательный, но может принимать значение 0 или null, в случае, когда не нужно указывать родительскую категорию)")
    article: str | None = Field(default=None, description="Артикул")
    comment: str | None = Field(default=None, description="Комментарий")


class GoodsCategoriesResponse200DataTypes(BaseModel):
    """Получить список категорий товаров
    Схема спеки: Root Type for goods_categories_response200_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: list[GoodsCategoriesResponse200DataTypesDataItem] | None = Field(default=None, alias="data", description="Массив объектов с данными")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")


class GoodsCompanyRequestDataType(BaseModel):
    """Метод создания товара
    Схема спеки: Root Type for goods_company_request_data_type
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    title: str = Field(description="Название товара")
    print_title: str | None = Field(default=None, description="Название для печати в чеке")
    article: str | None = Field(default=None, description="Артикул")
    barcode: str | None = Field(default=None, description="Штрих-код")
    category_id: int = Field(description="Идентификатор категории товара")
    cost: float | None = Field(default=None, description="Цена продажи")
    actual_cost: float | None = Field(default=None, description="Себестоимость")
    sale_unit_id: int = Field(description="Единица измерения для продажи")
    service_unit_id: int = Field(description="Единица измерения для списания")
    unit_equals: float | None = Field(default=None, description="Отношение ед.имзерения для продажи к ед.измерения для списания")
    critical_amount: float | None = Field(default=None, description="Критичный остаток")
    desired_amount: float | None = Field(default=None, description="Желаемый остаток")
    netto: float | None = Field(default=None, description="Масса нетто")
    brutto: float | None = Field(default=None, description="Масса брутто")
    comment: str | None = Field(default=None, description="Комментарий")
    tax_variant: int | None = Field(default=None, description="Система налогообложения")
    vat_id: int | None = Field(default=None, description="НДС")


class GoodsCompanyRequestWithRulesDataType(BaseModel):
    """Метод создания товара
    Схема спеки: Root Type for goods_company_request_data_type
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    title: str = Field(description="Название товара")
    print_title: str | None = Field(default=None, description="Название для печати в чеке")
    article: str | None = Field(default=None, description="Артикул")
    barcode: str | None = Field(default=None, description="Штрих-код")
    category_id: int = Field(description="Идентификатор категории товара")
    cost: float | None = Field(default=None, description="Цена продажи")
    actual_cost: float | None = Field(default=None, description="Себестоимость")
    sale_unit_id: int = Field(description="Единица измерения для продажи")
    service_unit_id: int = Field(description="Единица измерения для списания")
    unit_equals: float | None = Field(default=None, description="Отношение ед.имзерения для продажи к ед.измерения для списания")
    critical_amount: float | None = Field(default=None, description="Критичный остаток")
    desired_amount: float | None = Field(default=None, description="Желаемый остаток")
    netto: float | None = Field(default=None, description="Масса нетто")
    brutto: float | None = Field(default=None, description="Масса брутто")
    comment: str | None = Field(default=None, description="Комментарий")
    tax_variant: int | None = Field(default=None, description="Система налогообложения")
    vat_id: int | None = Field(default=None, description="НДС")
    correction_rules: list[GoodsCompanyRequestWithRulesDataTypeCorrectionRulesItem] | None = Field(default=None, description="Массив правил пересчета единиц измерения (необходим, если по товару есть складские операциии)")


class GoodsSearchResponse200DataTypes(BaseModel):
    """Пример запроса на получение списка
    Схема спеки: Root Type for goods_search_response200_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: list[GoodsSearchResponse200DataTypesDataItem] | None = Field(default=None, alias="data", description="Массив с объектами данных")
    meta: GoodsSearchResponse200DataTypesMeta | None = Field(default=None)


class GetAbonementIdCheckForActivityResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data_: CheckForActivity | None = Field(default=None, alias="data")


class GetApplicationApplicationIdResponse200Data(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    connection_status: GetApplicationApplicationIdResponse200DataConnectionStatus | None = Field(default=None)
    payments: list[GetApplicationApplicationIdResponse200DataPaymentsItem] | None = Field(default=None, description="Список оплат приложения в салоне")
    logs: list[GetApplicationApplicationIdResponse200DataLogsItem] | None = Field(default=None, description="Лог изменения статусов приложения в салоне")


class GetApplicationIdTariffsResponse200DataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="ID тарифа")
    title: str | None = Field(default=None, description="Название тарифа")
    options: list[GetApplicationIdTariffsResponse200DataItemOptionsItem] | None = Field(default=None, description="Опции тарифа")


class GetApplicationPaymentLinkResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: GetApplicationPaymentLinkResponse200Data | None = Field(default=None, alias="data")
    meta: dict[str, Any] | None = Field(default=None)


class GetCompanyIdFiltersResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: list[ActivityFilter] | None = Field(default=None, alias="data")
    meta: ResponseMetaCountObject | None = Field(default=None)


class GetCompanyIdSearchDatesRangeResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: ActivityDatesRange | None = Field(default=None, alias="data")
    meta: dict[str, Any] | None = Field(default=None)


class GetDepositHistoryDepositIdResponse200DataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    deposit_transaction: DepositTransaction | None = Field(default=None)
    deposit_transaction_type: DepositTransactionType | None = Field(default=None)


class GetIntegrationCallsResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: list[GetIntegrationCallsResponse200DataItem] | None = Field(default=None, alias="data", description="Список звонков")
    meta: dict[str, Any] | None = Field(default=None)


class GetStaffIdCalculationResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: list[SalaryStaffCalculation] | None = Field(default=None, alias="data")
    meta: ResponseMetaCountObject | None = Field(default=None)


class GetStaffIdCalculationResponse2002(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: SalaryStaffCalculation | None = Field(default=None, alias="data")
    meta: dict[str, Any] | None = Field(default=None)


class GetStaffIdSalarySchemesCountResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: SalaryStaffSchemesCount | None = Field(default=None, alias="data")
    meta: dict[str, Any] | None = Field(default=None)


class GetStaffIdSalarySchemesResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: list[SalaryStaffScheme] | None = Field(default=None, alias="data")
    meta: ResponseMetaCountObject | None = Field(default=None)


class GetStaffScheduleResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: list[MasterScheduleDayContainer] | None = Field(default=None, alias="data")
    meta: ResponseMetaCountObject | None = Field(default=None)


class GetStaffStaffIdResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: SalaryStaffCalculation | None = Field(default=None, alias="data")
    meta: dict[str, Any] | None = Field(default=None)


class GetStaffStaffIdResponse2002(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: SalaryStaffCalculation | None = Field(default=None, alias="data")
    meta: dict[str, Any] | None = Field(default=None)


class GetUserIdPermissionsResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: UserRolePermissions | None = Field(default=None, alias="data")
    meta: dict[str, Any] | None = Field(default=None)


class GetUserIdRolesResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: list[UserRoleWithSalonAndUser] | None = Field(default=None, alias="data")
    meta: dict[str, Any] | None = Field(default=None)


class GetUsersRolesResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: list[UserRoleWithSalonAndUser] | None = Field(default=None, alias="data")
    meta: dict[str, Any] | None = Field(default=None)


class GoodsCategoryNodeResponse200DataTypesData(BaseModel):
    """Объект с данными
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    parent_id: float | None = Field(default=None, description="Идентификатор родительского элемента (0 для корневых элементов)")
    item_id: float | None = Field(default=None, description="Идентификатор товара (всегда 0)")
    category_id: float | None = Field(default=None, description="Идентификатор товарной категории")
    title: str | None = Field(default=None, description="Название товарной категории")
    is_chain: bool | None = Field(default=None, description="Является ли элемент привязанным к сети? true - элемент привязан к сети, false - не привязан")
    is_category: bool | None = Field(default=None, description="Является ли элемент категорией? всегда true")
    is_item: bool | None = Field(default=None, description="Является ли элемент товаром? всегда false")
    children: list[GoodsCategoryNodeResponse200DataTypesDataChildrenItem] | None = Field(default=None, description="Дочерние элементы товарной категории")
    children_count: float | None = Field(default=None, description="Полное число дочерних товаров и категорий (без рекурсии)")


class GoodsCompanyGoodsIdResponse200DataTypesDataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    title: str | None = Field(default=None, description="Наименование товара")
    value: str | None = Field(default=None, description="Наименование товара")
    label: str | None = Field(default=None, description="Наименование товара с артикулом (если имеется)")
    good_id: str | None = Field(default=None, description="Тип платежа")
    cost: str | None = Field(default=None, description="Цена продажи")
    unit_id: str | None = Field(default=None, description="ID единицы измерения для продажи")
    unit_short_title: str | None = Field(default=None, description="Единица измерения для продажи")
    service_unit_id: str | None = Field(default=None, description="ID единицы измерения для списания")
    service_unit_short_title: str | None = Field(default=None, description="Единица измерения для списания")
    actual_cost: str | None = Field(default=None, description="Себестоимость")
    unit_actual_cost: str | None = Field(default=None, description="Себестоимость единицы")
    unit_actual_cost_format: str | None = Field(default=None, description="Формат себестоимости единицы")
    unit_equals: str | None = Field(default=None, description="Отношение единицы измерения для продажик еденице за списание")
    barcode: str | None = Field(default=None, description="Штрих-код")
    loyalty_abonement_type_id: float | None = Field(default=None, description="Идентификатор типа абонемента (если товар является абонементом)")
    loyalty_certificate_type_id: float | None = Field(default=None, description="Идентификатор типа сертификата (если товар является сертификатом)")
    loyalty_allow_empty_code: bool | None = Field(default=None, description="Разрешена ли продажа без кода")
    critical_amount: float | None = Field(default=None, description="Критичный остаток")
    desired_amount: float | None = Field(default=None, description="Желаемый остаток")
    actual_amounts: list[GoodsCompanyGoodsIdResponse200DataTypesDataItemActualAmountsItem] | None = Field(default=None, description="Остатки на складах")
    last_change_date: str | None = Field(default=None, description="Дата последнего изменения сущности")


class GroupGroupidClientsResponseDataTypesData(BaseModel):
    """Объект с данными
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    salon_group_id: float | None = Field(default=None, description="Идентификатор сети")
    phone: str | None = Field(default=None, description="Телефон клиента")
    clients: list[GroupGroupidClientsResponseDataTypesDataClientsItem] | None = Field(default=None, description="Массив клиентов в филиалах сети")


class GroupsResponseDataTypesDataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор сети")
    title: str | None = Field(default=None, description="Название сети")
    companies: list[GroupsResponseDataTypesDataItemCompaniesItem] | None = Field(default=None, description="Компании сети")
    access: GroupsResponseDataTypesDataItemAccess | None = Field(default=None)


class GoodsCategoryNodeResponse200DataTypes(BaseModel):
    """Пример запроса на получение состава категории
    Схема спеки: Root Type for goods_category_node_response200_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: GoodsCategoryNodeResponse200DataTypesData | None = Field(default=None, alias="data")


class GoodsCompanyGoodsIdResponse200DataTypes(BaseModel):
    """Получить товар (товары)
    Схема спеки: Root Type for goods_company_goods_id_response200_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: list[GoodsCompanyGoodsIdResponse200DataTypesDataItem] | None = Field(default=None, alias="data", description="Массив с объектами данных")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")


class GroupGroupidClientsResponseDataTypes(BaseModel):
    """Получить сетевого клиента по номеру телефона
    Схема спеки: Root Type for group_groupid_clients_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: GroupGroupidClientsResponseDataTypesData | None = Field(default=None, alias="data")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")


class GroupsResponseDataTypes(BaseModel):
    """Получение доступных пользователю сетей
    Схема спеки: Root Type for groups_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: list[GroupsResponseDataTypesDataItem] | None = Field(default=None, alias="data", description="Массив объектов с данными")


class GetApplicationApplicationIdResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: GetApplicationApplicationIdResponse200Data | None = Field(default=None, alias="data")
    meta: dict[str, Any] | None = Field(default=None)


class GetApplicationIdTariffsResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: list[GetApplicationIdTariffsResponse200DataItem] | None = Field(default=None, alias="data", description="Список тарифов")
    meta: dict[str, Any] | None = Field(default=None)


class GetClientIdCommentsResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: list[ClientCommentContainer] | None = Field(default=None, alias="data")
    meta: ResponseMetaCountObject | None = Field(default=None)


class GetDailyStaffIdResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: SalaryStaffCalculationDaily | None = Field(default=None, alias="data")
    meta: ResponseMetaCountObject | None = Field(default=None)


class GetDailyStaffIdResponse2002(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: SalaryStaffPeriodDaily | None = Field(default=None, alias="data")
    meta: ResponseMetaCountObject | None = Field(default=None)


class GetDayIdEventsResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: list[TimetableEventScheduleEvent2] | None = Field(default=None, alias="data")
    meta: ResponseMetaCountObject | None = Field(default=None)


class GetDepositHistoryDepositIdResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: list[GetDepositHistoryDepositIdResponse200DataItem] | None = Field(default=None, alias="data")
    meta: dict[str, Any] | None = Field(default=None)


class GetLicenseCompanyIdResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    license_option: LicenseOption2 | None = Field(default=None, alias="LicenseOption")
    active: float = Field(description="Активна ли лицензия")
    deactivation_date: str = Field(description="Дата окончания срока действия лицензии")
    id_: float = Field(alias="id", description="Идентификатор лицензии")
    name: str = Field(description="Наименование лицезнии")
    options: list[dict[str, Any]] = Field(description="Опции лицензии")
    salon_id: float = Field(description="Идентификатор компании")
    staff_limit: float = Field(description="Лимит сотрудников")
    start_date: str = Field(description="Дата начала срока действия лицензии")


class GetSettingsTimeslotsResponse200Data(BaseModel):
    """Объект модели "Настройки таймслотов".
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    is_enabled: bool | None = Field(default=None, description="Признак включения таймслотов.")
    weekdays_settings: CompanyGridWeekdaysContainer | None = Field(default=None)
    dates_settings: list[CompanyGridDaysSettingsContainerItem] | None = Field(default=None)

__all__ = [
    "GetAbonementIdCheckForActivityResponse200",
    "GetApplicationApplicationIdResponse200",
    "GetApplicationApplicationIdResponse200Data",
    "GetApplicationApplicationIdResponse200DataConnectionStatus",
    "GetApplicationApplicationIdResponse200DataLogsItem",
    "GetApplicationApplicationIdResponse200DataPaymentsItem",
    "GetApplicationIdTariffsResponse200",
    "GetApplicationIdTariffsResponse200DataItem",
    "GetApplicationIdTariffsResponse200DataItemOptionsItem",
    "GetApplicationPaymentLinkResponse200",
    "GetApplicationPaymentLinkResponse200Data",
    "GetClientIdCommentsResponse200",
    "GetCompanyIdFiltersResponse200",
    "GetCompanyIdSearchDatesRangeResponse200",
    "GetDailyStaffIdResponse200",
    "GetDailyStaffIdResponse2002",
    "GetDayIdEventsResponse200",
    "GetDepositHistoryDepositIdResponse200",
    "GetDepositHistoryDepositIdResponse200DataItem",
    "GetIntegrationCallsRequest",
    "GetIntegrationCallsResponse200",
    "GetIntegrationCallsResponse200DataItem",
    "GetLicenseCompanyIdResponse200",
    "GetSettingsTimeslotsResponse200Data",
    "GetStaffIdCalculationResponse200",
    "GetStaffIdCalculationResponse2002",
    "GetStaffIdDateResponse200",
    "GetStaffIdSalarySchemesCountResponse200",
    "GetStaffIdSalarySchemesResponse200",
    "GetStaffScheduleResponse200",
    "GetStaffStaffIdResponse200",
    "GetStaffStaffIdResponse2002",
    "GetStartDateEndDateResponse200",
    "GetUserIdPermissionsResponse200",
    "GetUserIdRolesResponse200",
    "GetUsersRolesResponse200",
    "GoodsCategoriesPostPutResponseDataTypes",
    "GoodsCategoriesPostPutResponseDataTypesData",
    "GoodsCategoriesRequestDataTypes",
    "GoodsCategoriesResponse200DataTypes",
    "GoodsCategoriesResponse200DataTypesDataItem",
    "GoodsCategoryNodeResponse200DataTypes",
    "GoodsCategoryNodeResponse200DataTypesData",
    "GoodsCategoryNodeResponse200DataTypesDataChildrenItem",
    "GoodsCompanyGoodsIdResponse200DataTypes",
    "GoodsCompanyGoodsIdResponse200DataTypesDataItem",
    "GoodsCompanyGoodsIdResponse200DataTypesDataItemActualAmountsItem",
    "GoodsCompanyRequestDataType",
    "GoodsCompanyRequestWithRulesDataType",
    "GoodsCompanyRequestWithRulesDataTypeCorrectionRulesItem",
    "GoodsSearchResponse200DataTypes",
    "GoodsSearchResponse200DataTypesDataItem",
    "GoodsSearchResponse200DataTypesMeta",
    "GroupGroupidClientsResponseDataTypes",
    "GroupGroupidClientsResponseDataTypesData",
    "GroupGroupidClientsResponseDataTypesDataClientsItem",
    "GroupsResponseDataTypes",
    "GroupsResponseDataTypesDataItem",
    "GroupsResponseDataTypesDataItemAccess",
    "GroupsResponseDataTypesDataItemCompaniesItem"
]
