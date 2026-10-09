"""Модели YCLIENTS API (p2: P).

Сгенерировано scripts/generate.py -- не редактируйте вручную.
"""

from __future__ import annotations

from datetime import date, datetime
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class PostUserIdCopyToCompaniesRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    user_company_links: list[PostUserIdCopyToCompaniesRequestUserCompanyLinksItem] = Field(description="Список филиалов, куда необходимо скопировать права пользователя")


class PostUserIdRemoveFromCompaniesRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    user_company_links: list[PostUserIdRemoveFromCompaniesRequestUserCompanyLinksItem] = Field(description="Список филиалов, откуда необходимо удалить пользователя")


class PutAbonementTypesLoyaltyAbonementTypeIdRequestAvailabilityItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    week_days: list[int] | None = Field(default=None, description="Дни недели, в которых действует условие. (1 - понедельник, 7 - воскресенье).")
    intervals: list[PutAbonementTypesLoyaltyAbonementTypeIdRequestAvailabilityItemIntervalsItem] | None = Field(default=None, description="Интервалы доступности.")


class PutStaffMasterIdResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: MasterServiceLink2 | None = Field(default=None, alias="data")
    meta: dict[str, Any] | None = Field(default=None)


class PutStaffScheduleRequestSchedulesToSetItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    staff_id: float | None = Field(default=None, description="Идентификатор сотрудника.")
    dates: list[str] | None = Field(default=None, description="Дата для установки графика работы сотрудника в формате Y-m-d.")
    slots: list[PutStaffScheduleRequestSchedulesToSetItemSlotsItem] | None = Field(default=None, description="Массив интервалов времени, когда сотрудник работает.")


class PutStaffScheduleResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: list[MasterScheduleDayContainer] | None = Field(default=None, alias="data")
    meta: ResponseMetaCountObject | None = Field(default=None)


class PutUserIdPermissionsResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: UserRolePermissions | None = Field(default=None, alias="data")
    meta: dict[str, Any] | None = Field(default=None)


class PutWaitingListWaitingListEntryIdRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    comment: str | None = Field(default=None, description="Комментарий")
    client_: PutWaitingListWaitingListEntryIdRequestClient = Field(alias="client")
    service_ids: list[Any] = Field(description="Идентификаторы услуг")
    staff_ids: list[Any] | None = Field(default=None, description="Идентификаторы сотрудников")
    intervals: list[PutWaitingListWaitingListEntryIdRequestIntervalsItem] | None = Field(default=None, description="Интервалы дат и времени, на которые клиент хочет создать запись")


class PostActivityIdRecordsRequestClient(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор клиента.")
    client_: PostActivityIdRecordsRequestClientClient | None = Field(default=None, alias="client")


class PostClientIdCommentsResponse201(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: ClientCommentContainer | None = Field(default=None, alias="data")
    meta: dict[str, Any] | None = Field(default=None)


class PostImagesEntityResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    image_group: ImageGroup2 | None = Field(default=None, alias="ImageGroup")
    image_group_2: ImageGroup2 = Field(alias="image_group")


class PostLoyaltyAbonementTypesRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    title: str = Field(description="Название типа абонемента.")
    salon_group_id: float = Field(description="Идентификатор сети.")
    cost: float = Field(description="Цена абонемента")
    salon_ids: list[float] | None = Field(default=None, description="Список ID филиалов.")
    period: float | None = Field(default=None, description="Продолжительность периода действия.")
    period_unit_id: int | None = Field(default=None, description="Тип единиц (1 - день, 2 - неделя, 3 - месяц, 4 - год).")
    allow_freeze: bool | None = Field(default=None, description="Возможность заморозки.")
    freeze_limit: int | None = Field(default=None, description="Максимальный общий период заморозки")
    freeze_limit_unit_id: int | None = Field(default=None, description="Единица измерения срока заморозки абонемента (1 - день, 2 - неделя, 3 - месяц, 4 - год).")
    service_price_correction: bool | None = Field(default=None, description="Возможность корректировки цены услуги при применении абонемента.")
    expiration_type_id: int | None = Field(default=None, description="Тип активации абонемента (1 - при продаже, 2 - при первом использовании, 3 - с конкретной даты).")
    is_allow_empty_code: bool | None = Field(default=None, description="Общий или именной абонемент. true - именной абонемент пользуется только один человек, который его купил. false - могут пользоваться несколько человек по специальному коду.")
    is_united_balance: bool = Field(description="Признак общего баланса (true - общий баланс, false - раздельный).")
    united_balance_services_count: int = Field(description="Количество посещений при общем балансе.")
    balance_edit_type_id: int | None = Field(default=None, description="Тип корректировки баланса (0 - корректировка запрещена, 1 - в филиале где был продан абонемент, 2 - во всех филиалах).")
    is_online_sale_enabled: bool | None = Field(default=None, description="Онлайн продажа (true - разрешена, false - запрещена). Если параметр передан равным true, то тогда параметр online_sale_price обязателен.")
    online_sale_title: str | None = Field(default=None, description="Название абонемента при онлайн продаже.")
    online_sale_description: str | None = Field(default=None, description="Описание абонемента при онлайн продаже.")
    online_sale_price: float | None = Field(default=None, description="Цена абонемента при онлайн продаже.")
    online_image: str | None = Field(default=None, description="Изображение абонемента при онлайн продаже.")
    autoactivation_period: int | None = Field(default=None, description="Максимальный период автоактивации.")
    autoactivation_time_in_days: int | None = Field(default=None, description="Количество единиц времени для автоактивации абонемента.")
    autoactivation_time_unit_id: int | None = Field(default=None, description="Единицы измерения для автоактивации (1 - дни, 2 - недели, 3 - месяцы, 4 - годы).")
    is_archived: bool | None = Field(default=None, description="Признак архивации абонемента.")
    services: list[int] | None = Field(default=None, description="Список ID услуг.")
    service_categories: list[int] = Field(description="Список ID категорий услуг.")
    availability: list[PostLoyaltyAbonementTypesRequestAvailabilityItem] | None = Field(default=None, description="Список условий времени действия абонемента, при пустом массиве абонемент действует в любое время.")


class PostLoyaltyAbonementTypesResponse201(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: LoyaltyAbonementTypeWithSalons | None = Field(default=None, alias="data")
    meta: dict[str, Any] | None = Field(default=None)


class PostStaffQuickResponse201(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: MasterWithPosition | None = Field(default=None, alias="data")
    meta: dict[str, Any] | None = Field(default=None)


class PutAbonementTypesLoyaltyAbonementTypeIdRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    title: str = Field(description="Название типа абонемента.")
    salon_group_id: float = Field(description="Идентификатор сети.")
    cost: float = Field(description="Цена абонемента.")
    salon_ids: list[float] | None = Field(default=None, description="Список ID филиалов.")
    period: float | None = Field(default=None, description="Продолжительность периода действия.")
    period_unit_id: int | None = Field(default=None, description="Тип единиц измерения продолжительности периода действия типа абонемента (1 - день, 2 - неделя, 3 - месяц, 4 - год).")
    allow_freeze: bool | None = Field(default=None, description="Возможность заморозки.")
    freeze_limit: int | None = Field(default=None, description="Максимальный общий период заморозки.")
    freeze_limit_unit_id: int | None = Field(default=None, description="Единица измерения срока заморозки абонемента (1 - день, 2 - неделя, 3 - месяц, 4 - год).")
    service_price_correction: bool | None = Field(default=None, description="Возможность корректировки цены услуги при применении абонемента.")
    expiration_type_id: int | None = Field(default=None, description="Тип активации абонемента (1 - при продаже, 2 - при первом использовании, 3 - с конкретной даты).")
    is_allow_empty_code: bool | None = Field(default=None, description="Общий или именной абонемент. true - именной абонемент пользуется только один человек, который его купил. false - могут пользоваться несколько человек по специальному коду.")
    is_united_balance: bool = Field(description="Признак общего баланса (true - общий баланс, false - раздельный).")
    united_balance_services_count: int = Field(description="Кол-во посещений при общем балансе.")
    balance_edit_type_id: int | None = Field(default=None, description="Тип корректировки баланса (0 - корректировка запрещена, 1 - в филиале где был продан абонемент, 2 - во всех филиалах).")
    is_online_sale_enabled: bool | None = Field(default=None, description="Онлайн продажа (true - разрешена, false - запрещена).")
    online_sale_title: str | None = Field(default=None, description="Название абонемента при онлайн продаже.")
    online_sale_description: str | None = Field(default=None, description="Описание абонемента при онлайн продаже.")
    online_sale_price: float | None = Field(default=None, description="Цена абонемента при онлайн продаже.")
    online_image: str | None = Field(default=None, description="Изображение абонемента при онлайн продаже.")
    autoactivation_period: int | None = Field(default=None, description="Максимальный период автоактивации.")
    autoactivation_time: int | None = Field(default=None, description="Кол-во единиц времени для автоактивации типа абонемента.")
    autoactivation_time_unit_id: int | None = Field(default=None, description="Единицы измерения для автоактивации (1 - дни, 2 - недели, 3 - месяцы, 4 - годы).")
    is_archived: bool | None = Field(default=None, description="Признак архивации абонемента.")
    services: list[int] | None = Field(default=None, description="Список ID услуг привязанных к типу абонемента.")
    service_categories: list[int] = Field(description="Список ID категорий услуг привязанных к типу абонемента.")
    availability: list[PutAbonementTypesLoyaltyAbonementTypeIdRequestAvailabilityItem] | None = Field(default=None, description="Список условий времени действия абонемента, при пустом массиве абонемент действует в любое время.")


class PutStaffScheduleRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    schedules_to_set: list[PutStaffScheduleRequestSchedulesToSetItem] | None = Field(default=None, description="Массив объектов с графиками работы сотрудников на конкретные даты.")
    schedules_to_delete: list[PutStaffScheduleRequestSchedulesToDeleteItem] | None = Field(default=None, description="Массив объектов с параметрами удаления графиков сотрудников на конкретные даты.")


class PatchDaysDayIdResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: TimetableEventScheduleDay2 | None = Field(default=None, alias="data")
    meta: dict[str, Any] | None = Field(default=None)


class PostActivityIdRecordsRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    client_id: int | None = Field(default=None, description="Идентификатор клиента.")
    comer_id: int | None = Field(default=None, description="Идентификатор посетителя.")
    client_: PostActivityIdRecordsRequestClient = Field(alias="client")
    comer: PostActivityIdRecordsRequestComer | None = Field(default=None)
    labels: list[int] | None = Field(default=None, description="Идентификаторы категорий записи.")
    clients_count: int = Field(description="Количество посетителей.")


class PostScheduleIdDaysResponse201(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: TimetableEventScheduleDay2 | None = Field(default=None, alias="data")
    meta: dict[str, Any] | None = Field(default=None)


class PatchClientSchedulesClientScheduleIdResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: TimetableEventScheduleClientSchedule | None = Field(default=None, alias="data")
    meta: dict[str, Any] | None = Field(default=None)


class PatchSchedulesScheduleIdResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: TimetableEventSchedule2 | None = Field(default=None, alias="data")
    meta: dict[str, Any] | None = Field(default=None)


class PostCompanyIdSchedulesResponse201(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: TimetableEventSchedule2 | None = Field(default=None, alias="data")
    meta: dict[str, Any] | None = Field(default=None)


class PostScheduleIdClientSchedulesResponse201(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: TimetableEventScheduleClientSchedule | None = Field(default=None, alias="data")
    meta: dict[str, Any] | None = Field(default=None)


class PostVisitsSearchResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: ClientVisitsHistory | None = Field(default=None, alias="data")
    meta: ResponseMetaDatePaginatorObject | None = Field(default=None)

__all__ = [
    "PatchClientSchedulesClientScheduleIdResponse200",
    "PatchDaysDayIdResponse200",
    "PatchSchedulesScheduleIdResponse200",
    "PostActivityIdRecordsRequest",
    "PostActivityIdRecordsRequestClient",
    "PostClientIdCommentsResponse201",
    "PostCompanyIdSchedulesResponse201",
    "PostImagesEntityResponse200",
    "PostLoyaltyAbonementTypesRequest",
    "PostLoyaltyAbonementTypesResponse201",
    "PostScheduleIdClientSchedulesResponse201",
    "PostScheduleIdDaysResponse201",
    "PostStaffQuickResponse201",
    "PostUserIdCopyToCompaniesRequest",
    "PostUserIdRemoveFromCompaniesRequest",
    "PostVisitsSearchResponse200",
    "PutAbonementTypesLoyaltyAbonementTypeIdRequest",
    "PutAbonementTypesLoyaltyAbonementTypeIdRequestAvailabilityItem",
    "PutStaffMasterIdResponse200",
    "PutStaffScheduleRequest",
    "PutStaffScheduleRequestSchedulesToSetItem",
    "PutStaffScheduleResponse200",
    "PutUserIdPermissionsResponse200",
    "PutWaitingListWaitingListEntryIdRequest"
]
