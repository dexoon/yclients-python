"""Модели YCLIENTS API (m: M).

Сгенерировано scripts/generate.py -- не редактируйте вручную.
"""

from __future__ import annotations

from datetime import date, datetime
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class MasterRecordReviewResponseDataTypesDataAgreementLinks(BaseModel):
    """Ссылки на соглашения
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    terms_of_use: str | None = Field(default=None, description="Обработка персональных данных")
    confidentiality_agreement: str | None = Field(default=None, description="Политика конфиденциальности")


class MasterRecordReviewResponseDataTypesDataCompany(BaseModel):
    """Компания
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор компании")
    title: str | None = Field(default=None, description="Название компании")
    logo: str | None = Field(default=None, description="Путь к логотипу компании")
    address: str | None = Field(default=None, description="Адрес, по которому расположена компания")


class MasterRecordReviewResponseDataTypesDataCurrency(BaseModel):
    """Валюта компании
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор валюты")
    iso: str | None = Field(default=None, description="Название в ISO формате")
    name: str | None = Field(default=None, description="Название валюты")
    symbol: str | None = Field(default=None, description="Обозначение валюты")
    is_symbol_after_amount: bool | None = Field(default=None)


class MasterRecordReviewResponseDataTypesDataLanguage(BaseModel):
    """Язык
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор языка")
    locale: str | None = Field(default=None, description="Локализация")
    iso: str | None = Field(default=None, description="Название в ISO формате")


class MasterRecordReviewResponseDataTypesDataMasterPosition(BaseModel):
    """Должность
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор должности")
    title: str | None = Field(default=None, description="Название должности")


class MasterRecordReviewResponseDataTypesDataRecord(BaseModel):
    """Запись
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор записи")
    payed_cost: str | None = Field(default=None, description="Оплаченная стоимость")
    date: str | None = Field(default=None, description="Дата")


class MasterScheduleDayContainerBusyIntervalsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    entity_type: Literal["record", "activity"] | None = Field(default=None, description="Тип сущности, в рамках которой сотрудник занят.")
    entity_id: float | None = Field(default=None, description="Идентификатор сущности, в рамках которой сотрудник занят.")
    from_: str | None = Field(default=None, alias="from", description="Начало интервала графика работы сотрудника в формате H:i:s.")
    to: str | None = Field(default=None, description="Конец интервала графика работы сотрудника в формате H:i:s.")


class MasterScheduleDayContainerSlotsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    from_: str | None = Field(default=None, alias="from", description="Начало интервала графика работы сотрудника в формате H:i.")
    to: str | None = Field(default=None, description="Конец интервала графика работы сотрудника в формате H:i.")


class MasterRecordReviewPostRequest(BaseModel):
    """Запрос отправки отзыва
    Схема спеки: Root Type for master_record_review_post_request
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    rating: int = Field(description="Оценка, выставляемая за отзыв (кол-во звезд от 1 до 5)")
    text: str | None = Field(default=None, description="Текст отзыва")
    tips_amount: float | None = Field(default=None, description="Сумма чаевых")
    redirect_prefix: str | None = Field(default=None, description="Префиксная часть url, на который будет выполнен редирект после возврата с формы оплаты")


class MasterScheduleDayContainer(BaseModel):
    """Данные по существующему в филиале графику работы сотрудника.
    Схема спеки: Объект модели "Расписание сотрудника"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    staff_id: float | None = Field(default=None, description="Идентификатор сотрудника.")
    date: str | None = Field(default=None, description="Дата в рамках графика в формате Y-m-d.")
    slots: list[MasterScheduleDayContainerSlotsItem] | None = Field(default=None, description="Массив интервалов времени, когда сотрудник работает.")
    busy_intervals: list[MasterScheduleDayContainerBusyIntervalsItem] | None = Field(default=None, description="Массив интервалов времени, занятого записями или событиями.")
    off_day_type: float | None = Field(default=None, description="Идентификатор типа нерабочего дня, созданного в филиале.")


class MasterServiceLink2(BaseModel):
    """Схема спеки: Объект модели "Сотрудник, оказывающий услугу"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    service_id: float | None = Field(default=None, description="Идентификатор услуги.")
    master_id: float | None = Field(default=None, description="Идентификатор сотрудника.")
    length: float | None = Field(default=None, description="Длительность оказания услуги указанным сотрудником в секундах.")
    technological_card_id: float | None = Field(default=None, description="Идентификатор технологической карты.")


class M200SuccessResponse(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: dict[str, Any] | None = Field(default=None, alias="data")
    meta: dict[str, Any] | None = Field(default=None)


class MasterRecordReviewResponseDataTypesDataMaster(BaseModel):
    """Сотрудник
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="Идентификатор сотрудника")
    name: str | None = Field(default=None, description="Имя сотрудника")
    company_id: float | None = Field(default=None, description="Идентификатор компании")
    specialization: str | None = Field(default=None, description="Специализация сотрудника")
    rating: int | None = Field(default=None, description="Рейтинг")
    show_rating: int | None = Field(default=None, description="Количество голосов")
    avatar: str | None = Field(default=None, description="Путь к аватарке сотрудника")
    prepaid: str | None = Field(default=None, description="Разрешена ли предоплата")
    position: MasterRecordReviewResponseDataTypesDataMasterPosition | None = Field(default=None)


class MasterWithPosition(BaseModel):
    """Схема спеки: Объект модели "Сотрудник с Должностью"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор сотрудника.")
    name: str | None = Field(default=None, description="Имя сотрудника.")
    company_id: float | None = Field(default=None, description="Идентификатор филиала, в котором создан сотрудник.")
    specialization: str | None = Field(default=None, description="Специализация сотрудника.")
    avatar: str | None = Field(default=None, description="Ссылка на аватар сотрудника (уменьшенный).")
    avatar_big: str | None = Field(default=None, description="Ссылка на аватар сотрудника (оригинальный).")
    position: dict[str, Any] | None = Field(default=None, description="Должность, к которой привязан сотрудник.")


class MasterRecordReviewResponseDataTypesData(BaseModel):
    """Объект с данными
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    favicon_url: str | None = Field(default=None, description="Пусть к логотипу")
    is_review_submitted: bool | None = Field(default=None, description="Отправлен ли отзыв")
    page_title: str | None = Field(default=None, description="Название страницы")
    master: MasterRecordReviewResponseDataTypesDataMaster | None = Field(default=None)
    company: MasterRecordReviewResponseDataTypesDataCompany | None = Field(default=None)
    tips: list[dict[str, Any]] | None = Field(default=None, description="Чаевые")
    record: MasterRecordReviewResponseDataTypesDataRecord | None = Field(default=None)
    currency: MasterRecordReviewResponseDataTypesDataCurrency | None = Field(default=None)
    agreement_links: MasterRecordReviewResponseDataTypesDataAgreementLinks | None = Field(default=None)
    language: MasterRecordReviewResponseDataTypesDataLanguage | None = Field(default=None)


class MasterRecordReviewResponseDataTypes(BaseModel):
    """Получение статуса формы отзыва
    Схема спеки: Root Type for master_record_review_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: MasterRecordReviewResponseDataTypesData | None = Field(default=None, alias="data")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")

__all__ = [
    "M200SuccessResponse",
    "MasterRecordReviewPostRequest",
    "MasterRecordReviewResponseDataTypes",
    "MasterRecordReviewResponseDataTypesData",
    "MasterRecordReviewResponseDataTypesDataAgreementLinks",
    "MasterRecordReviewResponseDataTypesDataCompany",
    "MasterRecordReviewResponseDataTypesDataCurrency",
    "MasterRecordReviewResponseDataTypesDataLanguage",
    "MasterRecordReviewResponseDataTypesDataMaster",
    "MasterRecordReviewResponseDataTypesDataMasterPosition",
    "MasterRecordReviewResponseDataTypesDataRecord",
    "MasterScheduleDayContainer",
    "MasterScheduleDayContainerBusyIntervalsItem",
    "MasterScheduleDayContainerSlotsItem",
    "MasterServiceLink2",
    "MasterWithPosition"
]
