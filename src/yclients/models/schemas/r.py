"""Модели YCLIENTS API (r: R).

Сгенерировано scripts/generate.py -- не редактируйте вручную.
"""

from __future__ import annotations

from datetime import date, datetime
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class RecordCompanyidResponse201DataTypesDataClient(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    phone: str | None = Field(default=None, description="Телефон клиента")
    name: str | None = Field(default=None, description="Имя клиента")
    email: str | None = Field(default=None, description="Email клиента")


class RecordCompanyidResponse201DataTypesDataDocumentsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор документа")
    type_id: float | None = Field(default=None, description="Тип документа")
    storage_id: float | None = Field(default=None, description="Идентификатор склада")
    user_id: float | None = Field(default=None, description="Идентификатор пользователя, создавшего документ")
    company_id: float | None = Field(default=None, description="Идентификатор компании")
    number: float | None = Field(default=None, description="Номер документа")
    comment: str | None = Field(default=None, description="Комментарий к документу")
    date_created: str | None = Field(default=None, description="Дата создания документа")
    category_id: int | None = Field(default=None, description="Идентификатор категории товара")
    visit_id: int | None = Field(default=None, description="Идентификатор визита")
    record_id: int | None = Field(default=None, description="Идентификатор записи")
    type_title: str | None = Field(default=None, description="Название сущности, к которой принадлежит документ")


class RecordCompanyidResponse201DataTypesDataServicesItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор услуги")
    first_cost: float | None = Field(default=None, description="Начальная стоимость услуги (без учета скидок)")
    discount: float | None = Field(default=None, description="Скидка")
    cost: float | None = Field(default=None, description="Итоговая стоимость услуги")


class RecordCompanyidResponse201DataTypesDataStaff(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор сотрудника")
    name: str | None = Field(default=None, description="Имя сотрудника")
    spec: str | None = Field(default=None, description="Специализация сотрудника")


class RecordCompanyidResponseDataTypesDataConsumablesItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор транзакции")
    document_id: int | None = Field(default=None, description="Идентификатор документа")
    type_id: float | None = Field(default=None, description="Тип транзакции")
    company_id: float | None = Field(default=None, description="Идентификатор компании")
    good_id: float | None = Field(default=None, description="Идентификатор товара")
    amount: float | None = Field(default=None, description="Количество товара")
    cost_per_unit: float | None = Field(default=None, description="Цена за единицу товара")
    discount: float | None = Field(default=None, description="Скидка")
    cost: float | None = Field(default=None, description="Итоговая стоимость")
    unit_id: float | None = Field(default=None, description="ID единицы измерения")
    operation_unit_type: float | None = Field(default=None, description="Тип единицы измерения: 1 - для продажи, 2 - для списания")
    storage_id: float | None = Field(default=None, description="Идентификатор склада")
    supplier_id: float | None = Field(default=None, description="Идентификатор поставщика")
    client_id: float | None = Field(default=None, description="Идентификатор клиента")
    master_id: float | None = Field(default=None, description="Идентификатор мастера")
    create_date: str | None = Field(default=None, description="Дата создания транзакции")
    comment: str | None = Field(default=None, description="Комментарий")
    service_id: float | None = Field(default=None, description="Идентификатор услуги")
    user_id: float | None = Field(default=None, description="Идентификатор пользователя")
    deleted: bool | None = Field(default=None, description="Статус удаленая транзакции, 1 - если удалена")
    pkg_amount: float | None = Field(default=None, description="Количество упаковок")


class RecordCompanyidResponseDataTypesDataDocumentsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор документа")
    type_id: float | None = Field(default=None, description="Тип документа")
    storage_id: float | None = Field(default=None, description="Идентификатор склада")
    user_id: float | None = Field(default=None, description="Идентификатор пользователя, создавшего документ")
    company_id: float | None = Field(default=None, description="Идентификатор компании")
    number: float | None = Field(default=None, description="Номер документа")
    comment: str | None = Field(default=None, description="Комментарий к документу")
    date_created: str | None = Field(default=None, description="Дата создания документа")
    category_id: int | None = Field(default=None, description="Идентификатор категории товара")
    visit_id: int | None = Field(default=None, description="Идентификатор визита")
    record_id: int | None = Field(default=None, description="Идентификатор записи")
    type_title: str | None = Field(default=None, description="Название сущности, к которой принадлежит документ")


class RecordCompanyidResponseDataTypesDataFinanceTransactionsItemAccount(BaseModel):
    """Касса
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор кассы")
    title: str | None = Field(default=None, description="Название кассы")


class RecordCompanyidResponseDataTypesDataFinanceTransactionsItemClient(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор клиента")
    name: str | None = Field(default=None, description="Имя клиента")
    phone: str | None = Field(default=None, description="Телефон клиента")


class RecordCompanyidResponseDataTypesDataFinanceTransactionsItemExpense(BaseModel):
    """Статья платежа
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор статьи платежа")
    title: str | None = Field(default=None, description="Название статьи платежа")


class RecordCompanyidResponseDataTypesDataRecordLabelsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: str | None = Field(default=None, alias="id", description="Идентификатор категории")
    title: str | None = Field(default=None, description="Название категории")
    color: str | None = Field(default=None, description="Цвет категории")
    icon: str | None = Field(default=None, description="Иконка")
    font_color: str | None = Field(default=None, description="Цвет шрифта категории")


class RecordCompanyidResponseDataTypesDataServicesItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор услуги")
    title: str | None = Field(default=None, description="Название услуги")
    cost: float | None = Field(default=None, description="Итоговая стоимость услуги")
    manual_cost: float | None = Field(default=None, description="Стоимость, указанная вручную")
    cost_per_unit: float | None = Field(default=None, description="Стоимость за единицу")
    discount: float | None = Field(default=None, description="Скидка")
    first_cost: float | None = Field(default=None, description="Начальная стоимость услуги (без учета скидок)")
    amount: float | None = Field(default=None, description="Количество")


class RecordCompanyidResponseDataTypesDataStaffPosition(BaseModel):
    """Должность сотрудника
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор должности")
    title: str | None = Field(default=None, description="Название должности")


class RecordsCompanyidRequestDataTypesClient(BaseModel):
    """Параметры клиента (телефон, имя, email)
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    phone: str | None = Field(default=None, description="Номер телефона клиента")
    name: str | None = Field(default=None, description="Имя клиента")
    surname: str | None = Field(default=None, description="Фамилия клиента")
    patronymic: str | None = Field(default=None, description="Отчество клиента")
    email: str | None = Field(default=None, description="Email клиента")


class RecordsCompanyidRequestDataTypesClientAgreements(BaseModel):
    """Юридические соглашения клиента
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    is_newsletter_allowed: bool | None = Field(default=None, description="Отправка информационно-рекламной рассылки")
    is_personal_data_processing_allowed: bool | None = Field(default=None, description="Обработка персональных данных")


class RecordsCompanyidRequestDataTypesCustomFields(BaseModel):
    """Дополнительные поля записи
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    my_custom_field: int | None = Field(default=None)
    some_another_field: list[str] | None = Field(default=None)


class RecordsCompanyidRequestDataTypesServicesItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор услуги")
    first_cost: float | None = Field(default=None, description="Начальная стоимость услуги")
    discount: float | None = Field(default=None, description="Скидка на услугу")
    cost: float | None = Field(default=None, description="Итоговая стоимость услуги")


class RecordsCompanyidResponseDataTypesDataItemClient(BaseModel):
    """Данные клиента (может быть пустым)
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор клиента")
    name: str | None = Field(default=None, description="Имя клиента")
    surname: str | None = Field(default=None, description="Фамилия клиента")
    patronymic: str | None = Field(default=None, description="Отчество клиента")
    display_name: str | None = Field(default=None, description="Отображаемое имя клиента")
    phone: str | None = Field(default=None, description="Номер телефона клиента")
    card: str | None = Field(default=None, description="Номер карты лояльности клиента")
    email: str | None = Field(default=None, description="Эл.Почта клиента")
    success_visits_count: int | None = Field(default=None, description="Количество завершенных визитов")
    fail_visits_count: int | None = Field(default=None, description="Количество визитов в статусе \"Не пришел\"")
    discount: int | None = Field(default=None, description="Скидка клиента")
    is_new: Any | None = Field(default=None, description="Клиент является новым")
    custom_fields: dict[str, Any] | None = Field(default=None, description="Дополнительные поля клиента")


class RecordsCompanyidResponseDataTypesDataItemClientAgreements(BaseModel):
    """Юридические соглашения клиента
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    client_id: float | None = Field(default=None, description="Идентификатор клиента")
    company_id: float | None = Field(default=None, description="Идентификатор филиала")
    is_newsletter_allowed: bool | None = Field(default=None, description="Отправка информационно-рекламной рассылки")
    is_personal_data_processing_allowed: bool | None = Field(default=None, description="Обработка персональных данных")


class RecordsCompanyidResponseDataTypesDataItemConsumablesItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор транзакции списания")
    document_id: int | None = Field(default=None, description="Идентификатор связанного документа")
    type_id: int | None = Field(default=None, description="Тип товарной транзакции (В рамках обьекта всегда 2)")
    company_id: int | None = Field(default=None, description="Идентификатор филиала")
    good_id: int | None = Field(default=None, description="Идентификатор товара")
    amount: Any | None = Field(default=None, description="Количество товара к списанию")
    cost_per_unit: int | None = Field(default=None, description="Стоимость за единицу")
    discount: int | None = Field(default=None, description="Скидка (в рамках списания расходников = 0)")
    cost: int | None = Field(default=None, description="Итоговая стоимость")
    unit_id: int | None = Field(default=None, description="Идентификатор единицы измерения")
    operation_unit_type: int | None = Field(default=None, description="Тип единицы измерения: 1 - для продажи, 2 - для списания")
    supplier_id: int | None = Field(default=None, description="Идентификатор контрагента")
    record_id: int | None = Field(default=None, description="Идентификатор записи")
    client_id: int | None = Field(default=None, description="Идентификатор клиента (в рамках списания расходников в записи всегда 0)")
    master_id: int | None = Field(default=None, description="Идентификатор сотрудника (в рамках списания расходников в записи всегда 0)")
    create_date: str | None = Field(default=None, description="Дата списания расходников (совпадает с датой визита)")
    service_id: int | None = Field(default=None, description="Идентификатор услуги")
    user_id: int | None = Field(default=None, description="Идентификатор пользователя")
    deleted: Any | None = Field(default=None, description="Списание удалено")


class RecordsCompanyidResponseDataTypesDataItemDocumentsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор документа")
    type_id: float | None = Field(default=None, description="Тип документа")
    storage_id: float | None = Field(default=None, description="Идентификатор склада")
    user_id: float | None = Field(default=None, description="Идентификатор пользователя, создавшего документ")
    company_id: float | None = Field(default=None, description="Идентификатор компании")
    number: float | None = Field(default=None, description="Номер документа")
    comment: str | None = Field(default=None, description="Комментарий к документу")
    date_created: str | None = Field(default=None, description="Дата создания документа")
    category_id: int | None = Field(default=None, description="Идентификатор категории товара")
    visit_id: int | None = Field(default=None, description="Идентификатор визита")
    record_id: int | None = Field(default=None, description="Идентификатор записи")
    type_title: str | None = Field(default=None, description="Название сущности, к которой принадлежит документ")


class RecordsCompanyidResponseDataTypesDataItemFinanceTransactionsItemAccountClient(BaseModel):
    """Информация о клиенте
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор клиента")
    name: str | None = Field(default=None, description="Имя клиента")
    phone: str | None = Field(default=None, description="Номер телефона клиента")
    email: str | None = Field(default=None, description="Эл.почта клиента")


class RecordsCompanyidResponseDataTypesDataItemFinanceTransactionsItemExpense(BaseModel):
    """Данные о статье платежа
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор статьи платежа")
    title: str | None = Field(default=None, description="Название статьи платежа")
    type_: int | None = Field(default=None, alias="type", description="Тип статьи платежа")


class RecordsCompanyidResponseDataTypesDataItemGoodsTransactionsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор складской операции")
    title: str | None = Field(default=None, description="Название товара")
    barcode: str | None = Field(default=None, description="Штрихкод")
    article: str | None = Field(default=None, description="Артикул")
    amount: Any | None = Field(default=None, description="Кол-во проданного товара")
    cost_per_unit: Any | None = Field(default=None, description="Цена за единицу товара")
    price: Any | None = Field(default=None, description="Цена")
    cost: Any | None = Field(default=None, description="Стоимость с учетом скидок")
    cost_to_pay: Any | None = Field(default=None, description="Стоимость к оплате")
    manual_cost: Any | None = Field(default=None, description="Стоимость с учетом предварительной скидки (за вычетом скидки переданной в параметре discount)")
    master_id: Any | None = Field(default=None, description="Сотрудник который совершил продажу")
    storage_id: Any | None = Field(default=None, description="Склад списания товара")
    good_id: Any | None = Field(default=None, description="Идентификатор товара")
    discount: Any | None = Field(default=None, description="Скидка")
    loyalty_abonement_id: Any | None = Field(default=None, description="Идентификатор абонемента, который создан в результате продажи (Если товар является абонеметном)")
    loyalty_certificate_id: int | None = Field(default=None, description="Идентификатор сертификата, который создан в результате продажи (Если товар является сертификатом)")
    good_special_number: str | None = Field(default=None, description="Код абонемента\\сертификата (Если товар является абонеметном\\сертификатом)")


class RecordsCompanyidResponseDataTypesDataItemServicesItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор услуги")
    title: str | None = Field(default=None, description="Название услуги")
    cost: float | None = Field(default=None, description="Итоговая стоимость услуги")
    manual_cost: float | None = Field(default=None, description="Стоимость, указанная вручную")
    cost_per_unit: float | None = Field(default=None, description="Стоимость за единицу")
    discount: float | None = Field(default=None, description="Скидка")
    first_cost: float | None = Field(default=None, description="Начальная стоимость услуги (без учета скидок)")
    amount: float | None = Field(default=None, description="Количество")


class RecordsCompanyidResponseDataTypesDataItemStaffPosition(BaseModel):
    """Должность сотрудника
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор должности")
    title: str | None = Field(default=None, description="Название должности")


class RecordsCompanyidResponseDataTypesMeta(BaseModel):
    """Метаданные (содержит номер страницы и количество записей на странице)
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    page_: int | None = Field(default=None, alias="page")
    total_count: int | None = Field(default=None)


class ReferencesBusinessGroupResponseDataTypesDataItemTypesItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор типа")
    title: str | None = Field(default=None, description="Название типа")
    business_group_id: float | None = Field(default=None, description="Идентификатор бизнес-группы")


class ReferencesBusinessGroupResponseDataTypesMeta(BaseModel):
    """Метаданные (содержит количество найденых бизнес-типов)
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    count_: int | None = Field(default=None, alias="count")


class ResourcesCompanyidDataTypesDataItemInstancesItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор экземпляра ресурса")
    title: str | None = Field(default=None, description="Название экземпляра ресурса")
    resource_id: float | None = Field(default=None, description="Идентификатор ресусра, которому принадлежит экземпляр")


class ResourcesCompanyidDataTypesMeta(BaseModel):
    """Метаданные (содержит количество найденных ресурсов)
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    count_: int | None = Field(default=None, alias="count")


class ResponseMetaDatePaginatorObjectDateCursorCurrent(BaseModel):
    """Информация о текущей странице.
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    to: str | None = Field(default=None, description="До какой даты включительно фильтруются данные на текущей странице.")
    from_: str | None = Field(default=None, alias="from", description="С какой даты фильтруются данные на текущей странице.")
    count_: float | None = Field(default=None, alias="count", description="Количество элементов на текущей странице.")


class ResponseMetaDatePaginatorObjectDateCursorNext(BaseModel):
    """Информация о предыдущей странице.
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    to: str | None = Field(default=None, description="До какой даты включительно фильтруются данные на следующей странице.")
    from_: str | None = Field(default=None, alias="from", description="С какой даты фильтруются данные на следующей странице.")
    count_: float | None = Field(default=None, alias="count", description="Количество элементов на следующей странице.")


class ResponseMetaDatePaginatorObjectDateCursorPrevious(BaseModel):
    """Информация о предыдущей странице.
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    to: str | None = Field(default=None, description="До какой даты включительно фильтруются данные на предыдущей странице.")
    from_: str | None = Field(default=None, alias="from", description="С какой даты фильтруются данные на предыдущей странице.")
    count_: float | None = Field(default=None, alias="count", description="Количество элементов на предыдущей странице.")


class RecordsCompanyidRequestDataTypes(BaseModel):
    """Создать новую запись
    Схема спеки: Root Type for records_companyid_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    staff_id: float | None = Field(default=None, description="Идентификатор сотрудника")
    services: list[RecordsCompanyidRequestDataTypesServicesItem] | None = Field(default=None, description="Параметры услуг (id, стоимость, скидка)")
    client_: RecordsCompanyidRequestDataTypesClient | None = Field(default=None, alias="client")
    save_if_busy: bool | None = Field(default=None, description="Сохранять ли запись если время занято или нерабочее, или выдать ошибку")
    datetime: str | None = Field(default=None, description="Дата и время записи")
    seance_length: float | None = Field(default=None, description="Длительность записи в секундах")
    send_sms: bool | None = Field(default=None, description="Отправлять ли смс с деталями записи клиенту")
    comment: str | None = Field(default=None, description="Комментарий к записи")
    sms_remain_hours: float | None = Field(default=None, description="За сколько часов до визита следует выслать смс напоминание клиенту (0 - если не нужно)")
    email_remain_hours: float | None = Field(default=None, description="За сколько часов до визита следует выслать email напоминание клиенту (0 - если не нужно)")
    attendance: float | None = Field(default=None, description="Статус записи (2 - Пользователь подтвердил запись, 1 - Пользователь пришел, услуги оказаны, 0 - ожидание пользователя, -1 - пользователь не пришел на визит)")
    api_id: str | None = Field(default=None, description="Идентификатор внешней системы")
    custom_color: str | None = Field(default=None, description="Цвет записи")
    record_labels: list[str] | None = Field(default=None, description="Массив идентификаторов категорий записи")
    client_agreements: RecordsCompanyidRequestDataTypesClientAgreements | None = Field(default=None)
    technical_break_duration: float | None = Field(default=None, description="Технический перерыв. - Строго кратно 300 (5 минутам). - Максимальное значение 3600 (1 час) - Если передан `null` или значение не передано — будет задан согласно настройкам в разделе *Настройки → Жу...")
    custom_fields: RecordsCompanyidRequestDataTypesCustomFields | None = Field(default=None)


class ResourceInstance(BaseModel):
    """Схема спеки: Объект модели "Экземпляр Ресурса"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор экземпляра ресурса.")
    title: str | None = Field(default=None, description="Наименование экземпляра ресурса.")
    resource_id: float | None = Field(default=None, description="Идентификатор ресурса, к которому привязан экземпляр.")


class ResponseMetaCountObject(BaseModel):
    """Дополнительная информация о запросе.
    Схема спеки: Объект дополнительной информации о запросе с кол-вом найденных результатов
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    count_: float | None = Field(default=None, alias="count", description="Количество найденных результатов.")


class RecordCompanyidResponse201DataTypesData(BaseModel):
    """Объект с данными
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id")
    services: list[RecordCompanyidResponse201DataTypesDataServicesItem] | None = Field(default=None)
    client_: RecordCompanyidResponse201DataTypesDataClient | None = Field(default=None, alias="client")
    clients_count: float | None = Field(default=None, description="Количество занятых мест в групповой записи")
    staff: RecordCompanyidResponse201DataTypesDataStaff | None = Field(default=None)
    datetime: str | None = Field(default=None, description="Дата сеанса")
    seance_length: float | None = Field(default=None, description="Длительность визита")
    create_date: str | None = Field(default=None, description="Дата создания")
    comment: str | None = Field(default=None, description="Комментарий к записи")
    confirmed: float | None = Field(default=None, description="Подтверждена ли запись")
    sms_before: float | None = Field(default=None, description="Отправить ли клиенту смс с напоминанием о записи (если клиент указан)")
    sms_now: float | None = Field(default=None, description="Отправляли ли смс при добавлении записи")
    sms_now_text: str | None = Field(default=None, description="Текст смс")
    email_now: float | None = Field(default=None, description="Отправлено ли уведомление по email")
    notified: float | None = Field(default=None, description="Флаг пождтверждения записи администратором филиала, если клиент попросил подтвердить запись")
    master_request: float | None = Field(default=None, description="Был ли указан определенный специалист при записи (false если был указан \"не имеет значения\")")
    api_id: str | None = Field(default=None, description="Внешний идентификатор записи")
    from_url: str | None = Field(default=None, description="С какой страницы был совершён переход для оформления записи (сайт, приложение ВК и прочее)")
    review_requested: float | None = Field(default=None, description="Флаг запроса у клиента отзыва о посещении")
    activity_id: float | None = Field(default=None, description="Идентификатор групповой записи")
    documents: list[RecordCompanyidResponse201DataTypesDataDocumentsItem] | None = Field(default=None)


class RecordCompanyidResponseDataTypesDataFinanceTransactionsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор финансовой транзакции")
    document_id: float | None = Field(default=None, description="Идентификатор документа")
    date: str | None = Field(default=None, description="Дата создания")
    type_id: float | None = Field(default=None, description="Тип статьи платежа")
    expense_id: float | None = Field(default=None, description="Идентификатор статьи платежа")
    account_id: float | None = Field(default=None, description="Идентификатор кассы")
    amount: float | None = Field(default=None, description="Сумма транзакции")
    client_id: float | None = Field(default=None, description="Идентификатор клиента")
    master_id: float | None = Field(default=None, description="Идентификатор сотрудника")
    supplier_id: float | None = Field(default=None, description="Идентификатор поставщика")
    comment: str | None = Field(default=None, description="Комментарий")
    item_id: float | None = Field(default=None, description="Идентификатор товара (0, если элемент - категория)")
    target_type_id: int | None = Field(default=None)
    record_id: float | None = Field(default=None, description="Идентификатор записи")
    goods_transaction_id: float | None = Field(default=None, description="Идентификатор товарной транзакции")
    expense: RecordCompanyidResponseDataTypesDataFinanceTransactionsItemExpense | None = Field(default=None)
    account: RecordCompanyidResponseDataTypesDataFinanceTransactionsItemAccount | None = Field(default=None)
    client_: RecordCompanyidResponseDataTypesDataFinanceTransactionsItemClient | None = Field(default=None, alias="client")
    master: list[dict[str, Any]] | None = Field(default=None, description="Сотрудники")
    supplier: list[dict[str, Any]] | None = Field(default=None, description="Поставщики")


class RecordCompanyidResponseDataTypesDataStaff(BaseModel):
    """Объект данных о сотруднике
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор сотрудника")
    api_id: str | None = Field(default=None, description="Внешний идентификатор сотрудника")
    name: str | None = Field(default=None, description="Имя сотрудника")
    specialization: str | None = Field(default=None, description="Специализация сотрудника")
    position: RecordCompanyidResponseDataTypesDataStaffPosition | None = Field(default=None)
    avatar: str | None = Field(default=None, description="Путь к файлу с аватаркой сотрудника")
    avatar_big: str | None = Field(default=None, description="Пусть к файлу с аватаркой сотрудника в высоком разрешении")
    rating: float | None = Field(default=None, description="Рейтинг сотрудника")
    votes_count: float | None = Field(default=None, description="Кол-во голосов, оценивших сотрудника")


class RecordsCompanyidResponseDataTypesDataItemFinanceTransactionsItemAccount(BaseModel):
    """Информация о кассе
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор кассы")
    title: str | None = Field(default=None, description="Название кассы")
    is_cash: Any | None = Field(default=None, description="Касса для оплаты наличными")
    is_default: Any | None = Field(default=None, description="Касса по-умолчанию")
    client_: RecordsCompanyidResponseDataTypesDataItemFinanceTransactionsItemAccountClient | None = Field(default=None, alias="client")


class RecordsCompanyidResponseDataTypesDataItemStaff(BaseModel):
    """Объект данных о сотруднике
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор сотрудника")
    api_id: str | None = Field(default=None, description="Внешний идентификатор сотрудника")
    name: str | None = Field(default=None, description="Имя сотрудника")
    specialization: str | None = Field(default=None, description="Специализация сотрудника")
    position: RecordsCompanyidResponseDataTypesDataItemStaffPosition | None = Field(default=None)
    avatar: str | None = Field(default=None, description="Путь к файлу с аватаркой сотрудника")
    avatar_big: str | None = Field(default=None, description="Пусть к файлу с аватаркой сотрудника в высоком разрешении")
    rating: float | None = Field(default=None, description="Рейтинг сотрудника")
    votes_count: float | None = Field(default=None, description="Кол-во голосов, оценивших сотрудника")


class ReferencesBusinessGroupResponseDataTypesDataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор категории")
    title: str | None = Field(default=None, description="Название категории")
    image: str | None = Field(default=None, description="Изображение группы")
    types: list[ReferencesBusinessGroupResponseDataTypesDataItemTypesItem] | None = Field(default=None, description="Связанные бизнес-типы")


class ResourcesCompanyidDataTypesDataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор ресурса")
    title: str | None = Field(default=None, description="Название ресурса")
    instances: list[ResourcesCompanyidDataTypesDataItemInstancesItem] | None = Field(default=None, description="Массив экземпляров ресурса")


class ResponseMetaDatePaginatorObjectDateCursor(BaseModel):
    """Информация о постраничной навигации.
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    previous: ResponseMetaDatePaginatorObjectDateCursorPrevious | None = Field(default=None)
    current: ResponseMetaDatePaginatorObjectDateCursorCurrent | None = Field(default=None)
    next_: ResponseMetaDatePaginatorObjectDateCursorNext | None = Field(default=None, alias="next")


class RecordCompanyidResponse201DataTypes(BaseModel):
    """Изменить запись
    Схема спеки: Root Type for record_companyid_response201_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешного выполнения (true)")
    data_: RecordCompanyidResponse201DataTypesData | None = Field(default=None, alias="data")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")


class ReferencesBusinessGroupResponseDataTypes(BaseModel):
    """Получение списка бизнес-типов сгруппированных по группам
    Схема спеки: Root Type for references_business_group_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: list[ReferencesBusinessGroupResponseDataTypesDataItem] | None = Field(default=None, alias="data", description="Массив объектов с данными")
    meta: ReferencesBusinessGroupResponseDataTypesMeta | None = Field(default=None)


class ResourcesCompanyidDataTypes(BaseModel):
    """Получение ресурсов в филиале
    Схема спеки: Root Type for resources_companyid_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: list[ResourcesCompanyidDataTypesDataItem] | None = Field(default=None, alias="data", description="Массив с объектами данных")
    meta: ResourcesCompanyidDataTypesMeta | None = Field(default=None)


class ResponseMetaDatePaginatorObject(BaseModel):
    """Информация о постраничной навигации, содержащая данные о текущей, следующей и предыдущей страницах.
    Данные отсортированы и разбиты на страницы по датам в убывающем порядке.
    Схема спеки: Объект информации о постраничной навигации, основанной на дате.
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    date_cursor: ResponseMetaDatePaginatorObjectDateCursor | None = Field(default=None, alias="dateCursor")


class RecordCompanyidResponseDataTypesData(BaseModel):
    """Объект с данными
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="ID записи")
    company_id: float | None = Field(default=None, description="Идентификатор компании")
    staff_id: float | None = Field(default=None, description="Идентификатор сотрудника")
    services: list[RecordCompanyidResponseDataTypesDataServicesItem] | None = Field(default=None, description="Массив объектов с услугами в записи")
    goods_transactions: list[dict[str, Any]] | None = Field(default=None, description="Массив товарных транзакций")
    staff: RecordCompanyidResponseDataTypesDataStaff | None = Field(default=None)
    client_: str | None = Field(default=None, alias="client", description="Данные клиента (может быть пустым)")
    date: str | None = Field(default=None, description="Дата сеанса")
    datetime: str | None = Field(default=None, description="Дата сеанса в ISO")
    create_date: str | None = Field(default=None, description="Дата создания сеанса")
    comment: str | None = Field(default=None, description="Комментарий к записи")
    online: bool | None = Field(default=None, description="(Только при чтении) Запись онлайновая или нет (false если запись внес администратор)")
    visit_attendance: float | None = Field(default=None, description="Статус визита, 2 - Пользователь подтвердил запись, 1 - Пользователь пришел, услуги оказаны, 0 - ожидание пользователя, -1 - пользователь не пришел на визит")
    attendance: float | None = Field(default=None, description="Статус записи, 2 - Пользователь подтвердил запись, 1 - Пользователь пришел, услуги оказаны, 0 - ожидание пользователя, -1 - пользователь не пришел на визит")
    confirmed: float | None = Field(default=None, description="Статус подтверждения записи, 0 - не подтверждена, 1 - подтверждена")
    seance_length: float | None = Field(default=None, description="Длительность сеанса")
    length: float | None = Field(default=None, description="Длительность сеанса")
    sms_before: float | None = Field(default=None, description="Отправить ли клиенту смс с напоминанием о записи (если клиент указан)")
    sms_now: float | None = Field(default=None, description="Отправляли ли смс при добавлении записи")
    sms_now_text: str | None = Field(default=None, description="Текст смс")
    email_now: float | None = Field(default=None, description="Отправлено ли уведомление по email")
    notified: float | None = Field(default=None, description="Флаг пождтверждения записи администратором филиала, если клиент попросил подтвердить запись")
    master_request: float | None = Field(default=None, description="Был ли указан определенный специалист при записи (false если был указан \"не имеет значения\")")
    api_id: str | None = Field(default=None, description="Внешний идентификатор записи")
    from_url: str | None = Field(default=None, description="С какой страницы был совершён переход для оформления записи (сайт, приложение ВК и прочее)")
    review_requested: float | None = Field(default=None, description="Флаг запроса у клиента отзыва о посещении")
    visit_id: float | None = Field(default=None, description="Идентификатор визита")
    created_user_id: float | None = Field(default=None, description="Идентификатор пользователя, создавшего запись")
    deleted: bool | None = Field(default=None, description="(Только при чтении) Удалена ли запись (true если удалена)")
    paid_full: float | None = Field(default=None, description="Флаг, оплачена ли запись полностью (1 - если оплачена полностью)")
    prepaid: bool | None = Field(default=None, description="Доступна ли онлайн-оплата")
    prepaid_confirmed: bool | None = Field(default=None, description="Статус онлайн-оплаты")
    payment_status: int | None = Field(default=None, description="Статус автооплаты абонементом (0 - Визит не оплачен, 1 - Визит оплачен, 2 - визит оплачен абонементом автоматически, 3 - Визит не удалось оплатить автоматически, 4 - будет оплачен абонементом автом...")
    last_change_date: str | None = Field(default=None, description="Дата последнего редактирования записи")
    technical_break_duration: float | None = Field(default=None, description="Длительность технического перерыва")
    custom_color: str | None = Field(default=None, description="Цвет записи в журнале")
    custom_font_color: str | None = Field(default=None, description="(Только при чтении) Цвет шрифта записи")
    record_labels: list[RecordCompanyidResponseDataTypesDataRecordLabelsItem] | None = Field(default=None, description="Массив категрий записи")
    activity_id: float | None = Field(default=None, description="Идентификатор группового события")
    custom_fields: dict[str, Any] | None = Field(default=None, description="Дополнительные поля записи")
    documents: list[RecordCompanyidResponseDataTypesDataDocumentsItem] | None = Field(default=None)
    sms_remain_hours: float | None = Field(default=None, description="За сколько часов до начала визита отправить sms с напоминанием")
    email_remain_hours: float | None = Field(default=None, description="За сколько часов до начала визита отправить email с напоминанием")
    bookform_id: float | None = Field(default=None, description="Идентификатор формы онлайн-записи")
    record_from: str | None = Field(default=None, description="Название формы онлайн-записи")
    is_mobile: float | None = Field(default=None, description="Тип устройства, с которого записались (0 - запись, создана администратором, через web-версию или моб. приложение для администраторов, 1 - Мобильный браузер, виджет онлайн-записи, 2 - Десктопный бра...")
    is_sale_bill_printed: bool | None = Field(default=None, description="Распечатан ли чек продажи")
    consumables: list[RecordCompanyidResponseDataTypesDataConsumablesItem] | None = Field(default=None, description="Массив расходных материалов")
    finance_transactions: list[RecordCompanyidResponseDataTypesDataFinanceTransactionsItem] | None = Field(default=None, description="Массив финансовых транзакций")


class RecordsCompanyidResponseDataTypesDataItemFinanceTransactionsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор кассы")
    document_id: int | None = Field(default=None, description="Идентификатор документа")
    date: int | None = Field(default=None, description="Дата финансовой операции")
    type_id: int | None = Field(default=None, description="Тип финансовой операции")
    expense_id: int | None = Field(default=None, description="Идентификатор статьи платежа")
    account_id: int | None = Field(default=None, description="Идентификатор кассы")
    amount: Any | None = Field(default=None, description="Сумма операции")
    client_id: int | None = Field(default=None, description="Идентификатор клиента")
    comment: str | None = Field(default=None, description="Комментарий к финансовой операции")
    item_id: int | None = Field(default=None, description="Идентификатор услуги\\складской операции")
    target_type_id: int | None = Field(default=None, description="Для транзакций по статье \"оказание услуг\" всегда равен 1, для продажи товаров всегда равен 0")
    record_id: int | None = Field(default=None, description="Идентификатор записи")
    goods_transaction_id: int | None = Field(default=None, description="Идентификатор складской операции")
    expense: RecordsCompanyidResponseDataTypesDataItemFinanceTransactionsItemExpense | None = Field(default=None)
    account: RecordsCompanyidResponseDataTypesDataItemFinanceTransactionsItemAccount | None = Field(default=None)


class RecordCompanyidResponseDataTypes(BaseModel):
    """Получить запись
    Схема спеки: Root Type for record_companyid_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: RecordCompanyidResponseDataTypesData | None = Field(default=None, alias="data")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")


class RecordsCompanyidResponseDataTypesDataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="ID записи")
    company_id: float | None = Field(default=None, description="Идентификатор компании")
    staff_id: float | None = Field(default=None, description="Идентификатор сотрудника")
    services: list[RecordsCompanyidResponseDataTypesDataItemServicesItem] | None = Field(default=None, description="Массив объектов с услугами в записи")
    goods_transactions: list[RecordsCompanyidResponseDataTypesDataItemGoodsTransactionsItem] | None = Field(default=None, description="Массив товарных транзакций")
    staff: RecordsCompanyidResponseDataTypesDataItemStaff | None = Field(default=None)
    client_: RecordsCompanyidResponseDataTypesDataItemClient | None = Field(default=None, alias="client")
    comer: dict[str, Any] | None = Field(default=None, description="Данные о посетителе (может быть null)")
    clients_count: int | None = Field(default=None, description="Количество клиентов (В индивидуальной записи всегда = 1)")
    date: str | None = Field(default=None, description="Дата сеанса")
    datetime: str | None = Field(default=None, description="Дата сеанса в ISO")
    create_date: str | None = Field(default=None, description="Дата создания сеанса")
    technical_break_duration: float | None = Field(default=None, description="Длительность технического перерыва")
    comment: str | None = Field(default=None, description="Комментарий к записи")
    online: bool | None = Field(default=None, description="(Только при чтении) Запись онлайновая или нет (false если запись внес администратор)")
    visit_attendance: float | None = Field(default=None, description="Статус визита, 2 - Пользователь подтвердил запись, 1 - Пользователь пришел, услуги оказаны, 0 - ожидание пользователя, -1 - пользователь не пришел на визит")
    attendance: float | None = Field(default=None, description="Статус записи, 2 - Пользователь подтвердил запись, 1 - Пользователь пришел, услуги оказаны, 0 - ожидание пользователя, -1 - пользователь не пришел на визит")
    confirmed: float | None = Field(default=None, description="Статус подтверждения записи, 0 - не подтверждена, 1 - подтверждена")
    seance_length: float | None = Field(default=None, description="Длительность сеанса")
    length: float | None = Field(default=None, description="Длительность сеанса")
    sms_before: float | None = Field(default=None, description="Отправить ли клиенту смс с напоминанием о записи (если клиент указан)")
    sms_now: float | None = Field(default=None, description="Отправляли ли смс при добавлении записи")
    sms_now_text: str | None = Field(default=None, description="Текст смс")
    email_now: float | None = Field(default=None, description="Отправлено ли уведомление по email")
    notified: float | None = Field(default=None, description="Флаг пождтверждения записи администратором филиала, если клиент попросил подтвердить запись")
    master_request: float | None = Field(default=None, description="Был ли указан определенный специалист при записи (false если был указан \"не имеет значения\")")
    api_id: str | None = Field(default=None, description="Внешний идентификатор записи")
    from_url: str | None = Field(default=None, description="С какой страницы был совершён переход для оформления записи (сайт, приложение ВК и прочее)")
    review_requested: float | None = Field(default=None, description="Флаг запроса у клиента отзыва о посещении")
    visit_id: float | None = Field(default=None, description="Идентификатор визита")
    created_user_id: float | None = Field(default=None, description="Идентификатор пользователя, создавшего запись")
    deleted: bool | None = Field(default=None, description="(Только при чтении) Удалена ли запись (true если удалена)")
    paid_full: float | None = Field(default=None, description="Флаг, оплачена ли запись полностью (1 - если оплачена полностью)")
    prepaid: bool | None = Field(default=None, description="Доступна ли онлайн-оплата")
    prepaid_confirmed: bool | None = Field(default=None, description="Статус онлайн-оплаты")
    payment_status: int | None = Field(default=None, description="Статус автооплаты абонементом (0 - Визит не оплачен, 1 - Визит оплачен, 2 - визит оплачен абонементом автоматически, 3 - Визит не удалось оплатить автоматически, 4 - будет оплачен абонементом автом...")
    last_change_date: str | None = Field(default=None, description="Дата последнего редактирования записи")
    custom_color: str | None = Field(default=None, description="Цвет записи в журнале")
    custom_font_color: str | None = Field(default=None, description="(Только при чтении) Цвет шрифта записи")
    record_labels: list[dict[str, Any]] | None = Field(default=None, description="Категории записи")
    activity_id: int | None = Field(default=None, description="Идентификатор группового события")
    custom_fields: dict[str, Any] | None = Field(default=None, description="Дополнительные поля")
    documents: list[RecordsCompanyidResponseDataTypesDataItemDocumentsItem] | None = Field(default=None, description="Массив документов")
    sms_remain_hours: float | None = Field(default=None, description="За сколько часов до начала визита отправить sms с напоминанием")
    email_remain_hours: float | None = Field(default=None, description="За сколько часов до начала визита отправить email с напоминанием")
    bookform_id: float | None = Field(default=None, description="Идентификатор формы онлайн-записи")
    record_from: str | None = Field(default=None, description="Название формы онлайн-записи")
    is_mobile: float | None = Field(default=None, description="Тип устройства, с которого записались (0 - запись, создана администратором, через web-версию или моб. приложение для администраторов, 1 - Мобильный браузер, виджет онлайн-записи, 2 - Десктопный бра...")
    client_agreements: RecordsCompanyidResponseDataTypesDataItemClientAgreements | None = Field(default=None)
    is_sale_bill_printed: bool | None = Field(default=None, description="Распечатан ли чек продажи")
    consumables: list[RecordsCompanyidResponseDataTypesDataItemConsumablesItem] | None = Field(default=None, description="Массив расходных материалов")
    finance_transactions: list[RecordsCompanyidResponseDataTypesDataItemFinanceTransactionsItem] | None = Field(default=None, description="Массив финансовых транзакций (может быть пустым)")


class RecordsCompanyidResponseDataTypes(BaseModel):
    """Получить список записей
    Схема спеки: Root Type for records_companyid_response_data-types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: list[RecordsCompanyidResponseDataTypesDataItem] | None = Field(default=None, alias="data", description="Массив объектов с данными")
    meta: RecordsCompanyidResponseDataTypesMeta | None = Field(default=None)

__all__ = [
    "RecordCompanyidResponse201DataTypes",
    "RecordCompanyidResponse201DataTypesData",
    "RecordCompanyidResponse201DataTypesDataClient",
    "RecordCompanyidResponse201DataTypesDataDocumentsItem",
    "RecordCompanyidResponse201DataTypesDataServicesItem",
    "RecordCompanyidResponse201DataTypesDataStaff",
    "RecordCompanyidResponseDataTypes",
    "RecordCompanyidResponseDataTypesData",
    "RecordCompanyidResponseDataTypesDataConsumablesItem",
    "RecordCompanyidResponseDataTypesDataDocumentsItem",
    "RecordCompanyidResponseDataTypesDataFinanceTransactionsItem",
    "RecordCompanyidResponseDataTypesDataFinanceTransactionsItemAccount",
    "RecordCompanyidResponseDataTypesDataFinanceTransactionsItemClient",
    "RecordCompanyidResponseDataTypesDataFinanceTransactionsItemExpense",
    "RecordCompanyidResponseDataTypesDataRecordLabelsItem",
    "RecordCompanyidResponseDataTypesDataServicesItem",
    "RecordCompanyidResponseDataTypesDataStaff",
    "RecordCompanyidResponseDataTypesDataStaffPosition",
    "RecordsCompanyidRequestDataTypes",
    "RecordsCompanyidRequestDataTypesClient",
    "RecordsCompanyidRequestDataTypesClientAgreements",
    "RecordsCompanyidRequestDataTypesCustomFields",
    "RecordsCompanyidRequestDataTypesServicesItem",
    "RecordsCompanyidResponseDataTypes",
    "RecordsCompanyidResponseDataTypesDataItem",
    "RecordsCompanyidResponseDataTypesDataItemClient",
    "RecordsCompanyidResponseDataTypesDataItemClientAgreements",
    "RecordsCompanyidResponseDataTypesDataItemConsumablesItem",
    "RecordsCompanyidResponseDataTypesDataItemDocumentsItem",
    "RecordsCompanyidResponseDataTypesDataItemFinanceTransactionsItem",
    "RecordsCompanyidResponseDataTypesDataItemFinanceTransactionsItemAccount",
    "RecordsCompanyidResponseDataTypesDataItemFinanceTransactionsItemAccountClient",
    "RecordsCompanyidResponseDataTypesDataItemFinanceTransactionsItemExpense",
    "RecordsCompanyidResponseDataTypesDataItemGoodsTransactionsItem",
    "RecordsCompanyidResponseDataTypesDataItemServicesItem",
    "RecordsCompanyidResponseDataTypesDataItemStaff",
    "RecordsCompanyidResponseDataTypesDataItemStaffPosition",
    "RecordsCompanyidResponseDataTypesMeta",
    "ReferencesBusinessGroupResponseDataTypes",
    "ReferencesBusinessGroupResponseDataTypesDataItem",
    "ReferencesBusinessGroupResponseDataTypesDataItemTypesItem",
    "ReferencesBusinessGroupResponseDataTypesMeta",
    "ResourceInstance",
    "ResourcesCompanyidDataTypes",
    "ResourcesCompanyidDataTypesDataItem",
    "ResourcesCompanyidDataTypesDataItemInstancesItem",
    "ResourcesCompanyidDataTypesMeta",
    "ResponseMetaCountObject",
    "ResponseMetaDatePaginatorObject",
    "ResponseMetaDatePaginatorObjectDateCursor",
    "ResponseMetaDatePaginatorObjectDateCursorCurrent",
    "ResponseMetaDatePaginatorObjectDateCursorNext",
    "ResponseMetaDatePaginatorObjectDateCursorPrevious"
]
