"""Модели YCLIENTS API, сгенерированы из docs/openapi.json.

Не редактируйте вручную: запустите scripts/generate.py.
"""





from __future__ import annotations

from datetime import date, datetime
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class GetApplicationApplicationIdResponse200DataConnectionStatus(BaseModel):
    """Модель статуса установки приложения в салоне
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    status: Literal["pending", "freezed", "active"] | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f \u0432 \u0441\u0430\u043b\u043e\u043d\u0435. Pending - \u0436\u0434\u0435\u0442 \u0430\u043a\u0442\u0438\u0432\u0430\u0446\u0438\u0438 \u043e\u0442 \u043f\u0430\u0440\u0442\u043d\u0435\u0440\u0430, Freezed - \u0437\u0430\u043c\u043e\u0440\u043e\u0436\u0435\u043d\u043e \u043f\u043e \u043f\u0440\u0438\u0447\u0438\u043d\u0435 \u043d\u0435\u0443\u043f\u043b\u0430\u0442\u044b, Active - \u0430\u043a\u0442\u0438\u0432\u043d\u043e")
    created_at: str | None = Field(default=None, description="\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f \u0441\u0432\u044f\u0437\u043a\u0438 \u041f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435-\u0421\u0430\u043b\u043e\u043d")


class GetApplicationApplicationIdResponse200DataLogsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    changed_at: str | None = Field(default=None, description="\u0414\u0430\u0442\u0430 \u0441\u043c\u0435\u043d\u044b \u0441\u0442\u0430\u0442\u0443\u0441\u0430")
    status_from: str | None = Field(default=None, description="\u041f\u0440\u0435\u0434\u044b\u0434\u0443\u0449\u0438\u0439 \u0441\u0442\u0430\u0442\u0443\u0441 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f \u0432 \u0441\u0430\u043b\u043e\u043d\u0435")
    status_to: str | None = Field(default=None, description="\u041d\u043e\u0432\u044b\u0439 \u0441\u0442\u0430\u0442\u0443\u0441 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f \u0432 \u0441\u0430\u043b\u043e\u043d\u0435")
    source: str | None = Field(default=None, description="\u0418\u0441\u0442\u043e\u0447\u043d\u0438\u043a \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u0441\u0442\u0430\u0442\u0443\u0441\u0430")


class GetApplicationApplicationIdResponse200DataPaymentsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="ID \u043f\u043b\u0430\u0442\u0435\u0436\u0430.")
    payment_sum: float | None = Field(default=None, description="\u0421\u0443\u043c\u043c\u0430 \u043e\u043f\u043b\u0430\u0442\u044b \u0437\u0430 \u043f\u0435\u0440\u0438\u043e\u0434.")
    payment_date: str | None = Field(default=None, description="\u0414\u0430\u0442\u0430 \u043e\u043f\u043b\u0430\u0442\u044b.")
    is_refunded: bool | None = Field(default=None, description="\u0411\u044b\u043b \u043b\u0438 \u0432\u043e\u0437\u0432\u0440\u0430\u0442 \u043f\u043b\u0430\u0442\u0435\u0436\u0430.")
    currency_iso: str | None = Field(default=None, description="ISO \u0432\u0430\u043b\u044e\u0442\u044b \u043f\u043b\u0430\u0442\u0435\u0436\u0430")
    period_from: str | None = Field(default=None, description="\u0414\u0430\u0442\u0430 \u043d\u0430\u0447\u0430\u043b\u0430 \u043f\u043e\u0434\u043f\u0438\u0441\u043a\u0438")
    period_to: str | None = Field(default=None, description="\u0414\u0430\u0442\u0430 \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f \u043f\u043e\u0434\u043f\u0438\u0441\u043a\u0438")


class GetApplicationIdTariffsResponse200DataItemOptionsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="ID \u041e\u043f\u0446\u0438\u0438 \u0442\u0430\u0440\u0438\u0444\u0430.")
    title: str | None = Field(default=None, description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043e\u043f\u0446\u0438\u0438 \u0442\u0430\u0440\u0438\u0444\u0430.")
    overall_price: float | None = Field(default=None, description="\u041e\u0431\u0449\u0430\u044f \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u043e\u043f\u0446\u0438\u0438 \u0442\u0430\u0440\u0438\u0444\u0430.")
    duration_in_months: bool | None = Field(default=None, description="\u0414\u043b\u0438\u043d\u0430 \u0432 \u043c\u0435\u0441\u044f\u0446\u0430\u0445 \u043e\u0441\u043d\u043e\u0432\u043d\u043e\u0433\u043e \u0442\u0435\u043b\u0430 \u0442\u0430\u0440\u0438\u0444\u0430.")
    currency_iso: str | None = Field(default=None, description="ISO \u0432\u0430\u043b\u044e\u0442\u044b \u0442\u0430\u0440\u0438\u0444\u0430")
    staff_amount: float | None = Field(default=None, description="\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u043e\u0432 \u0442\u0430\u0440\u0438\u0444\u0430 YCLIENTS, \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u044b\u0435 \u0434\u043b\u044f \u043f\u0440\u0438\u043e\u0431\u0440\u0435\u0442\u0435\u043d\u0438\u044f \u0434\u0430\u043d\u043d\u043e\u0439 \u043e\u043f\u0446\u0438\u0438")
    free_period_in_months: float | None = Field(default=None, description="\u0414\u043b\u0438\u043d\u0430 \u0432 \u043c\u0435\u0441\u044f\u0446\u0430\u0445 \u043f\u043e\u0434\u0430\u0440\u043e\u0447\u043d\u043e\u0433\u043e \u043f\u0435\u0440\u0438\u043e\u0434\u0430")


class GetApplicationPaymentLinkResponse200Data(BaseModel):
    """Объект со ссылкой на оплату
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    url: str | None = Field(default=None, description="\u0410\u0434\u0440\u0435\u0441 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b \u043e\u043f\u043b\u0430\u0442\u044b.")


class GetIntegrationCallsRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    salon_id: float = Field(description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0441\u0430\u043b\u043e\u043d\u0430.")
    date_from: str = Field(description="\u0414\u0430\u0442\u0430 \u043d\u0430\u0447\u0430\u043b\u0430 \u0432\u044b\u0431\u043e\u0440\u043a\u0438.")
    date_to: str = Field(description="\u0414\u0430\u0442\u0430 \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f \u0432\u044b\u0431\u043e\u0440\u043a\u0438.")
    phone: str | None = Field(default=None, description="\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430.")
    types: list[Literal["incoming", "outgoing", "internal"]] | None = Field(default=None, description="\u041d\u0430\u0431\u043e\u0440 \u0442\u0438\u043f\u043e\u0432 \u0437\u0432\u043e\u043d\u043a\u0430")
    statuses: list[Literal["success", "missed", "cancel", "busy", "notallowed", "notavailable", "notfound"]] | None = Field(default=None, description="\u041d\u0430\u0431\u043e\u0440 \u0441\u0442\u0430\u0442\u0443\u0441\u043e\u0432")
    page_: float | None = Field(default=None, alias="page", description="\u041d\u043e\u043c\u0435\u0440 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b")
    limit: float | None = Field(default=None, description="\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432 \u043d\u0430 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435")


class GetIntegrationCallsResponse200DataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="ID \u0437\u0432\u043e\u043d\u043a\u0430")
    client_id: int | None = Field(default=None, description="ID \u043a\u043b\u0438\u0435\u043d\u0442\u0430 (\u043f\u0440\u0438 \u043d\u0430\u043b\u0438\u0447\u0438\u0438 \u043a\u043b\u0438\u0435\u043d\u0442\u0430 \u0432 \u041a\u0411)")
    caller_phone: str | None = Field(default=None, description="\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430")
    record_link: str | None = Field(default=None, description="\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0437\u0430\u043f\u0438\u0441\u044c \u0437\u0432\u043e\u043d\u043a\u0430 (\u043f\u0440\u0438 \u043d\u0430\u043b\u0438\u0447\u0438\u0438)")
    duration: int | None = Field(default=None, description="\u041f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0437\u0432\u043e\u043d\u043a\u0430 \u0432 \u0441\u0435\u043a\u0443\u043d\u0434\u0430\u0445")
    status: Literal["success", "missed", "cancel", "busy", "notallowed", "notavailable", "notfound"] | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0434\u043e\u0437\u0432\u043e\u043d\u0430")
    type_: Literal["incoming", "outgoing", "internal"] | None = Field(default=None, alias="type", description="\u0422\u0438\u043f \u0437\u0432\u043e\u043d\u043a\u0430")
    call_date: str | None = Field(default=None, description="\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0437\u0432\u043e\u043d\u043a\u0430")


class GetStaffIdDateResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    time: str = Field(description="\u0412\u0440\u0435\u043c\u044f \u0441\u0435\u0430\u043d\u0441\u0430")
    is_free: bool = Field(description="\u0421\u0432\u043e\u0431\u043e\u0434\u043d\u043e \u0432\u0440\u0435\u043c\u044f \u0438\u043b\u0438 \u043d\u0435\u0442")


class GetStartDateEndDateResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    date: str = Field(description="\u0434\u0430\u0442\u0430 \u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435 iso8601.")
    is_working: bool = Field(description="\u0421\u0432\u043e\u0431\u043e\u0434\u043d\u043e \u0432\u0440\u0435\u043c\u044f \u0438\u043b\u0438 \u043d\u0435\u0442.")
    slots: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0430\u0441\u0441\u0438\u0432 (from, to) \u043f\u0440\u043e\u043c\u0435\u0436\u0443\u0442\u043a\u043e\u0432 \u0440\u0430\u0431\u043e\u0447\u0435\u0433\u043e \u0432\u0440\u0435\u043c\u0435\u043d\u0438.")


class PatchAbonementTypesLoyaltyAbonementTypeIdRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    is_archived: bool = Field(description="\u041f\u0440\u0438\u0437\u043d\u0430\u043a \u0430\u0440\u0445\u0438\u0432\u0430\u0446\u0438\u0438 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430. (true - \u0437\u0430\u0430\u0440\u0445\u0438\u0432\u0438\u0440\u043e\u0432\u0430\u043d, false - \u043d\u0435 \u0437\u0430\u0430\u0440\u0445\u0438\u0432\u0438\u0440\u043e\u0432\u0430\u043d).")


class PatchClientSchedulesClientScheduleIdRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    schedule_days_ids: list[float] = Field(description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440\u044b \u0441\u0435\u0440\u0438\u0439 \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f, \u043c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u043e 1 \u0441\u0435\u0440\u0438\u044f, \u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e 7 \u0441\u0435\u0440\u0438\u0439.")
    finish_date_type: Literal["end", "fixed", "abonement"] | None = Field(default=None, description="\u0422\u0438\u043f \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f")
    finish_date: str | None = Field(default=None, description="\u0414\u0430\u0442\u0430 \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f \u043a\u043b\u0438\u0435\u043d\u0442\u0441\u043a\u043e\u0433\u043e \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f **\u26a0\ufe0f \u041e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u043e**, \u0435\u0441\u043b\u0438 `finish_date_type=fixed`.")
    abonement_id: int | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430 **\u26a0\ufe0f\u041e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u0435\u043d, \u0435\u0441\u043b\u0438 finish_date_type=abonement**")


class PatchDaysDayIdRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    force: bool = Field(description="\u0424\u043b\u0430\u0433 \u043f\u0435\u0440\u0435\u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u044f \u0440\u0443\u0447\u043d\u044b\u0445 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0439 \u0432 \u0437\u0430\u043f\u0438\u0441\u044f\u0445/\u0441\u043e\u0431\u044b\u0442\u0438\u044f\u0445 \u043f\u0440\u0438 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u0438 \u0441\u0435\u0440\u0438\u0438 \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f.")
    events_master_id: float | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430, \u043e\u043a\u0430\u0437\u044b\u0432\u0430\u044e\u0449\u0435\u0433\u043e \u0443\u0441\u043b\u0443\u0433\u0438 \u0432 \u0440\u0430\u043c\u043a\u0430\u0445 \u0441\u0435\u0440\u0438\u0438 \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f.")
    events_time: str | None = Field(default=None, description="\u0412\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u0437\u0430\u043f\u0438\u0441\u0435\u0439 \u0438\u043b\u0438 \u0441\u043e\u0431\u044b\u0442\u0438\u0439 \u0432 \u0440\u0430\u043c\u043a\u0430\u0445 \u0441\u0435\u0440\u0438\u0438 \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f (\u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435 HH:MM:SS).")
    events_duration: float | None = Field(default=None, description="\u0414\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u0435\u0439 \u0438\u043b\u0438 \u0441\u043e\u0431\u044b\u0442\u0438\u0439 \u0432 \u0440\u0430\u043c\u043a\u0430\u0445 \u0441\u0435\u0440\u0438\u0438 \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f (\u0432 \u0441\u0435\u043a\u0443\u043d\u0434\u0430\u0445).")
    events_capacity: float | None = Field(default=None, description="\u0412\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u044c \u0441\u043e\u0431\u044b\u0442\u0438\u0439 \u0432 \u0440\u0430\u043c\u043a\u0430\u0445 \u0441\u0435\u0440\u0438\u0438 \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f (\u0434\u043b\u044f \u0437\u0430\u043f\u0438\u0441\u0435\u0439 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0434\u043e\u043b\u0436\u043d\u043e \u0431\u044b\u0442\u044c \u0440\u0430\u0432\u043d\u043e 1).")
    labels_ids: list[float] | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440\u044b \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0439, \u043f\u0440\u0438\u0432\u044f\u0437\u0430\u043d\u043d\u044b\u0445 \u043a \u0437\u0430\u043f\u0438\u0441\u044f\u043c \u0438\u043b\u0438 \u0441\u043e\u0431\u044b\u0442\u0438\u044f\u043c \u0432 \u0440\u0430\u043c\u043a\u0430\u0445 \u0441\u0435\u0440\u0438\u0438 \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f.")
    resource_instances_ids: list[float] | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440\u044b \u044d\u043a\u0437\u0435\u043c\u043f\u043b\u044f\u0440\u043e\u0432 \u0440\u0435\u0441\u0443\u0440\u0441\u043e\u0432, \u043f\u0440\u0438\u0432\u044f\u0437\u0430\u043d\u043d\u044b\u0445 \u043a \u0437\u0430\u043f\u0438\u0441\u044f\u043c \u0438\u043b\u0438 \u0441\u043e\u0431\u044b\u0442\u0438\u044f\u043c \u0432 \u0440\u0430\u043c\u043a\u0430\u0445 \u0441\u0435\u0440\u0438\u0438 \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f.")


class PatchSchedulesScheduleIdRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    date_end: str | None = Field(default=None, description="\u0414\u0430\u0442\u0430 \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f.")


class PostAbonementIdFreezeRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    freeze_till: str = Field(description="\u0414\u0430\u0442\u0430, \u0434\u043e \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u0431\u0443\u0434\u0435\u0442 \u0437\u0430\u043c\u043e\u0440\u043e\u0436\u0435\u043d \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442.")


class PostAbonementIdSetBalanceRequestServicesBalanceCountItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    service_id: int | None = Field(default=None)
    balance: int | None = Field(default=None)


class PostAbonementIdSetPeriodRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    period: float = Field(description="\u0414\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u043f\u0435\u0440\u0438\u043e\u0434\u0430")
    period_unit_id: float = Field(description="\u0422\u0438\u043f \u043f\u0435\u0440\u0438\u043e\u0434\u0430 (1 - \u0434\u0435\u043d\u044c, 2 - \u043d\u0435\u0434\u0435\u043b\u044f, 3 - \u043c\u0435\u0441\u044f\u0446, 4 - \u0433\u043e\u0434)")


class PostAbonementTypesLoyaltyAbonementTypeIdRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    restore_in_title: bool = Field(description="\u041d\u043e\u0432\u043e\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0442\u0438\u043f\u0430 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430, \u043a\u043e\u0442\u043e\u0440\u043e\u0435 \u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u0441\u044f \u043f\u043e\u0441\u043b\u0435 \u0432\u043e\u0441\u0441\u0442\u0430\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f \u0442\u0438\u043f\u0430 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430.")


class PostActivityIdRecordsRequestClientClientAgreementsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    is_newsletter_allowed: bool | None = Field(default=None, description="\u041f\u0440\u0438\u0437\u043d\u0430\u043a \u0441\u043e\u0433\u043b\u0430\u0441\u0438\u044f \u043d\u0430 \u0440\u0430\u0441\u0441\u044b\u043b\u043a\u0443 \u043d\u043e\u0432\u043e\u0441\u0442\u0435\u0439.")
    is_personal_data_processing_allowed: bool | None = Field(default=None, description="\u041f\u0440\u0438\u0437\u043d\u0430\u043a \u0441\u043e\u0433\u043b\u0430\u0441\u0438\u044f \u043d\u0430 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0443 \u043f\u0435\u0440\u0441\u043e\u043d\u0430\u043b\u044c\u043d\u044b\u0445 \u0434\u0430\u043d\u043d\u044b\u0445.")


class PostActivityIdRecordsRequestClientClientCustomFieldValuesItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    code: str | None = Field(default=None, description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u043e\u043b\u044f.")
    value: str | None = Field(default=None, description="\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043f\u043e\u043b\u044f.")


class PostActivityIdRecordsRequestComer(BaseModel):
    """Посетитель.
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    name: str | None = Field(default=None, description="\u0418\u043c\u044f.")


class PostApplicationAddDiscountRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    salon_ids: list[float] = Field(description="\u0421\u043f\u0438\u0441\u043e\u043a ID \u0441\u0430\u043b\u043e\u043d\u043e\u0432")
    application_id: float = Field(description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f.")
    discount: float = Field(description="\u0412\u0435\u043b\u0438\u0447\u0438\u043d\u0430 \u0441\u043a\u0438\u0434\u043a\u0438")


class PostApplicationUpdateChannelRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    salon_id: float = Field(description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0444\u0438\u043b\u0438\u0430\u043b\u0430.")
    application_id: float = Field(description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f (\u0432\u044b\u0434\u0430\u0435\u0442\u0441\u044f \u043f\u043e\u0441\u043b\u0435 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f \u0432 \u0432\u0438\u0442\u0440\u0438\u043d\u0435 YCLIENTS).")
    channel_slug: Literal["sms", "whatsapp"] = Field(description="\u041a\u0430\u043d\u0430\u043b, \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u043e\u0441\u0442\u044c \u043a\u043e\u0442\u043e\u0440\u043e\u0433\u043e \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u0438\u0437\u043c\u0435\u043d\u0438\u0442\u044c.")
    is_available: bool = Field(description="\u0424\u043b\u0430\u0433 \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u043e\u0441\u0442\u0438 \u043a\u0430\u043d\u0430\u043b\u0430 \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0438.")


class PostCallbackRedirectRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    salon_id: float = Field(description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0444\u0438\u043b\u0438\u0430\u043b\u0430.")
    application_id: float = Field(description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f (\u0432\u044b\u0434\u0430\u0435\u0442\u0441\u044f \u043f\u043e\u0441\u043b\u0435 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f \u0432 \u0432\u0438\u0442\u0440\u0438\u043d\u0435 YCLIENTS).")
    api_key: float | None = Field(default=None, description="API-\u043a\u043b\u044e\u0447 \u0434\u043b\u044f \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0438 \u0443\u0432\u0435\u0434\u043e\u043c\u043b\u0435\u043d\u0438\u0439.")
    webhook_urls: list[str] | None = Field(default=None, description="\u041c\u0430\u0441\u0441\u0438\u0432 \u0430\u0434\u0440\u0435\u0441\u043e\u0432 \u0432\u0435\u0431\u0445\u0443\u043a\u043e\u0432.")


class PostCardIdManualTransactionRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    amount: float = Field(description="\u0421\u0443\u043c\u043c\u0430 \u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f/\u043f\u043e\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f. \u041f\u043e\u043b\u043e\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u0434\u043b\u044f \u043f\u043e\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f, \u043e\u0442\u0440\u0438\u0446\u0430\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u0434\u043b\u044f \u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f.")
    title: str | None = Field(default=None, description="\u041f\u0440\u0438\u043c\u0435\u0447\u0430\u043d\u0438\u0435 \u043a \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u0438.")


class PostCardIdManualTransactionRequest2(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    amount: float = Field(description="\u0421\u0443\u043c\u043c\u0430 \u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f/\u043f\u043e\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f. \u041f\u043e\u043b\u043e\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u0434\u043b\u044f \u043f\u043e\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f, \u043e\u0442\u0440\u0438\u0446\u0430\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u0434\u043b\u044f \u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f.")
    title: str | None = Field(default=None, description="\u041f\u0440\u0438\u043c\u0435\u0447\u0430\u043d\u0438\u0435 \u043a \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u0438.")


class PostClientIdCommentsRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    text: str = Field(description="\u0422\u0435\u043a\u0441\u0442 \u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u044f \u043a \u043a\u043b\u0438\u0435\u043d\u0442\u0443.")


class PostCompanyIdSchedulesRequestDaysItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    day_of_week: Literal["mon", "tue", "wed", "thu", "fri", "sat", "sun"] = Field(description="\u0414\u0435\u043d\u044c \u043d\u0435\u0434\u0435\u043b\u0438 \u0441\u0435\u0440\u0438\u0438 \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f.")
    events_master_id: float = Field(description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430, \u043e\u043a\u0430\u0437\u044b\u0432\u0430\u044e\u0449\u0435\u0433\u043e \u0443\u0441\u043b\u0443\u0433\u0438 \u0432 \u0440\u0430\u043c\u043a\u0430\u0445 \u0441\u0435\u0440\u0438\u0438 \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f.")
    events_time: str = Field(description="\u0412\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u0437\u0430\u043f\u0438\u0441\u0435\u0439 \u0438\u043b\u0438 \u0441\u043e\u0431\u044b\u0442\u0438\u0439 \u0432 \u0440\u0430\u043c\u043a\u0430\u0445 \u0441\u0435\u0440\u0438\u0438 \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f (\u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435 HH:MM:SS).")
    events_duration: float = Field(description="\u0414\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u0435\u0439 \u0438\u043b\u0438 \u0441\u043e\u0431\u044b\u0442\u0438\u0439 \u0432 \u0440\u0430\u043c\u043a\u0430\u0445 \u0441\u0435\u0440\u0438\u0438 \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f (\u0432 \u0441\u0435\u043a\u0443\u043d\u0434\u0430\u0445).")
    events_capacity: float = Field(description="\u0412\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u044c \u0441\u043e\u0431\u044b\u0442\u0438\u0439 \u0432 \u0440\u0430\u043c\u043a\u0430\u0445 \u0441\u0435\u0440\u0438\u0438 \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f (\u0434\u043b\u044f \u0437\u0430\u043f\u0438\u0441\u0435\u0439 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0434\u043e\u043b\u0436\u043d\u043e \u0431\u044b\u0442\u044c \u0440\u0430\u0432\u043d\u043e 1).")
    labels_ids: list[float] | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440\u044b \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0439, \u043f\u0440\u0438\u0432\u044f\u0437\u0430\u043d\u043d\u044b\u0445 \u043a \u0437\u0430\u043f\u0438\u0441\u044f\u043c \u0438\u043b\u0438 \u0441\u043e\u0431\u044b\u0442\u0438\u044f\u043c \u0432 \u0440\u0430\u043c\u043a\u0430\u0445 \u0441\u0435\u0440\u0438\u0438 \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f.")
    resource_instances_ids: list[float] | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440\u044b \u044d\u043a\u0437\u0435\u043c\u043f\u043b\u044f\u0440\u043e\u0432 \u0440\u0435\u0441\u0443\u0440\u0441\u043e\u0432, \u043f\u0440\u0438\u0432\u044f\u0437\u0430\u043d\u043d\u044b\u0445 \u043a \u0437\u0430\u043f\u0438\u0441\u044f\u043c \u0438\u043b\u0438 \u0441\u043e\u0431\u044b\u0442\u0438\u044f\u043c \u0432 \u0440\u0430\u043c\u043a\u0430\u0445 \u0441\u0435\u0440\u0438\u0438 \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f.")


class PostCompanyIdWaitingListRequestClient(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float = Field(alias="id", description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043a\u043b\u0438\u0435\u043d\u0442\u0430")
    name: str = Field(description="\u0418\u043c\u044f \u043a\u043b\u0438\u0435\u043d\u0442\u0430. \u26a0\ufe0f\u041e\u0431\u043d\u043e\u0432\u043b\u044f\u0435\u0442 \u0438\u043c\u044f \u043a\u043b\u0438\u0435\u043d\u0442\u0430 \u0432 \u043a\u043b\u0438\u0435\u043d\u0442\u0441\u043a\u043e\u0439 \u0431\u0430\u0437\u0435, \u0435\u0441\u043b\u0438 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043e\u0442\u043b\u0438\u0447\u0430\u0435\u0442\u0441\u044f \u043e\u0442 \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u044e\u0449\u0435\u0433\u043e")
    surname: str = Field(description="\u0424\u0430\u043c\u0438\u043b\u0438\u044f \u043a\u043b\u0438\u0435\u043d\u0442\u0430")
    patronymic: str = Field(description="\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e \u043a\u043b\u0438\u0435\u043d\u0442\u0430")


class PostCompanyIdWaitingListRequestIntervalsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    date_from: str | None = Field(default=None, description="\u0414\u0430\u0442\u0430 \u043d\u0430\u0447\u0430\u043b\u0430")
    date_to: str | None = Field(default=None, description="\u0414\u0430\u0442\u0430 \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f")
    time_from: float | None = Field(default=None)
    time_to: float | None = Field(default=None)


class PostInviteSalonIdRequestInvitesItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    name: str | None = Field(default=None, description="\u0418\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f")
    search: str | None = Field(default=None, description="\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430 \u0438\u043b\u0438 email \u0430\u0434\u0440\u0435\u0441 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f")
    position: str | None = Field(default=None, description="\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c")
    user_role: Literal["worker", "administrator", "accountant", "manager", "owner"] | None = Field(default=None, description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0440\u043e\u043b\u0438")
    user_permissions: list[Any] | None = Field(default=None, description="\u0421\u043f\u0438\u0441\u043e\u043a \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0439 \u043f\u0440\u0430\u0432 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f")
    staff_id: float | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430 \u043f\u0440\u0438\u0432\u044f\u0437\u0430\u043d\u043d\u043e\u0433\u043e \u043a \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044e")


class PostLoyaltyAbonementTypesRequestAvailabilityItemIntervalsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    from_: int | None = Field(default=None, alias="from", description="\u041d\u0430\u0447\u0430\u043b\u043e \u0438\u043d\u0442\u0435\u0440\u0432\u0430\u043b\u0430 \u0432 \u0441\u0435\u043a\u0443\u043d\u0434\u0430\u0445.")
    to: int | None = Field(default=None, description="\u041a\u043e\u043d\u0435\u0446 \u0438\u043d\u0442\u0435\u0440\u0432\u0430\u043b\u0430 \u0432 \u0441\u0435\u043a\u0443\u043d\u0434\u0430\u0445.")


class PostMarketplaceWebhookRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    salon_id: float = Field(description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0444\u0438\u043b\u0438\u0430\u043b\u0430.")
    application_id: float = Field(description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f.")
    event: Literal["uninstall", "freeze"] = Field(description="Slug \u043f\u0440\u043e\u0438\u0437\u043e\u0448\u0435\u0434\u0448\u0435\u0433\u043e \u0441\u043e\u0431\u044b\u0442\u0438\u044f.")
    partner_token: str = Field(description="Bearer \u0442\u043e\u043a\u0435\u043d \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438 \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0447\u0438\u043a\u0430 (\u0434\u043b\u044f \u0443\u0434\u043e\u0441\u0442\u043e\u0432\u0435\u0440\u0435\u043d\u0438\u044f \u043f\u0440\u043e\u0438\u0441\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u044f \u0432\u0435\u0431\u0445\u0443\u043a\u0430).")


class PostPartnerCallbackRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    salon_id: float = Field(description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0444\u0438\u043b\u0438\u0430\u043b\u0430.")
    application_id: float = Field(description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f (\u0432\u044b\u0434\u0430\u0435\u0442\u0441\u044f \u043f\u043e\u0441\u043b\u0435 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f \u0432 \u0432\u0438\u0442\u0440\u0438\u043d\u0435 YCLIENTS).")
    api_key: float | None = Field(default=None, description="API-\u043a\u043b\u044e\u0447 \u0434\u043b\u044f \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0438 \u0443\u0432\u0435\u0434\u043e\u043c\u043b\u0435\u043d\u0438\u0439.")
    webhook_urls: list[str] | None = Field(default=None, description="\u041c\u0430\u0441\u0441\u0438\u0432 \u0430\u0434\u0440\u0435\u0441\u043e\u0432 \u0432\u0435\u0431\u0445\u0443\u043a\u043e\u0432.")
    channels: list[Literal["sms", "whatsapp"]] | None = Field(default=None, description="\u041a\u0430\u043d\u0430\u043b\u044b, \u043f\u043e \u043a\u043e\u0442\u043e\u0440\u044b\u043c \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u0430 \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0430 \u0443\u0432\u0435\u0434\u043e\u043c\u043b\u0435\u043d\u0438\u0439 (\u0442\u043e\u043b\u044c\u043a\u043e \u0434\u043b\u044f \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0439 \u0438\u0437 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0439 \u0427\u0430\u0442-\u0411\u043e\u0442\u044b \u0438 \u0421\u041c\u0421-\u0430\u0433\u0440\u0435\u0433\u0430\u0442\u043e\u0440\u044b).")


class PostPartnerPaymentRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    salon_id: float = Field(description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0444\u0438\u043b\u0438\u0430\u043b\u0430.")
    application_id: float = Field(description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f (\u0432\u044b\u0434\u0430\u0435\u0442\u0441\u044f \u043f\u043e\u0441\u043b\u0435 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f \u0432 \u0432\u0438\u0442\u0440\u0438\u043d\u0435 YCLIENTS).")
    payment_sum: float = Field(description="\u0421\u0443\u043c\u043c\u0430 \u043f\u043b\u0430\u0442\u0435\u0436\u0430.")
    currency_iso: str = Field(description="ISO \u0432\u0430\u043b\u044e\u0442\u044b \u043f\u043b\u0430\u0442\u0435\u0436\u0430 (\u043d\u0430\u043f\u0440\u0438\u043c\u0435\u0440: RUB, EUR, BYN)")
    payment_date: str = Field(description="\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u043f\u043b\u0430\u0442\u0435\u0436\u0430.")
    period_from: str = Field(description="\u0414\u0430\u0442\u0430, \u0441 \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u043d\u0430\u0447\u0438\u043d\u0430\u0435\u0442\u0441\u044f \u043e\u043f\u043b\u0430\u0447\u0435\u043d\u043d\u044b\u0439 \u043f\u0435\u0440\u0438\u043e\u0434 (\u0432\u043a\u043b\u044e\u0447\u0438\u0442\u0435\u043b\u044c\u043d\u043e).")
    period_to: str = Field(description="\u0414\u0430\u0442\u0430, \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u0437\u0430\u043a\u0430\u043d\u0447\u0438\u0432\u0430\u0435\u0442\u0441\u044f \u043e\u043f\u043b\u0430\u0447\u0435\u043d\u043d\u044b\u0439 \u043f\u0435\u0440\u0438\u043e\u0434 (\u0432\u043a\u043b\u044e\u0447\u0438\u0442\u0435\u043b\u044c\u043d\u043e).")


class PostPartnerPaymentResponse200Data(BaseModel):
    """Данные по запросу.
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="ID \u043f\u043b\u0430\u0442\u0435\u0436\u0430")


class PostPartnerShortNamesRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    salon_id: float = Field(description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0444\u0438\u043b\u0438\u0430\u043b\u0430.")
    application_id: float = Field(description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f (\u0432\u044b\u0434\u0430\u0435\u0442\u0441\u044f \u043f\u043e\u0441\u043b\u0435 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f \u0432 \u0432\u0438\u0442\u0440\u0438\u043d\u0435 YCLIENTS).")
    short_names: list[str] = Field(description="\u041c\u0430\u0441\u0441\u0438\u0432 \u043a\u043e\u0440\u043e\u0442\u043a\u0438\u0445 \u0438\u043c\u0435\u043d \u043e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u0435\u043b\u044f SMS-\u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0439")


class PostPositionsQuickRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    title: str = Field(description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0434\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u0438.")


class PostRecordsRecordIdRequestAttendanceGoodItemsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int = Field(alias="id", description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440.")
    good_id: int = Field(description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0442\u043e\u0432\u0430\u0440\u0430.")
    unit_id: int = Field(description="\u0415\u0434\u0438\u043d\u0438\u0446\u0430 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f \u043f\u0440\u043e\u0434\u0430\u0436\u0438.")
    storage_id: int = Field(description="\u0421\u043a\u043b\u0430\u0434 \u043f\u0440\u043e\u0434\u0430\u0436\u0438.")
    staff_id: int = Field(description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430.")
    operation_unit_type: Literal["sale", "consumable", "unknown"] = Field(description="\u0422\u0438\u043f \u0435\u0434\u0438\u043d\u0438\u0446\u044b \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438 \u043f\u0440\u043e\u0434\u0430\u0436\u0438.")
    number: int = Field(description="\u041d\u043e\u043c\u0435\u0440, \u0435\u0441\u043b\u0438 \u043f\u0440\u0438\u043c\u0435\u043d\u0438\u043c\u043e.")
    planned_activation_date: str = Field(description="\u0414\u0430\u0442\u0430 \u0430\u043a\u0442\u0438\u0432\u0430\u0446\u0438\u0438 \u0442\u043e\u0432\u0430\u0440\u0430, \u0435\u0441\u043b\u0438 \u043f\u0440\u0438\u043c\u0435\u043d\u0438\u043c\u043e.")
    marks: list[str] = Field(description="\u0421\u043f\u0438\u0441\u043e\u043a \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0439 \u043c\u0430\u0440\u043a\u0438\u0440\u043e\u0432\u043a\u0438.")
    quantity: int = Field(description="\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e.")
    cost_per_unit: float = Field(description="\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0437\u0430 \u0435\u0434\u0438\u043d\u0438\u0446\u0443 \u0442\u043e\u0432\u0430\u0440\u0430.")
    manual_cost: float = Field(description="\u0418\u0442\u043e\u0433\u043e\u0432\u0430\u044f \u043e\u0431\u0449\u0430\u044f \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c.")
    discount_percent: float = Field(description="\u0421\u043a\u0438\u0434\u043a\u0430 \u0432 \u043f\u0440\u043e\u0446\u0435\u043d\u0442\u0430\u0445.")


class PostRecordsRecordIdRequestAttendanceServiceItem(BaseModel):
    """Услуги.
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    cost_per_unit: float = Field(description="\u0418\u0441\u0445\u043e\u0434\u043d\u0430\u044f \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0437\u0430 \u0435\u0434\u0438\u043d\u0438\u0446\u0443.")
    discount_percent: float = Field(description="\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0441\u043a\u0438\u0434\u043a\u0438 \u0432 \u043f\u0440\u043e\u0446\u0435\u043d\u0442\u0430\u0445.")
    manual_cost: float = Field(description="\u041e\u0431\u0449\u0430\u044f \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0441 \u0443\u0447\u0435\u0442\u043e\u043c \u0441\u043a\u0438\u0434\u043a\u0438.")


class PostSalonIdActivitiesRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    staff_id: int = Field(description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043c\u0430\u0441\u0442\u0435\u0440\u0430.")
    service_id: int = Field(description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0443\u0441\u043b\u0443\u0433\u0438.")
    resource_instance_ids: list[int] | None = Field(default=None, description="\u0421\u043f\u0438\u0441\u043e\u043a \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440\u043e\u0432 \u0440\u0435\u0441\u0443\u0440\u0441\u0430.")
    label_ids: list[int] | None = Field(default=None, description="\u0421\u043f\u0438\u0441\u043e\u043a \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440\u043e\u0432 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0439.")
    date: str = Field(description="\u0414\u0430\u0442\u0430 \u0441\u043e\u0431\u044b\u0442\u0438\u044f.")
    length: int = Field(description="\u041f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0441\u043e\u0431\u044b\u0442\u0438\u044f \u0432 \u0441\u0435\u043a\u0443\u043d\u0434\u0430\u0445.")
    technical_break_duration: float | None = Field(default=None, description="\u0414\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0442\u0435\u0445\u043d\u0438\u0447\u0435\u0441\u043a\u043e\u0433\u043e \u043f\u0435\u0440\u0435\u0440\u044b\u0432\u0430 - \u0415\u0441\u043b\u0438 \u043d\u0435 \u043f\u0435\u0440\u0435\u0434\u0430\u043d. \u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e null - \u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 null, \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u0435\u0442 \u043e\u0431\u0449\u0435\u0439 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0435 \u0444\u0438\u043b\u0438\u0430\u043b\u0430, \u0438 \u0437\u0430\u0434\u0430\u0435\u0442\u0441\u044f \u0432 \u0440\u0430\u0437\u0434\u0435\u043b\u0435 *\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u2192 \u0416\u0443\u0440\u043d\u0430\u043b \u0437\u0430\u043f\u0438\u0441\u0438 \u2192 \u0422\u0435\u0445\u043d\u0438\u0447\u0435\u0441\u043a\u0438...")
    capacity: int = Field(description="\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043c\u0435\u0441\u0442 \u0432 \u0441\u043e\u0431\u044b\u0442\u0438\u0438.")
    comment: str | None = Field(default=None, description="\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439.")
    color: str | None = Field(default=None, description="\u0426\u0432\u0435\u0442 \u0441\u043e\u0431\u044b\u0442\u0438\u044f.")
    instructions: str | None = Field(default=None, description="\u0418\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u0438.")
    stream_link: str | None = Field(default=None, description="\u0421\u0441\u044b\u043b\u043a\u0430 \u0434\u043b\u044f \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f.")
    force: bool | None = Field(default=None, description="\u041f\u0440\u0438\u0437\u043d\u0430\u043a \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0438 \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u043e\u0441\u0442\u0438 \u0440\u0435\u0441\u0443\u0440\u0441\u043e\u0432 (true - \u043d\u0435 \u043f\u0440\u043e\u0432\u0435\u0440\u044f\u0435\u043c, false - \u043f\u0440\u043e\u0432\u0435\u0440\u044f\u0435\u043c).")


class PostScheduleIdClientSchedulesRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    client_id: float = Field(description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043a\u043b\u0438\u0435\u043d\u0442\u0430, \u0434\u043b\u044f \u043a\u043e\u0442\u043e\u0440\u043e\u0433\u043e \u0431\u0443\u0434\u0435\u0442 \u0441\u043e\u0437\u0434\u0430\u043d \u0433\u0440\u0430\u0444\u0438\u043a \u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u0439.")
    comer_id: float | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043f\u043e\u0441\u0435\u0442\u0438\u0442\u0435\u043b\u044f \u043a\u043b\u0438\u0435\u043d\u0442\u0430, \u0434\u043b\u044f \u043a\u043e\u0442\u043e\u0440\u043e\u0433\u043e \u0431\u0443\u0434\u0435\u0442 \u0441\u043e\u0437\u0434\u0430\u043d \u0433\u0440\u0430\u0444\u0438\u043a \u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u0439.")
    schedule_days_ids: list[float] = Field(description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440\u044b \u0441\u0435\u0440\u0438\u0439 \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f \u26a0\ufe0f**\u0427\u0438\u0441\u043b\u043e \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432 \u043c\u0430\u0441\u0441\u0438\u0432\u0430 \u0441\u0442\u0440\u043e\u0433\u043e \u043e\u0442 1 \u0434\u043e 7**")
    finish_date_type: Literal["end", "fixed", "abonement"] = Field(description="\u0422\u0438\u043f \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f")
    finish_date: str | None = Field(default=None, description="\u0414\u0430\u0442\u0430 \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f \u043a\u043b\u0438\u0435\u043d\u0442\u0441\u043a\u043e\u0433\u043e \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f **\u26a0\ufe0f \u041e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u043e**, \u0435\u0441\u043b\u0438 `finish_date_type=fixed`.")
    abonement_id: int | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430 **\u26a0\ufe0f\u041e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u0435\u043d, \u0435\u0441\u043b\u0438 finish_date_type=abonement**")


class PostScheduleIdDaysRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    day_of_week: Literal["mon", "tue", "wed", "thu", "fri", "sat", "sun"] = Field(description="\u0414\u0435\u043d\u044c \u043d\u0435\u0434\u0435\u043b\u0438 \u0441\u0435\u0440\u0438\u0438 \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f.")
    events_master_id: float = Field(description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430, \u043e\u043a\u0430\u0437\u044b\u0432\u0430\u044e\u0449\u0435\u0433\u043e \u0443\u0441\u043b\u0443\u0433\u0438 \u0432 \u0440\u0430\u043c\u043a\u0430\u0445 \u0441\u0435\u0440\u0438\u0438 \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f.")
    events_time: str = Field(description="\u0412\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u0437\u0430\u043f\u0438\u0441\u0435\u0439 \u0438\u043b\u0438 \u0441\u043e\u0431\u044b\u0442\u0438\u0439 \u0432 \u0440\u0430\u043c\u043a\u0430\u0445 \u0441\u0435\u0440\u0438\u0438 \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f (\u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435 HH:MM:SS).")
    events_duration: float = Field(description="\u0414\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u0435\u0439 \u0438\u043b\u0438 \u0441\u043e\u0431\u044b\u0442\u0438\u0439 \u0432 \u0440\u0430\u043c\u043a\u0430\u0445 \u0441\u0435\u0440\u0438\u0438 \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f (\u0432 \u0441\u0435\u043a\u0443\u043d\u0434\u0430\u0445).")
    events_capacity: float = Field(description="\u0412\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u044c \u0441\u043e\u0431\u044b\u0442\u0438\u0439 \u0432 \u0440\u0430\u043c\u043a\u0430\u0445 \u0441\u0435\u0440\u0438\u0438 \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f (\u0434\u043b\u044f \u0437\u0430\u043f\u0438\u0441\u0435\u0439 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0434\u043e\u043b\u0436\u043d\u043e \u0431\u044b\u0442\u044c \u0440\u0430\u0432\u043d\u043e 1).")
    labels_ids: list[float] | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440\u044b \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0439, \u043f\u0440\u0438\u0432\u044f\u0437\u0430\u043d\u043d\u044b\u0445 \u043a \u0437\u0430\u043f\u0438\u0441\u044f\u043c \u0438\u043b\u0438 \u0441\u043e\u0431\u044b\u0442\u0438\u044f\u043c \u0432 \u0440\u0430\u043c\u043a\u0430\u0445 \u0441\u0435\u0440\u0438\u0438 \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f.")
    resource_instances_ids: list[float] | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440\u044b \u044d\u043a\u0437\u0435\u043c\u043f\u043b\u044f\u0440\u043e\u0432 \u0440\u0435\u0441\u0443\u0440\u0441\u043e\u0432, \u043f\u0440\u0438\u0432\u044f\u0437\u0430\u043d\u043d\u044b\u0445 \u043a \u0437\u0430\u043f\u0438\u0441\u044f\u043c \u0438\u043b\u0438 \u0441\u043e\u0431\u044b\u0442\u0438\u044f\u043c \u0432 \u0440\u0430\u043c\u043a\u0430\u0445 \u0441\u0435\u0440\u0438\u0438 \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f.")


class PostServiceIdStaffRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    master_id: float = Field(description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430, \u043e\u043a\u0430\u0437\u044b\u0432\u0430\u044e\u0449\u0435\u0433\u043e \u0443\u0441\u043b\u0443\u0433\u0443.")
    seance_length: float = Field(description="\u0414\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u043e\u043a\u0430\u0437\u0430\u043d\u0438\u044f \u0443\u0441\u043b\u0443\u0433\u0438 \u0443\u043a\u0430\u0437\u0430\u043d\u043d\u044b\u043c \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u043e\u043c \u0432 \u0441\u0435\u043a\u0443\u043d\u0434\u0430\u0445, \u043c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u043e 300 \u0441\u0435\u043a\u0443\u043d\u0434 (5 \u043c\u0438\u043d\u0443\u0442), \u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e 86100 \u0441\u0435\u043a\u0443\u043d\u0434 (23 \u0447\u0430\u0441\u0430 55 \u043c\u0438\u043d\u0443\u0442).")
    technological_card_id: float = Field(description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0442\u0435\u0445\u043d\u043e\u043b\u043e\u0433\u0438\u0447\u0435\u0441\u043a\u043e\u0439 \u043a\u0430\u0440\u0442\u044b, \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u043c\u043e\u0439 \u043f\u0440\u0438 \u043e\u043a\u0430\u0437\u0430\u043d\u0438\u0438 \u0443\u0441\u043b\u0443\u0433\u0438 \u0443\u043a\u0430\u0437\u0430\u043d\u043d\u044b\u043c \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u043e\u043c.")


class PostStaffQuickRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    name: str = Field(description="\u0418\u043c\u044f \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430.")
    specialization: str = Field(description="\u0421\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430.")
    position_id: float = Field(description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0434\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u0438, \u043a \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u043f\u0440\u0438\u0432\u044f\u0437\u0430\u0442\u044c \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430.")
    phone_number: str = Field(description="\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f, \u043a \u043a\u043e\u0442\u043e\u0440\u043e\u043c\u0443 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u043f\u0440\u0438\u0432\u044f\u0437\u0430\u0442\u044c \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430 (\u0431\u0435\u0437 \"+\", \u043e\u0442 9 \u0434\u043e 15 \u0446\u0438\u0444\u0440).")


class PostUserIdCopyToCompaniesRequestUserCompanyLinksItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    company_id: float = Field(description="ID \u0444\u0438\u043b\u0438\u0430\u043b\u0430")
    user_permissions: list[Any] | None = Field(default=None, description="\u0421\u043f\u0438\u0441\u043e\u043a \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0439 \u043f\u0440\u0430\u0432 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f, \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u0438\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u0440\u0438 \u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0438")


class PostUserIdRemoveFromCompaniesRequestUserCompanyLinksItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    company_id: float = Field(description="ID \u0444\u0438\u043b\u0438\u0430\u043b\u0430")


class PostVisitsSearchRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    client_id: float = Field(description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043a\u043b\u0438\u0435\u043d\u0442\u0430.")
    client_phone: str = Field(description="\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430 \u043a\u043b\u0438\u0435\u043d\u0442\u0430.")
    from_: str = Field(alias="from", description="\u0414\u0430\u0442\u0430 \u043d\u0430\u0447\u0430\u043b\u0430 \u043f\u0435\u0440\u0438\u043e\u0434\u0430.")
    to: str = Field(description="\u0414\u0430\u0442\u0430 \u043a\u043e\u043d\u0446\u0430 \u043f\u0435\u0440\u0438\u043e\u0434\u0430.")
    payment_statuses: list[Literal["not_paid", "paid_not_full", "paid_full", "paid_over"]] = Field(description="\u0421\u0442\u0430\u0442\u0443\u0441 \u043e\u043f\u043b\u0430\u0442\u044b \u0432\u0438\u0437\u0438\u0442\u0430: `not_paid` - \u0432\u0438\u0437\u0438\u0442 \u043d\u0435\u043e\u043f\u043b\u0430\u0447\u0435\u043d, \u043d\u0438\u043a\u0430\u043a\u0438\u0445 \u043e\u043f\u043b\u0430\u0442 \u043f\u043e \u0432\u0438\u0437\u0438\u0442\u0443 \u043d\u0435 \u043f\u0440\u043e\u0445\u043e\u0434\u0438\u043b\u043e; `paid_not_full` - \u0432\u0438\u0437\u0438\u0442 \u043e\u043f\u043b\u0430\u0447\u0435\u043d \u0447\u0430\u0441\u0442\u0438\u0447\u043d\u043e; `paid_full` - \u0432\u0438\u0437\u0438\u0442 \u043e\u043f\u043b\u0430\u0447\u0435\u043d \u043f\u043e\u043b\u043d\u043e\u0441\u0442\u044c\u044e, \u043f\u0435\u0440\u0435\u043f\u043b\u0430\u0442\u044b \u043d\u0435\u0442; `paid_over`...")
    attendance: Literal[-1, 0, 1, 2] = Field(description="\u0421\u0442\u0430\u0442\u0443\u0441 \u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u044f: `-1`: - \u043a\u043b\u0438\u0435\u043d\u0442 \u043d\u0435 \u043f\u0440\u0438\u0448\u0451\u043b; `0`: - \u043e\u0436\u0438\u0434\u0430\u043d\u0438\u0435 \u043a\u043b\u0438\u0435\u043d\u0442\u0430; `1`: - \u043a\u043b\u0438\u0435\u043d\u0442 \u043f\u0440\u0438\u0448\u0451\u043b; `2`: - \u043a\u043b\u0438\u0435\u043d\u0442 \u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u043b \u0437\u0430\u043f\u0438\u0441\u044c.")


class PutAbonementTypesLoyaltyAbonementTypeIdRequestAvailabilityItemIntervalsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    from_: int | None = Field(default=None, alias="from", description="\u041d\u0430\u0447\u0430\u043b\u043e \u0438\u043d\u0442\u0435\u0440\u0432\u0430\u043b\u0430 \u0432 \u0441\u0435\u043a\u0443\u043d\u0434\u0430\u0445.")
    to: int | None = Field(default=None, description="\u041a\u043e\u043d\u0435\u0446 \u0438\u043d\u0442\u0435\u0440\u0432\u0430\u043b\u0430 \u0432 \u0441\u0435\u043a\u0443\u043d\u0434\u0430\u0445.")


class PutActivitiesActivityIdRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    staff_id: int = Field(description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043c\u0430\u0441\u0442\u0435\u0440\u0430.")
    service_id: int = Field(description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0443\u0441\u043b\u0443\u0433\u0438.")
    resource_instance_ids: list[int] | None = Field(default=None, description="\u0421\u043f\u0438\u0441\u043e\u043a \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440\u043e\u0432 \u0440\u0435\u0441\u0443\u0440\u0441\u0430.")
    label_ids: list[int] | None = Field(default=None, description="\u0421\u043f\u0438\u0441\u043e\u043a \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440\u043e\u0432 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0439.")
    date: str = Field(description="\u0414\u0430\u0442\u0430 \u0441\u043e\u0431\u044b\u0442\u0438\u044f.")
    length: int = Field(description="\u041f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0441\u043e\u0431\u044b\u0442\u0438\u044f \u0432 \u0441\u0435\u043a\u0443\u043d\u0434\u0430\u0445.")
    technical_break_duration: float | None = Field(default=None, description="\u0414\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0442\u0435\u0445\u043d\u0438\u0447\u0435\u0441\u043a\u043e\u0433\u043e \u043f\u0435\u0440\u0435\u0440\u044b\u0432\u0430 - \u0415\u0441\u043b\u0438 \u043d\u0435 \u043f\u0435\u0440\u0435\u0434\u0430\u043d. \u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e null - \u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 null, \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u0435\u0442 \u043e\u0431\u0449\u0435\u0439 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0435 \u0444\u0438\u043b\u0438\u0430\u043b\u0430, \u0438 \u0437\u0430\u0434\u0430\u0435\u0442\u0441\u044f \u0432 \u0440\u0430\u0437\u0434\u0435\u043b\u0435 *\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u2192 \u0416\u0443\u0440\u043d\u0430\u043b \u0437\u0430\u043f\u0438\u0441\u0438 \u2192 \u0422\u0435\u0445\u043d\u0438\u0447\u0435\u0441\u043a\u0438...")
    capacity: int = Field(description="\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043c\u0435\u0441\u0442 \u0432 \u0441\u043e\u0431\u044b\u0442\u0438\u0438.")
    comment: str | None = Field(default=None, description="\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439.")
    color: str | None = Field(default=None, description="\u0426\u0432\u0435\u0442 \u0441\u043e\u0431\u044b\u0442\u0438\u044f.")
    instructions: str | None = Field(default=None, description="\u0418\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u0438.")
    stream_link: str | None = Field(default=None, description="\u0421\u0441\u044b\u043b\u043a\u0430 \u0434\u043b\u044f \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f.")
    force: bool | None = Field(default=None, description="\u041f\u0440\u0438\u0437\u043d\u0430\u043a \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0438 \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u043e\u0441\u0442\u0438 \u0440\u0435\u0441\u0443\u0440\u0441\u043e\u0432 (true - \u043d\u0435 \u043f\u0440\u043e\u0432\u0435\u0440\u044f\u0435\u043c, false - \u043f\u0440\u043e\u0432\u0435\u0440\u044f\u0435\u043c).")


class PutStaffMasterIdRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    seance_length: float = Field(description="\u0414\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u043e\u043a\u0430\u0437\u0430\u043d\u0438\u044f \u0443\u0441\u043b\u0443\u0433\u0438 \u0443\u043a\u0430\u0437\u0430\u043d\u043d\u044b\u043c \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u043e\u043c \u0432 \u0441\u0435\u043a\u0443\u043d\u0434\u0430\u0445, \u043c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u043e 300 \u0441\u0435\u043a\u0443\u043d\u0434 (5 \u043c\u0438\u043d\u0443\u0442), \u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e 86100 \u0441\u0435\u043a\u0443\u043d\u0434 (23 \u0447\u0430\u0441\u0430 55 \u043c\u0438\u043d\u0443\u0442).")
    technological_card_id: float = Field(description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0442\u0435\u0445\u043d\u043e\u043b\u043e\u0433\u0438\u0447\u0435\u0441\u043a\u043e\u0439 \u043a\u0430\u0440\u0442\u044b, \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u043c\u043e\u0439 \u043f\u0440\u0438 \u043e\u043a\u0430\u0437\u0430\u043d\u0438\u0438 \u0443\u0441\u043b\u0443\u0433\u0438 \u0443\u043a\u0430\u0437\u0430\u043d\u043d\u044b\u043c \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u043e\u043c.")


class PutStaffScheduleRequestSchedulesToDeleteItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    staff_id: float | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430.")
    dates: list[str] | None = Field(default=None, description="\u0414\u0430\u0442\u0430 \u0434\u043b\u044f \u0443\u0434\u0430\u043b\u0435\u043d\u0438\u044f \u0433\u0440\u0430\u0444\u0438\u043a\u0430 \u0440\u0430\u0431\u043e\u0442\u044b \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430 \u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435 Y-m-d.")


class PutStaffScheduleRequestSchedulesToSetItemSlotsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    from_: str | None = Field(default=None, alias="from", description="\u041d\u0430\u0447\u0430\u043b\u043e \u0438\u043d\u0442\u0435\u0440\u0432\u0430\u043b\u0430 \u0433\u0440\u0430\u0444\u0438\u043a\u0430 \u0440\u0430\u0431\u043e\u0442\u044b \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430 \u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435 H:i.")
    to: str | None = Field(default=None, description="\u041a\u043e\u043d\u0435\u0446 \u0438\u043d\u0442\u0435\u0440\u0432\u0430\u043b\u0430 \u0433\u0440\u0430\u0444\u0438\u043a\u0430 \u0440\u0430\u0431\u043e\u0442\u044b \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430 \u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435 H:i.")


class PutUserIdPermissionsRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    user_role: Literal["worker", "administrator", "accountant", "manager", "owner"] | None = Field(default=None, description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0440\u043e\u043b\u0438")
    user_permissions: list[Any] | None = Field(default=None, description="\u0421\u043f\u0438\u0441\u043e\u043a \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0439 \u043f\u0440\u0430\u0432 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f")
    staff_id: float | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430 \u043f\u0440\u0438\u0432\u044f\u0437\u0430\u043d\u043d\u043e\u0433\u043e \u043a \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044e")


class PutWaitingListWaitingListEntryIdRequestClient(BaseModel):
    """Объект клиента
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float = Field(alias="id", description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043a\u043b\u0438\u0435\u043d\u0442\u0430")
    name: str = Field(description="\u0418\u043c\u044f \u043a\u043b\u0438\u0435\u043d\u0442\u0430. \u26a0\ufe0f\u041e\u0431\u043d\u043e\u0432\u043b\u044f\u0435\u0442 \u0438\u043c\u044f \u043a\u043b\u0438\u0435\u043d\u0442\u0430 \u0432 \u043a\u043b\u0438\u0435\u043d\u0442\u0441\u043a\u043e\u0439 \u0431\u0430\u0437\u0435, \u0435\u0441\u043b\u0438 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043e\u0442\u043b\u0438\u0447\u0430\u0435\u0442\u0441\u044f \u043e\u0442 \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u044e\u0449\u0435\u0433\u043e")
    surname: str = Field(description="\u0424\u0430\u043c\u0438\u043b\u0438\u044f \u043a\u043b\u0438\u0435\u043d\u0442\u0430")
    patronymic: str = Field(description="\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e \u043a\u043b\u0438\u0435\u043d\u0442\u0430")


class PutWaitingListWaitingListEntryIdRequestIntervalsItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    date_from: str | None = Field(default=None, description="\u0414\u0430\u0442\u0430 \u043d\u0430\u0447\u0430\u043b\u0430")
    date_to: str | None = Field(default=None, description="\u0414\u0430\u0442\u0430 \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f")
    time_from: float | None = Field(default=None)
    time_to: float | None = Field(default=None)


class AbonementTypeAvailability(BaseModel):
    """Схема спеки: Объект модели "Период доступности абонемента".
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    week_days: list[float] | None = Field(default=None, description="\u0414\u043d\u0438 \u043d\u0435\u0434\u0435\u043b\u0438, \u0432 \u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u0434\u0435\u0439\u0441\u0442\u0432\u0443\u0435\u0442 \u0443\u0441\u043b\u043e\u0432\u0438\u0435.")
    intervals: list[dict[str, Any]] | None = Field(default=None, description="\u0418\u043d\u0442\u0435\u0440\u0432\u0430\u043b\u044b \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u043e\u0441\u0442\u0438.")


class AccountsResponseDataTypes(BaseModel):
    """Получить кассы компании
    Схема спеки: Root Type for accounts_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: list[dict[str, Any]] | None = Field(default=None, alias="data", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class ActivityCompanyidActivityidBookResponseDataTypes(BaseModel):
    """Создать запись в групповом событии
    Схема спеки: Root Type for activity_company_id__activity_book_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: dict[str, Any] | None = Field(default=None, alias="data", description="\u041e\u0431\u044a\u0435\u043a\u0442 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class ActivityCompanyidRequestDataTypes(BaseModel):
    """Создание группового события
    Схема спеки: Root Type for activity_companyid_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    date: str = Field(description="\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f")
    service_id: float = Field(description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0443\u0441\u043b\u0443\u0433\u0438")
    staff_id: float = Field(description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430")
    capacity: float = Field(description="\u0412\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u044c")
    resource_instance_ids: list[float] | None = Field(default=None, description="\u041c\u0430\u0441\u0441\u0438\u0432 \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440\u043e\u0432 \u044d\u043a\u0437\u0435\u043c\u043f\u043b\u044f\u0440\u043e\u0432 \u0440\u0435\u0441\u0443\u0440\u0441\u043e\u0432")
    force: bool = Field(description="\u0418\u0433\u043d\u043e\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043e\u0448\u0438\u0431\u043a\u0438 (\u0437\u0430\u043d\u044f\u0442\u043e\u0441\u0442\u044c \u043c\u0430\u0441\u0442\u0435\u0440\u0430/\u0440\u0435\u0441\u0443\u0440\u0441\u043e\u0432 \u0438 \u0442.\u043f.)")
    length: float | None = Field(default=None, description="\u0414\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0441\u043e\u0431\u044b\u0442\u0438\u044f \u0432 \u0441\u0435\u043a\u0443\u043d\u0434\u0430\u0445")
    color: str | None = Field(default=None, description="\u0426\u0432\u0435\u0442 \u0441\u043e\u0431\u044b\u0442\u0438\u044f")
    label_ids: list[Any] | None = Field(default=None, description="\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0441\u043e\u0431\u044b\u0442\u0438\u0439")
    comment: str | None = Field(default=None, description="\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 \u0441\u043e\u0431\u044b\u0442\u0438\u044f")
    stream_link: str | None = Field(default=None, description="\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u043e\u043d\u043b\u0430\u0439\u043d-\u0441\u043e\u0431\u044b\u0442\u0438\u0435")
    technical_break_duration: float | None = Field(default=None, description="\u0414\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0442\u0435\u0445\u043d\u0438\u0447\u0435\u0441\u043a\u043e\u0433\u043e \u043f\u0435\u0440\u0435\u0440\u044b\u0432\u0430 - \u0415\u0441\u043b\u0438 \u043d\u0435 \u043f\u0435\u0440\u0435\u0434\u0430\u043d. \u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e null - \u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 null, \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u0435\u0442 \u043e\u0431\u0449\u0435\u0439 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0435 \u0444\u0438\u043b\u0438\u0430\u043b\u0430, \u0438 \u0437\u0430\u0434\u0430\u0435\u0442\u0441\u044f \u0432 \u0440\u0430\u0437\u0434\u0435\u043b\u0435 *\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u2192 \u0416\u0443\u0440\u043d\u0430\u043b \u0437\u0430\u043f\u0438\u0441\u0438 \u2192 \u0422\u0435\u0445\u043d\u0438\u0447\u0435\u0441\u043a\u0438...")
    instructions: str | None = Field(default=None, description="\u0418\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u0438")


class ActivityCompanyidResponseDataTypes(BaseModel):
    """Создание группового события
    Схема спеки: Root Type for activity_companyid_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: dict[str, Any] | None = Field(default=None, alias="data", description="\u041e\u0431\u044a\u0435\u043a\u0442 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class ActivityCompanyidSearchResponseDataTypes(BaseModel):
    """Поиск групповых событий
    Схема спеки: Root Type for activity_companyid_search_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: list[dict[str, Any]] | None = Field(default=None, alias="data", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: dict[str, Any] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u0441\u043e\u0434\u0435\u0440\u0436\u0438\u0442 \u0432 \u0441\u0435\u0431\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043d\u0430\u0439\u0434\u0435\u043d\u043d\u044b\u0445 \u0441\u043e\u0431\u044b\u0442\u0438\u0439)")


class ActivityCompanyidServicesRequestDataTypes(BaseModel):
    """Поиск групповых услуг
    Схема спеки: Root Type for activity_companyid_services_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    staff_id: float | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430 \u0434\u043b\u044f \u0444\u0438\u043b\u044c\u0442\u0440\u0430\u0446\u0438\u0438")
    term: str | None = Field(default=None, description="\u041f\u043e\u0438\u0441\u043a \u043f\u043e \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u044e \u0438\u043b\u0438 \u0447\u0430\u0441\u0442\u0438 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u044f \u0443\u0441\u043b\u0443\u0433\u0438")


class ActivityCompanyidServicesResponseDataTypes(BaseModel):
    """Поиск групповых услуг
    Схема спеки: Root Type for activity_companyid_services_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: list[dict[str, Any]] | None = Field(default=None, alias="data", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: dict[str, Any] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u0441\u043e\u0434\u0435\u0440\u0436\u0438\u0442 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043d\u0430\u0439\u0434\u0435\u043d\u043d\u044b\u0445 \u0443\u0441\u043b\u0443\u0433)")


class ActivityDatesRange(BaseModel):
    """Диапазон данных для поиска событий.
    Схема спеки: Объект "Диапазон данных для поиска событий"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    min_date: str | None = Field(default=None, description="\u0414\u0430\u0442\u0430 \u043d\u0430\u0447\u0430\u043b\u0430 \u0434\u0438\u0430\u043f\u0430\u0437\u043e\u043d\u0430 (\u0413\u0413\u0413\u0413-\u041c\u041c-\u0414\u0414).")
    max_date: str | None = Field(default=None, description="\u0414\u0430\u0442\u0430 \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f \u0434\u0438\u0430\u043f\u0430\u0437\u043e\u043d\u0430 (\u0413\u0413\u0413\u0413-\u041c\u041c-\u0414\u0414).")


class ActivityFilter(BaseModel):
    """Фильтр для поиска событий.
    Схема спеки: Объект "Фильтр для поиска событий"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    code: Literal["staff", "resource", "service", "service_category"] | None = Field(default=None, description="\u0422\u0438\u043f \u0444\u0438\u043b\u044c\u0442\u0440\u0430.")
    title: str | None = Field(default=None, description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0444\u0438\u043b\u044c\u0442\u0440\u0430.")
    data_: list[dict[str, Any]] | None = Field(default=None, alias="data", description="\u042d\u043b\u0435\u043c\u0435\u043d\u0442\u044b \u0444\u0438\u043b\u044c\u0442\u0440\u0430.")


class AnalyticsReportOverallChartScalarItem2(BaseModel):
    """Данные для построения агрегирующей диаграммы в отчете Основные показатели
    Схема спеки: Root Type for AnalyticsReportOverallChartRow
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    label: str | None = Field(default=None, description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u043e\u043a\u0430\u0437\u0430\u0442\u0435\u043b\u044f")
    data_: int | None = Field(default=None, alias="data", description="\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043f\u043e\u043a\u0430\u0437\u0430\u0442\u0435\u043b\u044f")


class AnalyticsReportOverallClientStats2(BaseModel):
    """Сводные показатели по количеству клиентов
    Схема спеки: Root Type for AnalyticsReportOverallClientStats
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    total_count: int | None = Field(default=None, description="\u041e\u0431\u0449\u0435\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043a\u043b\u0438\u0435\u043d\u0442\u043e\u0432")
    new_count: int | None = Field(default=None, description="\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043d\u043e\u0432\u044b\u0445 \u043a\u043b\u0438\u0435\u043d\u0442\u043e\u0432 \u0432 \u0430\u043d\u0430\u043b\u0438\u0437\u0438\u0440\u0443\u0435\u043c\u043e\u043c \u043f\u0435\u0440\u0438\u043e\u0434\u0435")
    new_percent: int | None = Field(default=None, description="\u041f\u0440\u043e\u0446\u0435\u043d\u0442 \u043d\u043e\u0432\u044b\u0445 \u043a\u043b\u0438\u0435\u043d\u0442\u043e\u0432 \u043e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u043e \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u0430 \u0430\u043a\u0442\u0438\u0432\u043d\u044b\u0445 \u043a\u043b\u0438\u0435\u043d\u0442\u043e\u0432")
    return_count: int | None = Field(default=None, description="\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043a\u043b\u0438\u0435\u043d\u0442\u043e\u0432, \u0432\u0435\u0440\u043d\u0443\u0432\u0448\u0438\u0445\u0441\u044f \u0432 \u0430\u043d\u0430\u043b\u0438\u0437\u0438\u0440\u0443\u0435\u043c\u043e\u043c \u043f\u0435\u0440\u0438\u043e\u0434\u0435")
    return_percent: int | None = Field(default=None, description="\u041f\u0440\u043e\u0446\u0435\u043d\u0442 \u0432\u0435\u0440\u043d\u0443\u0432\u0448\u0438\u0445\u0441\u044f \u043a\u043b\u0438\u0435\u043d\u0442\u043e\u0432 \u043e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u043e \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u0430 \u0430\u043a\u0442\u0438\u0432\u043d\u044b\u0445 \u043a\u043b\u0438\u0435\u043d\u0442\u043e\u0432")
    active_count: int | None = Field(default=None, description="\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0430\u043a\u0442\u0438\u0432\u043d\u044b\u0445 \u043a\u043b\u0438\u0435\u043d\u0442\u043e\u0432 \u0432 \u0430\u043d\u0430\u043b\u0438\u0437\u0438\u0440\u0443\u0435\u043c\u043e\u043c \u043f\u0435\u0440\u0438\u043e\u0434\u0435")
    lost_count: int | None = Field(default=None, description="\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u043e\u0442\u0435\u0440\u044f\u043d\u043d\u044b\u0445 \u043a\u043b\u0438\u0435\u043d\u0442\u043e\u0432 \u0432 \u0430\u043d\u0430\u043b\u0438\u0437\u0438\u0440\u0443\u0435\u043c\u043e\u043c \u043f\u0435\u0440\u0438\u043e\u0434\u0435")
    lost_percent: int | None = Field(default=None, description="\u041f\u0440\u043e\u0446\u0435\u043d\u0442 \u043f\u043e\u0442\u0435\u0440\u044f\u043d\u043d\u044b\u0445 \u043a\u043b\u0438\u0435\u043d\u0442\u043e\u0432 \u043e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u043e \u043e\u0431\u0449\u0435\u0433\u043e \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u0430 \u043a\u043b\u0438\u0435\u043d\u0442\u043e\u0432")


class AnalyticsReportOverallFullnessStats2(BaseModel):
    """Сводные показатели заполненности рабочего времени сотрудников компании
    Схема спеки: Root Type for AnalyticsReportOverallFullnessStats
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    current_percent: float | None = Field(default=None, description="\u041f\u0440\u043e\u0446\u0435\u043d\u0442 \u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u043e\u0441\u0442\u0438 \u0432 \u0442\u0435\u043a\u0443\u0449\u0435\u043c \u043f\u0435\u0440\u0438\u043e\u0434\u0435")
    previous_percent: float | None = Field(default=None, description="\u041f\u0440\u043e\u0446\u0435\u043d\u0442 \u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u043e\u0441\u0442\u0438 \u0432 \u043f\u0440\u0435\u0434\u044b\u0434\u0443\u0449\u0435\u043c \u043f\u0435\u0440\u0438\u043e\u0434\u0435")
    change_percent: int | None = Field(default=None, description="\u041f\u0440\u043e\u0446\u0435\u043d\u0442 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u0442\u0435\u043a\u0443\u0449\u0435\u0433\u043e \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u043f\u043e\u043a\u0430\u0437\u0430\u0442\u0435\u043b\u044f \u043e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u043e \u043f\u0440\u043e\u0448\u043b\u043e\u0433\u043e. Null, \u0435\u0441\u043b\u0438 \u043f\u0440\u043e\u0448\u043b\u044b\u0439 \u043f\u043e\u043a\u0430\u0437\u0430\u0442\u0435\u043b\u044c \u0440\u0430\u0432\u0435\u043d 0, \u0430 \u0442\u0435\u043a\u0443\u0449\u0438\u0439 \u043e\u0442\u043b\u0438\u0447\u0435\u043d \u043e\u0442 0.")


class AnalyticsReportOverallRecordStats2(BaseModel):
    """Сводные показатели по количеству записей
    Схема спеки: Root Type for AnalyticsReportOverallRecordStats
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    current_completed_count: int | None = Field(default=None, description="\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u043d\u044b\u0445 \u0437\u0430\u043f\u0438\u0441\u0435\u0439")
    current_completed_percent: int | None = Field(default=None, description="\u041f\u0440\u043e\u0446\u0435\u043d\u0442 \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u043d\u044b\u0445 \u0437\u0430\u043f\u0438\u0441\u0435\u0439 \u043e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u043e \u043e\u0431\u0449\u0435\u0433\u043e \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u0430. Null, \u0435\u0441\u043b\u0438 \u043e\u0431\u0449\u0435\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0440\u0430\u0432\u043d\u043e 0.")
    current_pending_count: int | None = Field(default=None, description="\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043d\u0435\u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u043d\u044b\u0445 \u0437\u0430\u043f\u0438\u0441\u0435\u0439")
    current_pending_percent: int | None = Field(default=None, description="\u041f\u0440\u043e\u0446\u0435\u043d\u0442 \u043d\u0435\u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u043d\u044b\u0445 \u0437\u0430\u043f\u0438\u0441\u0435\u0439 \u043e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u043e \u043e\u0431\u0449\u0435\u0433\u043e \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u0430. Null, \u0435\u0441\u043b\u0438 \u043e\u0431\u0449\u0435\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0440\u0430\u0432\u043d\u043e 0.")
    current_canceled_count: int | None = Field(default=None, description="\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043e\u0442\u043c\u0435\u043d\u0435\u043d\u043d\u044b\u0445 \u0437\u0430\u043f\u0438\u0441\u0435\u0439")
    current_canceled_percent: int | None = Field(default=None, description="\u041f\u0440\u043e\u0446\u0435\u043d\u0442 \u043e\u0442\u043c\u0435\u043d\u0435\u043d\u043d\u044b\u0445 \u0437\u0430\u043f\u0438\u0441\u0435\u0439 \u043e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u043e \u043e\u0431\u0449\u0435\u0433\u043e \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u0430. Null, \u0435\u0441\u043b\u0438 \u043e\u0431\u0449\u0435\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0440\u0430\u0432\u043d\u043e 0.")
    current_total_count: int | None = Field(default=None, description="\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0432\u0441\u0435\u0445 \u0437\u0430\u043f\u0438\u0441\u0435\u0439 \u0432 \u0442\u0435\u043a\u0443\u0449\u0435\u043c \u043f\u0435\u0440\u0438\u043e\u0434\u0435")
    previous_total_count: int | None = Field(default=None, description="\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0432\u0441\u0435\u0445 \u0437\u0430\u043f\u0438\u0441\u0435\u0439 \u0432 \u043f\u0440\u0435\u0434\u044b\u0434\u0443\u0449\u0435\u043c \u043f\u0435\u0440\u0438\u043e\u0434\u0435")
    change_percent: int | None = Field(default=None, description="\u041f\u0440\u043e\u0446\u0435\u043d\u0442 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u0442\u0435\u043a\u0443\u0449\u0435\u0433\u043e \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u043f\u043e\u043b\u043d\u043e\u0433\u043e \u0447\u0438\u0441\u043b\u0430 \u0437\u0430\u043f\u0438\u0441\u0435\u0439 \u043e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u043e \u043f\u0440\u043e\u0448\u043b\u043e\u0433\u043e. Null, \u0435\u0441\u043b\u0438 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0437\u0430\u043f\u0438\u0441\u0435\u0439 \u0432 \u043f\u0440\u0435\u0434\u044b\u0434\u0443\u0449\u0435\u043c \u043f\u0435\u0440\u0438\u043e\u0434\u0435 \u0440\u0430\u0432\u043d\u043e 0, \u0430 \u0442\u0435\u043a\u0443\u0449\u0435\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043e\u0442\u043b\u0438\u0447\u043d\u043e \u043e\u0442 0.")


class ApiV2CompanyWaitingListCreateResponse(BaseModel):
    """Схема спеки: Создание заявки в листе ожидания
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data_: dict[str, Any] | None = Field(default=None, alias="data", description="\u041e\u0431\u044a\u0435\u043a\u0442 \u043e\u043f\u0438\u0441\u044b\u0432\u0430\u044e\u0449\u0438\u0439 \u0441\u043e\u0437\u0434\u0430\u043d\u043d\u0443\u044e \u0437\u0430\u044f\u0432\u043a\u0443 \u0432 \u043b\u0438\u0441\u0442\u0435 \u043e\u0436\u0438\u0434\u0430\u043d\u0438\u044f")


class ApiV2CompanyWaitingListGetResponse(BaseModel):
    """Схема спеки: Получение заявок в листе ожидания
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data_: dict[str, Any] | None = Field(default=None, alias="data", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u0437\u0430\u044f\u0432\u043e\u043a \u0432 \u043b\u0438\u0441\u0442\u0435 \u043e\u0436\u0438\u0434\u0430\u043d\u0438\u044f")
    meta: dict[str, Any] | None = Field(default=None)


class AuthRequest2(BaseModel):
    """Авторизация пользователя
    Схема спеки: Базовая авторизация
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    login: str = Field(description="\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430 \u0438\u043b\u0438 Email")
    password: str = Field(description="\u041f\u0430\u0440\u043e\u043b\u044c")


class AuthRequest2fa(BaseModel):
    """Авторизация пользователя
    Схема спеки: Передать код подтверждения 2FA
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    login: str = Field(description="\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430 \u0438\u043b\u0438 Email")
    password: str = Field(description="\u041f\u0430\u0440\u043e\u043b\u044c")
    param_2fa: dict[str, Any] | None = Field(default=None, alias="2fa", description="\u041e\u0431\u044a\u0435\u043a\u0442 \u0434\u0432\u0443\u0445\u0444\u0430\u043a\u0442\u043e\u0440\u043d\u043e\u0439 \u0430\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u0438. \u26a0\ufe0f\u0415\u0441\u043b\u0438 \u0443 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f \u0432\u043a\u043b\u044e\u0447\u0435\u043d\u0430 2fa \u0441\u043d\u0430\u0447\u0430\u043b\u0430 \u043e\u0442\u043f\u0440\u0430\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u0437\u0430\u043f\u0440\u043e\u0441 \u0442\u043e\u043b\u044c\u043a\u043e \u0441 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430\u043c\u0438 login \u0438 password \u0432\u0442\u043e\u0440\u044b\u043c \u0437\u0430\u043f\u0440\u043e\u0441\u043e\u043c login, password \u0438 \u043e\u0431\u044a\u0435\u043a\u0442 2fa.")


class AuthResponse2(BaseModel):
    """Авторизация пользователя
    Схема спеки: Пользователь авторизован
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f")
    user_token: str | None = Field(default=None, description="User_token \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f")
    name: str | None = Field(default=None, description="\u0418\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f")
    phone: str | None = Field(default=None, description="\u0422\u0435\u043b\u0435\u0444\u043e\u043d \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f")
    login: str | None = Field(default=None, description="\u041b\u043e\u0433\u0438\u043d \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f")
    email: str | None = Field(default=None, description="\u041f\u043e\u0447\u0442\u043e\u0432\u044b\u0439 \u0430\u0434\u0440\u0435\u0441 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f")
    avatar: str | None = Field(default=None, description="\u041f\u0443\u0442\u044c \u043a \u0444\u0430\u0439\u043b\u0443 \u0430\u0432\u0430\u0442\u0430\u0440\u043a\u0438 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f")
    is_approved: bool | None = Field(default=None, description="\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d \u043b\u0438 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c \u0432 \u0441\u0438\u0441\u0442\u0435\u043c\u0435")
    is_email_confirmed: bool | None = Field(default=None, description="\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d \u043b\u0438 email \u0443 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f")


class AuthResponse2faNeed(BaseModel):
    """Авторизация пользователя с включенной двухфакторной авторизацией
    Схема спеки: Нужна авторизация 2fa
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0423\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u044c \u0437\u0430\u043f\u0440\u043e\u0441\u0430")
    data_: dict[str, Any] | None = Field(default=None, alias="data")
    meta: list[Any] | None = Field(default=None)


class BookCheckCompanyidRequestDataTypes(BaseModel):
    """Проверить параметры записи
    Схема спеки: Root Type for book_check_companyid_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    appointments: list[dict[str, Any]] = Field(description="\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0437\u0430\u043f\u0438\u0441\u0438 (\u0443\u0441\u043b\u0443\u0433\u0438, \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0441\u0442\u044b...)")


class BookCheckCompanyidResponse201DataTypes(BaseModel):
    """Проверить параметры записи
    Схема спеки: Root Type for book_check_companyid_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    meta: dict[str, Any] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435")


class BookCodeCompanyidDataTypeResponse(BaseModel):
    """Схема спеки: Root Type for book_code_companyid_resp
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    meta: dict[str, Any] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435")


class BookCodeCompanyidDataTypesRequest(BaseModel):
    """Отправить СМС код подтверждения номера телефона
    Схема спеки: Root Type for book_code_companyid_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    phone: str = Field(description="\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430 \u043a\u043b\u0438\u0435\u043d\u0442\u0430")
    fulname: str | None = Field(default=None, description="\u0418\u043c\u044f \u043a\u043b\u0438\u0435\u043d\u0442\u0430")


class BookDatesCompanyidDataTypes(BaseModel):
    """Получить список дат доступных для бронирования
    Схема спеки: Root Type for book_dates_company_id_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: dict[str, Any] | None = Field(default=None, alias="data", description="\u0414\u0430\u043d\u043d\u044b\u0435 (\u043e\u0431\u044a\u0435\u043a\u0442)")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class BookRecordCompanyidRecordRequestDataTypes(BaseModel):
    """Перенести запись на сеанс
    Схема спеки: Root Type for book_record_companyid_record_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    datetime: str | None = Field(default=None, description="\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u043d\u0430 \u043a\u043e\u0442\u043e\u0440\u043e\u0435 \u043c\u044b \u0445\u043e\u0442\u0438\u043c \u043f\u0435\u0440\u0435\u043d\u0435\u0441\u0442\u0438 \u0437\u0430\u043f\u0438\u0441\u044c")
    comment: str | None = Field(default=None, description="\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 \u043a \u0437\u0430\u043f\u0438\u0441\u0438")


class BookRecordCompanyidRecordResponseDataTypes(BaseModel):
    """Перенести запись на сеанс
    Схема спеки: Root Type for book_record_companyid_record_respnse_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: dict[str, Any] | None = Field(default=None, alias="data", description="\u0414\u0430\u043d\u043d\u044b\u0435 (\u043e\u0431\u044a\u0435\u043a\u0442)")


class BookRecordCompanyidRecordidRecordhashResponseDataTypes(BaseModel):
    """Получить запись
    Схема спеки: Root Type for book_record_companyid_recordid_recordhash_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="ID \u0437\u0430\u043f\u0438\u0441\u0438")
    services: list[dict[str, Any]] | None = Field(default=None, description="\u0421\u043f\u0438\u0441\u043e\u043a ID \u0443\u0441\u043b\u0443\u0433")
    company: dict[str, Any] | None = Field(default=None, description="\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438")
    staff: dict[str, Any] | None = Field(default=None, description="\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430")
    clients_count: int | None = Field(default=None)
    date: str | None = Field(default=None, description="\"2025-01-01 12:00:00\" (required, string) - \u0414\u0430\u0442\u0430 \u0441\u0435\u0430\u043d\u0441\u0430")
    datetime: str | None = Field(default=None, description="\u0414\u0430\u0442\u0430 \u0441\u0435\u0430\u043d\u0441\u0430 \u0432 ISO")
    create_date: str | None = Field(default=None, description="\"2025-01-01 12:00:00\" (required, string) - \u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f \u0437\u0430\u043f\u0438\u0441\u0438")
    comment: str | None = Field(default=None, description="\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 \u043a \u0437\u0430\u043f\u0438\u0441\u0438")
    deleted: bool | None = Field(default=None, description="\u0423\u0434\u0430\u043b\u0435\u043d\u0430 \u043b\u0438 \u0437\u0430\u043f\u0438\u0441\u044c (true \u0435\u0441\u043b\u0438 \u0443\u0434\u0430\u043b\u0435\u043d\u0430)")
    attendance: float | None = Field(default=None, description="2 - \u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c \u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u043b \u0437\u0430\u043f\u0438\u0441\u044c, 1 - \u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c \u043f\u0440\u0438\u0448\u0435\u043b, \u0443\u0441\u043b\u0443\u0433\u0438 \u043e\u043a\u0430\u0437\u0430\u043d\u044b, 0 - \u043e\u0436\u0438\u0434\u0430\u043d\u0438\u0435 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f, -1 - \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c \u043d\u0435 \u043f\u0440\u0438\u0448\u0435\u043b \u043d\u0430 \u0432\u0438\u0437\u0438\u0442")
    length: float | None = Field(default=None, description="\u0414\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0441\u0435\u0430\u043d\u0441\u0430")
    notify_by_sms: float | None = Field(default=None, description="\u0417\u0430 \u043a\u0430\u043a\u043e\u0435 \u043a\u043e\u043b-\u0432\u043e \u0447\u0430\u0441\u043e\u0432 \u043e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u0441\u043c\u0441 \u043d\u0430\u043f\u043e\u043c\u0438\u043d\u0430\u043d\u0438\u0435 \u043e \u0437\u0430\u043f\u0438\u0441\u0438 (0 \u0435\u0441\u043b\u0438 \u043d\u0435 \u043d\u0443\u0436\u043d\u043e \u043d\u0430\u043f\u043e\u043c\u0438\u043d\u0430\u0442\u044c)")
    notify_by_email: float | None = Field(default=None, description="\u0417\u0430 \u043a\u0430\u043a\u043e\u0435 \u043a\u043e\u043b-\u0432\u043e \u0447\u0430\u0441\u043e\u0432 \u043e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c email \u043d\u0430\u043f\u043e\u043c\u0438\u043d\u0430\u043d\u0438\u0435 \u043e \u0437\u0430\u043f\u0438\u0441\u0438 (0 \u0435\u0441\u043b\u0438 \u043d\u0435 \u043d\u0443\u0436\u043d\u043e \u043d\u0430\u043f\u043e\u043c\u0438\u043d\u0430\u0442\u044c)")
    master_requested: bool | None = Field(default=None, description="\u0411\u044b\u043b \u043b\u0438 \u0443\u043a\u0430\u0437\u0430\u043d \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u043d\u044b\u0439 \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0441\u0442 \u043f\u0440\u0438 \u0437\u0430\u043f\u0438\u0441\u0438 (false \u0435\u0441\u043b\u0438 \u0431\u044b\u043b \u0443\u043a\u0430\u0437\u0430\u043d \"\u043d\u0435 \u0438\u043c\u0435\u0435\u0442 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f\")")
    online: bool | None = Field(default=None, description="\u0417\u0430\u043f\u0438\u0441\u044c \u043e\u043d\u043b\u0430\u0439\u043d\u043e\u0432\u0430\u044f \u0438\u043b\u0438 \u043d\u0435\u0442 (false \u0435\u0441\u043b\u0438 \u0437\u0430\u043f\u0438\u0441\u044c \u0432\u043d\u0435\u0441 \u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440)")
    api_id: str | None = Field(default=None, description="\u0412\u043d\u0435\u0448\u043d\u0438\u0439 \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0437\u0430\u043f\u0438\u0441\u0438")
    last_change_date: str | None = Field(default=None, description="\u0414\u0430\u0442\u0430 \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0433\u043e \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f \u0437\u0430\u043f\u0438\u0441\u0438")
    prepaid: bool | None = Field(default=None, description="\u0414\u043e\u0441\u0442\u0443\u043f\u043d\u0430 \u043b\u0438 \u043e\u043d\u043b\u0430\u0439\u043d-\u043e\u043f\u043b\u0430\u0442\u0430 \u0434\u043b\u044f \u0437\u0430\u043f\u0438\u0441\u0438")
    prepaid_confirmed: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 online-\u043e\u043f\u043b\u0430\u0442\u044b")
    activity_id: float | None = Field(default=None, description="ID \u0433\u0440\u0443\u043f\u043f\u043e\u0432\u043e\u0439 \u0437\u0430\u043f\u0438\u0441\u0438")


class BookRecordCompanyidRequestDataTypes(BaseModel):
    """Создать запись на сеанс
    Схема спеки: Root Type for book_record_companyid_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    phone: str = Field(description="\u0422\u0435\u043b\u0435\u0444\u043e\u043d \u043a\u043b\u0438\u0435\u043d\u0442\u0430")
    fullname: str = Field(description="\u0418\u043c\u044f \u043a\u043b\u0438\u0435\u043d\u0442\u0430")
    surname: str | None = Field(default=None, description="\u0424\u0430\u043c\u0438\u043b\u0438\u044f \u043a\u043b\u0438\u0435\u043d\u0442\u0430")
    patronymic: str | None = Field(default=None, description="\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e \u043a\u043b\u0438\u0435\u043d\u0442\u0430")
    email: str = Field(description="\u041f\u043e\u0447\u0442\u043e\u0432\u044b\u0439 \u0430\u0434\u0440\u0435\u0441 \u043a\u043b\u0438\u0435\u043d\u0442\u0430")
    code: float | None = Field(default=None, description="\u041a\u043e\u0434 \u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u0438\u044f \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430, \u0432\u044b\u0441\u043b\u0430\u043d\u043d\u044b\u0439 \u043f\u043e \u0441\u043c\u0441 (\u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u0435\u043d \u0435\u0441\u043b\u0438 \u0443 \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438 \u0432\u044b\u0441\u0442\u0430\u0432\u043b\u0435\u043d phone_conformation = true)")
    comment: str | None = Field(default=None, description="\u041a\u043e\u043c\u043c\u0430\u0435\u043d\u0442\u0430\u0440\u0438\u0439 \u043a \u0437\u0430\u043f\u0438\u0441\u0438")
    notify_by_sms: float | None = Field(default=None, description="\u0417\u0430 \u0441\u043a\u043e\u043b\u044c\u043a\u043e \u0447\u0430\u0441\u043e\u0432 \u0434\u043e \u0432\u0438\u0437\u0438\u0442\u0430 \u0441\u043b\u0435\u0434\u0443\u0435\u0442 \u0432\u044b\u0441\u043b\u0430\u0442\u044c \u0441\u043c\u0441 \u043d\u0430\u043f\u043e\u043c\u0438\u043d\u0430\u043d\u0438\u0435 \u043a\u043b\u0438\u0435\u043d\u0442\u0443 (0 - \u0435\u0441\u043b\u0438 \u043d\u0435 \u043d\u0443\u0436\u043d\u043e)")
    notify_by_email: float | None = Field(default=None, description="\u0417\u0430 \u0441\u043a\u043e\u043b\u044c\u043a\u043e \u0447\u0430\u0441\u043e\u0432 \u0434\u043e \u0432\u0438\u0437\u0438\u0442\u0430 \u0441\u043b\u0435\u0434\u0443\u0435\u0442 \u0432\u044b\u0441\u043b\u0430\u0442\u044c email \u043d\u0430\u043f\u043e\u043c\u0438\u043d\u0430\u043d\u0438\u0435 \u043a\u043b\u0438\u0435\u043d\u0442\u0443 (0 - \u0435\u0441\u043b\u0438 \u043d\u0435 \u043d\u0443\u0436\u043d\u043e)")
    api_id: float | None = Field(default=None, description="ID \u0437\u0430\u043f\u0438\u0441\u0438 \u0438\u0437 \u0432\u043d\u0435\u0448\u043d\u0435\u0439 \u0441\u0438\u0441\u0442\u0435\u043c\u044b")
    is_newsletter_allowed: bool | None = Field(default=None, description="\u041e\u0442\u043f\u0440\u0430\u0432\u043a\u0430 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u043e\u043d\u043d\u043e-\u0440\u0435\u043a\u043b\u0430\u043c\u043d\u043e\u0439 \u0440\u0430\u0441\u0441\u044b\u043b\u043a\u0438")
    is_personal_data_processing_allowed: bool | None = Field(default=None, description="\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430 \u043f\u0435\u0440\u0441\u043e\u043d\u0430\u043b\u044c\u043d\u044b\u0445 \u0434\u0430\u043d\u043d\u044b\u0445")
    appointments: list[dict[str, Any]] | None = Field(default=None, description="\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0437\u0430\u043f\u0438\u0441\u0435\u0439 (\u0441\u0435\u0430\u043d\u0441, \u0443\u0441\u043b\u0443\u0433\u0438, \u043c\u0430\u0441\u0442\u0435\u0440)")


class BookRecordCompanyidResponseDataTypes(BaseModel):
    """Перенести запись на сеанс
    Схема спеки: Root Type for book_record_companyid_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: list[dict[str, Any]] | None = Field(default=None, alias="data", description="\u0414\u0430\u043d\u043d\u044b\u0435 (\u043c\u0430\u0441\u0441\u0438\u0432 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432)")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class BookServicesCompanyidDataTypes(BaseModel):
    """Получить списокуслуг доступных для бронирования
    Схема спеки: Root Type for get_book_services_type
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: dict[str, Any] | None = Field(default=None, alias="data", description="\u041e\u0431\u044a\u0435\u043a\u0442 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class BookStaffCompanyidDataTypes(BaseModel):
    """Получить список сотрудников доступных для бронирования
    Схема спеки: Root Type for book_staff_company_id_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: list[dict[str, Any]] | None = Field(default=None, alias="data", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class BookStaffSeancesCompanyidStaffidDataTypes(BaseModel):
    """Получить список ближайших доступных сеансов
    Схема спеки: Root Type for book_staff_seances_companyid_staffid
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: dict[str, Any] | None = Field(default=None, alias="data", description="\u041e\u0431\u044a\u0435\u043a\u0442 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class BookTimesCompanyidDataTypes(BaseModel):
    """Получить список сеансов доступных для бронирования
    Схема спеки: Root Type for book_times_company_id_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: list[dict[str, Any]] | None = Field(default=None, alias="data", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class BookformCreateRequest2(BaseModel):
    """Запрос для создания букформы
    Схема спеки: Root Type BookformCreateRequest
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    title: str = Field(description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0431\u0443\u043a\u0444\u043e\u0440\u043c\u044b")
    description: str | None = Field(default=None, description="\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0431\u0443\u043a\u0444\u043e\u0440\u043c\u044b")
    is_default: bool | None = Field(default=None, description="\u0424\u043b\u0430\u0433 \u0434\u0435\u0444\u043e\u043b\u0442\u043d\u043e\u0439 \u0431\u0443\u043a\u0444\u043e\u0440\u043c\u044b")
    without_menu: bool | None = Field(default=None, description="\u0424\u043b\u0430\u0433 \u043f\u043e\u0448\u0430\u0433\u043e\u0432\u043e\u0433\u043e \u0440\u0435\u0436\u0438\u043c\u0430")
    service_step_default: float | None = Field(default=None, description="ID \u0443\u0441\u043b\u0443\u0433\u0438")
    service_step_hide: bool | None = Field(default=None, description="\u0424\u043b\u0430\u0433 \u0441\u043a\u0440\u044b\u0442\u0438\u044f \u0443\u0441\u043b\u0443\u0433\u0438")
    master_step_default: float | None = Field(default=None, description="ID \u043c\u0430\u0441\u0442\u0435\u0440\u0430")
    master_step_hide: bool | None = Field(default=None, description="\u0424\u043b\u0430\u0433 \u0441\u043a\u0440\u044b\u0442\u0438\u044f \u043c\u0430\u0441\u0442\u0435\u0440\u0430")
    service_step_num: float | None = Field(default=None, description="\u041f\u043e\u0440\u044f\u0434\u043a\u043e\u0432\u044b\u0439 \u043d\u043e\u043c\u0435\u0440 \u0448\u0430\u0433\u0430 \u0443\u0441\u043b\u0443\u0433\u0438")
    master_step_num: float | None = Field(default=None, description="\u041f\u043e\u0440\u044f\u0434\u043a\u043e\u0432\u044b\u0439 \u043d\u043e\u043c\u0435\u0440 \u0448\u0430\u0433\u0430 \u043c\u0430\u0441\u0442\u0435\u0440\u0430")
    datetime_step_num: float | None = Field(default=None, description="\u041f\u043e\u0440\u044f\u0434\u043a\u043e\u0432\u044b\u0439 \u043d\u043e\u043c\u0435\u0440 \u0448\u0430\u0433\u0430 \u0434\u0430\u0442\u044b \u0438 \u0432\u0440\u0435\u043c\u0435\u043d\u0438")
    show_button: bool | None = Field(default=None, description="\u0424\u043b\u0430\u0433 \u0432\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f \u0432\u0438\u0434\u0438\u043c\u043e\u0441\u0442\u0438 \u043a\u043d\u043e\u043f\u043a\u0438")
    button_position: Literal["bottom right", "bottom left", "top right", "top left "] | None = Field(default=None, description="\u0420\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u043a\u043d\u043e\u043f\u043a\u0438 \u043d\u0430 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435")
    form_position: Literal["right", "left"] | None = Field(default=None, description="\u0420\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u043f\u0430\u043d\u0435\u043b\u0438 \u043d\u0430 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435")
    button_color: str | None = Field(default=None, description="\u0426\u0432\u0435\u0442 \u043a\u043d\u043e\u043f\u043a\u0438")
    button_animation: bool | None = Field(default=None, description="\u0424\u043b\u0430\u0433 \u0432\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f \u0430\u043d\u0438\u043c\u0430\u0446\u0438\u0438 \u043a\u043d\u043e\u043f\u043a\u0438")


class BookformIdInfoDataTypes(BaseModel):
    """Настройки формы бронирования записи
    Схема спеки: Root Type for bookform_info_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: dict[str, Any] | None = Field(default=None, alias="data", description="\u041e\u0431\u044a\u0435\u043a\u0442 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class BookformSettingsResponse2(BaseModel):
    """Настройки букформы
    Схема спеки: Root Type BookformSettingsResponse
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float = Field(alias="id", description="ID \u0431\u0443\u043a\u0444\u043e\u0440\u043c\u044b")
    title: str = Field(description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0431\u0443\u043a\u0444\u043e\u0440\u043c\u044b")
    description: str = Field(description="\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0431\u0443\u043a\u0444\u043e\u0440\u043c\u044b")
    is_default: bool = Field(description="\u0424\u043b\u0430\u0433 \u0434\u0435\u0444\u043e\u043b\u0442\u043d\u043e\u0439 \u0431\u0443\u043a\u0444\u043e\u0440\u043c\u044b")
    without_menu: bool = Field(description="\u0424\u043b\u0430\u0433 \u043f\u043e\u0448\u0430\u0433\u043e\u0432\u043e\u0433\u043e \u0440\u0435\u0436\u0438\u043c\u0430")
    service_step_default: float = Field(description="ID \u0443\u0441\u043b\u0443\u0433\u0438")
    service_step_hide: bool = Field(description="\u0424\u043b\u0430\u0433 \u0441\u043a\u0440\u044b\u0442\u0438\u044f \u0443\u0441\u043b\u0443\u0433\u0438")
    master_step_default: float = Field(description="ID \u043c\u0430\u0441\u0442\u0435\u0440\u0430")
    master_step_hide: bool = Field(description="\u0424\u043b\u0430\u0433 \u0441\u043a\u0440\u044b\u0442\u0438\u044f \u043c\u0430\u0441\u0442\u0435\u0440\u0430")
    service_step_num: float = Field(description="\u041f\u043e\u0440\u044f\u0434\u043a\u043e\u0432\u044b\u0439 \u043d\u043e\u043c\u0435\u0440 \u0443\u0441\u043b\u0443\u0433\u0438")
    master_step_num: float = Field(description="\u041f\u043e\u0440\u044f\u0434\u043a\u043e\u0432\u044b\u0439 \u043d\u043e\u043c\u0435\u0440 \u043c\u0430\u0441\u0442\u0435\u0440\u0430")
    datetime_step_num: float = Field(description="\u041f\u043e\u0440\u044f\u0434\u043a\u043e\u0432\u044b\u0439 \u043d\u043e\u043c\u0435\u0440 \u0434\u0430\u0442\u044b \u0438 \u0432\u0440\u0435\u043c\u0435\u043d\u0438")
    show_button: bool = Field(description="\u0428\u0430\u0433 \u0432\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f \u0432\u0438\u0434\u0438\u043c\u043e\u0441\u0442\u0438 \u043a\u043d\u043e\u043f\u043a\u0438")
    button_position: str = Field(description="\u0420\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u043a\u043d\u043e\u043f\u043a\u0438 \u043d\u0430 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435")
    form_position: str = Field(description="\u0420\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u043f\u0430\u043d\u0435\u043b\u0438 \u043d\u0430 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435")
    button_color: str = Field(description="\u0426\u0432\u0435\u0442 \u043a\u043d\u043e\u043f\u043a\u0438")
    button_animation: bool = Field(description="\u0424\u043b\u0430\u0433 \u0432\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f \u0430\u043d\u0438\u043c\u0430\u0446\u0438\u0438 \u043a\u043d\u043e\u043f\u043a\u0438")
    html_code: str = Field(description="\u041a\u043e\u0434 \u0434\u043b\u044f \u0432\u0441\u0442\u0430\u0432\u043a\u0438 \u043a\u043d\u043e\u043f\u043a\u0438 \u043d\u0430 \u0441\u0430\u0439\u0442")
    ab_test_enabled: bool = Field(description="\u0424\u043b\u0430\u0433 \u0432\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f \u0430\u0431-\u0442\u0435\u0441\u0442\u0430 \u0431\u0443\u043a\u0444\u043e\u0440\u043c\u044b")


class BookformUpdateRequest2(BaseModel):
    """Запрос для изменения букформы
    Схема спеки: Root Type for BookformUpdateRequest
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    title: str = Field(description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0431\u0443\u043a\u0444\u043e\u0440\u043c\u044b")
    description: str = Field(description="\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0431\u0443\u043a\u0444\u043e\u0440\u043c\u044b")
    is_default: bool = Field(description="\u0424\u043b\u0430\u0433 \u0434\u0435\u0444\u043e\u043b\u0442\u043d\u043e\u0439 \u0431\u0443\u043a\u0444\u043e\u0440\u043c\u044b")
    without_menu: bool = Field(description="\u0424\u043b\u0430\u0433 \u043f\u043e\u0448\u0430\u0433\u043e\u0432\u043e\u0433\u043e \u0440\u0435\u0436\u0438\u043c\u0430")
    service_step_default: float = Field(description="ID \u0443\u0441\u043b\u0443\u0433\u0438")
    service_step_hide: bool = Field(description="\u0424\u043b\u0430\u0433 \u0441\u043a\u0440\u044b\u0442\u0438\u044f \u0443\u0441\u043b\u0443\u0433\u0438")
    master_step_default: float = Field(description="ID \u043c\u0430\u0441\u0442\u0435\u0440\u0430")
    master_step_hide: bool = Field(description="\u0424\u043b\u0430\u0433 \u0441\u043a\u0440\u044b\u0442\u0438\u044f \u043c\u0430\u0441\u0442\u0435\u0440\u0430")
    service_step_num: float = Field(description="\u041f\u043e\u0440\u044f\u0434\u043a\u043e\u0432\u044b\u0439 \u043d\u043e\u043c\u0435\u0440 \u0448\u0430\u0433\u0430 \u0443\u0441\u043b\u0443\u0433\u0438")
    master_step_num: float = Field(description="\u041f\u043e\u0440\u044f\u0434\u043a\u043e\u0432\u044b\u0439 \u043d\u043e\u043c\u0435\u0440 \u0448\u0430\u0433\u0430 \u043c\u0430\u0441\u0442\u0435\u0440\u0430")
    datetime_step_num: float = Field(description="\u041f\u043e\u0440\u044f\u0434\u043a\u043e\u0432\u044b\u0439 \u043d\u043e\u043c\u0435\u0440 \u0448\u0430\u0433\u0430 \u0434\u0430\u0442\u044b \u0438 \u0432\u0440\u0435\u043c\u0435\u043d\u0438")
    show_button: bool = Field(description="\u0428\u0430\u0433 \u0432\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f \u0432\u0438\u0434\u0438\u043c\u043e\u0441\u0442\u0438 \u043a\u043d\u043e\u043f\u043a\u0438")
    button_position: Literal["bottom right", "bottom left", "top right", "top left"] = Field(description="\u0420\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u043a\u043d\u043e\u043f\u043a\u0438 \u043d\u0430 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435")
    form_position: Literal["right", "left"] = Field(description="\u0420\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u043f\u0430\u043d\u0435\u043b\u0438 \u043d\u0430 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435")
    button_color: str = Field(description="\u0426\u0432\u0435\u0442 \u043a\u043d\u043e\u043f\u043a\u0438")
    button_animation: bool = Field(description="\u0424\u043b\u0430\u0433 \u0432\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f \u0430\u043d\u0438\u043c\u0430\u0446\u0438\u0438 \u043a\u043d\u043e\u043f\u043a\u0438")


class BookingAuthResponse(BaseModel):
    """Авторизация пользователя
    Схема спеки: Root Type for auth_response
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f")
    user_token: str | None = Field(default=None, description="User_token \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f")
    name: str | None = Field(default=None, description="\u0418\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f")
    phone: str | None = Field(default=None, description="\u0422\u0435\u043b\u0435\u0444\u043e\u043d \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f")
    login: str | None = Field(default=None, description="\u041b\u043e\u0433\u0438\u043d \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f")
    email: str | None = Field(default=None, description="\u041f\u043e\u0447\u0442\u043e\u0432\u044b\u0439 \u0430\u0434\u0440\u0435\u0441 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f")
    avatar: str | None = Field(default=None, description="\u041f\u0443\u0442\u044c \u043a \u0444\u0430\u0439\u043b\u0443 \u0430\u0432\u0430\u0442\u0430\u0440\u043a\u0438 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f")


class BookingAuthResponse2(BaseModel):
    """Авторизация пользователя
    Схема спеки: Root Type for auth_response
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f")
    user_token: str | None = Field(default=None, description="User_token \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f")
    name: str | None = Field(default=None, description="\u0418\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f")
    phone: str | None = Field(default=None, description="\u0422\u0435\u043b\u0435\u0444\u043e\u043d \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f")
    login: str | None = Field(default=None, description="\u041b\u043e\u0433\u0438\u043d \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f")
    email: str | None = Field(default=None, description="\u041f\u043e\u0447\u0442\u043e\u0432\u044b\u0439 \u0430\u0434\u0440\u0435\u0441 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f")
    avatar: str | None = Field(default=None, description="\u041f\u0443\u0442\u044c \u043a \u0444\u0430\u0439\u043b\u0443 \u0430\u0432\u0430\u0442\u0430\u0440\u043a\u0438 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f")


class BookingAuthWithCode(BaseModel):
    """Авторизация пользователя
    Схема спеки: Авторизация по коду подтверждения
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    phone: str = Field(description="\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430")
    code: str = Field(description="\u041a\u043e\u0434 \u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u0438\u044f")


class BookingUserGetDataResponseDataTypes(BaseModel):
    """Получение данных пользователя онлайн-записи
    Схема спеки: Root Type for booking_user_get_data_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    param_0: str | None = Field(default=None, alias="0", description="\u0422\u043e\u043a\u0435\u043d \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f")
    id_: int | None = Field(default=None, alias="id", description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f")
    user_token: str | None = Field(default=None, description="\u0422\u043e\u043a\u0435\u043d \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f")
    name: str | None = Field(default=None, description="\u0418\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f")
    phone: str | None = Field(default=None, description="\u0422\u0435\u043b\u0435\u0444\u043e\u043d \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f")
    login: str | None = Field(default=None, description="\u041b\u043e\u0433\u0438\u043d \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f")
    email: str | None = Field(default=None, description="\u041f\u043e\u0447\u0442\u0430 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f")
    avatar: str | None = Field(default=None, description="\u0410\u0432\u0430\u0442\u0430\u0440 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f")


class BookingUserUpdateInfoRequestDataTypes(BaseModel):
    """Обновление данных пользователя онлайн-записи
    Схема спеки: Root Type for booking_user_update_info_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    name: str | None = Field(default=None, description="\u0418\u043c\u044f")
    email: str | None = Field(default=None, description="\u041f\u043e\u0447\u0442\u0430")
    phone: str | None = Field(default=None, description="\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430")
    confirmation_code: str | None = Field(default=None, description="\u041a\u043e\u0434 \u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u0438\u044f \u0438\u0437 \u0441\u043c\u0441 (\u043f\u0440\u0438 \u0441\u043c\u0435\u043d\u0435 \u043d\u043e\u043c\u0435\u0440\u0430 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430)")


class BookingUserUpdatePasswordRequestDataTypes(BaseModel):
    """Обновление пароля пользователя онлайн-записи
    Схема спеки: Root Type for booking_user_update_password_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    old_password: str | None = Field(default=None, description="\u0422\u0435\u043a\u0443\u0449\u0438\u0439 \u043f\u0430\u0440\u043e\u043b\u044c")
    new_password: str | None = Field(default=None, description="\u041d\u043e\u0432\u044b\u0439 \u043f\u0430\u0440\u043e\u043b\u044c")


class BookingUserUpdatePasswordResponseDataTypes(BaseModel):
    """Обновление пароля пользователя онлайн-записи
    Схема спеки: Root Type for booking_user_update_password_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: dict[str, Any] | None = Field(default=None, alias="data", description="\u041e\u0431\u044a\u0435\u043a\u0442 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class CheckForActivity(BaseModel):
    """Описание количества доступных записей и дату последней возможной записи по абонементу
    Схема спеки: Проверка абонемента на количество доступных записей и последнюю дату записи
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: str | None = Field(default=None, alias="id", description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430")
    type_: str | None = Field(default=None, alias="type", description="\u0422\u0438\u043f \u043e\u0431\u044a\u0435\u043a\u0442\u0430.")
    attributes: dict[str, Any] | None = Field(default=None, description="\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043e\u0431\u044c\u0435\u043a\u0442\u0430 \u0443\u043a\u0430\u0437\u044b\u0432\u0430\u044e\u0449\u0438\u0435 \u0434\u0430\u0442\u0443 \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0439 \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0439 \u0437\u0430\u043f\u0438\u0441\u0438 \u0438 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0437\u0430\u043f\u0438\u0441\u0435\u0439 \u0432 \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0438 \u0441\u043e\u0431\u044b\u0442\u0438\u044f")


class CitiesResponseDataTypes(BaseModel):
    """Получить список городов
    Схема спеки: Root Type for cities_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: list[dict[str, Any]] | None = Field(default=None, alias="data", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class ClientCommentFileDto(BaseModel):
    """Данные существующего файла в карточке клиента.
    Схема спеки: Объект модели "Файл в карточке клиента"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    link: str | None = Field(default=None, description="\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0441\u043a\u0430\u0447\u0438\u0432\u0430\u043d\u0438\u0435 \u0444\u0430\u0439\u043b\u0430 \u0432 \u043a\u0430\u0440\u0442\u043e\u0447\u043a\u0435 \u043a\u043b\u0438\u0435\u043d\u0442\u0430.")
    filename: str | None = Field(default=None, description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0444\u0430\u0439\u043b\u0430 \u0432 \u043a\u0430\u0440\u0442\u043e\u0447\u043a\u0435 \u043a\u043b\u0438\u0435\u043d\u0442\u0430.")


class ClientVisitsHistoryGoodsTransactionGood(BaseModel):
    """Данные о проданном товаре.
    Схема спеки: Объект модели "Проданный товар в истории посещений клиента"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0442\u043e\u0432\u0430\u0440\u0430.")
    title: str | None = Field(default=None, description="\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u0430.")
    amount: float | None = Field(default=None, description="\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u0440\u043e\u0434\u0430\u043d\u043d\u043e\u0433\u043e \u0442\u043e\u0432\u0430\u0440\u0430.")
    unit: str | None = Field(default=None, description="\u0415\u0434\u0438\u043d\u0438\u0446\u0430 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f \u043f\u0440\u043e\u0434\u0430\u043d\u043d\u043e\u0433\u043e \u0442\u043e\u0432\u0430\u0440\u0430.")
    cost_per_unit: float | None = Field(default=None, description="\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0435\u0434\u0438\u043d\u0438\u0446\u044b \u0442\u043e\u0432\u0430\u0440\u0430 \u0431\u0435\u0437 \u0441\u043a\u0438\u0434\u043a\u0438.")
    first_cost: float | None = Field(default=None, description="\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0432\u0441\u0435\u0433\u043e \u0442\u043e\u0432\u0430\u0440\u0430 \u0431\u0435\u0437 \u0441\u043a\u0438\u0434\u043a\u0438.")
    discount_percent: float | None = Field(default=None, description="\u041f\u0440\u043e\u0446\u0435\u043d\u0442 \u0441\u043a\u0438\u0434\u043a\u0438.")
    cost_to_pay: float | None = Field(default=None, description="\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0442\u043e\u0432\u0430\u0440\u0430 \u0441 \u0443\u0447\u0435\u0442\u043e\u043c \u0441\u043a\u0438\u0434\u043a\u0438.")
    paid_sum: float | None = Field(default=None, description="\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0442\u043e\u0432\u0430\u0440\u0430 \u0441 \u0443\u0447\u0435\u0442\u043e\u043c \u0441\u043a\u0438\u0434\u043a\u0438.")
    payment_status: Literal["not_paid", "paid_not_full", "paid_full", "paid_over"] | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u043e\u043f\u043b\u0430\u0442\u044b \u0432\u0438\u0437\u0438\u0442\u0430: `not_paid` - \u0432\u0438\u0437\u0438\u0442 \u043d\u0435\u043e\u043f\u043b\u0430\u0447\u0435\u043d, \u043d\u0438\u043a\u0430\u043a\u0438\u0445 \u043e\u043f\u043b\u0430\u0442 \u043f\u043e \u0432\u0438\u0437\u0438\u0442\u0443 \u043d\u0435 \u043f\u0440\u043e\u0445\u043e\u0434\u0438\u043b\u043e; `paid_not_full` - \u0432\u0438\u0437\u0438\u0442 \u043e\u043f\u043b\u0430\u0447\u0435\u043d \u0447\u0430\u0441\u0442\u0438\u0447\u043d\u043e; `paid_full` - \u0432\u0438\u0437\u0438\u0442 \u043e\u043f\u043b\u0430\u0447\u0435\u043d \u043f\u043e\u043b\u043d\u043e\u0441\u0442\u044c\u044e, \u043f\u0435\u0440\u0435\u043f\u043b\u0430\u0442\u044b \u043d\u0435\u0442; `paid_over`...")


class ClientVisitsHistoryRecordServiceConsumable(BaseModel):
    """Данные по расходнику.
    Схема спеки: Объект модели "Расходник в услуге"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    title: str | None = Field(default=None, description="\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0440\u0430\u0441\u0445\u043e\u0434\u043d\u0438\u043a\u0430.")
    amount: float | None = Field(default=None, description="\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0442\u043e\u0432\u0430\u0440\u0430 \u0432 \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0439 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u043c \u0435\u0434\u0438\u043d\u0438\u0446\u0435 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f.")
    cost_per_unit: float | None = Field(default=None, description="\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0437\u0430 \u0435\u0434\u0438\u043d\u0438\u0446\u0443 \u0442\u043e\u0432\u0430\u0440\u0430.")
    unit: str | None = Field(default=None, description="\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0435\u0434\u0438\u043d\u0438\u0446\u044b \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f \u0442\u043e\u0432\u0430\u0440\u0430.")


class ClientsCompanyidResponseDeprecatedDataTypes(BaseModel):
    """Устаревшее. Получить список клиентов
    Схема спеки: Root Type for clients_companyid_response_deprecated_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: list[dict[str, Any]] | None = Field(default=None, alias="data", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: dict[str, Any] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u0441\u043e\u0434\u0435\u0440\u0436\u0438\u0442 \u043d\u043e\u043c\u0435\u0440 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b \u0438 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043a\u043b\u0438\u0435\u043d\u0442\u043e\u0432 \u043d\u0430 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435)")


class ClientsFilesClientidReaponseDataTypes(BaseModel):
    """Пример запроса на получение списка файлов клиента
    Схема спеки: Root Type for clients_files_clientid_reaponse_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: list[dict[str, Any]] | None = Field(default=None, alias="data", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: dict[str, Any] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u0441\u043e\u0434\u0435\u0440\u0436\u0438\u0442 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0444\u0430\u0439\u043b\u043e\u0432)")


class Comer(BaseModel):
    """Схема спеки: Объект модели "Посетитель"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043f\u043e\u0441\u0435\u0442\u0438\u0442\u0435\u043b\u044f.")
    title: str | None = Field(default=None, description="\u0418\u043c\u044f \u043f\u043e\u0441\u0435\u0442\u0438\u0442\u0435\u043b\u044f.")
    slug: Literal["person", "pet", "vehicle"] | None = Field(default=None, description="\u0422\u0438\u043f \u043f\u043e\u0441\u0435\u0442\u0438\u0442\u0435\u043b\u044f: `person` - \u0447\u0435\u043b\u043e\u0432\u0435\u043a; `pet` - \u043f\u0438\u0442\u043e\u043c\u0435\u0446; `vehicle` - \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u043d\u043e\u0435 \u0441\u0440\u0435\u0434\u0441\u0442\u0432\u043e.")


class CommentsCompanyidRequestDataTypes(BaseModel):
    """Оставить комментарии
    Схема спеки: Root Type for comments_companyid_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    mark: float = Field(description="\u041e\u0446\u0435\u043d\u043a\u0430 \u043e\u0442 1 \u0434\u043e 5")
    text: str = Field(description="\u0422\u0435\u043a\u0441\u0442 \u043e\u0442\u0437\u044b\u0432\u0430")
    name: str = Field(description="\u0418\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f, \u043a\u043e\u0442\u043e\u0440\u043e\u0435 \u0431\u0443\u0434\u0435\u0442 \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u043e \u043d\u0430 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435 \u0441 \u043e\u0442\u0437\u044b\u0432\u0430\u043c\u0438")


class CommentsCompanyidRessponse200DataTypes(BaseModel):
    """Получить комментарии
    Схема спеки: Root Type for comments_companyid_ressponse200_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: list[dict[str, Any]] | None = Field(default=None, alias="data", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class CompaniesDataTypes(BaseModel):
    """Получить список компаний
    Схема спеки: Root Type for companies_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0433\u043e \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: list[dict[str, Any]] | None = Field(default=None, alias="data", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class CompaniesDataTypes2(BaseModel):
    """Получить список компаний
    Схема спеки: Root Type for companies_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0433\u043e \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: list[dict[str, Any]] | None = Field(default=None, alias="data", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class Company2(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float = Field(alias="id", description="ID \u043a\u043e\u043f\u0430\u043d\u0438\u0438\u0438")
    title: str = Field(description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0438")
    country: str = Field(description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u0442\u0440\u0430\u043d\u044b, \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u0440\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0430 \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u044f")
    country_id: float = Field(description="ID \u0441\u0442\u0440\u0430\u043d\u044b")
    city: str = Field(description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0433\u043e\u0440\u043e\u0434\u0430, \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u043c \u0440\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0430 \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u044f")
    city_id: float = Field(description="ID \u0433\u043e\u0440\u043e\u0434\u0430")
    phone: str = Field(description="\u0422\u0435\u043b\u0435\u0444\u043e\u043d \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438")
    timezone: str = Field(description="\u0412\u0440\u0435\u043c\u0435\u043d\u043d\u0430\u044f \u0437\u043e\u043d\u0430 \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438")
    address: str = Field(description="\u0410\u0434\u0440\u0435\u0441 \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438")
    coordinate_lat: float = Field(description="\u0428\u0438\u0440\u043e\u0442\u0430")
    coordinate_lng: float = Field(description="\u0414\u043e\u043b\u0433\u043e\u0442\u0430")


class CompanyAnalyticsLoyaltyProgramsIncomeDataTypes(BaseModel):
    """Статистика по выручке
    Схема спеки: Root Type for company_analytics_loyalty_programs_income_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f")
    data_: dict[str, Any] | None = Field(default=None, alias="data", description="\u041e\u0431\u044a\u0435\u043a\u0442 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class CompanyAnalyticsLoyaltyProgramsStaffDataTypes(BaseModel):
    """Получить статистику позвращаемости по сотруднику.
    Схема спеки: Root Type for company_analytics_loyalty_programs_staff_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f")
    data_: list[dict[str, Any]] | None = Field(default=None, alias="data", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u0441 \u043e\u0431\u044a\u0435\u043a\u0442\u0430\u043c\u0438 \u0434\u0430\u043d\u043d\u044b\u0445")
    meta: dict[str, Any] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u0441\u043e\u0434\u0435\u0440\u0436\u0438\u0442 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043d\u0430\u0439\u0434\u0435\u043d\u043d\u044b\u0445 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432)")


class CompanyAnalyticsLoyaltyProgramsVisitsDataTypes(BaseModel):
    """Получение статистики по клиентам
    Схема спеки: Root Type for company_analytics_loyalty_programs_visits_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f")
    data_: dict[str, Any] | None = Field(default=None, alias="data", description="\u041e\u0431\u044a\u0435\u043a\u0442 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class CompanyCompanyIdUsersResponseDataTypes(BaseModel):
    """Получить пользователей компании
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: list[dict[str, Any]] | None = Field(default=None, alias="data", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: dict[str, Any] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u0441\u043e\u0434\u0435\u0440\u0436\u0438\u0442 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043d\u0430\u0439\u0434\u0435\u043d\u043d\u044b\u0445 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0439)")


class CompanyCompanyidClientsSearchRequestDataTypes(BaseModel):
    """Получить список клиентов
    Схема спеки: Root Type for company_cpmpanuid_clients_search_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    page_: float | None = Field(default=None, alias="page", description="\u041d\u043e\u043c\u0435\u0440 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430")
    page_size: float | None = Field(default=None, description="\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0432\u044b\u0432\u043e\u0434\u0438\u043c\u044b\u0445 \u0441\u0442\u0440\u043e\u043a \u043d\u0430 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435. \u041c\u0430\u043a\u0441\u0438\u043c\u0443\u043c 200. (\u041f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e 25)")
    fields: list[str] | None = Field(default=None, description="\u041f\u043e\u043b\u044f, \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u043d\u0443\u0436\u043d\u043e \u0432\u0435\u0440\u043d\u0443\u0442\u044c \u0432 \u043e\u0442\u0432\u0435\u0442\u0435")
    order_by: Literal["id", "name", "phone", "email", "discount", "first_visit_date", "last_visit_date", "sold_amount", "visits_count"] | None = Field(default=None, description="\u041f\u043e \u043a\u0430\u043a\u043e\u043c\u0443 \u043f\u043e\u043b\u044e \u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c")
    order_by_direction: Literal["ASC", "DESC"] | None = Field(default=None, description="\u041a\u0430\u043a \u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c (\u043f\u043e \u0432\u043e\u0437\u0440\u0430\u0441\u0442\u0430\u043d\u0438\u044e / \u043f\u043e \u0443\u0431\u044b\u0432\u0430\u043d\u0438\u044e)")
    operation: Literal["AND", "OR"] | None = Field(default=None, description="\u0422\u0438\u043f \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438")
    filters: list[dict[str, Any]] | None = Field(default=None, description="\u0424\u0438\u043b\u044c\u0442\u0440\u044b \u0434\u043b\u044f \u043f\u043e\u0438\u0441\u043a\u0430 \u043f\u043e \u043a\u043b\u0438\u0435\u043d\u0442\u0430\u043c")


class CompanyCompanyidClientsSearchResponseDataTypes(BaseModel):
    """Получить список клиентов
    Схема спеки: Root Type for company_companyid_clients_search_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: list[dict[str, Any]] | None = Field(default=None, alias="data", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: dict[str, Any] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u0441\u043e\u0434\u0435\u0440\u0436\u0438\u0442 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043d\u0430\u0439\u0434\u0435\u043d\u043d\u044b\u0445 \u043a\u043b\u0438\u0435\u043d\u0442\u043e\u0432)")


class CompanyCompanyidServiceCategoriesResponse200DataTypes(BaseModel):
    """Получить список категорий услуг
    Схема спеки: Root Type for company_companyid_service_categories_response200_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: list[dict[str, Any]] | None = Field(default=None, alias="data", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432")
    meta: dict[str, Any] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0439)")


class CompanyCompanyidServicesServiceidResponse200DataTypes(BaseModel):
    """Получить список услуг / конкретную услугу
    Схема спеки: Root Type for company_companyid_services_serviceid_response200_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: list[dict[str, Any]] | None = Field(default=None, alias="data", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: dict[str, Any] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u0441\u043e\u0434\u0435\u0440\u0436\u0438\u0442 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043d\u0430\u0439\u0434\u0435\u043d\u043d\u044b\u0445 \u0443\u0441\u043b\u0443\u0433)")


class CompanyCompanyidStaffStaffidResponseDataTypes(BaseModel):
    """Получить список сотрудников / конкретного сотрудника
    Схема спеки: Root Type for company_companyid_staff_staffid_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: list[dict[str, Any]] | None = Field(default=None, alias="data", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: dict[str, Any] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u0441\u043e\u0434\u0435\u0440\u0436\u0430\u0442 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043d\u0430\u0439\u0434\u0435\u043d\u043d\u044b\u0445 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u043e\u0432)")


class CompanyCompanyidStaffStaffidResponseDataTypesDeprecated(BaseModel):
    """Устаревшее. Получить список сотрудников / конкретного сотрудника
    Схема спеки: Root Type for company_companyid_staff_staffid_response_data_types_deprecated
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: list[dict[str, Any]] | None = Field(default=None, alias="data", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class CompanyCreateRequestDataTypes(BaseModel):
    """Создать компанию
    Схема спеки: Root Type for company_create_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    title: str | None = Field(default=None, description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438")
    country_id: float | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0441\u0442\u0440\u0430\u043d\u044b, \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u0440\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0430 \u043a\u043e\u043f\u0430\u043d\u0438\u044f ([\u043c\u0435\u0442\u043e\u0434 \u043f\u043e\u043b\u0443\u0447\u0435\u043d\u0438\u044f \u0441\u0442\u0440\u0430\u043d](#countries))")
    city_id: float | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0433\u043e\u0440\u043e\u0434\u0430, \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u043c \u0440\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0430 \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u044f ([\u043c\u0435\u0442\u043e\u0434 \u043f\u043e\u043b\u0443\u0447\u0435\u043d\u0438\u044f \u0433\u043e\u0440\u043e\u0434\u043e\u0432](#cities))")
    address: str | None = Field(default=None, description="\u0410\u0434\u0440\u0435\u0441 \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438")
    site: str | None = Field(default=None, description="\u0421\u0430\u0439\u0442 \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438")
    coordinate_lat: float | None = Field(default=None, description="\u0428\u0438\u0440\u043e\u0442\u0430")
    coordinate_lot: float | None = Field(default=None, description="\u0414\u043e\u043b\u0433\u043e\u0442\u0430")
    business_type_id: float | None = Field(default=None, description="\u0421\u0444\u0435\u0440\u0430 \u0431\u0438\u0437\u043d\u0435\u0441\u0430")
    short_descr: str | None = Field(default=None, description="\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438")


class CompanyCreateResponseDataTypes(BaseModel):
    """Создать компанию
    Схема спеки: Root Type for company_create_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0433\u043e \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: dict[str, Any] | None = Field(default=None, alias="data", description="\u041e\u0431\u044a\u0435\u043a\u0442 \u0434\u0430\u043d\u043d\u044b\u0445")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class CompanyGetOnlineSettingsResponseDataFieldDataTypes(BaseModel):
    """Схема спеки: Root Type for company_get_online_settings_response_data_field_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    confirm_number: bool = Field(description="\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0430\u0442\u044c \u043d\u043e\u043c\u0435\u0440 \u043a\u043b\u0438\u0435\u043d\u0442\u0430 \u043f\u043e SMS")
    any_master: bool = Field(description="\u0420\u0435\u0436\u0438\u043c \"\u041b\u044e\u0431\u043e\u0439 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\"")
    seance_delay_step: int = Field(description="\u0417\u0430\u0434\u0435\u0440\u0436\u043a\u0430 \u0434\u043e \u0431\u043b\u0438\u0436\u0430\u0439\u0448\u0435\u0433\u043e \u0441\u0435\u0430\u043d\u0441\u0430, \u0432 \u043c\u0438\u043d\u0443\u0442\u0430\u0445 \u043e\u0442 0 \u0434\u043e 23 \u0447\u0430\u0441\u043e\u0432 (\u0432\u043a\u043b\u044e\u0447\u0438\u0442\u0435\u043b\u044c\u043d\u043e) \u0441 \u0448\u0430\u0433\u043e\u043c 30 \u043c\u0438\u043d\u0443\u0442")
    activity_online_record_clients_count_max: int = Field(description="\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043c\u0435\u0441\u0442 \u0432 \u043e\u0434\u043d\u043e\u0439 \u0437\u0430\u043f\u0438\u0441\u0438 \u0441\u043e\u0431\u044b\u0442\u0438\u044f")


class CompanyGetOnlineSettingsResponseDataTypes(BaseModel):
    """Получение настроек онлайн-записи
    Схема спеки: Root Type for company_get_online_settings_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: CompanyGetOnlineSettingsResponseDataFieldDataTypes | None = Field(default=None, alias="data")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435")


class CompanyGetResponseDataTypes(BaseModel):
    """Получить компанию
    Схема спеки: Root Type for company_get_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0433\u043e \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: dict[str, Any] | None = Field(default=None, alias="data", description="\u041e\u0431\u044a\u0435\u043a\u0442 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class CompanyGetTimetableSettingsResponseDataFieldDataTypes(BaseModel):
    """Схема спеки: Root Type for company_get_timetable_settings_response_data_field_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    record_type: int = Field(description="\u0422\u0438\u043f \u0437\u0430\u043f\u0438\u0441\u0438 \u043f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e: 0 - \u0421\u043c\u0435\u0448\u0430\u043d\u043d\u0430\u044f \u0437\u0430\u043f\u0438\u0441\u044c, 1 - \u0418\u043d\u0434\u0438\u0432\u0438\u0434\u0443\u0430\u043b\u044c\u043d\u0430\u044f \u0437\u0430\u043f\u0438\u0441\u044c, 2 - \u0413\u0440\u0443\u043f\u043f\u043e\u0432\u0430\u044f \u0437\u0430\u043f\u0438\u0441\u044c")
    activity_record_clients_count_max: int = Field(description="\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043c\u0435\u0441\u0442 \u0432 \u043e\u0434\u043d\u043e\u0439 \u0437\u0430\u043f\u0438\u0441\u0438 \u0441\u043e\u0431\u044b\u0442\u0438\u044f")


class CompanyGetTimetableSettingsResponseDataTypes(BaseModel):
    """Получение настроек журнала записи
    Схема спеки: Root Type for company_get_timetable_settings_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: CompanyGetTimetableSettingsResponseDataFieldDataTypes | None = Field(default=None, alias="data")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435")


class CompanyGridSettingContainer(BaseModel):
    """Правила построения слотов.
    Схема спеки: Объект модели "Настройки формирования сетки"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    grid_first_timeslot: float | None = Field(default=None, description="\u041d\u0438\u0436\u043d\u0435\u0435 \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u0435 \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u043e\u0441\u0442\u0438 \u0441\u043b\u043e\u0442\u043e\u0432 (\u201c\u0432\u0440\u0435\u043c\u044f \u0434\u043b\u044f \u043e\u043d\u043b\u0430\u0439\u043d \u0437\u0430\u043f\u0438\u0441\u0438\u201d \u0432 \u0438\u043d\u0442\u0435\u0440\u0444\u0435\u0439\u0441\u0435).")
    grid_last_timeslot: float | None = Field(default=None, description="\u0412\u0435\u0440\u0445\u043d\u0435\u0435 \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u0435 \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u043e\u0441\u0442\u0438 \u0441\u043b\u043e\u0442\u043e\u0432 (\u201c\u0432\u0440\u0435\u043c\u044f \u0434\u043b\u044f \u043e\u043d\u043b\u0430\u0439\u043d \u0437\u0430\u043f\u0438\u0441\u0438\u201d \u0432 \u0438\u043d\u0442\u0435\u0440\u0444\u0435\u0439\u0441\u0435).")
    grid_display_step: float | None = Field(default=None, description="\u0428\u0430\u0433 \u0432\u044b\u0432\u043e\u0434\u0430 \u0441\u043b\u043e\u0442\u043e\u0432 (\u0432 \u0441\u0435\u043a\u0443\u043d\u0434\u0430\u0445).")
    grid_nearest_timeslot_delay: float | None = Field(default=None, description="\u0417\u0430\u0434\u0435\u0440\u0436\u043a\u0430 \u0434\u043e \u0431\u043b\u0438\u0436\u0430\u0439\u0448\u0435\u0433\u043e \u0441\u0435\u0430\u043d\u0441\u0430 (\u0432 \u0441\u0435\u043a\u0443\u043d\u0434\u0430\u0445).")
    grid_base_type: str | None = Field(default=None, description="\u0422\u0438\u043f \u0441\u0435\u0442\u043a\u0438 `predefined` - \u201c\u0444\u0438\u043a\u0441\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u043e\u201d/\u201c\u043e\u043f\u0442\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u201d + \u201c\u043e\u0442 \u0432\u0440\u0435\u043c\u0435\u043d\u0438 \u0434\u043b\u044f \u043e\u043d\u043b\u0430\u0439\u043d \u0437\u0430\u043f\u0438\u0441\u0438\u201d; `schedule` - \u201c\u0444\u0438\u043a\u0441\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u043e\u201d/\u201c\u043e\u043f\u0442\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u201d + \u201c\u043e\u0442 \u0433\u0440\u0430\u0444\u0438\u043a\u0430 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430\u201d; `timeslots` - \u201c\u0434\u0438\u043d\u0430\u043c\u0438\u0447\u0435\u0441\u043a\u0438\u201d enum: - predef...")
    is_grid_flexible: bool | None = Field(default=None, description="\u0424\u043b\u0430\u0433 \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u044f \"\u0433\u0438\u0431\u043a\u043e\u0433\u043e\" \u0441\u043b\u043e\u0442\u0430.")


class CompanyGridWeekdaysContainer(BaseModel):
    """Получение настроек формирования таймслотов филиала.
    Схема спеки: Настройки слотов по дням недели
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    weekday: float | None = Field(default=None, description="\u0414\u0435\u043d\u044c \u043d\u0435\u0434\u0435\u043b\u0438 [1 - 7].")
    timeslots: list[float] | None = Field(default=None, description="\u0412\u043a\u043b\u044e\u0447\u0435\u043d\u043d\u044b\u0435 \u0434\u043b\u044f \u0437\u0430\u043f\u0438\u0441\u0438 \u0441\u043b\u043e\u0442\u044b (\u0434\u043b\u044f \u0440\u0435\u0436\u0438\u043c\u0430 \"predefined\", \u0432 \u043e\u0441\u0442\u0430\u043b\u044c\u043d\u044b\u0445 \u0441\u043b\u0443\u0447\u0430\u044f\u0445 \u043d\u0435\u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u043e).")
    setting: CompanyGridSettingContainer | None = Field(default=None)


class CompanyLoyaltyProgramsSearchDataTypes(BaseModel):
    """Получение списка акций, доступных для филиала
    Схема спеки: Root Type for company_loyalty_programs_search_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f.")
    data_: list[dict[str, Any]] | None = Field(default=None, alias="data", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438.")
    meta: dict[str, Any] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u0441\u043e\u0434\u0435\u0440\u0436\u0438\u0442 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043d\u0430\u0439\u0434\u0435\u043d\u043d\u044b\u0445 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432)")


class CompanyMinimal(BaseModel):
    """Схема спеки: Объект модели "Филиал, минимальная информация"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0444\u0438\u043b\u0438\u0430\u043b\u0430.")
    title: str | None = Field(default=None, description="\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0444\u0438\u043b\u0438\u0430\u043b\u0430.")


class CompanyPutRequestDataTypes(BaseModel):
    """Изменить компанию
    Схема спеки: Root Type for company_put_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    title: str | None = Field(default=None, description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438")
    country_id: float | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0441\u0442\u0440\u0430\u043d\u044b (\u043f\u0440\u0438\u043e\u0440\u0438\u0442\u0435\u0442\u043d\u0435\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430 country)")
    country: str | None = Field(default=None, description="\u0421\u0442\u0440\u0430\u043d\u0430")
    city_id: float | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0433\u043e\u0440\u043e\u0434\u0430 (\u043f\u0440\u0438\u043e\u0440\u0438\u0442\u0435\u0442\u043d\u0435\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430 city)")
    city: str | None = Field(default=None, description="\u0413\u043e\u0440\u043e\u0434")
    address: str | None = Field(default=None, description="\u0410\u0434\u0440\u0435\u0441 \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438")
    zip: str | None = Field(default=None, description="\u0418\u043d\u0434\u0435\u043a\u0441")
    phones: list[str] | None = Field(default=None, description="\u0422\u0435\u043b\u0435\u0444\u043e\u043d\u044b")
    social: dict[str, Any] | None = Field(default=None, description="\u0421\u043e\u0446\u0438\u0430\u043b\u044c\u043d\u044b\u0435 \u0441\u0435\u0442\u0438 \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438")
    site: str | None = Field(default=None, description="\u0421\u0430\u0439\u0442 \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438")
    coordinate_lat: float | None = Field(default=None, description="\u0428\u0438\u0440\u043e\u0442\u0430")
    coordinate_lon: float | None = Field(default=None, description="\u0414\u043e\u043b\u0433\u043e\u0442\u0430")
    description: str | None = Field(default=None, description="\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435")
    business_type_id: float | None = Field(default=None, description="\u0421\u0444\u0435\u0440\u0430 \u0431\u0438\u0437\u043d\u0435\u0441\u0430")
    short_descr: str | None = Field(default=None, description="\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f \u0431\u0438\u0437\u043d\u0435\u0441\u0430")


class CompanyPutResponseDataTypes(BaseModel):
    """Изменить компанию
    Схема спеки: Root Type for company_put_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438")
    title: str | None = Field(default=None, description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438")
    country_id: float | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0441\u0442\u0440\u0430\u043d\u044b, \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u0440\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0430 \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u044f")
    country: str | None = Field(default=None, description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u0442\u0440\u0430\u043d\u044b, \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u0440\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0430 \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u044f")
    city_id: float | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0433\u043e\u0440\u043e\u0434\u0430, \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u043c \u0440\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0430 \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u044f")
    city: str | None = Field(default=None, description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0433\u043e\u0440\u043e\u0434\u0430, \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u043c \u0440\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0430 \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u044f")
    timezone_name: str | None = Field(default=None, description="\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0439 \u0437\u043e\u043d\u044b, \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u0440\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0430 \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u044f")
    address: str | None = Field(default=None, description="\u0410\u0434\u0440\u0435\u0441, \u043f\u043e \u043a\u043e\u0442\u043e\u0440\u043e\u043c\u0443 \u0440\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0430 \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u044f")
    zip: float | None = Field(default=None, description="\u0418\u043d\u0434\u0435\u043a\u0441")
    social: dict[str, Any] | None = Field(default=None, description="\u0421\u043e\u0446\u0438\u0430\u043b\u044c\u043d\u044b\u0435 \u0441\u0435\u0442\u0438 \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438")
    site: str | None = Field(default=None, description="\u0421\u0430\u0439\u0442 \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438")
    coordinate_lat: float | None = Field(default=None, description="\u0428\u0438\u0440\u043e\u0442\u0430")
    coordinate_lon: float | None = Field(default=None, description="\u0414\u043e\u043b\u0433\u043e\u0442\u0430")
    description: str | None = Field(default=None, description="\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435")
    business_type_id: float | None = Field(default=None, description="\u0421\u0444\u0435\u0440\u0430 \u0431\u0438\u0437\u043d\u0435\u0441\u0430")
    short_descr: str | None = Field(default=None, description="\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f \u0431\u0438\u0437\u043d\u0435\u0441\u0430")
    phone_confirmation: bool | None = Field(default=None, description="\u041d\u0443\u0436\u043d\u043e \u043b\u0438 \u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0430\u0442\u044c \u0442\u0435\u043b\u0435\u0444\u043e\u043d \u043f\u043e \u0441\u043c\u0441, \u043f\u0440\u0438 \u0431\u0440\u043e\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0438")
    group_priority: int | None = Field(default=None, description="\u0427\u0435\u043c \u0431\u043e\u043b\u044c\u0448\u0435 \u043f\u0440\u0438\u043e\u0440\u0438\u0442\u0435\u0442, \u0442\u0435\u043c \u0432\u044b\u0448\u0435 \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u044f \u043f\u0440\u0438 \u0432\u044b\u0432\u043e\u0434\u0435 \u0432 \u0441\u043f\u0438\u0441\u043a\u0435 \u0444\u0438\u043b\u0438\u0430\u043b\u043e\u0432 \u0441\u0435\u0442\u0438")
    push_notification_phone_confirm: bool | None = Field(default=None, description="\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0430\u0442\u044c \u043d\u043e\u043c\u0435\u0440 \u043a\u043b\u0438\u0435\u043d\u0442\u0430 \u0434\u043b\u044f \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0438 push \u0443\u0432\u0435\u0434\u043e\u043c\u043b\u0435\u043d\u0438\u0439")
    access: dict[str, Any] | None = Field(default=None, description="\u0421\u043f\u0438\u0441\u043e\u043a \u043f\u0440\u0430\u0432")


class CompanySalonIdSaleDocumentidResponseDataTypes(BaseModel):
    """Получение операции продажи
    Схема спеки: Root Type for company_salon_id_sale_documentid_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: dict[str, Any] | None = Field(default=None, alias="data", description="\u041e\u0431\u044a\u0435\u043a\u0442 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class CompanySalonidSaleDocumentidPaymentAbonements(BaseModel):
    """В случае оплаты абонементом, если у пользователя нет права "Оплата сертификатом и абонементом без кода" в теле запроса также необходимо передать пераметр "number" (string), содержащий код абонемента.
    Схема спеки: Оплата при помощи абонемента - работает только для визита.
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    payment: dict[str, Any] | None = Field(default=None, description="\u041e\u0431\u044a\u0435\u043a\u0442, \u0441\u043e\u0434\u0435\u0440\u0436\u0430\u0449\u0438\u0439 \u043c\u0435\u0442\u043e\u0434 \u043e\u043f\u043b\u0430\u0442\u044b")


class CompanySalonidSaleDocumentidPaymentAccount(BaseModel):
    """Оплата в кассу
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    payment: dict[str, Any] | None = Field(default=None, description="\u041e\u0431\u044a\u0435\u043a\u0442, \u0441\u043e\u0434\u0435\u0440\u0436\u0430\u0449\u0438\u0439 \u043c\u0435\u0442\u043e\u0434 \u043e\u043f\u043b\u0430\u0442\u044b")


class CompanySalonidSaleDocumentidPaymentCertificate(BaseModel):
    """В случае оплаты сертификатом, если у пользователя нет права "Оплата сертификатом и абонементом без кода" в теле запроса также необходимо передать пераметр "number" (string), содержащий код сертификата.
    Схема спеки: Оплата при помощи сертификата
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    payment: dict[str, Any] | None = Field(default=None, description="\u041e\u0431\u044a\u0435\u043a\u0442, \u0441\u043e\u0434\u0435\u0440\u0436\u0430\u0449\u0438\u0439 \u043c\u0435\u0442\u043e\u0434 \u043e\u043f\u043b\u0430\u0442\u044b")


class CompanySalonidSaleDocumentidPaymentDeposit(BaseModel):
    """Оплата лояльностью (различными методами)
    Схема спеки: Оплата при помощи личного счета - депозита
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    payment: dict[str, Any] | None = Field(default=None, description="\u041e\u0431\u044a\u0435\u043a\u0442, \u0441\u043e\u0434\u0435\u0440\u0436\u0430\u0449\u0438\u0439 \u043c\u0435\u0442\u043e\u0434 \u043e\u043f\u043b\u0430\u0442\u044b")


class CompanySalonidSaleDocumentidPaymentLoyaltyCard(BaseModel):
    """Оплата при помощи карты лояльности
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    payment: dict[str, Any] | None = Field(default=None, description="\u041e\u0431\u044a\u0435\u043a\u0442, \u0441\u043e\u0434\u0435\u0440\u0436\u0430\u0449\u0438\u0439 \u043c\u0435\u0442\u043e\u0434 \u043e\u043f\u043b\u0430\u0442\u044b")


class CompanySalonidSaleDocumentidPaymentLoyaltyProgram(BaseModel):
    """Оплата при помощи программы лояльности
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    payment: dict[str, Any] | None = Field(default=None, description="\u041e\u0431\u044a\u0435\u043a\u0442, \u0441\u043e\u0434\u0435\u0440\u0436\u0430\u0449\u0438\u0439 \u043c\u0435\u0442\u043e\u0434 \u043e\u043f\u043b\u0430\u0442\u044b")


class CompanySalonidSaleDocumentidPaymentReferal(BaseModel):
    """Оплата при помощи реферальной программы - работает только для визита
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    payment: dict[str, Any] | None = Field(default=None, description="\u041e\u0431\u044a\u0435\u043a\u0442, \u0441\u043e\u0434\u0435\u0440\u0436\u0430\u0449\u0438\u0439 \u043c\u0435\u0442\u043e\u0434 \u043e\u043f\u043b\u0430\u0442\u044b")


class CompanyUpdateOnlineSettingsDataTypes(BaseModel):
    """Схема спеки: Root Type for company_update_online_settings_data_type
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    confirm_number: bool = Field(description="\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0430\u0442\u044c \u043d\u043e\u043c\u0435\u0440 \u043a\u043b\u0438\u0435\u043d\u0442\u0430 \u043f\u043e SMS")
    any_master: bool = Field(description="\u0420\u0435\u0436\u0438\u043c \"\u041b\u044e\u0431\u043e\u0439 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\"")
    seance_delay_step: int = Field(description="\u0417\u0430\u0434\u0435\u0440\u0436\u043a\u0430 \u0434\u043e \u0431\u043b\u0438\u0436\u0430\u0439\u0448\u0435\u0433\u043e \u0441\u0435\u0430\u043d\u0441\u0430, \u0432 \u043c\u0438\u043d\u0443\u0442\u0430\u0445 \u043e\u0442 0 \u0434\u043e 23 \u0447\u0430\u0441\u043e\u0432 (\u0432\u043a\u043b\u044e\u0447\u0438\u0442\u0435\u043b\u044c\u043d\u043e) \u0441 \u0448\u0430\u0433\u043e\u043c 30 \u043c\u0438\u043d\u0443\u0442")
    activity_online_record_clients_count_max: int = Field(description="\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043c\u0435\u0441\u0442 \u0432 \u043e\u0434\u043d\u043e\u0439 \u0437\u0430\u043f\u0438\u0441\u0438 \u0441\u043e\u0431\u044b\u0442\u0438\u044f")


class CompanyUpdateTimetableSettingsDataTypes(BaseModel):
    """Схема спеки: Root Type for company_update_timetable_settings_data_type
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    record_type: int = Field(description="\u0422\u0438\u043f \u0437\u0430\u043f\u0438\u0441\u0438 \u043f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e: 0 - \u0421\u043c\u0435\u0448\u0430\u043d\u043d\u0430\u044f \u0437\u0430\u043f\u0438\u0441\u044c, 1 - \u0418\u043d\u0434\u0438\u0432\u0438\u0434\u0443\u0430\u043b\u044c\u043d\u0430\u044f \u0437\u0430\u043f\u0438\u0441\u044c, 2 - \u0413\u0440\u0443\u043f\u043f\u043e\u0432\u0430\u044f \u0437\u0430\u043f\u0438\u0441\u044c")
    activity_record_clients_count_max: int = Field(description="\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043c\u0435\u0441\u0442 \u0432 \u043e\u0434\u043d\u043e\u0439 \u0437\u0430\u043f\u0438\u0441\u0438 \u0441\u043e\u0431\u044b\u0442\u0438\u044f")


class CompanyUsersDeprecatedResponseDataTypes(BaseModel):
    """Получить пользователей компании
    Схема спеки: Root Type for company_users_deprecated_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: list[dict[str, Any]] | None = Field(default=None, alias="data", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class Consumables2(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    consumables: list[dict[str, Any]] | None = Field(default=None, description="\u0421\u043f\u0438\u0441\u043e\u043a \u0440\u0430\u0441\u0445\u043e\u0434\u043d\u0438\u043a\u043e\u0432")


class CountriesResponseDataTypes(BaseModel):
    """Получить список стран
    Схема спеки: Root Type for countries_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: list[dict[str, Any]] | None = Field(default=None, alias="data", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class Currency2(BaseModel):
    """Валюта
    Схема спеки: Root Type for Currency
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0432\u0430\u043b\u044e\u0442\u044b")
    iso: str | None = Field(default=None, description="\u0422\u0440\u0435\u0445\u0431\u0443\u043a\u0432\u0435\u043d\u043d\u044b\u0439 \u043a\u043e\u0434 \u0432\u0430\u043b\u044e\u0442\u044b \u0432 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0438\u0438 \u0441 ISO 4217")
    name: str | None = Field(default=None, description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0432\u0430\u043b\u044e\u0442\u044b")
    symbol: str | None = Field(default=None, description="\u0421\u0438\u043c\u0432\u043e\u043b \u0432\u0430\u043b\u044e\u0442\u044b, \u0443\u043a\u0430\u0437\u044b\u0432\u0430\u0435\u043c\u044b\u0439 \u0440\u044f\u0434\u043e\u043c \u0441 \u0441\u0443\u043c\u043c\u043e\u0439")
    is_symbol_after_amount: bool | None = Field(default=None, description="\u0424\u043b\u0430\u0433, \u0433\u0434\u0435 \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0442\u044c \u0441\u0438\u043c\u0432\u043e\u043b \u0432\u0430\u043b\u044e\u0442\u044b \u043e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u043e \u0441\u0443\u043c\u043c\u044b (true - \u043f\u043e\u0441\u043b\u0435 \u0441\u0443\u043c\u043c\u044b, false - \u043f\u0435\u0440\u0435\u0434)")


class CustomFieldsRequestDataType(BaseModel):
    """Добавление дополнительного поля
    Схема спеки: Root Type for custom_fields_request_data_type
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    type_: str = Field(alias="type", description="\u0422\u0438\u043f \u043f\u043e\u043b\u044f")
    code: str = Field(description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043f\u043e\u043b\u044f")
    title: str = Field(description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u043e\u043b\u044f")
    user_can_edit: bool = Field(description="\u041c\u043e\u0436\u0435\u0442 \u043b\u0438 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043f\u043e\u043b\u0435")
    show_in_ui: bool = Field(description="\u041f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c \u043b\u0438 \u043f\u043e\u043b\u0435 \u0432 \u0438\u043d\u0442\u0435\u0440\u0444\u0435\u0439\u0441\u0435")


class CustomFieldsResponseDataTypes(BaseModel):
    """Получение коллекции полей филиала
    Схема спеки: Root Type for custom_fields_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: list[dict[str, Any]] | None = Field(default=None, alias="data", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class DepositOperationResponseDataTypes(BaseModel):
    """Создание операции поплонения личного счета
    Схема спеки: Root Type for deposit_operation_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: dict[str, Any] | None = Field(default=None, alias="data", description="\u041e\u0431\u044a\u0435\u043a\u0442 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class DepositTransaction(BaseModel):
    """Транзакция по личному счету.
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="ID \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u0438.")
    salon_id: float | None = Field(default=None, description="ID \u0444\u0438\u043b\u0438\u0430\u043b\u0430.")
    salon_group_id: float | None = Field(default=None, description="ID \u0441\u0435\u0442\u0438.")
    user_id: float | None = Field(default=None, description="\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c, \u043d\u0430 \u0441\u0447\u0435\u0442\u0443 \u043a\u043e\u0442\u043e\u0440\u043e\u0433\u043e \u0441\u043e\u0432\u0435\u0440\u0448\u0435\u043d\u0430 \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u044f.")
    amount: float | None = Field(default=None, description="\u0421\u0443\u043c\u043c\u0430 \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u0438.")
    date_create: str | None = Field(default=None, description="\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u0438.")
    comment: str | None = Field(default=None, description="\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 \u043a \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u0438.")
    deleted: bool | None = Field(default=None, description="\u0424\u043b\u0430\u0433 \u0443\u0434\u0430\u043b\u0435\u043d\u0430 \u043b\u0438 \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u044f.")


class DepositTransactionType(BaseModel):
    """Тип транзакции по личному счету.
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="ID \u0442\u0438\u043f\u0430 \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u0438.")
    comment: str | None = Field(default=None, description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0442\u0438\u043f\u0430 \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u0438.")


class DeprecatedServicesCompanyidRequestDataTypes(BaseModel):
    """Изменить услугу
    Схема спеки: Root Type for deprecated_services_companyid_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    title: str | None = Field(default=None, description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0443\u0441\u043b\u0443\u0433\u0438")
    category_id: float | None = Field(default=None, description="ID \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0443\u0441\u043b\u0443\u0433")
    price_min: float | None = Field(default=None, description="\u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0443\u0441\u043b\u0443\u0433\u0438")
    price_max: float | None = Field(default=None, description="\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0443\u0441\u043b\u0443\u0433\u0438")
    duration: float | None = Field(default=None, description="\u0414\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0443\u0441\u043b\u0443\u0433\u0438, \u043f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e \u0440\u0430\u0432\u043d\u0430 3600 \u0441\u0435\u043a\u0443\u043d\u0434\u0430\u043c")
    discount: float | None = Field(default=None, description="\u0421\u043a\u0438\u0434\u043a\u0430 \u043f\u0440\u0438 \u043e\u043a\u0430\u0437\u0430\u043d\u0438\u0438 \u0443\u0441\u043b\u0443\u0433\u0438")
    comment: str | None = Field(default=None, description="\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 \u043a \u0443\u0441\u043b\u0443\u0433\u0435")
    weight: float | None = Field(default=None, description="\u0412\u0435\u0441 \u0443\u0441\u043b\u0443\u0433\u0438 (\u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u0442\u0441\u044f \u0434\u043b\u044f \u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0438 \u0443\u0441\u043b\u0443\u0433 \u043f\u0440\u0438 \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0438)")
    service_type: float | None = Field(default=None, description="\u0414\u043e\u0441\u0442\u0443\u043f\u043d\u0430 \u043b\u0438 \u0434\u043b\u044f \u043e\u043d\u043b\u0430\u0439\u043d \u0437\u0430\u043f\u0438\u0441\u0438 \u0443\u0441\u043b\u0443\u0433\u0430. 1 - \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u0430, 0 \u043d\u0435 \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u0430.")
    api_service_id: str | None = Field(default=None, description="\u0412\u043d\u0435\u0448\u043d\u0438\u0439 \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0443\u0441\u043b\u0443\u0433\u0438")
    staff: list[dict[str, Any]] | None = Field(default=None, description="\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0438, \u043e\u043a\u0430\u0437\u044b\u0432\u0430\u044e\u0448\u0438\u0435 \u0443\u0441\u043b\u0443\u0433\u0443 \u0438 \u0434\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u043e\u043a\u0430\u0437\u0430\u043d\u0438\u044f \u0443\u0441\u043b\u0443\u0433\u0438 \u043a\u0430\u0436\u0434\u044b\u043c \u0438\u0437 \u043d\u0438\u0445")


class DeprecatedServicesCompanyidResponseDataTypes(BaseModel):
    """Изменить услугу
    Схема спеки: Root Type for deprecated_services_companyid_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: dict[str, Any] | None = Field(default=None, alias="data", description="\u041e\u0431\u044a\u0435\u043a\u0442 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class EmailClientsByFilterRequestDataTypes(BaseModel):
    """Отправить Email рассылку по клиентам, подходящим под фильтры
    Схема спеки: Root Type for email_clients_by_filter_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    subject: str = Field(description="\u0422\u0435\u043c\u0430 Email \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f")
    text: str = Field(description="\u0422\u0435\u043a\u0441\u0442 Email \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f")


class EmailClientsByIdRequestDataTypes(BaseModel):
    """Отправить Email рассылку по списку клиентов
    Схема спеки: Root Type for email_clients_by_id_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    client_ids: list[float] = Field(description="\u041c\u0430\u0441\u0441\u0438\u0432 \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440\u043e\u0432 \u043a\u043b\u0438\u0435\u043d\u0442\u043e\u0432")
    subject: str = Field(description="\u0422\u0435\u043c\u0430 Email \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f")
    text: str = Field(description="\u0422\u0435\u043a\u0441\u0442 Email \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f")


class FinanceTransactionRequestDataTypes(BaseModel):
    """Создание финансовой транзакции
    Схема спеки: Root Type for finance_transaction_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    expense_id: float | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u044c\u044f \u043f\u043b\u0430\u0442\u0435\u0436\u0430")
    amount: float | None = Field(default=None, description="\u0421\u0443\u043c\u043c\u0430 \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u0438")
    account_id: float | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043a\u0430\u0441\u0441\u044b")
    client_id: float | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043a\u043b\u0438\u0435\u043d\u0442\u0430")
    supplier_id: float | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043a\u043e\u043d\u0442\u0440\u0430\u0433\u0435\u043d\u0442\u0430")
    master_id: float | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430")
    comment: float | None = Field(default=None, description="\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439")
    date: str | None = Field(default=None, description="\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u0438")


class FinanceTransactionResponseDataTypes(BaseModel):
    """Создание финансовой транзакции
    Схема спеки: Root Type for finance_transaction_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: dict[str, Any] | None = Field(default=None, alias="data", description="\u041e\u0431\u044a\u0435\u043a\u0442 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class GoodsCategoriesPostPutResponseDataTypes(BaseModel):
    """Создать категорию товаров
    Схема спеки: Root Type for goods_categories_response201_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f")
    data_: dict[str, Any] | None = Field(default=None, alias="data", description="\u041e\u0431\u044a\u0435\u043a\u0442 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class GoodsCategoriesRequestDataTypes(BaseModel):
    """Создать категорию товаров
    Схема спеки: Root Type for goods_categories_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    title: str = Field(description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0442\u043e\u0432\u0430\u0440\u043e\u0432")
    parent_category_id: int | None = Field(default=None, description="\u0418\u043d\u0435\u0434\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0440\u043e\u0434\u0438\u0442\u0435\u043b\u044c\u0441\u043a\u043e\u0439 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 (\u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u043d\u0435\u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u044b\u0439, \u043d\u043e \u043c\u043e\u0436\u0435\u0442 \u043f\u0440\u0438\u043d\u0438\u043c\u0430\u0442\u044c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 0 \u0438\u043b\u0438 null, \u0432 \u0441\u043b\u0443\u0447\u0430\u0435, \u043a\u043e\u0433\u0434\u0430 \u043d\u0435 \u043d\u0443\u0436\u043d\u043e \u0443\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c \u0440\u043e\u0434\u0438\u0442\u0435\u043b\u044c\u0441\u043a\u0443\u044e \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e)")
    article: str | None = Field(default=None, description="\u0410\u0440\u0442\u0438\u043a\u0443\u043b")
    comment: str | None = Field(default=None, description="\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439")


class GoodsCategoriesResponse200DataTypes(BaseModel):
    """Получить список категорий товаров
    Схема спеки: Root Type for goods_categories_response200_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: list[dict[str, Any]] | None = Field(default=None, alias="data", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class GoodsCategoryNodeResponse200DataTypes(BaseModel):
    """Пример запроса на получение состава категории
    Схема спеки: Root Type for goods_category_node_response200_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: dict[str, Any] | None = Field(default=None, alias="data", description="\u041e\u0431\u044a\u0435\u043a\u0442 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")


class GoodsCompanyGoodsIdResponse200DataTypes(BaseModel):
    """Получить товар (товары)
    Схема спеки: Root Type for goods_company_goods_id_response200_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: list[dict[str, Any]] | None = Field(default=None, alias="data", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u0441 \u043e\u0431\u044a\u0435\u043a\u0442\u0430\u043c\u0438 \u0434\u0430\u043d\u043d\u044b\u0445")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class GoodsCompanyRequestDataType(BaseModel):
    """Метод создания товара
    Схема спеки: Root Type for goods_company_request_data_type
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    title: str = Field(description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u0430")
    print_title: str | None = Field(default=None, description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0434\u043b\u044f \u043f\u0435\u0447\u0430\u0442\u0438 \u0432 \u0447\u0435\u043a\u0435")
    article: str | None = Field(default=None, description="\u0410\u0440\u0442\u0438\u043a\u0443\u043b")
    barcode: str | None = Field(default=None, description="\u0428\u0442\u0440\u0438\u0445-\u043a\u043e\u0434")
    category_id: int = Field(description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0442\u043e\u0432\u0430\u0440\u0430")
    cost: float | None = Field(default=None, description="\u0426\u0435\u043d\u0430 \u043f\u0440\u043e\u0434\u0430\u0436\u0438")
    actual_cost: float | None = Field(default=None, description="\u0421\u0435\u0431\u0435\u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c")
    sale_unit_id: int = Field(description="\u0415\u0434\u0438\u043d\u0438\u0446\u0430 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f \u0434\u043b\u044f \u043f\u0440\u043e\u0434\u0430\u0436\u0438")
    service_unit_id: int = Field(description="\u0415\u0434\u0438\u043d\u0438\u0446\u0430 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f \u0434\u043b\u044f \u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f")
    unit_equals: float | None = Field(default=None, description="\u041e\u0442\u043d\u043e\u0448\u0435\u043d\u0438\u0435 \u0435\u0434.\u0438\u043c\u0437\u0435\u0440\u0435\u043d\u0438\u044f \u0434\u043b\u044f \u043f\u0440\u043e\u0434\u0430\u0436\u0438 \u043a \u0435\u0434.\u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f \u0434\u043b\u044f \u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f")
    critical_amount: float | None = Field(default=None, description="\u041a\u0440\u0438\u0442\u0438\u0447\u043d\u044b\u0439 \u043e\u0441\u0442\u0430\u0442\u043e\u043a")
    desired_amount: float | None = Field(default=None, description="\u0416\u0435\u043b\u0430\u0435\u043c\u044b\u0439 \u043e\u0441\u0442\u0430\u0442\u043e\u043a")
    netto: float | None = Field(default=None, description="\u041c\u0430\u0441\u0441\u0430 \u043d\u0435\u0442\u0442\u043e")
    brutto: float | None = Field(default=None, description="\u041c\u0430\u0441\u0441\u0430 \u0431\u0440\u0443\u0442\u0442\u043e")
    comment: str | None = Field(default=None, description="\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439")
    tax_variant: int | None = Field(default=None, description="\u0421\u0438\u0441\u0442\u0435\u043c\u0430 \u043d\u0430\u043b\u043e\u0433\u043e\u043e\u0431\u043b\u043e\u0436\u0435\u043d\u0438\u044f")
    vat_id: int | None = Field(default=None, description="\u041d\u0414\u0421")


class GoodsCompanyRequestWithRulesDataType(BaseModel):
    """Метод создания товара
    Схема спеки: Root Type for goods_company_request_data_type
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    title: str = Field(description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u0430")
    print_title: str | None = Field(default=None, description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0434\u043b\u044f \u043f\u0435\u0447\u0430\u0442\u0438 \u0432 \u0447\u0435\u043a\u0435")
    article: str | None = Field(default=None, description="\u0410\u0440\u0442\u0438\u043a\u0443\u043b")
    barcode: str | None = Field(default=None, description="\u0428\u0442\u0440\u0438\u0445-\u043a\u043e\u0434")
    category_id: int = Field(description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0442\u043e\u0432\u0430\u0440\u0430")
    cost: float | None = Field(default=None, description="\u0426\u0435\u043d\u0430 \u043f\u0440\u043e\u0434\u0430\u0436\u0438")
    actual_cost: float | None = Field(default=None, description="\u0421\u0435\u0431\u0435\u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c")
    sale_unit_id: int = Field(description="\u0415\u0434\u0438\u043d\u0438\u0446\u0430 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f \u0434\u043b\u044f \u043f\u0440\u043e\u0434\u0430\u0436\u0438")
    service_unit_id: int = Field(description="\u0415\u0434\u0438\u043d\u0438\u0446\u0430 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f \u0434\u043b\u044f \u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f")
    unit_equals: float | None = Field(default=None, description="\u041e\u0442\u043d\u043e\u0448\u0435\u043d\u0438\u0435 \u0435\u0434.\u0438\u043c\u0437\u0435\u0440\u0435\u043d\u0438\u044f \u0434\u043b\u044f \u043f\u0440\u043e\u0434\u0430\u0436\u0438 \u043a \u0435\u0434.\u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f \u0434\u043b\u044f \u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f")
    critical_amount: float | None = Field(default=None, description="\u041a\u0440\u0438\u0442\u0438\u0447\u043d\u044b\u0439 \u043e\u0441\u0442\u0430\u0442\u043e\u043a")
    desired_amount: float | None = Field(default=None, description="\u0416\u0435\u043b\u0430\u0435\u043c\u044b\u0439 \u043e\u0441\u0442\u0430\u0442\u043e\u043a")
    netto: float | None = Field(default=None, description="\u041c\u0430\u0441\u0441\u0430 \u043d\u0435\u0442\u0442\u043e")
    brutto: float | None = Field(default=None, description="\u041c\u0430\u0441\u0441\u0430 \u0431\u0440\u0443\u0442\u0442\u043e")
    comment: str | None = Field(default=None, description="\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439")
    tax_variant: int | None = Field(default=None, description="\u0421\u0438\u0441\u0442\u0435\u043c\u0430 \u043d\u0430\u043b\u043e\u0433\u043e\u043e\u0431\u043b\u043e\u0436\u0435\u043d\u0438\u044f")
    vat_id: int | None = Field(default=None, description="\u041d\u0414\u0421")
    correction_rules: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0430\u0441\u0441\u0438\u0432 \u043f\u0440\u0430\u0432\u0438\u043b \u043f\u0435\u0440\u0435\u0441\u0447\u0435\u0442\u0430 \u0435\u0434\u0438\u043d\u0438\u0446 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f (\u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c, \u0435\u0441\u043b\u0438 \u043f\u043e \u0442\u043e\u0432\u0430\u0440\u0443 \u0435\u0441\u0442\u044c \u0441\u043a\u043b\u0430\u0434\u0441\u043a\u0438\u0435 \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438\u0438)")


class GoodsSearchResponse200DataTypes(BaseModel):
    """Пример запроса на получение списка
    Схема спеки: Root Type for goods_search_response200_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: list[dict[str, Any]] | None = Field(default=None, alias="data", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u0441 \u043e\u0431\u044a\u0435\u043a\u0442\u0430\u043c\u0438 \u0434\u0430\u043d\u043d\u044b\u0445")
    meta: dict[str, Any] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u0441\u043e\u0434\u0435\u0440\u0436\u0438\u0442 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043d\u0430\u0439\u0434\u0435\u043d\u043d\u044b\u0445 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0439)")


class GroupGroupidClientsResponseDataTypes(BaseModel):
    """Получить сетевого клиента по номеру телефона
    Схема спеки: Root Type for group_groupid_clients_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: dict[str, Any] | None = Field(default=None, alias="data", description="\u041e\u0431\u044a\u0435\u043a\u0442 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class GroupsResponseDataTypes(BaseModel):
    """Получение доступных пользователю сетей
    Схема спеки: Root Type for groups_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: list[dict[str, Any]] | None = Field(default=None, alias="data", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")


class I18nLangInfoDataTypes(BaseModel):
    """Интернационализация вормы бронирования.
    Схема спеки: Root Type for i18n_lang_info
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    param_404: dict[str, Any] | None = Field(default=None, alias="404")
    action: dict[str, Any] | None = Field(default=None)
    tips: dict[str, Any] | None = Field(default=None)
    payment_status: dict[str, Any] | None = Field(default=None, alias="payment-status")
    user_data_form: dict[str, Any] | None = Field(default=None, alias="user-data-form")
    and_: str | None = Field(default=None, alias="and")
    terms_of_agreement: str | None = Field(default=None, alias="terms-of-agreement")
    data_processing: str | None = Field(default=None, alias="data-processing")
    license_agreement: str | None = Field(default=None, alias="license-agreement")
    personal_data: str | None = Field(default=None, alias="personal-data")
    buy_for: str | None = Field(default=None, alias="buy-for")
    group_booking: dict[str, Any] | None = Field(default=None)
    geo: dict[str, Any] | None = Field(default=None)
    tooltips: dict[str, Any] | None = Field(default=None)
    prepaid: dict[str, Any] | None = Field(default=None)
    back: str | None = Field(default=None)
    back_city: str | None = Field(default=None, alias="backCity")
    back_filials: str | None = Field(default=None, alias="backFilials")
    back_record_type: str | None = Field(default=None, alias="backRecordType")
    filials: str | None = Field(default=None)
    my_profile: str | None = Field(default=None)
    about_us: str | None = Field(default=None)
    record: dict[str, Any] | None = Field(default=None)
    at: str | None = Field(default=None)
    on: str | None = Field(default=None)
    h: str | None = Field(default=None)
    m: str | None = Field(default=None)
    from_: str | None = Field(default=None, alias="from")
    dist_m: str | None = Field(default=None)
    dist_km: str | None = Field(default=None)
    yesterday: str | None = Field(default=None)
    today: str | None = Field(default=None)
    tomorrow: str | None = Field(default=None)
    close: str | None = Field(default=None, alias="Close")
    yes: str | None = Field(default=None, alias="Yes")
    no: str | None = Field(default=None, alias="No")
    refresh: str | None = Field(default=None)
    online_record_disabled: str | None = Field(default=None)
    online_record_disabled_long_text: str | None = Field(default=None)
    address: dict[str, Any] | None = Field(default=None)
    common: dict[str, Any] | None = Field(default=None)
    notification: dict[str, Any] | None = Field(default=None)
    header: dict[str, Any] | None = Field(default=None)
    loyalty: dict[str, Any] | None = Field(default=None)
    save: str | None = Field(default=None)
    proceed: str | None = Field(default=None)
    profile: dict[str, Any] | None = Field(default=None)
    registration: dict[str, Any] | None = Field(default=None)
    menu: dict[str, Any] | None = Field(default=None)
    footer: dict[str, Any] | None = Field(default=None)
    city: dict[str, Any] | None = Field(default=None)
    company: dict[str, Any] | None = Field(default=None)
    steps: dict[str, Any] | None = Field(default=None)
    master: dict[str, Any] | None = Field(default=None)
    cart: dict[str, Any] | None = Field(default=None)
    reviews: dict[str, Any] | None = Field(default=None)
    date: dict[str, Any] | None = Field(default=None)
    time: dict[str, Any] | None = Field(default=None)
    service: dict[str, Any] | None = Field(default=None)
    confirm: dict[str, Any] | None = Field(default=None)
    login: dict[str, Any] | None = Field(default=None)
    jan: str | None = Field(default=None, alias="Jan")
    feb: str | None = Field(default=None, alias="Feb")
    march: str | None = Field(default=None, alias="March")
    mar: str | None = Field(default=None, alias="Mar")
    apr: str | None = Field(default=None, alias="Apr")
    may: str | None = Field(default=None, alias="May")
    jun: str | None = Field(default=None, alias="Jun")
    jul: str | None = Field(default=None, alias="Jul")
    aug: str | None = Field(default=None, alias="Aug")
    sep: str | None = Field(default=None, alias="Sep")
    oct: str | None = Field(default=None, alias="Oct")
    nov: str | None = Field(default=None, alias="Nov")
    dec: str | None = Field(default=None, alias="Dec")
    activity: dict[str, Any] | None = Field(default=None)
    button: dict[str, Any] | None = Field(default=None)
    landscape: str | None = Field(default=None)


class Image2(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float = Field(alias="id", description="id \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f")
    path: str = Field(description="\u041f\u0443\u0442\u044c \u043a \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044e")
    width: float = Field(description="\u0428\u0438\u0440\u0438\u043d\u0430 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f")
    height: float = Field(description="\u0412\u044b\u0441\u043e\u0442\u0430 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f")
    type_: str = Field(alias="type", description="\u0422\u0438\u043f \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f")
    image_group_id: float = Field(description="Id \u0433\u0440\u0443\u043f\u043f\u044b \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0439")
    version: str = Field(description="\u0412\u0435\u0440\u0441\u0438\u044f \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f")


class KkmTransactionsPrintResponseDataType(BaseModel):
    """Напечатать чек
    Схема спеки: Root Type for kkm_transactions_print_response_data_type
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: dict[str, Any] | None = Field(default=None, alias="data", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class KkmTransactionsResponseDataType(BaseModel):
    """Получить транзакции
    Схема спеки: Root Type for kkm_transactions_response_data_type
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: list[dict[str, Any]] | None = Field(default=None, alias="data", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: dict[str, Any] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u0441\u043e\u0434\u0435\u0440\u0436\u0438\u0442 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043d\u0430\u0439\u0434\u0435\u043d\u043d\u044b\u0445 \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u0439)")


class Label(BaseModel):
    """Схема спеки: Объект модели "Категория"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438.")
    title: str | None = Field(default=None, description="\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438.")
    color: str | None = Field(default=None, description="\u0426\u0432\u0435\u0442 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 (#rrggbb).")


class LabelsClientsResponse200DataTypes(BaseModel):
    """Клиентские категории филиала
    Схема спеки: Root Type for labels_clients_response200_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: list[dict[str, Any]] | None = Field(default=None, alias="data", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u0441 \u043e\u0431\u044a\u0435\u043a\u0442\u0430\u043c\u0438 \u0434\u0430\u043d\u043d\u044b\u0445")
    meta: dict[str, Any] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u0441\u043e\u0434\u0435\u0440\u0436\u0438\u0442 \u043d\u043e\u043c\u0435\u0440 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b \u0438 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043d\u0430\u0439\u0434\u0435\u043d\u043d\u044b\u0445 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0439)")


class LabelsCreateResponse200DataTypes(BaseModel):
    """Создание категории
    Схема спеки: Root Type for labels_create_response200_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: dict[str, Any] | None = Field(default=None, alias="data", description="\u041e\u0431\u044a\u0435\u043a\u0442 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class LabelsUpdateRequestDataTypes(BaseModel):
    """Обновить категорию
    Схема спеки: Root Type for labels_update_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    title: str | None = Field(default=None, description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438")
    color: str | None = Field(default=None, description="\u0426\u0432\u0435\u0442 \u043c\u0435\u0442\u043a\u0438 \u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435 #RRGGBB")
    entity: float | None = Field(default=None, description="\u041e\u0431\u044a\u0435\u043a\u0442 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 (1 - \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f \u0434\u043b\u044f \u043a\u043b\u0438\u0435\u043d\u0442\u043e\u0432, 2 - \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f \u0434\u043b\u044f \u0437\u0430\u043f\u0438\u0441\u0435\u0439)")
    icon: str | None = Field(default=None, description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0438\u043a\u043e\u043d\u043a\u0438")


class LicenseOption2(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float = Field(alias="id", description="id \u043e\u043f\u0446\u0438\u0438")
    title: str = Field(description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043e\u043f\u0446\u0438\u0438")


class LoyaltyAbonementsResponseDataTypes(BaseModel):
    """Получить список абонементов клиента
    Схема спеки: Root Type for loyalty_abonements_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: list[dict[str, Any]] | None = Field(default=None, alias="data", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: dict[str, Any] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u0441\u043e\u0434\u0435\u0440\u0436\u0438\u0442 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043d\u0430\u0439\u0434\u0435\u043d\u043d\u044b\u0445 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u043e\u0432)")


class LoyaltyAbonementsTypeSearchResponseDataTypes(BaseModel):
    """Получить список доступных типов абонементов
    Схема спеки: Root Type for loyalty_abonements_type_search_reaponse_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: list[dict[str, Any]] | None = Field(default=None, alias="data", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u0441 \u043e\u0431\u044a\u0435\u043a\u0442\u0430\u043c\u0438 \u0434\u0430\u043d\u043d\u044b\u0445")
    meta: dict[str, Any] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u0441\u043e\u0434\u0435\u0440\u0436\u0438\u0442 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043d\u0430\u0439\u0434\u0435\u043d\u043d\u044b\u0445 \u0442\u0438\u043f\u043e\u0432 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u043e\u0432)")


class LoyaltyCard2(BaseModel):
    """Карта лояльности
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043a\u0430\u0440\u0442\u044b")
    balance: float | None = Field(default=None, description="\u0411\u0430\u043b\u0430\u043d\u0441 \u043a\u0430\u0440\u0442\u044b")
    points: float | None = Field(default=None, description="\u041e\u0447\u043a\u0438")
    paid_amount: float | None = Field(default=None, description="\u0421\u0443\u043c\u043c\u0430 \\\"\u041e\u043f\u043b\u0430\u0447\u0435\u043d\u043e\\\"")
    sold_amount: float | None = Field(default=None, description="\u0421\u0443\u043c\u043c\u0430 \\\"\u041f\u0440\u043e\u0434\u0430\u043d\u043e\\\"")
    visits_count: float | None = Field(default=None, description="\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0432\u0438\u0437\u0438\u0442\u043e\u0432")
    number: str | None = Field(default=None, description="\u041d\u043e\u043c\u0435\u0440 \u043a\u0430\u0440\u0442\u044b")
    type_id: float | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0442\u0438\u043f\u0430 \u043a\u0430\u0440\u0442\u044b")
    salon_group_id: float | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0441\u0435\u0442\u0438")
    max_discount_percent: float | None = Field(default=None, description="\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u044b\u0439 \u043f\u0440\u043e\u0446\u0435\u043d\u0442 \u0441\u043a\u0438\u0434\u043a\u0438")
    max_discount_amount: float | None = Field(default=None, description="\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0444\u0438\u043a\u0441\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u0430\u044f \u0441\u043a\u0438\u0434\u043a\u0430")


class LoyaltyCardType2(BaseModel):
    """Тип карты лояльности
    Схема спеки: Root Type for LoyaltyCardType
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0442\u0438\u043f\u0430 \u043a\u0430\u0440\u0442\u044b")
    title: str | None = Field(default=None, description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0442\u0438\u043f\u0430 \u043a\u0430\u0440\u0442\u044b")


class LoyaltyCardsRequestDataTypes(BaseModel):
    """Выдать карту лояльности
    Схема спеки: Root Type for loyalty_cards_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    loyalty_card_number: str | None = Field(default=None, description="\u041d\u043e\u043c\u0435\u0440 \u043a\u0430\u0440\u0442\u044b \u043b\u043e\u044f\u043b\u044c\u043d\u043e\u0441\u0442\u0438")
    loyalty_card_type_id: str | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0442\u0438\u043f\u0430 \u043a\u0430\u0440\u0442\u044b \u043b\u043e\u044f\u043b\u044c\u043d\u043e\u0441\u0442\u0438")
    phone: float | None = Field(default=None, description="\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430 \u043a\u043b\u0438\u0435\u043d\u0442\u0430 \u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435 70001234567")


class LoyaltyCardsResponseDataTypes(BaseModel):
    """Получить список карт клиента
    Схема спеки: Root Type for loyalty_cards_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043a\u0430\u0440\u0442\u044b \u043b\u043e\u044f\u043b\u044c\u043d\u043e\u0441\u0442\u0438")
    balance: float | None = Field(default=None, description="\u0411\u0430\u043b\u0430\u043d\u0441 \u043a\u0430\u0440\u0442\u044b \u043b\u043e\u044f\u043b\u044c\u043d\u043e\u0441\u0442\u0438")
    points: int | None = Field(default=None)
    paid_amount: float | None = Field(default=None, description="\u0421\u0443\u043c\u043c\u0430 \"\u041e\u043f\u043b\u0430\u0447\u0435\u043d\u043e\"")
    sold_amount: float | None = Field(default=None, description="\u0421\u0443\u043c\u043c\u0430 \"\u041f\u0440\u043e\u0434\u0430\u043d\u043e\"")
    visits_count: int | None = Field(default=None, description="\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0432\u0438\u0437\u0438\u0442\u043e\u0432")
    number: str | None = Field(default=None, description="\u041d\u043e\u043c\u0435\u0440 \u043a\u0430\u0440\u0442\u044b")
    type_id: int | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0442\u0438\u043f\u0430 \u043a\u0430\u0440\u0442\u044b \u043b\u043e\u044f\u043b\u044c\u043d\u043e\u0441\u0442\u0438")
    salon_group_id: int | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0441\u0435\u0442\u0438, \u0433\u0434\u0435 \u0441\u043e\u0437\u0434\u0430\u043d\u0430 \u043a\u0430\u0440\u0442\u0430")
    type_: dict[str, Any] | None = Field(default=None, alias="type", description="\u041e\u0431\u044a\u0435\u043a\u0442, \u0441\u043e\u0434\u0435\u0440\u0436\u0430\u0449\u0438\u0439 \u0432 \u0441\u0435\u0431\u0435 \u043f\u043e\u043b\u044f \"id\" \u0438 \"title\": \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0442\u0438\u043f\u0430 \u043a\u0430\u0440\u0442\u044b \u0438 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0442\u0438\u043f\u0430 \u043a\u0430\u0440\u0442\u044b, \u0441\u043e\u043e\u0442\u0432\u0435\u0441\u0442\u0432\u0435\u043d\u043d\u043e")
    salon_group: dict[str, Any] | None = Field(default=None, description="\u041e\u0431\u044a\u0435\u043a\u0442, \u0441\u043e\u0434\u0435\u0440\u0436\u0430\u0449\u0438\u0439 \u0432 \u0441\u0435\u0431\u0435 \u043f\u043e\u043b\u044f \"id\" \u0438 \"title\": \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0441\u0435\u0442\u0438, \u0433\u0434\u0435 \u0441\u043e\u0437\u0434\u0430\u043d \u0442\u0438\u043f \u043a\u0430\u0440\u0442\u044b \u0438 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u044d\u0442\u043e\u0439 \u0441\u0435\u0442\u0438")
    programs: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0430\u0441\u0441\u0438\u0432 \u0441 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0435\u0439 \u043e\u0431 \u0430\u043a\u0446\u0438\u044f\u0445, \u043f\u0440\u0438\u0432\u044f\u0437\u0430\u043d\u043d\u044b\u0445 \u043a \u043a\u0430\u0440\u0442\u0435 \u043b\u043e\u044f\u043b\u044c\u043d\u043e\u0441\u0442\u0438")


class LoyaltyCertificateTypeSearchResponseDataTypes(BaseModel):
    """Получить список доступных типов сертификатов
    Схема спеки: Root Type for loyalty_certificate_type_search_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: list[dict[str, Any]] | None = Field(default=None, alias="data", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: dict[str, Any] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u0441\u043e\u0434\u0435\u0440\u0436\u0438\u0442 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043d\u0430\u0439\u0434\u0435\u043d\u043d\u044b\u0445 \u0442\u0438\u043f\u043e\u0432 \u0441\u0435\u0440\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0432)")


class LoyaltyCertificatesResponseDataTypes(BaseModel):
    """Получить сертификаты
    Схема спеки: Root Type for loyalty_certificates_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: list[dict[str, Any]] | None = Field(default=None, alias="data", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: dict[str, Any] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u0441\u043e\u0434\u0435\u0440\u0436\u0438\u0442 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043d\u0430\u0439\u0434\u0435\u043d\u043d\u044b\u0445 \u0441\u0435\u0440\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0432)")


class LoyaltyEntityAttendanceItem2(BaseModel):
    """Сущность, к которой применяется акция (при выборочном применении)
    Схема спеки: Root Type for LoyaltyEntityAttendanceItem
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0441\u0432\u044f\u0437\u0430\u043d\u043d\u043e\u0439 \u0441\u0443\u0449\u043d\u043e\u0441\u0442\u0438")
    title: str | None = Field(default=None, description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u0432\u044f\u0437\u0430\u043d\u043d\u043e\u0439 \u0441\u0443\u0449\u043d\u043e\u0441\u0442\u0438")
    is_service: bool | None = Field(default=None, description="\u0424\u043b\u0430\u0433: true - \u0443\u0441\u043b\u0443\u0433\u0430/\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f \u0443\u0441\u043b\u0443\u0433, false - \u0442\u043e\u0432\u0430\u0440/\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f \u0442\u043e\u0432\u0430\u0440\u043e\u0432")
    is_category: bool | None = Field(default=None, description="\u0424\u043b\u0430\u0433: true - \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f \u0443\u0441\u043b\u0443\u0433/\u0442\u043e\u0432\u0430\u0440\u043e\u0432, false - \u0443\u0441\u043b\u0443\u0433\u0430/\u0442\u043e\u0432\u0430\u0440")


class LoyaltyGenerateCode200DataOption2(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    code: str = Field(description="\u0421\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u043a\u043e\u0434")


class LoyaltyNotificationMessageTemplate2(BaseModel):
    """Шаблон уведомлений лояльности
    Схема спеки: Root Type for LoyaltyNotificationMessageTemplate
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0448\u0430\u0431\u043b\u043e\u043d\u0430")
    type_: Literal["big", "mid", "small", "custom"] | None = Field(default=None, alias="type", description="\u0412\u0430\u0440\u0438\u0430\u043d\u0442 \u0448\u0430\u0431\u043b\u043e\u043d\u0430")
    body: str | None = Field(default=None, description="\u0422\u0435\u043a\u0441\u0442 \u0448\u0430\u0431\u043b\u043e\u043d\u0430")
    message_type: Literal["loyalty_discount_expiration", "loyalty_cashback_expiration", "loyalty_discount_increased", "loyalty_discount_decreased", "loyalty_card_created", "loyalty_card_withdraw", "loyalty_withdraw_cancelled", "loyalty_card_manual", "loyalty_card_manual_withdraw", "loyalty_card_cashback", "loyalty_card_cashback_cancelled", "loyalty_card_income", "loyalty_discount_changed", "loyalty_cashback_changed", "loyalty_settings_abonement_notification"] | None = Field(default=None, description="\u0422\u0438\u043f \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f")


class LoyaltyNotificationMessageTemplateRequest2(BaseModel):
    """Тело запроса на привязку шаблона уведомления лояльности
    Схема спеки: Root Type for LoyaltyNotificationMessageTemplateRequest
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    type_: Literal["none", "big", "mid", "small", "custom"] | None = Field(default=None, alias="type", description="\u0412\u0430\u0440\u0438\u0430\u043d\u0442 \u0448\u0430\u0431\u043b\u043e\u043d\u0430")
    body: str | None = Field(default=None, description="\u0422\u0435\u043a\u0441\u0442 \u0448\u0430\u0431\u043b\u043e\u043d\u0430 (\u0442\u043e\u043b\u044c\u043a\u043e \u0434\u043b\u044f \u0432\u0430\u0440\u0438\u0430\u043d\u0442\u0430 \"\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u0441\u043a\u0438\u0439\")")


class LoyaltyProgramRule2(BaseModel):
    """Правило для акции лояльности
    Схема спеки: Root Type for LoyaltyProgramRule
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043f\u0440\u0430\u0432\u0438\u043b\u0430")
    parameter: int | None = Field(default=None, description="\u041f\u043e\u0440\u043e\u0433\u043e\u0432\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043f\u0440\u0430\u0432\u0438\u043b\u0430 (0 \u0434\u043b\u044f \u0444\u0438\u043a\u0441\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0445 \u0442\u0438\u043f\u043e\u0432 \u0430\u043a\u0446\u0438\u0439)")
    value: float | None = Field(default=None, description="\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0441\u043a\u0438\u0434\u043a\u0438\u0438 \u0438\u043b\u0438 \u0431\u043e\u043d\u0443\u0441\u0430")
    loyalty_program_id: int | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0430\u043a\u0446\u0438\u0438 \u043b\u043e\u044f\u043b\u044c\u043d\u043e\u0441\u0442\u0438")
    loyalty_type_id: int | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0442\u0438\u043f\u0430 \u0430\u043a\u0446\u0438\u0438 \u043b\u043e\u044f\u043b\u044c\u043d\u043e\u0441\u0442\u0438")
    service_id: int | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0443\u0441\u043b\u0443\u0433\u0438 (\u0442\u043e\u043b\u044c\u043a\u043e \u0434\u043b\u044f \u0430\u043a\u0446\u0438\u0438 \"\u0421\u043a\u0438\u0434\u043a\u0430 \u043f\u043e \u0443\u0441\u043b\u043e\u0432\u0438\u044e\")")


class LoyaltyProgramRuleRequest2(BaseModel):
    """Тело запроса на изменение правила для акции лояльности
    Схема спеки: Root Type for LoyaltyProgramRuleRequest
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    parameter: int | None = Field(default=None, description="\u041f\u043e\u0440\u043e\u0433\u043e\u0432\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043f\u0440\u0430\u0432\u0438\u043b\u0430 (0 \u0434\u043b\u044f \u0444\u0438\u043a\u0441\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0445 \u0442\u0438\u043f\u043e\u0432 \u0430\u043a\u0446\u0438\u0439)")
    value: float | None = Field(default=None, description="\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0441\u043a\u0438\u0434\u043a\u0438\u0438 \u0438\u043b\u0438 \u0431\u043e\u043d\u0443\u0441\u0430")
    service_id: int | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0443\u0441\u043b\u0443\u0433\u0438 (\u0442\u043e\u043b\u044c\u043a\u043e \u0434\u043b\u044f \u0430\u043a\u0446\u0438\u0438 \"\u0421\u043a\u0438\u0434\u043a\u0430 \u043f\u043e \u0443\u0441\u043b\u043e\u0432\u0438\u044e\")")


class LoyaltyTransaction2(BaseModel):
    """Транзакция лояльности
    Схема спеки: Root Type for LoyaltyTransaction
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: list[dict[str, Any]] | None = Field(default=None, alias="data", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: dict[str, Any] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u0441\u043e\u0434\u0435\u0440\u0436\u0438\u0442 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432 \u0432 \u043e\u0442\u0432\u0435\u0442\u0435)")


class MasterRecordReviewPostRequest(BaseModel):
    """Запрос отправки отзыва
    Схема спеки: Root Type for master_record_review_post_request
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    rating: int = Field(description="\u041e\u0446\u0435\u043d\u043a\u0430, \u0432\u044b\u0441\u0442\u0430\u0432\u043b\u044f\u0435\u043c\u0430\u044f \u0437\u0430 \u043e\u0442\u0437\u044b\u0432 (\u043a\u043e\u043b-\u0432\u043e \u0437\u0432\u0435\u0437\u0434 \u043e\u0442 1 \u0434\u043e 5)")
    text: str | None = Field(default=None, description="\u0422\u0435\u043a\u0441\u0442 \u043e\u0442\u0437\u044b\u0432\u0430")
    tips_amount: float | None = Field(default=None, description="\u0421\u0443\u043c\u043c\u0430 \u0447\u0430\u0435\u0432\u044b\u0445")
    redirect_prefix: str | None = Field(default=None, description="\u041f\u0440\u0435\u0444\u0438\u043a\u0441\u043d\u0430\u044f \u0447\u0430\u0441\u0442\u044c url, \u043d\u0430 \u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u0431\u0443\u0434\u0435\u0442 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d \u0440\u0435\u0434\u0438\u0440\u0435\u043a\u0442 \u043f\u043e\u0441\u043b\u0435 \u0432\u043e\u0437\u0432\u0440\u0430\u0442\u0430 \u0441 \u0444\u043e\u0440\u043c\u044b \u043e\u043f\u043b\u0430\u0442\u044b")


class MasterRecordReviewResponseDataTypes(BaseModel):
    """Получение статуса формы отзыва
    Схема спеки: Root Type for master_record_review_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: dict[str, Any] | None = Field(default=None, alias="data", description="\u041e\u0431\u044a\u0435\u043a\u0442 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class MasterScheduleDayContainer(BaseModel):
    """Данные по существующему в филиале графику работы сотрудника.
    Схема спеки: Объект модели "Расписание сотрудника"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    staff_id: float | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430.")
    date: str | None = Field(default=None, description="\u0414\u0430\u0442\u0430 \u0432 \u0440\u0430\u043c\u043a\u0430\u0445 \u0433\u0440\u0430\u0444\u0438\u043a\u0430 \u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435 Y-m-d.")
    slots: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0430\u0441\u0441\u0438\u0432 \u0438\u043d\u0442\u0435\u0440\u0432\u0430\u043b\u043e\u0432 \u0432\u0440\u0435\u043c\u0435\u043d\u0438, \u043a\u043e\u0433\u0434\u0430 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a \u0440\u0430\u0431\u043e\u0442\u0430\u0435\u0442.")
    busy_intervals: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0430\u0441\u0441\u0438\u0432 \u0438\u043d\u0442\u0435\u0440\u0432\u0430\u043b\u043e\u0432 \u0432\u0440\u0435\u043c\u0435\u043d\u0438, \u0437\u0430\u043d\u044f\u0442\u043e\u0433\u043e \u0437\u0430\u043f\u0438\u0441\u044f\u043c\u0438 \u0438\u043b\u0438 \u0441\u043e\u0431\u044b\u0442\u0438\u044f\u043c\u0438.")
    off_day_type: float | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0442\u0438\u043f\u0430 \u043d\u0435\u0440\u0430\u0431\u043e\u0447\u0435\u0433\u043e \u0434\u043d\u044f, \u0441\u043e\u0437\u0434\u0430\u043d\u043d\u043e\u0433\u043e \u0432 \u0444\u0438\u043b\u0438\u0430\u043b\u0435.")


class MasterServiceLink2(BaseModel):
    """Схема спеки: Объект модели "Сотрудник, оказывающий услугу"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    service_id: float | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0443\u0441\u043b\u0443\u0433\u0438.")
    master_id: float | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430.")
    length: float | None = Field(default=None, description="\u0414\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u043e\u043a\u0430\u0437\u0430\u043d\u0438\u044f \u0443\u0441\u043b\u0443\u0433\u0438 \u0443\u043a\u0430\u0437\u0430\u043d\u043d\u044b\u043c \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u043e\u043c \u0432 \u0441\u0435\u043a\u0443\u043d\u0434\u0430\u0445.")
    technological_card_id: float | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0442\u0435\u0445\u043d\u043e\u043b\u043e\u0433\u0438\u0447\u0435\u0441\u043a\u043e\u0439 \u043a\u0430\u0440\u0442\u044b.")


class NotificationSettingsNotificationTypesDataType(BaseModel):
    """Настройки уведомлений филиала
    Схема спеки: Root Type for notification_settings_notification_types_data_type
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f")
    data_: list[dict[str, Any]] | None = Field(default=None, alias="data", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432")
    meta: dict[str, Any] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u0441\u043e\u0434\u0435\u0440\u0436\u0438\u0442 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432)")


class NotificationSettingsUsersDataType(BaseModel):
    """Получить настройки уведомлений пользователя
    Схема спеки: Root Type for notification_settings_users_data_type
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f")
    data_: dict[str, Any] | None = Field(default=None, alias="data", description="\u041e\u0431\u044a\u0435\u043a\u0442 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class NotificationSettingsUsersRequestDataType(BaseModel):
    """Изменить настройки PUSH-уведомлений пользователя
    Схема спеки: Root Type for notification_settings_users_request_data_type
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    notification_types: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0430\u0441\u0441\u0438\u0432 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432")


class Position(BaseModel):
    """Данные существующей должности в сети.
    Схема спеки: Объект модели "Должность"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0434\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u0438.")
    chain_id: float | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0441\u0435\u0442\u0438, \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u0441\u043e\u0437\u0434\u0430\u043d\u0430 \u0434\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c.")
    title: str | None = Field(default=None, description="\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0434\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u0438.")
    description: str | None = Field(default=None, description="\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0434\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u0438.")
    services_binding_type: Literal[0, 2] | None = Field(default=None, description="\u0422\u0438\u043f \u043f\u0440\u0438\u0432\u044f\u0437\u043a\u0438 \u0443\u0441\u043b\u0443\u0433 \u043a \u0434\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u0438: `0`: - \u043f\u0440\u0438\u0432\u044f\u0437\u043a\u0430 \u043e\u0442\u043a\u043b\u044e\u0447\u0435\u043d\u0430; `2`: - \u0436\u0435\u0441\u0442\u043a\u0430\u044f \u043f\u0440\u0438\u0432\u044f\u0437\u043a\u0430.")
    rules_required_fields: list[str] | None = Field(default=None, description="\u041d\u0430\u0431\u043e\u0440 \u043f\u043e\u043b\u0435\u0439, \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u044b\u0445 \u0434\u043b\u044f \u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f \u043f\u0435\u0440\u0435\u0434 \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u044c\u044e \u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430 \u043d\u0430 \u0434\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c.")
    only_chain_appointment: bool | None = Field(default=None, description="\u0414\u043e\u0441\u0442\u0443\u043f\u043d\u043e\u0441\u0442\u044c \u043f\u0440\u0438\u0432\u044f\u0437\u043a\u0438 \u0434\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u0438 \u043a \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0443 \u0442\u043e\u043b\u044c\u043a\u043e \u0432 \u0441\u0435\u0442\u0438.")


class PositionCompact(BaseModel):
    """Данные существующей должности в сети.
    Схема спеки: Объект модели "Должность"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0434\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u0438.")
    title: str | None = Field(default=None, description="\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0434\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u0438.")


class RecordCompanyidResponse201DataTypes(BaseModel):
    """Изменить запись
    Схема спеки: Root Type for record_companyid_response201_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0433\u043e \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: dict[str, Any] | None = Field(default=None, alias="data", description="\u041e\u0431\u044a\u0435\u043a\u0442 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class RecordCompanyidResponseDataTypes(BaseModel):
    """Получить запись
    Схема спеки: Root Type for record_companyid_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: dict[str, Any] | None = Field(default=None, alias="data", description="\u041e\u0431\u044a\u0435\u043a\u0442 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class RecordsCompanyidRequestDataTypes(BaseModel):
    """Создать новую запись
    Схема спеки: Root Type for records_companyid_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    staff_id: float | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430")
    services: list[dict[str, Any]] | None = Field(default=None, description="\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0443\u0441\u043b\u0443\u0433 (id, \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c, \u0441\u043a\u0438\u0434\u043a\u0430)")
    client_: dict[str, Any] | None = Field(default=None, alias="client", description="\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043a\u043b\u0438\u0435\u043d\u0442\u0430 (\u0442\u0435\u043b\u0435\u0444\u043e\u043d, \u0438\u043c\u044f, email)")
    save_if_busy: bool | None = Field(default=None, description="\u0421\u043e\u0445\u0440\u0430\u043d\u044f\u0442\u044c \u043b\u0438 \u0437\u0430\u043f\u0438\u0441\u044c \u0435\u0441\u043b\u0438 \u0432\u0440\u0435\u043c\u044f \u0437\u0430\u043d\u044f\u0442\u043e \u0438\u043b\u0438 \u043d\u0435\u0440\u0430\u0431\u043e\u0447\u0435\u0435, \u0438\u043b\u0438 \u0432\u044b\u0434\u0430\u0442\u044c \u043e\u0448\u0438\u0431\u043a\u0443")
    datetime: str | None = Field(default=None, description="\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0437\u0430\u043f\u0438\u0441\u0438")
    seance_length: float | None = Field(default=None, description="\u0414\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u0438 \u0432 \u0441\u0435\u043a\u0443\u043d\u0434\u0430\u0445")
    send_sms: bool | None = Field(default=None, description="\u041e\u0442\u043f\u0440\u0430\u0432\u043b\u044f\u0442\u044c \u043b\u0438 \u0441\u043c\u0441 \u0441 \u0434\u0435\u0442\u0430\u043b\u044f\u043c\u0438 \u0437\u0430\u043f\u0438\u0441\u0438 \u043a\u043b\u0438\u0435\u043d\u0442\u0443")
    comment: str | None = Field(default=None, description="\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 \u043a \u0437\u0430\u043f\u0438\u0441\u0438")
    sms_remain_hours: float | None = Field(default=None, description="\u0417\u0430 \u0441\u043a\u043e\u043b\u044c\u043a\u043e \u0447\u0430\u0441\u043e\u0432 \u0434\u043e \u0432\u0438\u0437\u0438\u0442\u0430 \u0441\u043b\u0435\u0434\u0443\u0435\u0442 \u0432\u044b\u0441\u043b\u0430\u0442\u044c \u0441\u043c\u0441 \u043d\u0430\u043f\u043e\u043c\u0438\u043d\u0430\u043d\u0438\u0435 \u043a\u043b\u0438\u0435\u043d\u0442\u0443 (0 - \u0435\u0441\u043b\u0438 \u043d\u0435 \u043d\u0443\u0436\u043d\u043e)")
    email_remain_hours: float | None = Field(default=None, description="\u0417\u0430 \u0441\u043a\u043e\u043b\u044c\u043a\u043e \u0447\u0430\u0441\u043e\u0432 \u0434\u043e \u0432\u0438\u0437\u0438\u0442\u0430 \u0441\u043b\u0435\u0434\u0443\u0435\u0442 \u0432\u044b\u0441\u043b\u0430\u0442\u044c email \u043d\u0430\u043f\u043e\u043c\u0438\u043d\u0430\u043d\u0438\u0435 \u043a\u043b\u0438\u0435\u043d\u0442\u0443 (0 - \u0435\u0441\u043b\u0438 \u043d\u0435 \u043d\u0443\u0436\u043d\u043e)")
    attendance: float | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0437\u0430\u043f\u0438\u0441\u0438 (2 - \u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c \u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u043b \u0437\u0430\u043f\u0438\u0441\u044c, 1 - \u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c \u043f\u0440\u0438\u0448\u0435\u043b, \u0443\u0441\u043b\u0443\u0433\u0438 \u043e\u043a\u0430\u0437\u0430\u043d\u044b, 0 - \u043e\u0436\u0438\u0434\u0430\u043d\u0438\u0435 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f, -1 - \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c \u043d\u0435 \u043f\u0440\u0438\u0448\u0435\u043b \u043d\u0430 \u0432\u0438\u0437\u0438\u0442)")
    api_id: str | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0432\u043d\u0435\u0448\u043d\u0435\u0439 \u0441\u0438\u0441\u0442\u0435\u043c\u044b")
    custom_color: str | None = Field(default=None, description="\u0426\u0432\u0435\u0442 \u0437\u0430\u043f\u0438\u0441\u0438")
    record_labels: list[str] | None = Field(default=None, description="\u041c\u0430\u0441\u0441\u0438\u0432 \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440\u043e\u0432 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0439 \u0437\u0430\u043f\u0438\u0441\u0438")
    client_agreements: dict[str, Any] | None = Field(default=None, description="\u042e\u0440\u0438\u0434\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u0441\u043e\u0433\u043b\u0430\u0448\u0435\u043d\u0438\u044f \u043a\u043b\u0438\u0435\u043d\u0442\u0430")
    technical_break_duration: float | None = Field(default=None, description="\u0422\u0435\u0445\u043d\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u043f\u0435\u0440\u0435\u0440\u044b\u0432. - \u0421\u0442\u0440\u043e\u0433\u043e \u043a\u0440\u0430\u0442\u043d\u043e 300 (5 \u043c\u0438\u043d\u0443\u0442\u0430\u043c). - \u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 3600 (1 \u0447\u0430\u0441) - \u0415\u0441\u043b\u0438 \u043f\u0435\u0440\u0435\u0434\u0430\u043d `null` \u0438\u043b\u0438 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043d\u0435 \u043f\u0435\u0440\u0435\u0434\u0430\u043d\u043e \u2014 \u0431\u0443\u0434\u0435\u0442 \u0437\u0430\u0434\u0430\u043d \u0441\u043e\u0433\u043b\u0430\u0441\u043d\u043e \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430\u043c \u0432 \u0440\u0430\u0437\u0434\u0435\u043b\u0435 *\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u2192 \u0416\u0443...")
    custom_fields: dict[str, Any] | None = Field(default=None, description="\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u043f\u043e\u043b\u044f \u0437\u0430\u043f\u0438\u0441\u0438")


class RecordsCompanyidResponseDataTypes(BaseModel):
    """Получить список записей
    Схема спеки: Root Type for records_companyid_response_data-types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: list[dict[str, Any]] | None = Field(default=None, alias="data", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: dict[str, Any] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u0441\u043e\u0434\u0435\u0440\u0436\u0438\u0442 \u043d\u043e\u043c\u0435\u0440 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b \u0438 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0437\u0430\u043f\u0438\u0441\u0435\u0439 \u043d\u0430 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435)")


class ReferencesBusinessGroupResponseDataTypes(BaseModel):
    """Получение списка бизнес-типов сгруппированных по группам
    Схема спеки: Root Type for references_business_group_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: list[dict[str, Any]] | None = Field(default=None, alias="data", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: dict[str, Any] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u0441\u043e\u0434\u0435\u0440\u0436\u0438\u0442 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043d\u0430\u0439\u0434\u0435\u043d\u044b\u0445 \u0431\u0438\u0437\u043d\u0435\u0441-\u0442\u0438\u043f\u043e\u0432)")


class ResourceInstance(BaseModel):
    """Схема спеки: Объект модели "Экземпляр Ресурса"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u044d\u043a\u0437\u0435\u043c\u043f\u043b\u044f\u0440\u0430 \u0440\u0435\u0441\u0443\u0440\u0441\u0430.")
    title: str | None = Field(default=None, description="\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u044d\u043a\u0437\u0435\u043c\u043f\u043b\u044f\u0440\u0430 \u0440\u0435\u0441\u0443\u0440\u0441\u0430.")
    resource_id: float | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0440\u0435\u0441\u0443\u0440\u0441\u0430, \u043a \u043a\u043e\u0442\u043e\u0440\u043e\u043c\u0443 \u043f\u0440\u0438\u0432\u044f\u0437\u0430\u043d \u044d\u043a\u0437\u0435\u043c\u043f\u043b\u044f\u0440.")


class ResourcesCompanyidDataTypes(BaseModel):
    """Получение ресурсов в филиале
    Схема спеки: Root Type for resources_companyid_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: list[dict[str, Any]] | None = Field(default=None, alias="data", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u0441 \u043e\u0431\u044a\u0435\u043a\u0442\u0430\u043c\u0438 \u0434\u0430\u043d\u043d\u044b\u0445")
    meta: dict[str, Any] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u0441\u043e\u0434\u0435\u0440\u0436\u0438\u0442 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043d\u0430\u0439\u0434\u0435\u043d\u043d\u044b\u0445 \u0440\u0435\u0441\u0443\u0440\u0441\u043e\u0432)")


class ResponseMetaCountObject(BaseModel):
    """Дополнительная информация о запросе.
    Схема спеки: Объект дополнительной информации о запросе с кол-вом найденных результатов
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    count_: float | None = Field(default=None, alias="count", description="\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043d\u0430\u0439\u0434\u0435\u043d\u043d\u044b\u0445 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u043e\u0432.")


class ResponseMetaDatePaginatorObject(BaseModel):
    """Информация о постраничной навигации, содержащая данные о текущей, следующей и предыдущей страницах.
    Данные отсортированы и разбиты на страницы по датам в убывающем порядке.
    Схема спеки: Объект информации о постраничной навигации, основанной на дате.
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    date_cursor: dict[str, Any] | None = Field(default=None, alias="dateCursor", description="\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u043f\u043e\u0441\u0442\u0440\u0430\u043d\u0438\u0447\u043d\u043e\u0439 \u043d\u0430\u0432\u0438\u0433\u0430\u0446\u0438\u0438.")


class SalaryPayrollCalculation(BaseModel):
    """Схема спеки: Объект начисления заработной платы
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043d\u0430\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u044f.")
    company_id: float | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0444\u0438\u043b\u0438\u0430\u043b\u0430.")
    staff_id: float | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430.")
    amount: float | None = Field(default=None, description="\u0421\u0443\u043c\u043c\u0430 \u043d\u0430\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u044f.")
    status: Literal["draft", "confirmed"] | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u043d\u0430\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u044f.")
    date_create: str | None = Field(default=None, description="\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f \u043d\u0430\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u044f.")
    date_from: str | None = Field(default=None, description="\u0414\u0430\u0442\u0430 \u043d\u0430\u0447\u0430\u043b\u0430 \u043f\u0435\u0440\u0438\u043e\u0434\u0430 \u043d\u0430\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u044f.")
    date_to: str | None = Field(default=None, description="\u0414\u0430\u0442\u0430 \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f \u043f\u0435\u0440\u0438\u043e\u0434\u0430 \u043d\u0430\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u044f.")
    comment: str | None = Field(default=None, description="\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 \u043a \u043d\u0430\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u044e.")


class SalaryPayrollCalculationItemDiscrepancy(BaseModel):
    """Схема спеки: Объект информации о найденном расхождении по позиции начисления зарплаты
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    reason: Literal["new", "deleted", "updated_rule", "updated_sum"] | None = Field(default=None, description="\u0422\u0438\u043f \u0440\u0430\u0441\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u044f.")
    actual_sum: str | None = Field(default=None, description="\u0414\u0435\u0439\u0441\u0442\u0432\u0438\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u0441\u0443\u043c\u043c\u0430 \u0437\u0430\u0440\u043f\u043b\u0430\u0442\u044b.")
    difference_sum: str | None = Field(default=None, description="\u0421\u0443\u043c\u043c\u0430 \u0440\u0430\u0441\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u044f \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0439 \u0438 \u043d\u0430\u0447\u0438\u0441\u043b\u0435\u043d\u043d\u043e\u0439 \u0437\u0430\u0440\u043f\u043b\u0430\u0442\u044b.")


class SalaryPayrollCalculationItemInfoContainer(BaseModel):
    """Схема спеки: Объект информации о применённом правиле расчёта зарплаты
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    criteria_title: str | None = Field(default=None, description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u0440\u0438\u0442\u0435\u0440\u0438\u044f \u0440\u0430\u0441\u0447\u0451\u0442\u0430 \u0437\u0430\u0440\u043f\u043b\u0430\u0442\u044b.")
    param_title: str | None = Field(default=None, description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430 \u0440\u0430\u0441\u0447\u0451\u0442\u0430 \u0437\u0430\u0440\u043f\u043b\u0430\u0442\u044b.")
    scheme_title: str | None = Field(default=None, description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u0445\u0435\u043c\u044b \u0440\u0430\u0441\u0447\u0451\u0442\u0430 \u0437\u0430\u0440\u043f\u043b\u0430\u0442\u044b.")


class SalaryPayrollCalculationItemPaidContainer(BaseModel):
    """Схема спеки: Объект детализации оплат
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    money_sum: str | None = Field(default=None, description="\u0421\u0443\u043c\u043c\u0430, \u043e\u043f\u043b\u0430\u0447\u0435\u043d\u043d\u0430\u044f \u0434\u0435\u043d\u044c\u0433\u0430\u043c\u0438.")
    discount_sum: str | None = Field(default=None, description="\u0421\u0443\u043c\u043c\u0430 \u0441\u043a\u0438\u0434\u043a\u0438.")
    bonus_sum: str | None = Field(default=None, description="\u0421\u0443\u043c\u043c\u0430, \u043e\u043f\u043b\u0430\u0447\u0435\u043d\u043d\u0430\u044f \u0431\u043e\u043d\u0443\u0441\u043d\u044b\u043c\u0438 \u0431\u0430\u043b\u043b\u0430\u043c\u0438.")
    certificate_sum: str | None = Field(default=None, description="\u0421\u0443\u043c\u043c\u0430, \u043e\u043f\u043b\u0430\u0447\u0435\u043d\u043d\u0430\u044f \u043f\u043e\u0434\u0430\u0440\u043e\u0447\u043d\u044b\u043c \u0441\u0435\u0440\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u043c.")
    abonement_sum: str | None = Field(default=None, description="\u0421\u0443\u043c\u043c\u0430, \u043e\u043f\u043b\u0430\u0447\u0435\u043d\u043d\u0430\u044f \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u043e\u043c.")
    deposit_sum: str | None = Field(default=None, description="\u0421\u0443\u043c\u043c\u0430, \u043e\u043f\u043b\u0430\u0447\u0435\u043d\u043d\u0430\u044f \u0441 \u043b\u0438\u0447\u043d\u043e\u0433\u043e \u0441\u0447\u0451\u0442\u0430.")


class SalaryPayrollCalculationItemTargetCalculation(BaseModel):
    """Схема спеки: Объект расчёта начисления заработной платы по отдельной позиции
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    type_slug: Literal["fix", "percent"] | None = Field(default=None, description="\u0422\u0438\u043f \u0440\u0430\u0441\u0447\u0451\u0442\u0430.")
    value: float | None = Field(default=None, description="\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435.")
    description: str | None = Field(default=None, description="\u041f\u043e\u0434\u0440\u043e\u0431\u043d\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0440\u0430\u0441\u0447\u0451\u0442\u0430.")


class SalaryPayrollCalculationItemTargetContainer(BaseModel):
    """Схема спеки: Объект детализации позиции начисления заработной платы
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    target_type_slug: Literal["service", "good"] | None = Field(default=None, description="\u0422\u0438\u043f \u0434\u0435\u0442\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u0438.")
    target_id: float | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0434\u0435\u0442\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u0438 \u043f\u043e\u0437\u0438\u0446\u0438\u0438.")
    title: str | None = Field(default=None, description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0434\u0435\u0442\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u0438 \u043f\u043e\u0437\u0438\u0446\u0438\u0438.")
    cost: str | None = Field(default=None, description="\u0411\u0430\u0437\u043e\u0432\u0430\u044f \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0434\u0435\u0442\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u0438 \u043f\u043e\u0437\u0438\u0446\u0438\u0438.")
    net_cost: str | None = Field(default=None, description="\u0411\u0430\u0437\u043e\u0432\u0430\u044f \u0441\u0435\u0431\u0435\u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0434\u0435\u0442\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u0438 \u043f\u043e\u0437\u0438\u0446\u0438\u0438.")
    salary_sum: str | None = Field(default=None, description="\u041f\u043e\u043b\u043d\u0430\u044f \u0441\u0443\u043c\u043c\u0430 \u043d\u0430\u0447\u0438\u0441\u043b\u0435\u043d\u043d\u043e\u0439 \u0437\u0430\u0440\u043f\u043b\u0430\u0442\u044b \u0432 \u0440\u0430\u043c\u043a\u0430\u0445 \u0434\u0435\u0442\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u0438 \u043f\u043e\u0437\u0438\u0446\u0438\u0438.")
    salary_promotion_sum: str | None = Field(default=None, description="\u0421\u0443\u043c\u043c\u0430 \u043d\u0430\u0447\u0438\u0441\u043b\u0435\u043d\u043d\u043e\u0439 \u0437\u0430\u0440\u043f\u043b\u0430\u0442\u044b \u043e\u0442 \u043f\u0440\u0438\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u0430\u043a\u0446\u0438\u0439 \u0432 \u0440\u0430\u043c\u043a\u0430\u0445 \u0434\u0435\u0442\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u0438 \u043f\u043e\u0437\u0438\u0446\u0438\u0438.")
    salary_calculation: dict[str, Any] | None = Field(default=None, description="\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0440\u0430\u0441\u0447\u0451\u0442\u0435 \u0437\u0430\u0440\u043f\u043b\u0430\u0442\u044b.")


class SalaryStaffBalance(BaseModel):
    """Схема спеки: Объект баланса по заработной плате
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    income: str | None = Field(default=None, description="\u041f\u0440\u0438\u0445\u043e\u0434.")
    expense: str | None = Field(default=None, description="\u0420\u0430\u0441\u0445\u043e\u0434.")
    balance: str | None = Field(default=None, description="\u0411\u0430\u043b\u0430\u043d\u0441.")


class SalaryStaffCalculation(BaseModel):
    """Взаиморасчёты.
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    total_sum: SalaryStaffBalance | None = Field(default=None, description="\u041e\u0431\u0449\u0430\u044f \u0441\u0443\u043c\u043c\u0430.")
    currency: Currency2 | None = Field(default=None, description="\u0412\u0430\u043b\u044e\u0442\u0430.")


class SalaryStaffCalculationDaily(BaseModel):
    """Взаиморасчёты с группировкой по дате.
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    payroll_daily: list[dict[str, Any]] | None = Field(default=None)
    currency: Currency2 | None = Field(default=None, description="\u0412\u0430\u043b\u044e\u0442\u0430.")


class SalaryStaffScheme(BaseModel):
    """Схема спеки: Объект схемы расчёта зарплаты
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    staff_id: int | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430.")
    date_start: str | None = Field(default=None, description="\u0414\u0430\u0442\u0430, \u0441 \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u0443 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430 \u0434\u0435\u0439\u0441\u0442\u0432\u0443\u0435\u0442 \u0441\u0445\u0435\u043c\u0430 \u0440\u0430\u0441\u0447\u0451\u0442\u0430 \u0437\u0430\u0440\u043f\u043b\u0430\u0442\u044b.")
    date_end: str | None = Field(default=None, description="\u0414\u0430\u0442\u0430, \u0434\u043e \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u0443 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430 \u0434\u0435\u0439\u0441\u0442\u0432\u0443\u0435\u0442 \u0441\u0445\u0435\u043c\u0430 \u0440\u0430\u0441\u0447\u0451\u0442\u0430 \u0437\u0430\u0440\u043f\u043b\u0430\u0442\u044b \u0438\u043b\u0438 null, \u0435\u0441\u043b\u0438 \u043d\u0435 \u0438\u043c\u0435\u0435\u0442 \u0434\u0430\u0442\u044b \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f.")
    salary_scheme: dict[str, Any] | None = Field(default=None, description="\u0421\u0445\u0435\u043c\u0430 \u0440\u0430\u0441\u0447\u0451\u0442\u0430 \u0437\u0430\u0440\u043f\u043b\u0430\u0442\u044b.")


class SalaryStaffSchemesCount(BaseModel):
    """Схема спеки: Количество прикреплённых схем расчёта зарплат
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    staff_id: int | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430.")
    salary_schemes_count: int | None = Field(default=None, description="\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u0440\u0438\u043a\u0440\u0435\u043f\u043b\u0451\u043d\u043d\u044b\u0445 \u0441\u0445\u0435\u043c \u0440\u0430\u0441\u0447\u0451\u0442\u0430 \u0437\u0430\u0440\u043f\u043b\u0430\u0442.")


class SalaryStaffSummary(BaseModel):
    """Схема спеки: Объект итогов по заработной плате
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    working_days_count: int | None = Field(default=None, description="\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0440\u0430\u0431\u043e\u0447\u0438\u0445 \u0434\u043d\u0435\u0439.")
    working_hours_count: int | None = Field(default=None, description="\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0440\u0430\u0431\u043e\u0447\u0438\u0445 \u0447\u0430\u0441\u043e\u0432.")
    group_services_count: int | None = Field(default=None, description="\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043e\u043a\u0430\u0437\u0430\u043d\u043d\u044b\u0445 \u0433\u0440\u0443\u043f\u043f\u043e\u0432\u044b\u0445 \u0443\u0441\u043b\u0443\u0433.")
    services_count: int | None = Field(default=None, description="\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043e\u043a\u0430\u0437\u0430\u043d\u043d\u044b\u0445 \u0443\u0441\u043b\u0443\u0433.")
    services_sum: str | None = Field(default=None, description="\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u043e\u043a\u0430\u0437\u0430\u043d\u043d\u044b\u0445 \u0443\u0441\u043b\u0443\u0433.")
    goods_sales_count: int | None = Field(default=None, description="\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u0440\u043e\u0434\u0430\u043d\u043d\u044b\u0445 \u0442\u043e\u0432\u0430\u0440\u043e\u0432.")
    goods_sales_sum: str | None = Field(default=None, description="\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u043f\u0440\u043e\u0434\u0430\u043d\u043d\u044b\u0445 \u0442\u043e\u0432\u0430\u0440\u043e\u0432.")
    total_sum: str | None = Field(default=None, description="\u0421\u0443\u043c\u043c\u0430\u0440\u043d\u0430\u044f \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c.")
    salary: str | None = Field(default=None, description="\u0417\u0430\u0440\u043f\u043b\u0430\u0442\u0430.")


class SalonService(BaseModel):
    """Схема спеки: Объект модели "Услуга / Категория услуг в филиале".
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0443\u0441\u043b\u0443\u0433\u0438 (\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0443\u0441\u043b\u0443\u0433).")
    is_category: bool | None = Field(default=None, description="\u041f\u0440\u0438\u0437\u043d\u0430\u043a \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0443\u0441\u043b\u0443\u0433 (true \u0434\u043b\u044f \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0443\u0441\u043b\u0443\u0433, false \u0434\u043b\u044f \u0443\u0441\u043b\u0443\u0433\u0438).")
    category_id: float | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0440\u043e\u0434\u0438\u0442\u0435\u043b\u044c\u0441\u043a\u043e\u0439 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0443\u0441\u043b\u0443\u0433.")
    title: str | None = Field(default=None, description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0443\u0441\u043b\u0443\u0433\u0438 (\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0443\u0441\u043b\u0443\u0433).")


class ServiceCategoriesCompanyidRequestDataTypes(BaseModel):
    """Создать категорию услуги
    Схема спеки: Root Type for service_categories_companyid_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    title: str | None = Field(default=None, description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0443\u0441\u043b\u0443\u0433")
    api_id: str | None = Field(default=None, description="\u0412\u043d\u0435\u0448\u043d\u0438\u0439 \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438")
    weight: float | None = Field(default=None, description="\u0412\u0435\u0441 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 (\u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u0442\u0441\u044f \u0434\u043b\u044f \u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0438 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0439 \u043f\u0440\u0438 \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0438)")
    staff: list[float] | None = Field(default=None, description="\u0421\u043f\u0438\u0441\u043e\u043a ID \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u043e\u0432, \u043e\u043a\u0430\u0437\u044b\u0432\u0430\u044e\u0449\u0438\u0445 \u0443\u0441\u043b\u0443\u0433\u0438 \u0438\u0437 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438")


class ServiceCategoriesCompanyidResponseDataTypes(BaseModel):
    """Создать категорию услуг
    Схема спеки: Root Type for service_categories_companyid_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: dict[str, Any] | None = Field(default=None, alias="data", description="\u041e\u0431\u044a\u0435\u043a\u0442 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class ServiceTitle2(BaseModel):
    """Название услуги
    Схема спеки: Root Type for ServiceTitle
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0443\u0441\u043b\u0443\u0433\u0438")
    title: str | None = Field(default=None, description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0443\u0441\u043b\u0443\u0433\u0438")


class ServicesChangeCompanyidRequestDataTypes(BaseModel):
    """Создать услугу
    Схема спеки: Root Type for services_change_companyid_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    title: str = Field(description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0443\u0441\u043b\u0443\u0433\u0438")
    booking_title: str = Field(description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0443\u0441\u043b\u0443\u0433\u0438 \u0434\u043b\u044f \u043e\u043d\u043b\u0430\u0439\u043d-\u0437\u0430\u043f\u0438\u0441\u0438")
    category_id: float = Field(description="ID \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0443\u0441\u043b\u0443\u0433")
    price_min: float = Field(description="\u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0443\u0441\u043b\u0443\u0433\u0438")
    price_max: float = Field(description="\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0443\u0441\u043b\u0443\u0433\u0438")
    duration: float = Field(description="\u0414\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0443\u0441\u043b\u0443\u0433\u0438, \u043f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e \u0440\u0430\u0432\u043d\u0430 3600 \u0441\u0435\u043a\u0443\u043d\u0434\u0430\u043c")
    technical_break_duration: float | None = Field(default=None, description="\u0414\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0442\u0435\u0445\u043d\u0438\u0447\u0435\u0441\u043a\u043e\u0433\u043e \u043f\u0435\u0440\u0435\u0440\u044b\u0432\u0430 - \u0415\u0441\u043b\u0438 \u043d\u0435 \u043f\u0435\u0440\u0435\u0434\u0430\u043d. \u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e null - \u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 null, \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u0435\u0442 \u043e\u0431\u0449\u0435\u0439 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0435 \u0444\u0438\u043b\u0438\u0430\u043b\u0430, \u0438 \u0437\u0430\u0434\u0430\u0435\u0442\u0441\u044f \u0432 \u0440\u0430\u0437\u0434\u0435\u043b\u0435 *\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u2192 \u0416\u0443\u0440\u043d\u0430\u043b \u0437\u0430\u043f\u0438\u0441\u0438 \u2192 \u0422\u0435\u0445\u043d\u0438\u0447\u0435\u0441\u043a\u0438...")
    discount: float | None = Field(default=None, description="\u0421\u043a\u0438\u0434\u043a\u0430 \u043f\u0440\u0438 \u043e\u043a\u0430\u0437\u0430\u043d\u0438\u0438 \u0443\u0441\u043b\u0443\u0433\u0438")
    comment: str | None = Field(default=None, description="\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 \u043a \u0443\u0441\u043b\u0443\u0433\u0435")
    is_multi: bool = Field(description="false - \u0438\u043d\u0434\u0438\u0432\u0438\u0434\u0443\u0430\u043b\u044c\u043d\u0430\u044f \u0443\u0441\u043b\u0443\u0433\u0430, true - \u0433\u0440\u0443\u043f\u043f\u043e\u0432\u0430\u044f \u0443\u0441\u043b\u0443\u0433\u0430")
    tax_variant: float = Field(description="ID \u0441\u0438\u0441\u0442\u0435\u043c\u044b \u043d\u0430\u043b\u043e\u0433\u043e\u043e\u0431\u043b\u043e\u0436\u0435\u043d\u0438\u044f")
    vat_id: float = Field(description="ID \u041d\u0414\u0421")
    is_need_limit_date: bool = Field(description="\u041e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u0435 \u043f\u043e \u0434\u0430\u0442\u0430\u043c \u0434\u043b\u044f \u043e\u043d\u043b\u0430\u0439\u043d-\u0437\u0430\u043f\u0438\u0441\u0438")
    date_from: str | None = Field(default=None, description="\u0414\u0430\u0442\u0430 \u0441 \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u0443\u0441\u043b\u0443\u0433\u0430 \u0431\u0443\u0434\u0435\u0442 \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u0430 \u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435 yyyy-mm-dd")
    date_to: str | None = Field(default=None, description="\u0414\u0430\u0442\u0430 \u0434\u043e \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u0443\u0441\u043b\u0443\u0433\u0430 \u0431\u0443\u0434\u0435\u0442 \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u0430 \u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435 yyyy-mm-dd")
    dates: Any | None = Field(default=None, description="\u0421\u043f\u0438\u0441\u043e\u043a \u0434\u0430\u0442 \u0432 \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u0431\u0443\u0434\u0435\u0442 \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u0430 \u043e\u043d\u043b\u0430\u0439\u043d \u0437\u0430\u043f\u0438\u0441\u044c (\u0435\u0441\u043b\u0438 \u043c\u0430\u0441\u0441\u0438\u0432 \u043d\u0435 \u043f\u0435\u0440\u0435\u0434\u0430\u043d, \u0432\u0441\u0435 \u0434\u0430\u0442\u044b \u0437\u0430 \u0443\u043a\u0430\u0437\u0430\u043d\u043d\u044b\u0439 \u043f\u0435\u0440\u0438\u043e\u0434 \u0431\u0443\u0434\u0443\u0442 \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u044b)")
    seance_search_start: float = Field(description="\u041d\u0430\u0447\u0430\u043b\u043e \u043f\u0435\u0440\u0438\u043e\u0434\u0430 \u0432 \u043a\u0430\u043a\u043e\u0435 \u0432\u0440\u0435\u043c\u044f \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u0430 \u0437\u0430\u043f\u0438\u0441\u044c, \u0443\u043a\u0430\u0437\u044b\u0432\u0430\u0435\u0442\u0441\u044f \u0432 \u0441\u0435\u043a\u0443\u043d\u0434\u0430\u0445")
    seance_search_finish: float = Field(description="\u041a\u043e\u043d\u0435\u0446 \u043f\u0435\u0440\u0438\u043e\u0434\u0430 \u0432 \u043a\u0430\u043a\u043e\u0435 \u0432\u0440\u0435\u043c\u044f \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u0430 \u0437\u0430\u043f\u0438\u0441\u044c, \u0443\u043a\u0430\u0437\u044b\u0432\u0430\u0435\u0442\u0441\u044f \u0432 \u0441\u0435\u043a\u0443\u043d\u0434\u0430\u0445")
    step: float = Field(description="\u0428\u0430\u0433 \u0432\u044b\u0432\u043e\u0434\u0430 \u0441\u0435\u0430\u043d\u0441\u043e\u0432, \u0443\u043a\u0430\u0437\u044b\u0432\u0430\u0435\u0442\u0441\u044f \u0432 \u0441\u0435\u043a\u0443\u043d\u0434\u0430\u0445")
    seance_search_step: float = Field(description="\u0428\u0430\u0433 \u043f\u043e\u0438\u0441\u043a\u0430 \u0441\u0435\u0430\u043d\u0441\u043e\u0432, \u0443\u043a\u0430\u0437\u044b\u0432\u0430\u0435\u0442\u0441\u044f \u0432 \u0441\u0435\u043a\u0443\u043d\u0434\u0430\u0445")
    weight: float | None = Field(default=None, description="\u0412\u0435\u0441 \u0443\u0441\u043b\u0443\u0433\u0438 (\u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u0442\u0441\u044f \u0434\u043b\u044f \u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0438 \u0443\u0441\u043b\u0443\u0433 \u043f\u0440\u0438 \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0438)")
    service_type: float | None = Field(default=None, description="\u0414\u043e\u0441\u0442\u0443\u043f\u043d\u0430 \u043b\u0438 \u0434\u043b\u044f \u043e\u043d\u043b\u0430\u0439\u043d \u0437\u0430\u043f\u0438\u0441\u0438 \u0443\u0441\u043b\u0443\u0433\u0430. 1 - \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u0430, 0 \u043d\u0435 \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u0430.")
    api_service_id: int | None = Field(default=None, description="\u0412\u043d\u0435\u0448\u043d\u0438\u0439 \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0443\u0441\u043b\u0443\u0433\u0438")
    online_invoicing_status: int | None = Field(default=None, description="\u041e\u043d\u043b\u0430\u0439\u043d-\u043f\u0440\u0435\u0434\u043e\u043f\u043b\u0430\u0442\u0430 \u0432\u043a\u043b\u044e\u0447\u0435\u043d\u0430 (0-\u0432\u044b\u043a\u043b\u044e\u0447\u0435\u043d\u0430, 2-\u0432\u043a\u043b\u044e\u0447\u0435\u043d\u0430)")
    price_prepaid_percent: int | None = Field(default=None, description="\u0420\u0430\u0437\u043c\u0435\u0440 \u043f\u0440\u0435\u0434\u043e\u043f\u043b\u0430\u0442\u044b \u0432 \u043f\u0440\u043e\u0446\u0435\u043d\u0442\u0430\u0445 (\u043e\u0442 \u043c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0439 \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u0438 \u0443\u0441\u043b\u0443\u0433\u0438)")
    price_prepaid_amount: int | None = Field(default=None, description="\u0421\u0443\u043c\u043c\u0430 \u043f\u0440\u0435\u0434\u043e\u043f\u043b\u0430\u0442\u044b")
    abonement_restriction_value: int | None = Field(default=None, description="\u0417\u0430\u043f\u0440\u0435\u0442 \u0437\u0430\u043f\u0438\u0441\u0438 \u0431\u0435\u0437 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430 (\u0422\u043e\u043b\u044c\u043a\u043e \u0435\u0441\u043b\u0438 online_invoicing_status=0)")
    is_abonement_autopayment_enabled: int | None = Field(default=None, description="\u0410\u0432\u0442\u043e\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0441 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430")
    autopayment_before_visit_time: int | None = Field(default=None, description="\u0417\u0430 \u043a\u0430\u043a\u043e\u0435 \u0432\u0440\u0435\u043c\u044f \u0434\u043e \u0432\u0438\u0437\u0438\u0442\u0430 \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0441\u044f \u0430\u0432\u0442\u043e\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0435")
    staff: list[dict[str, Any]] | None = Field(default=None, description="\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0438, \u043e\u043a\u0430\u0437\u044b\u0432\u0430\u044e\u0448\u0438\u0435 \u0443\u0441\u043b\u0443\u0433\u0443 \u0438 \u0434\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u043e\u043a\u0430\u0437\u0430\u043d\u0438\u044f \u0443\u0441\u043b\u0443\u0433\u0438 \u043a\u0430\u0436\u0434\u044b\u043c \u0438\u0437 \u043d\u0438\u0445")


class ServicesChangeCompanyidResponseDataTypes(BaseModel):
    """Изменить услугу
    Схема спеки: Root Type for services_change_companyid_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: dict[str, Any] | None = Field(default=None, alias="data")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class ServicesCompanyidLinksRequestDataTypes(BaseModel):
    """Изменить длительность оказания услуги сотрудниками, технические карты, названия на других языках
    Схема спеки: Root Type for services_companyid_links_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    service_id: float = Field(description="ID \u0443\u0441\u043b\u0443\u0433\u0438")
    master_settings: list[dict[str, Any]] = Field(description="\u0421\u043f\u0438\u0441\u043e\u043a \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u043e\u0432, \u043e\u043a\u0430\u0437\u044b\u0432\u0430\u044e\u0449\u0438\u0445 \u0443\u0441\u043b\u0443\u0433\u0443 c \u0434\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c\u044e \u0441\u0435\u0430\u043d\u0441\u0430 \u0438 \u0442\u0435\u0445\u043d\u043e\u043b\u043e\u0433\u0438\u0447\u0435\u0441\u043a\u0438\u043c\u0438 \u043a\u0430\u0440\u0442\u0430\u043c\u0438")
    resource_ids: list[float] = Field(description="\u0421\u043f\u0438\u0441\u043e\u043a \u0440\u0435\u0441\u0443\u0440\u0441\u043e\u0432 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u044b\u0445 \u0434\u043b\u044f \u043e\u043a\u0430\u0437\u0430\u043d\u0438\u044f \u0443\u0441\u043b\u0443\u0433\u0438")
    translations: list[dict[str, Any]] = Field(description="\u0421\u043f\u0438\u0441\u043e\u043a \u043f\u0435\u0440\u0435\u0432\u043e\u0434\u043e\u0432 \u0434\u043b\u044f \u043a\u0430\u0436\u0434\u043e\u0433\u043e \u044f\u0437\u044b\u043a\u0430")


class ServicesCompanyidRequestDataTypes(BaseModel):
    """Создать услугу
    Схема спеки: Root Type for services_companyid_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    title: str | None = Field(default=None, description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0443\u0441\u043b\u0443\u0433\u0438")
    category_id: float | None = Field(default=None, description="ID \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0443\u0441\u043b\u0443\u0433")
    price_min: float | None = Field(default=None, description="\u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0443\u0441\u043b\u0443\u0433\u0438")
    price_max: float | None = Field(default=None, description="\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0443\u0441\u043b\u0443\u0433\u0438")
    duration: float | None = Field(default=None, description="\u0414\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0443\u0441\u043b\u0443\u0433\u0438, \u043f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e \u0440\u0430\u0432\u043d\u0430 3600 \u0441\u0435\u043a\u0443\u043d\u0434\u0430\u043c")
    technical_break_duration: float | None = Field(default=None, description="\u0414\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0442\u0435\u0445\u043d\u0438\u0447\u0435\u0441\u043a\u043e\u0433\u043e \u043f\u0435\u0440\u0435\u0440\u044b\u0432\u0430 - \u0415\u0441\u043b\u0438 \u043d\u0435 \u043f\u0435\u0440\u0435\u0434\u0430\u043d. \u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e null - \u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 null, \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u0435\u0442 \u043e\u0431\u0449\u0435\u0439 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0435 \u0444\u0438\u043b\u0438\u0430\u043b\u0430, \u0438 \u0437\u0430\u0434\u0430\u0435\u0442\u0441\u044f \u0432 \u0440\u0430\u0437\u0434\u0435\u043b\u0435 *\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u2192 \u0416\u0443\u0440\u043d\u0430\u043b \u0437\u0430\u043f\u0438\u0441\u0438 \u2192 \u0422\u0435\u0445\u043d\u0438\u0447\u0435\u0441\u043a\u0438...")
    discount: float | None = Field(default=None, description="\u0421\u043a\u0438\u0434\u043a\u0430 \u043f\u0440\u0438 \u043e\u043a\u0430\u0437\u0430\u043d\u0438\u0438 \u0443\u0441\u043b\u0443\u0433\u0438")
    comment: str | None = Field(default=None, description="\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 \u043a \u0443\u0441\u043b\u0443\u0433\u0435")
    weight: float | None = Field(default=None, description="\u0412\u0435\u0441 \u0443\u0441\u043b\u0443\u0433\u0438 (\u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u0442\u0441\u044f \u0434\u043b\u044f \u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0438 \u0443\u0441\u043b\u0443\u0433 \u043f\u0440\u0438 \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0438)")
    service_type: float | None = Field(default=None, description="\u0414\u043e\u0441\u0442\u0443\u043f\u043d\u0430 \u043b\u0438 \u0434\u043b\u044f \u043e\u043d\u043b\u0430\u0439\u043d \u0437\u0430\u043f\u0438\u0441\u0438 \u0443\u0441\u043b\u0443\u0433\u0430. 1 - \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u0430, 0 \u043d\u0435 \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u0430.")
    api_service_id: str | None = Field(default=None, description="\u0412\u043d\u0435\u0448\u043d\u0438\u0439 \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0443\u0441\u043b\u0443\u0433\u0438")
    staff: list[dict[str, Any]] | None = Field(default=None, description="\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0438, \u043e\u043a\u0430\u0437\u044b\u0432\u0430\u044e\u0448\u0438\u0435 \u0443\u0441\u043b\u0443\u0433\u0443 \u0438 \u0434\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u043e\u043a\u0430\u0437\u0430\u043d\u0438\u044f \u0443\u0441\u043b\u0443\u0433\u0438 \u043a\u0430\u0436\u0434\u044b\u043c \u0438\u0437 \u043d\u0438\u0445")


class ServicesCompanyidResponseDataTypes(BaseModel):
    """Создать услугу
    Схема спеки: Root Type for services_companyid_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: dict[str, Any] | None = Field(default=None, alias="data", description="\u041e\u0431\u044a\u0435\u043a\u0442 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class SmsClientsByFilterRequestDataTypes(BaseModel):
    """Отправить SMS рассылку по клиентам, подходящим под фильтры
    Схема спеки: Root Type for sms_clients_by_filter_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    text: str | None = Field(default=None, description="\u0422\u0435\u043a\u0441\u0442 SMS \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f")


class SmsClientsByIdRequestDataTypes(BaseModel):
    """Отправить SMS рассылку по списку клиентов
    Схема спеки: Root Type for sms_clients_by_id_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    client_ids: list[float] | None = Field(default=None, description="\u041c\u0430\u0441\u0441\u0438\u0432 \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440\u043e\u0432 \u043a\u043b\u0438\u0435\u043d\u0442\u043e\u0432")
    text: str | None = Field(default=None, description="\u0422\u0435\u043a\u0441\u0442 SMS \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f")


class SmsClientsByIdResponseDataTypes(BaseModel):
    """Отправить SMS рассылку по списку клиентов
    Схема спеки: Root Type for sms_clients_by_id_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: str | None = Field(default=None, alias="data", description="\u0418\u043c\u0435\u0435\u0442 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 null")
    meta: dict[str, Any] | None = Field(default=None, description="\u041e\u0431\u044a\u0435\u043a\u0442, \u0441\u043e\u0434\u0435\u0440\u0436\u0430\u0449\u0438\u0439 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435 201 \u0441\u0442\u0430\u0442\u0443\u0441-\u043a\u043e\u0434\u0430")


class StaffCompanyidRequestDataTypes(BaseModel):
    """Добавить нового сотрудника
    Схема спеки: Root Type for staff_companyid_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    name: str | None = Field(default=None, description="\u0418\u043c\u044f \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430")
    specialization: str | None = Field(default=None, description="\u0421\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430")
    weight: float | None = Field(default=None, description="\u0412\u0435\u0441 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430. \u041f\u0440\u0438 \u0432\u044b\u0432\u043e\u0434\u0435 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0438 \u0441\u043e\u0440\u0442\u0438\u0440\u0443\u044e\u0442\u0441\u044f \u043f\u043e \u0432\u0435\u0441\u0443, \u0441\u043d\u0430\u0447\u0430\u043b\u0430 \u0431\u043e\u043b\u0435\u0435 \u0442\u044f\u0436\u0435\u043b\u044b\u0435")
    information: str | None = Field(default=None, description="\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0435 (HTML-\u0444\u043e\u0440\u043c\u0430\u0442)")
    api_id: str | None = Field(default=None, description="\u0412\u043d\u0435\u0449\u043d\u0438\u0439 \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430")
    hidden: float | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f \u0432 \u043e\u043d\u043b\u0430\u0439\u043d-\u0437\u0430\u043f\u0438\u0441\u0438, 1 - \u0441\u043a\u0440\u044b\u0442, 0 - \u043d\u0435 \u0441\u043a\u0440\u044b\u0442")
    fired: float | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0432\u043e\u043b\u044c\u043d\u0435\u043d\u0438\u044f \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430, 1 - \u0443\u0432\u043e\u043b\u0435\u043d, 0 - \u043d\u0435 \u0443\u0432\u043e\u043b\u0435\u043d")
    user_id: float | None = Field(default=None, description="ID \u043f\u0440\u0438\u0432\u044f\u0437\u0430\u043d\u043d\u043e\u0433\u043e \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f, 0 - \u0443\u0434\u0430\u043b\u0438\u0442\u044c \u0441\u0432\u044f\u0437\u044c \u0441 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u043c")


class StaffPosition2(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float = Field(alias="id", description="id \u0434\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u0438")
    title: str = Field(description="\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0434\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u0438")


class StorageOperationDocumentsRequestDataTypes(BaseModel):
    """Создать документ
    Схема спеки: Root Type for storage_operation_documents_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    type_id: float = Field(description="\u0422\u0438\u043f \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430 (1 \u043f\u0440\u043e\u0434\u0430\u0436\u0430, 3 \u043f\u0440\u0438\u0445\u043e\u0434, 4 \u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0435)")
    comment: str | None = Field(default=None, description="\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439")
    storage_id: float = Field(description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0441\u043a\u043b\u0430\u0434\u0430")
    create_date: str = Field(description="\u0414\u0430\u0442\u0430 \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u044f \u0441\u043a\u043b\u0430\u0434\u0441\u043a\u043e\u0439 \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438")


class StorageOperationDocumentsResponseDataTypes(BaseModel):
    """Создать документ
    Схема спеки: Root Type for storage_operation_documents_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: dict[str, Any] | None = Field(default=None, alias="data", description="\u041e\u0431\u044a\u0435\u043a\u0442 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class StorageOperationFinanceTransactionResponseDataTypes(BaseModel):
    """Получить финансовые транзакции документа
    Схема спеки: Root Type for storage_operation_finance_transaction_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: list[dict[str, Any]] | None = Field(default=None, alias="data", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class StorageOperationGoodTransactionRequestDataTypes(BaseModel):
    """Создать транзакцию
    Схема спеки: Root Type for storage_operation_good_transaction_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    document_id: float = Field(description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430")
    good_id: float = Field(description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0442\u043e\u0432\u0430\u0440\u0430")
    amount: float = Field(description="\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e")
    cost_per_unit: float = Field(description="\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0437\u0430 \u0435\u0434\u0438\u043d\u0438\u0446\u0443 \u0442\u043e\u0432\u0430\u0440\u0430")
    discount: float = Field(description="\u0421\u043a\u0438\u0434\u043a\u0430 \u0432 %")
    cost: float = Field(description="\u0418\u0442\u043e\u0433\u043e\u0432\u0430\u044f \u0441\u0443\u043c\u043c\u0430 \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u0438")
    operation_unit_type: float = Field(description="\u0442\u0438\u043f \u0435\u0434\u0438\u043d\u0438\u0446\u044b \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f: 1 - \u0434\u043b\u044f \u043f\u0440\u043e\u0434\u0430\u0436\u0438, 2 - \u0434\u043b\u044f \u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f")
    good_special_number: str | None = Field(default=None, description="\u041a\u043e\u0434 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430\\\u0441\u0435\u0440\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u0430, \u0435\u0441\u043b\u0438 \u0442\u043e\u0432\u0430\u0440 \u044f\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u043e\u043c \u0438\u043b\u0438 \u0441\u0435\u0440\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u043c")
    master_id: float | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043c\u0430\u0441\u0442\u0435\u0440\u0430, \u043f\u0440\u043e\u0434\u0430\u0432\u0448\u0435\u0433\u043e \u0442\u043e\u0432\u0430\u0440")
    client_id: float | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043a\u043b\u0438\u0435\u043d\u0442\u0430, \u043a\u0443\u043f\u0438\u0432\u0448\u0435\u0433\u043e \u0442\u043e\u0432\u0430\u0440")
    supplier_id: float | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u0430")
    comment: str | None = Field(default=None, description="\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439")


class StorageOperationGoodTransactionResponse200DataTypes(BaseModel):
    """Создать транзакцию
    Схема спеки: Root Type for storage_operation_good_transaction_response200_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: dict[str, Any] | None = Field(default=None, alias="data", description="\u041e\u0431\u044a\u0435\u043a\u0442 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class StorageOperationGoodTransactionResponseDataTypes(BaseModel):
    """Получить товарные транзакции документа
    Схема спеки: Root Type for storage_operation_good_transaction_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: list[dict[str, Any]] | None = Field(default=None, alias="data", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: dict[str, Any] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043d\u0430\u0439\u0434\u0435\u043d\u043d\u044b\u0445 \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u0439)")


class StorageOperationOperationResponseDataTypes(BaseModel):
    """Создание складской операции
    Схема спеки: Root Type for storage_operation_operation_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: dict[str, Any] | None = Field(default=None, alias="data", description="\u041e\u0431\u044a\u0435\u043a\u0442 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class StorageResponseDataTypes(BaseModel):
    """Получить склады компании
    Схема спеки: Root Type for storage_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: list[dict[str, Any]] | None = Field(default=None, alias="data", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class StoragesTransactionResponseDataTypes(BaseModel):
    """Поиск товарных транзакций
    Схема спеки: Root Type for storages_transaction_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: list[dict[str, Any]] | None = Field(default=None, alias="data", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class TaxSystemResponseDataTypes2(BaseModel):
    """Пример запроса на получение списка
    Схема спеки: Root Type for tax_system_response_data_Types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: list[dict[str, Any]] | None = Field(default=None, alias="data", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: dict[str, Any] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u0441\u043e\u0434\u0435\u0440\u0436\u0438\u0442 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043d\u0430\u0439\u0434\u0435\u043d\u043d\u044b\u0445 \u0441\u0438\u0441\u0442\u0435\u043c \u043d\u0430\u043b\u043e\u0433\u043e\u043e\u0431\u043b\u043e\u0436\u0435\u043d\u0438\u044f)")


class TechnologicalCardsConsumablesResponse200DataTypes(BaseModel):
    """Получить список тех. карт и расходников записи
    Схема спеки: Root Type for technological_cards_consumables_response200_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: list[dict[str, Any]] | None = Field(default=None, alias="data", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class TechnologicalCardsConsumablesResponse200DeleteDataTypes(BaseModel):
    """Удалит технологическую карты из связи запись-услуга
    Схема спеки: Root Type for technological_cards_consumables_response200_delete_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: list[dict[str, Any]] | None = Field(default=None, alias="data", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u0441 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u043c")
    meta: dict[str, Any] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class TechnologicalCardsResponse200DataTypes(BaseModel):
    """Получить список тех. карт
    Схема спеки: Root Type for technological_cards_response200_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: list[dict[str, Any]] | None = Field(default=None, alias="data", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u043e\u0431\u044a\u0435\u043a\u043e\u0432 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class TimetableActivityResponse(BaseModel):
    """Схема спеки: Объект модели "Групповое событие"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data_: dict[str, Any] | None = Field(default=None, alias="data")


class TimetableRecordResponse(BaseModel):
    """Схема спеки: Объект модели "Групповое событие"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data_: dict[str, Any] | None = Field(default=None, alias="data")


class TipsReduce(BaseModel):
    """Информация о наличии чаевых сотруднику. Модель используется, когда текущий пользователь не является мастером в данной записи.
    Схема спеки: Объект модели "Наличие чаевых без суммы"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    has_tips: bool | None = Field(default=None, description="\u0415\u0441\u0442\u044c \u043b\u0438 \u0447\u0430\u0435\u0432\u044b\u0435 \u0432 \u0434\u0430\u043d\u043d\u043e\u0439 \u0437\u0430\u043f\u0438\u0441\u0438.")
    sum: float | None = Field(default=None, description="\u0421\u0443\u043c\u043c\u0430 \u0447\u0430\u0435\u0432\u044b\u0445 \u043d\u0435 \u043f\u043e\u0434\u0441\u0447\u0438\u0442\u044b\u0432\u0430\u0435\u0442\u0441\u044f \u0438 \u0440\u0430\u0432\u043d\u0430 `null`.")


class TipsReduceWithFullInfo(BaseModel):
    """Информация о сумме всех чаевых сотруднику. Используется, если текущий пользователь является мастером в данной записи.
    Схема спеки: Объект модели "Суммарные чаевые"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    has_tips: bool | None = Field(default=None, description="\u0415\u0441\u0442\u044c \u043b\u0438 \u0447\u0430\u0435\u0432\u044b\u0435 \u0432 \u0434\u0430\u043d\u043d\u043e\u0439 \u0437\u0430\u043f\u0438\u0441\u0438.")
    sum: float | None = Field(default=None, description="\u0421\u0443\u043c\u043c\u0430 \u0447\u0430\u0435\u0432\u044b\u0445.")


class TipsSettingResponseDataTypes(BaseModel):
    """Получить список мастеров салона с их чаевыми
    Схема спеки: Root Type for tips_setting_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: list[dict[str, Any]] | None = Field(default=None, alias="data", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: dict[str, Any] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u0441\u043e\u0434\u0435\u0440\u0436\u0438\u0442 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043d\u0430\u0439\u0434\u0435\u043d\u043d\u044b\u0445 \u043c\u0430\u0441\u0442\u0435\u0440\u043e\u0432)")


class TransactionCompanyidResponseDataTypes(BaseModel):
    """Получить транзакции
    Схема спеки: Root Type for transaction_companyid_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: list[dict[str, Any]] | None = Field(default=None, alias="data", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class UserInviteResponseDataTypes(BaseModel):
    """Создание и отправка приглашения
    Схема спеки: Root Type for user_invite_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0439 \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0430 (true)")
    data_: str | None = Field(default=None, alias="data", description="\u0418\u043c\u0435\u0435\u0442 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 null")
    meta: dict[str, Any] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u0441\u043e\u0434\u0435\u0440\u0436\u0438\u0442 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435 \u043e \u0442\u043e\u043c, \u0447\u0442\u043e \u0434\u0430\u043d\u043d\u044b\u0435 \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u044b)")


class UserNameAvatar(BaseModel):
    """Данные по существующему пользователю.
    Схема спеки: Объект модели "Пользователь с именем и аватаром"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f.")
    name: str | None = Field(default=None, description="\u0418\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f.")
    avatar: str | None = Field(default=None, description="\u0410\u0432\u0430\u0442\u0430\u0440 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f.")


class UserPermissionsResponseDataTypes(BaseModel):
    """Получить список прав
    Схема спеки: Root Type for user_permissions_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: dict[str, Any] | None = Field(default=None, alias="data", description="\u041e\u0431\u044a\u0435\u043a\u0442 \u0441 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f\u043c\u0438 \u043f\u0440\u0430\u0432 \u0434\u043e\u0441\u0442\u0443\u043f\u0430")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class UserRecordsResponseDataTypes(BaseModel):
    """Получить записи пользователя
    Схема спеки: Root Type for user_records_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: list[dict[str, Any]] | None = Field(default=None, alias="data", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class UserRolePermissions(BaseModel):
    """Данные по правам и роли пользователя
    Схема спеки: Объект модели "Права и роль пользователя"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    user_role: Literal["worker", "administrator", "accountant", "manager", "owner"] | None = Field(default=None, description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0440\u043e\u043b\u0438")
    staff_id: float | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430 \u043f\u0440\u0438\u0432\u044f\u0437\u0430\u043d\u043d\u043e\u0433\u043e \u043a \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044e")
    is_editable: bool | None = Field(default=None, description="\u0414\u043e\u0441\u0442\u0443\u043f\u043d\u044b \u043b\u0438 \u043f\u0440\u0430\u0432\u0430 \u0438 \u0440\u043e\u043b\u044c \u0434\u043b\u044f \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f")
    user_permissions: list[Any] | None = Field(default=None, description="\u0421\u043f\u0438\u0441\u043e\u043a \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0439 \u043f\u0440\u0430\u0432 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f")


class UserRoleWithSalonAndUser(BaseModel):
    """Данные по роли пользователя
    Схема спеки: Объект модели "Роль пользователя"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    slug: Literal["worker", "administrator", "accountant", "manager", "owner"] | None = Field(default=None, description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0440\u043e\u043b\u0438")
    title: str | None = Field(default=None, description="\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0440\u043e\u043b\u0438")
    description: str | None = Field(default=None, description="\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0440\u043e\u043b\u0438")
    weight: float | None = Field(default=None, description="\u0412\u0435\u0441 \u0440\u043e\u043b\u0438, \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u044f\u044e\u0449\u0438\u0439 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u044b\u0445 \u043f\u0440\u0430\u0432")
    user_permissions: list[Any] | None = Field(default=None, description="\u0421\u043f\u0438\u0441\u043e\u043a \u043f\u0440\u0430\u0432 \u044d\u0442\u043e\u0439 \u0440\u043e\u043b\u0438 \u0412\u043e\u0437\u0432\u0440\u0430\u0449\u0430\u0435\u0442\u0441\u044f \u0432 \u043e\u0442\u0432\u0435\u0442\u0435, \u0435\u0441\u043b\u0438 \u0432 \u0437\u0430\u043f\u0440\u043e\u0441\u0435 \u0443\u043a\u0430\u0437\u0430\u043d \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 `include` \u0441 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u043c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435\u043c.")


class VisitDetailsDataTypes(BaseModel):
    """Получить детали визита
    Схема спеки: Root Type for visit_details_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: dict[str, Any] | None = Field(default=None, alias="data", description="\u041e\u0431\u044a\u0435\u043a\u0442 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class VisitLoyaltyApplyResponseDataTypes(BaseModel):
    """Применение лояльности в визите
    Схема спеки: Root Type for visit_loyalty_apply_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    payment_transactions: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0430\u0441\u0441\u0438\u0432 \u0441 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0435\u0439 \u043e \u0444\u0438\u043d\u0430\u043d\u0441\u043e\u0432\u044b\u0445 \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u044f\u0445 \u0437\u0430\u043f\u0438\u0441\u0438")
    loyalty_transactions: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0430\u0441\u0441\u0438\u0432 \u0441 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0435\u0439 \u043e \u043f\u0440\u0438\u043c\u0435\u043d\u0435\u043d\u043d\u044b\u0445 \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u044f\u0445 \u043b\u043e\u044f\u043b\u044c\u043d\u043e\u0441\u0442\u0438 \u0432 \u0432\u0438\u0437\u0438\u0442\u0435")
    kkm_transaction_details_container: dict[str, Any] | None = Field(default=None, description="\u041e\u0431\u044a\u0435\u043a\u0442 \u0441 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0435\u0439 \u043e \u041a\u041a\u041c \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u044f\u0445 \u0437\u0430\u043f\u0438\u0441\u0438")
    items_: list[dict[str, Any]] | None = Field(default=None, alias="items", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u0441 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0435\u0439 \u043e \u0442\u043e\u0432\u0430\u0440\u0430\u0445 \u0438 \u0443\u0441\u043b\u0443\u0433\u0430\u0445 \u0437\u0430\u043f\u0438\u0441\u0438")


class VisitLoyaltyCancelResponseDataTypes(BaseModel):
    """Отмена лояльности в визите
    Схема спеки: Root Type for visit_loyalty_cancel_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    payment_transactions: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0430\u0441\u0441\u0438\u0432 \u0441 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0435\u0439 \u043e \u0444\u0438\u043d\u0430\u043d\u0441\u043e\u0432\u044b\u0445 \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u044f\u0445 \u0437\u0430\u043f\u0438\u0441\u0438")
    loyalty_transactions: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0430\u0441\u0441\u0438\u0432 \u0441 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0435\u0439 \u043e \u043f\u0440\u0438\u043c\u0435\u043d\u0435\u043d\u043d\u044b\u0445 \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u044f\u0445 \u043b\u043e\u044f\u043b\u044c\u043d\u043e\u0441\u0442\u0438 \u0432 \u0432\u0438\u0437\u0438\u0442\u0435")
    kkm_transaction_details_container: dict[str, Any] | None = Field(default=None, description="\u041e\u0431\u044a\u0435\u043a\u0442 \u0441 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0435\u0439 \u043e \u041a\u041a\u041c \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u044f\u0445 \u0437\u0430\u043f\u0438\u0441\u0438")
    items_: list[dict[str, Any]] | None = Field(default=None, alias="items", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u0441 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0435\u0439 \u043e \u0442\u043e\u0432\u0430\u0440\u0430\u0445 \u0438 \u0443\u0441\u043b\u0443\u0433\u0430\u0445 \u0437\u0430\u043f\u0438\u0441\u0438")


class VisitLoyaltyRequestDataTypes(BaseModel):
    """Применить акцию
    Схема спеки: Root Type for visit_loyalty_request_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    record_id: float = Field(description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0437\u0430\u043f\u0438\u0441\u0438")
    visit_id: float = Field(description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0432\u0438\u0437\u0438\u0442\u0430")


class VisitsVisitidDataTypes(BaseModel):
    """Получить визит
    Схема спеки: Root Type for visits_visitid_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: dict[str, Any] | None = Field(default=None, alias="data", description="\u041e\u0431\u044a\u0435\u043a\u0442 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class VoipIntegrationDisableRequestDataTypes(BaseModel):
    """Отключить интеграцию
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    command: str = Field(description="Slug \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438 'setup'")
    type_: str = Field(alias="type", description="\u0422\u0438\u043f \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438, \u0432 \u0434\u0430\u043d\u043d\u043e\u043c \u0441\u043b\u0443\u0447\u0430\u0435 'disable'")
    crm_token: str = Field(description="CRM-\u0442\u043e\u043a\u0435\u043d \u0438\u0437 \u0440\u0430\u0437\u0434\u0435\u043b\u0430 \u0422\u0435\u043b\u0435\u0444\u043e\u043d\u0438\u044f-\u0418\u043d\u0442\u0435\u0433\u0440\u0430\u0446\u0438\u044f \u0432 \u0441\u0435\u0442\u0438 \u043a\u043b\u0438\u0435\u043d\u0442\u0430")


class VoipIntegrationEnableRequestDataTypes(BaseModel):
    """Подключить интеграцию
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    command: str = Field(description="Slug \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438 'setup'")
    type_: str = Field(alias="type", description="\u0422\u0438\u043f \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438, \u0432 \u0434\u0430\u043d\u043d\u043e\u043c \u0441\u043b\u0443\u0447\u0430\u0435 'enable'")
    crm_token: str = Field(description="CRM-\u0442\u043e\u043a\u0435\u043d \u0438\u0437 \u0440\u0430\u0437\u0434\u0435\u043b\u0430 \u0422\u0435\u043b\u0435\u0444\u043e\u043d\u0438\u044f-\u0418\u043d\u0442\u0435\u0433\u0440\u0430\u0446\u0438\u044f \u0432 \u0441\u0435\u0442\u0438 \u043a\u043b\u0438\u0435\u043d\u0442\u0430")


class VoipIntegrationHistoryRequestDataTypes(BaseModel):
    """Сохранение информации о звонке
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    command: str = Field(description="\u041e\u043f\u0435\u0440\u0430\u0446\u0438\u0438 'history'")
    type_: str = Field(alias="type", description="\u0422\u0438\u043f \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438 (\"incoming\", \"outgoing\", \"internal\")")
    crm_token: str = Field(description="CRM-\u0442\u043e\u043a\u0435\u043d \u0438\u0437 \u0440\u0430\u0437\u0434\u0435\u043b\u0430 \u0422\u0435\u043b\u0435\u0444\u043e\u043d\u0438\u044f-\u0418\u043d\u0442\u0435\u0433\u0440\u0430\u0446\u0438\u044f \u0432 \u0441\u0435\u0442\u0438 \u043a\u043b\u0438\u0435\u043d\u0442\u0430")
    phone: str = Field(description="\u041d\u043e\u043c\u0435\u0440 \u0437\u0432\u043e\u043d\u044f\u0449\u0435\u0433\u043e \u0430\u0431\u043e\u043d\u0435\u043d\u0442\u0430")
    user: str | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0430\u0431\u043e\u043d\u0435\u043d\u0442\u0430 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0438\u0438, sip")
    diversion: str = Field(description="\u041d\u043e\u043c\u0435\u0440 \u0447\u0435\u0440\u0435\u0437 \u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u043f\u0440\u0438\u0448\u0435\u043b \u0437\u0432\u043e\u043d\u043e\u043a")
    duration: float | None = Field(default=None, description="\u0414\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0437\u0432\u043e\u043d\u043a\u0430 (\u0432 \u0441\u0435\u043a\u0443\u043d\u0434\u0430\u0445)")
    link: str | None = Field(default=None, description="\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0437\u0430\u043f\u0438\u0441\u044c \u0437\u0432\u043e\u043d\u043a\u0430")
    call_id: str | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0437\u0432\u043e\u043d\u043a\u0430 \u0432 \u0441\u0438\u0441\u0442\u0435\u043c\u0435 voip")
    status: str | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0437\u0432\u043e\u043d\u043a\u0430 'success'|'missed'")
    date: str | None = Field(default=None, description="\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0437\u0432\u043e\u043d\u043a\u0430 (ISO8601)")


class VoipIntegrationNotificationRequestDataTypes(BaseModel):
    """Уведомление о звонке
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    command: str = Field(description="Slug \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438 'event'")
    type_: str = Field(alias="type", description="\u0422\u0438\u043f \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438, \u0432 \u0434\u0430\u043d\u043d\u043e\u043c \u0441\u043b\u0443\u0447\u0430\u0435 \"incoming\"")
    crm_token: str = Field(description="CRM-\u0442\u043e\u043a\u0435\u043d \u0438\u0437 \u0440\u0430\u0437\u0434\u0435\u043b\u0430 \u0422\u0435\u043b\u0435\u0444\u043e\u043d\u0438\u044f-\u0418\u043d\u0442\u0435\u0433\u0440\u0430\u0446\u0438\u044f \u0432 \u0441\u0435\u0442\u0438 \u043a\u043b\u0438\u0435\u043d\u0442\u0430")
    phone: str = Field(description="\u041d\u043e\u043c\u0435\u0440 \u0437\u0432\u043e\u043d\u044f\u0449\u0435\u0433\u043e \u0430\u0431\u043e\u043d\u0435\u043d\u0442\u0430")
    user: str | None = Field(default=None, description="SIP \u043d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0438\u0438")
    diversion: str = Field(description="\u041d\u043e\u043c\u0435\u0440 \u0447\u0435\u0440\u0435\u0437 \u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u043f\u0440\u0438\u0448\u0435\u043b \u0437\u0432\u043e\u043d\u043e\u043a")


class VoipIntegrationResponseDataTypes(BaseModel):
    """Подключить интеграцию
    Схема спеки: Root Type for voip_integration_setup_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: str | None = Field(default=None, alias="data", description="\u0421\u043e\u0434\u0435\u0440\u0436\u0438\u0442 null")
    meta: dict[str, Any] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u0441\u043e\u0434\u0435\u0440\u0436\u0438\u0442\u044c \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435 \"Accepted\")")


class ZReportResponseDataTypes(BaseModel):
    """Получить данные Z-Отчета
    Схема спеки: Root Type for z_report_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")
    data_: dict[str, Any] | None = Field(default=None, alias="data", description="\u041e\u0431\u044a\u0435\u043a\u0442 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class M200SuccessResponse(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: dict[str, Any] | None = Field(default=None, alias="data")
    meta: dict[str, Any] | None = Field(default=None)


class DeleteClientSchedulesClientScheduleIdResponse204(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: dict[str, Any] | None = Field(default=None, alias="data")
    meta: dict[str, Any] | None = Field(default=None)


class DeleteCommentsCommentIdResponse204(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: dict[str, Any] | None = Field(default=None, alias="data")
    meta: dict[str, Any] | None = Field(default=None)


class DeleteDaysDayIdResponse204(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: dict[str, Any] | None = Field(default=None, alias="data")
    meta: dict[str, Any] | None = Field(default=None)


class DeleteSchedulesScheduleIdResponse204(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: dict[str, Any] | None = Field(default=None, alias="data")
    meta: dict[str, Any] | None = Field(default=None)


class DeleteStaffMasterIdResponse204(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: dict[str, Any] | None = Field(default=None, alias="data")
    meta: dict[str, Any] | None = Field(default=None)


class GetAbonementIdCheckForActivityResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data_: CheckForActivity | None = Field(default=None, alias="data")


class GetAbonementsSearchForActivityResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data_: list[dict[str, Any]] | None = Field(default=None, alias="data")
    included: list[Any] | None = Field(default=None, description="\u041c\u0430\u0441\u0441\u0438\u0432 \u0438\u043d\u043a\u043b\u044e\u0434\u043e\u0432 (\u0432\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0439)")


class GetApplicationApplicationIdResponse200Data(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    connection_status: GetApplicationApplicationIdResponse200DataConnectionStatus | None = Field(default=None)
    payments: list[GetApplicationApplicationIdResponse200DataPaymentsItem] | None = Field(default=None, description="\u0421\u043f\u0438\u0441\u043e\u043a \u043e\u043f\u043b\u0430\u0442 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f \u0432 \u0441\u0430\u043b\u043e\u043d\u0435")
    logs: list[GetApplicationApplicationIdResponse200DataLogsItem] | None = Field(default=None, description="\u041b\u043e\u0433 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u0441\u0442\u0430\u0442\u0443\u0441\u043e\u0432 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f \u0432 \u0441\u0430\u043b\u043e\u043d\u0435")


class GetApplicationIdTariffsResponse200DataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="ID \u0442\u0430\u0440\u0438\u0444\u0430")
    title: str | None = Field(default=None, description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0442\u0430\u0440\u0438\u0444\u0430")
    options: list[GetApplicationIdTariffsResponse200DataItemOptionsItem] | None = Field(default=None, description="\u041e\u043f\u0446\u0438\u0438 \u0442\u0430\u0440\u0438\u0444\u0430")


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


class GetDailyStaffIdResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: SalaryStaffCalculationDaily | None = Field(default=None, alias="data")
    meta: ResponseMetaCountObject | None = Field(default=None)


class GetDepositHistoryDepositIdResponse200DataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    deposit_transaction: DepositTransaction | None = Field(default=None)
    deposit_transaction_type: DepositTransactionType | None = Field(default=None)


class GetIntegrationCallsResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: list[GetIntegrationCallsResponse200DataItem] | None = Field(default=None, alias="data", description="\u0421\u043f\u0438\u0441\u043e\u043a \u0437\u0432\u043e\u043d\u043a\u043e\u0432")
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


class PostAbonementIdSetBalanceRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    united_balance_services_count: float = Field(description="\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0443\u0441\u043b\u0443\u0433 \u0434\u043b\u044f \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430 \u0441 \u043e\u0431\u044a\u0435\u0434\u0438\u043d\u0435\u043d\u043d\u044b\u043c \u0431\u0430\u043b\u0430\u043d\u0441\u043e\u043c")
    services_balance_count: list[PostAbonementIdSetBalanceRequestServicesBalanceCountItem] = Field(description="\u041f\u0435\u0440\u0435\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u0435 \u0443\u0441\u043b\u0443\u0433\u0430-\u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0434\u043b\u044f \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430 \u0441 \u0440\u0430\u0437\u0434\u0435\u043b\u044c\u043d\u044b\u043c \u0431\u0430\u043b\u0430\u043d\u0441\u043e\u043c")


class PostActivityIdRecordsRequestClientClient(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    name: str = Field(description="\u0418\u043c\u044f.")
    phone_string: str = Field(description="\u0422\u0435\u043b\u0435\u0444\u043e\u043d.")
    email: str = Field(description="\u041f\u043e\u0447\u0442\u0430.")
    surname: str | None = Field(default=None, description="\u0424\u0430\u043c\u0438\u043b\u0438\u044f.")
    patronymic: str | None = Field(default=None, description="\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e.")
    sex: Literal[0, 1, 2] | None = Field(default=None, description="\u041f\u043e\u043b. (0 - \u043d\u0435\u0438\u0437\u0432\u0435\u0441\u0442\u0435\u043d, 1 - \u043c\u0443\u0436\u0441\u043a\u043e\u0439, 2 - \u0436\u0435\u043d\u0441\u043a\u0438\u0439.)")
    birthday: str | None = Field(default=None, description="\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f.")
    custom_field_values: list[PostActivityIdRecordsRequestClientClientCustomFieldValuesItem] | None = Field(default=None, description="\u0421\u043f\u0438\u0441\u043e\u043a \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0439 \u0434\u043e\u043f \u043f\u043e\u043b\u0435\u0439.")
    agreements: list[PostActivityIdRecordsRequestClientClientAgreementsItem] | None = Field(default=None, description="\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u0441\u043a\u0438\u0435 \u0441\u043e\u0433\u043b\u0430\u0448\u0435\u043d\u0438\u044f.")


class PostCardIdManualTransactionResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: LoyaltyCard2 | None = Field(default=None, alias="data")
    meta: dict[str, Any] | None = Field(default=None)


class PostCardIdManualTransactionResponse2002(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: LoyaltyCard2 | None = Field(default=None, alias="data")
    meta: dict[str, Any] | None = Field(default=None)


class PostCompanyIdSchedulesRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    original_entity_type: Literal["record", "activity"] = Field(description="\u0422\u0438\u043f \u0441\u0443\u0449\u043d\u043e\u0441\u0442\u0438, \u043d\u0430 \u043e\u0441\u043d\u043e\u0432\u0435 \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u0431\u0443\u0434\u0435\u0442 \u043f\u043e\u0441\u0442\u0440\u043e\u0435\u043d\u043e \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0435: `record` - \u0438\u043d\u0434\u0438\u0432\u0438\u0434\u0443\u0430\u043b\u044c\u043d\u0430\u044f \u0437\u0430\u043f\u0438\u0441\u044c, \u043d\u0435 \u043f\u043e\u0434\u0434\u0435\u0440\u0436\u0438\u0432\u0430\u0435\u0442\u0441\u044f \u0432 \u0442\u0435\u043a\u0443\u0449\u0438\u0439 \u043c\u043e\u043c\u0435\u043d\u0442; `activity` - \u0433\u0440\u0443\u043f\u043f\u043e\u0432\u043e\u0435 \u0441\u043e\u0431\u044b\u0442\u0438\u0435.")
    original_entity_id: float = Field(description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0441\u0443\u0449\u043d\u043e\u0441\u0442\u0438, \u043d\u0430 \u043e\u0441\u043d\u043e\u0432\u0435 \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u0431\u0443\u0434\u0435\u0442 \u043f\u043e\u0441\u0442\u0440\u043e\u0435\u043d\u043e \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0435.")
    date_end: str = Field(description="\u0414\u0430\u0442\u0430 \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f.")
    days: list[PostCompanyIdSchedulesRequestDaysItem] = Field(description="\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0441\u0435\u0440\u0438\u0439 \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f, \u043c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u043e 1 \u0441\u0435\u0440\u0438\u044f, \u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e 7 \u0441\u0435\u0440\u0438\u0439 (\u0441\u0435\u0440\u0438\u044f \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u0435\u0442 \u0434\u043d\u044e \u043d\u0435\u0434\u0435\u043b\u0438).")


class PostCompanyIdWaitingListRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    comment: str | None = Field(default=None, description="\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439")
    client_: PostCompanyIdWaitingListRequestClient = Field(alias="client")
    service_ids: list[Any] = Field(description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440\u044b \u0443\u0441\u043b\u0443\u0433")
    staff_ids: list[Any] | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440\u044b \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u043e\u0432")
    intervals: list[PostCompanyIdWaitingListRequestIntervalsItem] | None = Field(default=None, description="\u0418\u043d\u0442\u0435\u0440\u0432\u0430\u043b\u044b \u0434\u0430\u0442 \u0438 \u0432\u0440\u0435\u043c\u0435\u043d\u0438, \u043d\u0430 \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u043a\u043b\u0438\u0435\u043d\u0442 \u0445\u043e\u0447\u0435\u0442 \u0441\u043e\u0437\u0434\u0430\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c")


class PostInviteSalonIdRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    invites: list[PostInviteSalonIdRequestInvitesItem] = Field(description="\u041c\u0430\u0441\u0441\u0438\u0432 \u043f\u0440\u0438\u0433\u043b\u0430\u0448\u0435\u043d\u0438\u0439")


class PostLoyaltyAbonementTypesRequestAvailabilityItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    week_days: list[int] | None = Field(default=None, description="\u0414\u043d\u0438 \u043d\u0435\u0434\u0435\u043b\u0438, \u0432 \u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u0434\u0435\u0439\u0441\u0442\u0432\u0443\u0435\u0442 \u0443\u0441\u043b\u043e\u0432\u0438\u0435. (1 - \u043f\u043e\u043d\u0435\u0434\u0435\u043b\u044c\u043d\u0438\u043a, 7 - \u0432\u043e\u0441\u043a\u0440\u0435\u0441\u0435\u043d\u044c\u0435).")
    intervals: list[PostLoyaltyAbonementTypesRequestAvailabilityItemIntervalsItem] | None = Field(default=None, description="\u0418\u043d\u0442\u0435\u0440\u0432\u0430\u043b\u044b \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u043e\u0441\u0442\u0438.")


class PostPartnerPaymentResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0437\u0430\u043f\u0440\u043e\u0441\u0430.")
    data_: PostPartnerPaymentResponse200Data | None = Field(default=None, alias="data")


class PostPositionsQuickResponse201(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: Position | None = Field(default=None, alias="data")
    meta: dict[str, Any] | None = Field(default=None)


class PostRecordsRecordIdRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    attendance_service_item: PostRecordsRecordIdRequestAttendanceServiceItem
    attendance_good_items: list[PostRecordsRecordIdRequestAttendanceGoodItemsItem] | None = Field(default=None, description="\u0422\u043e\u0432\u0430\u0440\u044b.")
    comment: str | None = Field(default=None, description="\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439.")
    label_ids: list[int] | None = Field(default=None, description="\u0421\u043f\u0438\u0441\u043e\u043a \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440\u043e\u0432 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0439.")
    color: str | None = Field(default=None, description="\u0426\u0432\u0435\u0442.")
    clients_count: int = Field(description="\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u043e\u0441\u0435\u0442\u0438\u0442\u0435\u043b\u0435\u0439.")


class PostServiceIdStaffResponse201(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: MasterServiceLink2 | None = Field(default=None, alias="data")
    meta: dict[str, Any] | None = Field(default=None)


class PostUserIdCopyToCompaniesRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    user_company_links: list[PostUserIdCopyToCompaniesRequestUserCompanyLinksItem] = Field(description="\u0421\u043f\u0438\u0441\u043e\u043a \u0444\u0438\u043b\u0438\u0430\u043b\u043e\u0432, \u043a\u0443\u0434\u0430 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u0441\u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043f\u0440\u0430\u0432\u0430 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f")


class PostUserIdRemoveFromCompaniesRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    user_company_links: list[PostUserIdRemoveFromCompaniesRequestUserCompanyLinksItem] = Field(description="\u0421\u043f\u0438\u0441\u043e\u043a \u0444\u0438\u043b\u0438\u0430\u043b\u043e\u0432, \u043e\u0442\u043a\u0443\u0434\u0430 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u0443\u0434\u0430\u043b\u0438\u0442\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f")


class PutAbonementTypesLoyaltyAbonementTypeIdRequestAvailabilityItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    week_days: list[int] | None = Field(default=None, description="\u0414\u043d\u0438 \u043d\u0435\u0434\u0435\u043b\u0438, \u0432 \u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u0434\u0435\u0439\u0441\u0442\u0432\u0443\u0435\u0442 \u0443\u0441\u043b\u043e\u0432\u0438\u0435. (1 - \u043f\u043e\u043d\u0435\u0434\u0435\u043b\u044c\u043d\u0438\u043a, 7 - \u0432\u043e\u0441\u043a\u0440\u0435\u0441\u0435\u043d\u044c\u0435).")
    intervals: list[PutAbonementTypesLoyaltyAbonementTypeIdRequestAvailabilityItemIntervalsItem] | None = Field(default=None, description="\u0418\u043d\u0442\u0435\u0440\u0432\u0430\u043b\u044b \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u043e\u0441\u0442\u0438.")


class PutStaffMasterIdResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: MasterServiceLink2 | None = Field(default=None, alias="data")
    meta: dict[str, Any] | None = Field(default=None)


class PutStaffScheduleRequestSchedulesToSetItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    staff_id: float | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430.")
    dates: list[str] | None = Field(default=None, description="\u0414\u0430\u0442\u0430 \u0434\u043b\u044f \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 \u0433\u0440\u0430\u0444\u0438\u043a\u0430 \u0440\u0430\u0431\u043e\u0442\u044b \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430 \u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435 Y-m-d.")
    slots: list[PutStaffScheduleRequestSchedulesToSetItemSlotsItem] | None = Field(default=None, description="\u041c\u0430\u0441\u0441\u0438\u0432 \u0438\u043d\u0442\u0435\u0440\u0432\u0430\u043b\u043e\u0432 \u0432\u0440\u0435\u043c\u0435\u043d\u0438, \u043a\u043e\u0433\u0434\u0430 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a \u0440\u0430\u0431\u043e\u0442\u0430\u0435\u0442.")


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

    comment: str | None = Field(default=None, description="\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439")
    client_: PutWaitingListWaitingListEntryIdRequestClient = Field(alias="client")
    service_ids: list[Any] = Field(description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440\u044b \u0443\u0441\u043b\u0443\u0433")
    staff_ids: list[Any] | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440\u044b \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u043e\u0432")
    intervals: list[PutWaitingListWaitingListEntryIdRequestIntervalsItem] | None = Field(default=None, description="\u0418\u043d\u0442\u0435\u0440\u0432\u0430\u043b\u044b \u0434\u0430\u0442 \u0438 \u0432\u0440\u0435\u043c\u0435\u043d\u0438, \u043d\u0430 \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u043a\u043b\u0438\u0435\u043d\u0442 \u0445\u043e\u0447\u0435\u0442 \u0441\u043e\u0437\u0434\u0430\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c")


class AbonementTypeServiceLinksContainer(BaseModel):
    """Схема спеки: Объект модели "Баланс абонемента".
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    links: list[dict[str, Any]] | None = Field(default=None, description="\u041c\u0430\u0441\u0441\u0438\u0432 \u0443\u0441\u043b\u0443\u0433, \u043d\u0430 \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u0440\u0430\u0441\u043f\u0440\u043e\u0441\u0442\u0440\u0430\u043d\u044f\u0435\u0442\u0441\u044f \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442.")


class AnalyticsReportOverallChartDailyRow2(BaseModel):
    """Данные для построения диаграммы в разрезе по дням в отчете Основные показатели
    Схема спеки: Root Type for AnalyticsReportOverallChartRow
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    label: str | None = Field(default=None, description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0440\u044f\u0434\u0430 \u0434\u0430\u043d\u043d\u044b\u0445")
    data_: list[list[int]] | None = Field(default=None, alias="data", description="\u0414\u0430\u043d\u043d\u044b\u0435 \u0437\u0430 \u043a\u0430\u0436\u0434\u044b\u0439 \u0434\u0435\u043d\u044c. \u041a\u0430\u0436\u0434\u044b\u0439 \u0434\u0435\u043d\u044c - \u044d\u0442\u043e \u043c\u0430\u0441\u0441\u0438\u0432 \u0438\u0437 \u0434\u0432\u0443\u0445 \u0447\u0438\u0441\u0435\u043b. \u041f\u0435\u0440\u0432\u043e\u0435 \u0447\u0438\u0441\u043b\u043e - timestamp \u043d\u0430\u0447\u0430\u043b\u0430 \u0434\u043d\u044f \u0432 \u0437\u043e\u043d\u0435 UTC, \u0432\u0442\u043e\u0440\u043e\u0435 \u0447\u0438\u0441\u043b\u043e - \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043f\u043e\u043a\u0430\u0437\u0430\u0442\u0435\u043b\u044f \u0432 \u044d\u0442\u043e\u0442 \u0434\u0435\u043d\u044c.")


class AnalyticsReportOverallSumStats2(BaseModel):
    """Схема спеки: Root Type for AnalyticsReportOverallSumStats
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    current_sum: str | None = Field(default=None, description="\u0422\u0435\u043a\u0443\u0449\u0435\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043f\u043e\u043a\u0430\u0437\u0430\u0442\u0435\u043b\u044f")
    previous_sum: str | None = Field(default=None, description="\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043f\u043e\u043a\u0430\u0437\u0430\u0442\u0435\u043b\u044f \u0432 \u043f\u0440\u0435\u0434\u044b\u0434\u0443\u0449\u0435\u043c \u043f\u0435\u0440\u0438\u043e\u0434\u0435")
    change_percent: int | None = Field(default=None, description="\u041f\u0440\u043e\u0446\u0435\u043d\u0442 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u0442\u0435\u043a\u0443\u0449\u0435\u0433\u043e \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u043f\u043e\u043a\u0430\u0437\u0430\u0442\u0435\u043b\u044f \u043e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u043e \u043f\u0440\u043e\u0448\u043b\u043e\u0433\u043e. Null, \u0435\u0441\u043b\u0438 \u043f\u0440\u043e\u0448\u043b\u044b\u0439 \u043f\u043e\u043a\u0430\u0437\u0430\u0442\u0435\u043b\u044c \u0440\u0430\u0432\u0435\u043d 0, \u0430 \u0442\u0435\u043a\u0443\u0449\u0438\u0439 \u043e\u0442\u043b\u0438\u0447\u0435\u043d \u043e\u0442 0.")
    currency: Currency2 | None = Field(default=None)


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


class ClientCommentContainer(BaseModel):
    """Данные по комментарию к клиенту.
    Схема спеки: Объект модели "Комментарий к клиенту"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u044f \u043a \u043a\u043b\u0438\u0435\u043d\u0442\u0443.")
    create_date: str | None = Field(default=None, description="\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f \u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u044f \u043a \u043a\u043b\u0438\u0435\u043d\u0442\u0443.")
    update_date: str | None = Field(default=None, description="\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0433\u043e \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f \u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u044f \u043a \u043a\u043b\u0438\u0435\u043d\u0442\u0443.")
    type_: Literal["default", "file"] | None = Field(default=None, alias="type", description="\u0422\u0438\u043f \u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u044f \u043a \u043a\u043b\u0438\u0435\u043d\u0442\u0443: `default`: - \u0442\u0435\u043a\u0441\u0442\u043e\u0432\u044b\u0439 \u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439; `file`: - \u0437\u0430\u0433\u0440\u0443\u0436\u0435\u043d\u043d\u044b\u0439 \u0444\u0430\u0439\u043b.")
    text: str | None = Field(default=None, description="\u0422\u0435\u043a\u0441\u0442 \u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u044f \u043a \u043a\u043b\u0438\u0435\u043d\u0442\u0443 (`type` = \"default\", \u0434\u043b\u044f `type` = \"file\" \u0442\u0435\u043a\u0441\u0442 \u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u044f \u0432\u043e\u0437\u0432\u0440\u0430\u0449\u0430\u0435\u0442\u0441\u044f \u043f\u0443\u0441\u0442\u044b\u043c).")
    files: list[ClientCommentFileDto] | None = Field(default=None, description="\u0424\u0430\u0439\u043b\u044b \u0432 \u043a\u0430\u0440\u0442\u043e\u0447\u043a\u0435 \u043a\u043b\u0438\u0435\u043d\u0442\u0430, \u0437\u0430\u0433\u0440\u0443\u0437\u043a\u0430 \u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u043f\u043e\u0440\u043e\u0434\u0438\u043b\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u044f \u043a \u043a\u043b\u0438\u0435\u043d\u0442\u0443 (`type` = \"file\", \u0434\u043b\u044f `type` = \"default\" \u043c\u0430\u0441\u0441\u0438\u0432 \u0444\u0430\u0439\u043b\u043e\u0432 \u0432\u043e\u0437\u0432\u0440\u0430\u0449\u0430\u0435\u0442\u0441\u044f \u043f\u0443\u0441\u0442\u044b\u043c).")
    user: dict[str, Any] | None = Field(default=None, description="\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c, \u043e\u0441\u0442\u0430\u0432\u0438\u0432\u0448\u0438\u0439 \u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 \u043a \u043a\u043b\u0438\u0435\u043d\u0442\u0443 \u0438\u043b\u0438 \u0437\u0430\u0433\u0440\u0443\u0437\u0438\u0432\u0448\u0438\u0439 \u0444\u0430\u0439\u043b\u044b \u0432 \u043a\u0430\u0440\u0442\u043e\u0447\u043a\u0443 \u043a\u043b\u0438\u0435\u043d\u0442\u0430.")


class ClientVisitsHistoryRecordService(BaseModel):
    """Данные по услуге.
    Схема спеки: Объект модели "Услуга в записи истории посещений клиента"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0443\u0441\u043b\u0443\u0433\u0438.")
    title: str | None = Field(default=None, description="\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0443\u0441\u043b\u0443\u0433\u0438.")
    first_cost: float | None = Field(default=None, description="\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0443\u0441\u043b\u0443\u0433\u0438 \u0431\u0435\u0437 \u0441\u043a\u0438\u0434\u043a\u0438.")
    discount_percent: float | None = Field(default=None, description="\u041f\u0440\u043e\u0446\u0435\u043d\u0442 \u0441\u043a\u0438\u0434\u043a\u0438.")
    cost_to_pay: float | None = Field(default=None, description="\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0443\u0441\u043b\u0443\u0433\u0438 \u0441 \u0443\u0447\u0435\u0442\u043e\u043c \u0441\u043a\u0438\u0434\u043a\u0438.")
    paid_sum: float | None = Field(default=None, description="\u0421\u0443\u043c\u043c\u0430, \u043a\u043e\u0442\u043e\u0440\u0430\u044f \u0431\u044b\u043b\u0430 \u043e\u043f\u043b\u0430\u0447\u0435\u043d\u0430 \u043a\u043b\u0438\u0435\u043d\u0442\u043e\u043c.")
    payment_status: Literal["not_paid", "paid_not_full", "paid_full", "paid_over"] | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u043e\u043f\u043b\u0430\u0442\u044b \u0432\u0438\u0437\u0438\u0442\u0430: `not_paid` - \u0432\u0438\u0437\u0438\u0442 \u043d\u0435\u043e\u043f\u043b\u0430\u0447\u0435\u043d, \u043d\u0438\u043a\u0430\u043a\u0438\u0445 \u043e\u043f\u043b\u0430\u0442 \u043f\u043e \u0432\u0438\u0437\u0438\u0442\u0443 \u043d\u0435 \u043f\u0440\u043e\u0445\u043e\u0434\u0438\u043b\u043e; `paid_not_full` - \u0432\u0438\u0437\u0438\u0442 \u043e\u043f\u043b\u0430\u0447\u0435\u043d \u0447\u0430\u0441\u0442\u0438\u0447\u043d\u043e; `paid_full` - \u0432\u0438\u0437\u0438\u0442 \u043e\u043f\u043b\u0430\u0447\u0435\u043d \u043f\u043e\u043b\u043d\u043e\u0441\u0442\u044c\u044e, \u043f\u0435\u0440\u0435\u043f\u043b\u0430\u0442\u044b \u043d\u0435\u0442; `paid_over`...")
    consumables: list[ClientVisitsHistoryRecordServiceConsumable] | None = Field(default=None, description="\u0420\u0430\u0441\u0445\u043e\u0434\u043d\u0438\u043a\u0438 \u0442\u043e\u0432\u0430\u0440\u043e\u0432, \u043f\u0440\u0438\u043a\u0440\u0435\u043f\u043b\u0435\u043d\u043d\u044b\u0435 \u043a \u0434\u0430\u043d\u043d\u043e\u0439 \u0443\u0441\u043b\u0443\u0433\u0435.")


class CompanyStaffPositionListDataType(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data_: list[StaffPosition2] = Field(alias="data", description="\u041c\u0430\u0441\u0441\u0438\u0432 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438")
    meta: list[dict[str, Any]] = Field(description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u0441\u043e\u0434\u0435\u0440\u0436\u0438\u0442 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043d\u0430\u0439\u0434\u0435\u043d\u043d\u044b\u0445 \u0434\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u0435\u0439)")
    success: bool = Field(description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")


class ImageGroup2(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float = Field(alias="id", description="id \u0433\u0440\u0443\u043f\u043f\u044b \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0439")
    entity: str | None = Field(default=None, description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u0443\u0449\u043d\u043e\u0441\u0442\u0438, \u043a \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u043f\u0440\u0438\u0432\u044f\u0437\u0430\u043d\u0430 \u0433\u0440\u0443\u043f\u043f\u0430")
    entity_id: float | None = Field(default=None, description="Id \u0441\u0443\u0449\u043d\u043e\u0441\u0442\u0438")
    images: Image2
    image_binded: bool = Field(description="\u0421\u0442\u0430\u0442\u0443\u0441 \u043f\u0440\u0438\u0432\u044f\u0437\u043a\u0438 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0439 \u043a \u0441\u0443\u0449\u043d\u043e\u0441\u0442\u0438")
    image_group: dict[str, Any] = Field(description="\u041e\u0431\u044a\u0435\u043a\u0442 \u0433\u0440\u0443\u043f\u043f\u0430 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0439")


class LoyaltyAbonementTypeWithSalons(BaseModel):
    """Схема спеки: Объект модели "Тип абонемента"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0442\u0438\u043f\u0430 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430.")
    salon_group_id: float | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0441\u0435\u0442\u0438, \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u0434\u0435\u0439\u0441\u0442\u0432\u0443\u0435\u0442 \u0442\u0438\u043f \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430.")
    title: str | None = Field(default=None, description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0442\u0438\u043f\u0430 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u044b.")
    period: float | None = Field(default=None, description="\u0421\u0440\u043e\u043a \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430 (0, \u0435\u0441\u043b\u0438 \u043d\u0435 \u0437\u0430\u0434\u0430\u043d).")
    period_unit_id: float | None = Field(default=None, description="\u0415\u0434\u0438\u043d\u0438\u0446\u0430 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f \u0441\u0440\u043e\u043a\u0430 \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430 (1 - \u0434\u0435\u043d\u044c, 2 - \u043d\u0435\u0434\u0435\u043b\u044f, 3 - \u043c\u0435\u0441\u044f\u0446, 4 - \u0433\u043e\u0434, \u0435\u0441\u043b\u0438 \u043d\u0435 \u0437\u0430\u0434\u0430\u043d - 0).")
    allow_freeze: bool | None = Field(default=None, description="\u0414\u043e\u043f\u0443\u0441\u043a\u0430\u0435\u0442\u0441\u044f \u043b\u0438 \u0437\u0430\u043c\u043e\u0440\u043e\u0437\u043a\u0430 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u043e\u0432: true - \u0434\u043e\u043f\u0443\u0441\u043a\u0430\u0435\u0442\u0441\u044f, false - \u043d\u0435 \u0434\u043e\u043f\u0443\u0441\u043a\u0430\u0435\u0442\u0441\u044f.")
    freeze_limit: float | None = Field(default=None, description="\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u044b\u0439 \u043e\u0431\u0449\u0438\u0439 \u043f\u0435\u0440\u0438\u043e\u0434 \u0437\u0430\u043c\u043e\u0440\u043e\u0437\u043a\u0438.")
    freeze_limit_unit_id: float | None = Field(default=None, description="\u0415\u0434\u0438\u043d\u0438\u0446\u0430 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f \u0441\u0440\u043e\u043a\u0430 \u0437\u0430\u043c\u043e\u0440\u043e\u0437\u043a\u0438 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430 (1 - \u0434\u0435\u043d\u044c, 2 - \u043d\u0435\u0434\u0435\u043b\u044f, 3 - \u043c\u0435\u0441\u044f\u0446, 4 - \u0433\u043e\u0434).")
    is_allow_empty_code: bool | None = Field(default=None, description="\u0420\u0430\u0437\u0440\u0435\u0448\u0438\u0442\u044c \u043f\u0440\u043e\u0434\u0430\u0436\u0443 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430 \u0431\u0435\u0437 \u043a\u043e\u0434\u0430: true - \u0440\u0430\u0437\u0440\u0435\u0448\u0438\u0442\u044c, false - \u043d\u0435 \u0440\u0430\u0437\u0440\u0435\u0448\u0430\u0442\u044c.")
    is_united_balance: bool | None = Field(default=None, description="\u041e\u0431\u0449\u0438\u0439 \u0438\u043b\u0438 \u0440\u0430\u0437\u0434\u0435\u043b\u044c\u043d\u044b\u0439 \u0431\u0430\u043b\u0430\u043d\u0441 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430: true - \u043e\u0431\u0449\u0438\u0439, false - \u0440\u0430\u0437\u0434\u0435\u043b\u044c\u043d\u044b\u0439.")
    cost: float | None = Field(default=None, description="\u0426\u0435\u043d\u0430 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430.")
    expiration_type_id: float | None = Field(default=None, description="\u0422\u0438\u043f \u0430\u043a\u0442\u0438\u0432\u0430\u0446\u0438\u0438 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430 (1 - \u043f\u0440\u0438 \u043f\u0440\u043e\u0434\u0430\u0436\u0435, 2 - \u043f\u0440\u0438 \u043f\u0435\u0440\u0432\u043e\u043c \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u0438, 3 - \u0441 \u043a\u043e\u043d\u043a\u0440\u0435\u0442\u043d\u043e\u0439 \u0434\u0430\u0442\u044b).")
    is_online_sale_enabled: bool | None = Field(default=None, description="\u041e\u043d\u043b\u0430\u0439\u043d \u043f\u0440\u043e\u0434\u0430\u0436\u0430 (true - \u0440\u0430\u0437\u0440\u0435\u0448\u0435\u043d\u0430, false - \u0437\u0430\u043f\u0440\u0435\u0449\u0435\u043d\u0430).")
    online_sale_title: str | None = Field(default=None, description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430 \u043f\u0440\u0438 \u043e\u043d\u043b\u0430\u0439\u043d \u043f\u0440\u043e\u0434\u0430\u0436\u0435.")
    online_sale_description: str | None = Field(default=None, description="\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430 \u043f\u0440\u0438 \u043e\u043d\u043b\u0430\u0439\u043d \u043f\u0440\u043e\u0434\u0430\u0436\u0435.")
    online_sale_price: float | None = Field(default=None, description="\u0426\u0435\u043d\u0430 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430 \u043f\u0440\u0438 \u043f\u0440\u043e\u0434\u0430\u0436\u0435 \u043e\u043d\u043b\u0430\u0439\u043d.")
    service_price_correction: bool | None = Field(default=None, description="\u0412\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u044c \u043a\u043e\u0440\u0440\u0435\u043a\u0442\u0438\u0440\u043e\u0432\u043a\u0438 \u0446\u0435\u043d\u044b \u0443\u0441\u043b\u0443\u0433\u0438 \u043f\u0440\u0438 \u043f\u0440\u0438\u043c\u0435\u043d\u0435\u043d\u0438\u0438 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430.")
    united_balance_services_count: float | None = Field(default=None, description="\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u0439 \u0434\u043b\u044f \u043e\u0431\u0449\u0435\u0433\u043e \u0431\u0430\u043b\u0430\u043d\u0441\u0430.")
    autoactivation_time: float | None = Field(default=None, description="\u041a\u043e\u043b-\u0432\u043e \u0435\u0434\u0438\u043d\u0438\u0446 \u0432\u0440\u0435\u043c\u0435\u043d\u0438 \u0434\u043b\u044f \u0430\u0432\u0442\u043e\u0430\u043a\u0442\u0438\u0432\u0430\u0446\u0438\u0438 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430.")
    autoactivation_time_unit_id: int | None = Field(default=None, description="\u0415\u0434\u0438\u043d\u0438\u0446\u044b \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f \u0434\u043b\u044f \u0430\u0432\u0442\u043e\u0430\u043a\u0442\u0438\u0432\u0430\u0446\u0438\u0438 (1 - \u0434\u043d\u0438, 2 - \u043d\u0435\u0434\u0435\u043b\u0438, 3 - \u043c\u0435\u0441\u044f\u0446\u044b, 4 - \u0433\u043e\u0434\u044b).")
    attached_salon_ids: list[float] | None = Field(default=None, description="\u0421\u043f\u0438\u0441\u043e\u043a ID \u043f\u0440\u0438\u043a\u0440\u0435\u043f\u043b\u0451\u043d\u043d\u044b\u0445 \u043a \u0442\u0438\u043f\u0443 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430 \u0444\u0438\u043b\u0438\u0430\u043b\u043e\u0432.")
    online_sale_image: str | None = Field(default=None, description="\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u043f\u0440\u0438 \u043e\u043d\u043b\u0430\u0439\u043d \u043f\u0440\u043e\u0434\u0430\u0436\u0435.")
    availability: list[dict[str, Any]] | None = Field(default=None, description="\u0421\u043f\u0438\u0441\u043e\u043a \u0443\u0441\u043b\u043e\u0432\u0438\u0439 \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u043e\u0441\u0442\u0438 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430.")
    balance_container: dict[str, Any] | None = Field(default=None, description="\u041e\u0431\u044a\u0435\u043a\u0442 \u0441 \u043c\u0430\u0441\u0441\u0438\u0432\u043e\u043c \u043f\u0440\u0438\u043a\u0440\u0435\u043f\u043b\u0435\u043d\u043d\u044b\u0445 \u0443\u0441\u043b\u0443\u0433 \u0438/\u0438\u043b\u0438 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0439 \u0438 \u0438\u0445 \u0431\u0430\u043b\u0430\u043d\u0441\u043e\u043c.")


class LoyaltyGenerateCode200Option2(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool = Field(description="\u0444\u043b\u0430\u0433 \u043f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u044e\u0449\u0438\u0439, \u0447\u0442\u043e \u043e\u0442\u0432\u0435\u0442 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d \u0431\u0435\u0437 \u043e\u0448\u0438\u0431\u043e\u043a (true)")
    data_: LoyaltyGenerateCode200DataOption2 = Field(alias="data")
    meta: list[dict[str, Any]] = Field(description="\u043c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435 (\u043f\u0443\u0441\u0442\u043e\u0439 \u043c\u0430\u0441\u0441\u0438\u0432)")


class LoyaltyProgram2(BaseModel):
    """Акция лояльности
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="\u0418\u0434\u0435\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0430\u043a\u0446\u0438\u0438")
    title: str | None = Field(default=None, description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0430\u043a\u0446\u0438\u0438")
    type_: Literal["discount_static", "discount_accumulative_visits", "discount_accumulative_sold", "discount_accumulative_paid", "cashback_static_sold", "cashback_static_paid", "cashback_accumulative_paid", "cashback_accumulative_sold", "cashback_accumulative_paid_visits", "cashback_accumulative_sold_visits", "cashback_sold_visits", "cashback_paid_visits", "package_discount"] | None = Field(default=None, alias="type", description="\u0422\u0438\u043f \u0430\u043a\u0446\u0438\u0438")
    service_item_type: Literal["any_allowed", "not_allowed", "custom_allowed"] | None = Field(default=None, description="\u0422\u0438\u043f \u043f\u0440\u0438\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u043a \u0443\u0441\u043b\u0443\u0433\u0430\u043c")
    good_item_type: Literal["any_allowed", "not_allowed", "custom_allowed"] | None = Field(default=None, description="\u0422\u0438\u043f \u043f\u0440\u0438\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u043a \u0442\u043e\u0432\u0430\u0440\u0430\u043c")
    value_unit: Literal["percent", "amount"] | None = Field(default=None, description="\u0415\u0434\u0438\u043d\u0438\u0446\u0430 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f \u0431\u043e\u043d\u0443\u0441\u0430 \u0438\u043b\u0438 \u0441\u043a\u0438\u0434\u043a\u0438 (\u043f\u0440\u043e\u0446\u0435\u043d\u0442, \u0444\u0438\u043a\u0441\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u0430\u044f \u0441\u0443\u043c\u043c\u0430)")
    usage_limit: int | None = Field(default=None, description="\u041e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u0435 \u043f\u043e \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u0443 \u043f\u0440\u0438\u043c\u0435\u043d\u0435\u043d\u0438\u0439 (\u0442\u043e\u043b\u044c\u043a\u043e \u0434\u043b\u044f \u043a\u044d\u0448\u0431\u0435\u043a\u0430)")
    visit_multiplicity: int | None = Field(default=None, description="\u041a\u0440\u0430\u0442\u043d\u043e\u0441\u0442\u044c \u043f\u0440\u0438\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u043f\u043e \u0432\u0438\u0437\u0438\u0442\u0430\u043c (\u0442\u043e\u043b\u044c\u043a\u043e \u0434\u043b\u044f \u043a\u044d\u0448\u0431\u0435\u043a\u0430)")
    sold_items_multiplicity: int | None = Field(default=None, description="\u0421\u043a\u043e\u043b\u044c\u043a\u043e \u0443\u0441\u043b\u0443\u0433 \u043d\u0443\u0436\u043d\u043e \u043e\u043f\u043b\u0430\u0442\u0438\u0442\u044c, \u0447\u0442\u043e\u0431\u044b \u043f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0441\u043a\u0438\u0434\u043a\u0443 \u043d\u0430 \u0430\u043a\u0446\u0438\u043e\u043d\u043d\u044b\u0435 \u0443\u0441\u043b\u0443\u0433\u0438 (\u0442\u043e\u043b\u044c\u043a\u043e \u0434\u043b\u044f \u0442\u0438\u043f\u0430 \u0430\u043a\u0446\u0438\u0438 \"\u0421\u043a\u0438\u0434\u043a\u0430 \u043f\u043e \u0443\u0441\u043b\u043e\u0432\u0438\u044e\")")
    expiration_timeout: int | None = Field(default=None, description="\u0421\u0440\u043e\u043a \u0441\u0433\u043e\u0440\u0430\u043d\u0438\u044f \u0431\u043e\u043d\u0443\u0441\u043e\u0432 \u0438\u043b\u0438 \u0441\u043a\u0438\u0434\u043a\u0438")
    expiration_timeout_unit: Literal["day", "week", "month", "year"] | None = Field(default=None, description="\u0415\u0434\u0438\u043d\u0438\u0446\u0430 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f \u0441\u0440\u043e\u043a\u0430 \u0441\u0433\u043e\u0440\u0430\u043d\u0438\u044f \u0431\u043e\u043d\u0443\u0441\u043e\u0432 \u0438\u043b\u0438 \u0441\u043a\u0438\u0434\u043a\u0438")
    expiration_notification_timeout: int | None = Field(default=None, description="\u0417\u0430 \u0441\u043a\u043e\u043b\u044c\u043a\u043e \u0434\u043d\u0435\u0439 \u0434\u043e \u043d\u0430\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u044f \u0441\u0440\u043e\u043a\u0430 \u0441\u0433\u043e\u0440\u0430\u043d\u0438\u044f \u0431\u043e\u043d\u0443\u0441\u0430 \u0438\u043b\u0438 \u0441\u043a\u0438\u0434\u043a\u0438 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u043e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u043a\u043b\u0438\u0435\u043d\u0442\u0443 \u0443\u0432\u0435\u0434\u043e\u043c\u043b\u0435\u043d\u0438\u0435")
    params_source_type: Literal["loyalty_card", "active_companies", "chain"] | None = Field(default=None, description="\u041e\u0442\u043a\u0443\u0434\u0430 \u0431\u0440\u0430\u0442\u044c \u0438\u0441\u0442\u043e\u0440\u0438\u044e \u043a\u043b\u0438\u0435\u043d\u0442\u0430 \u0434\u043b\u044f \u0440\u0430\u0441\u0447\u0435\u0442\u0430 \u0440\u0430\u0437\u043c\u0435\u0440\u0430 \u0431\u043e\u043d\u0443\u0441\u0430 \u0438\u043b\u0438 \u0441\u043a\u0438\u0434\u043a\u0438 (\u0434\u043b\u044f \u043d\u0430\u043a\u043f\u043e\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0445 \u0430\u043a\u0446\u0438\u0439 \u0438\u043b\u0438 \u0441\u043a\u0438\u0434\u043a\u0438 \u043f\u043e \u0443\u0441\u043b\u043e\u0432\u0438\u044e)")
    history_start_date: str | None = Field(default=None, description="\u0421 \u043a\u0430\u043a\u043e\u0439 \u0434\u0430\u0442\u044b \u0443\u0447\u0438\u0442\u044b\u0432\u0430\u0442\u044c \u0438\u0441\u0442\u043e\u0440\u0438\u044e \u043a\u043b\u0438\u0435\u043d\u0442\u0430 \u0434\u043b\u044f \u0440\u0430\u0441\u0447\u0435\u0442\u0430 \u0440\u0430\u0437\u043c\u0435\u0440\u0430 \u0431\u043e\u043d\u0443\u0441\u0430 \u0438\u043b\u0438 \u0441\u043a\u0438\u0434\u043a\u0438 (\u0434\u043b\u044f \u043d\u0430\u043a\u043e\u043f\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0445 \u0430\u043a\u0446\u0438\u0439 \u0438\u043b\u0438 \u0441\u043a\u0438\u0434\u043a\u0438 \u043f\u043e \u0443\u0441\u043b\u043e\u0432\u0438\u044e)")
    on_changed_notification_template_id: int | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0448\u0430\u0431\u043b\u043e\u043d\u0430 \u0443\u0432\u0435\u0434\u043e\u043c\u043b\u0435\u043d\u0438\u044f \u043f\u0440\u0438 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0438 \u0431\u043e\u043d\u0443\u0441\u0430 \u0438\u043b\u0438 \u0441\u043a\u0438\u0434\u043a\u0438")
    on_expiration_notification_template_id: int | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0448\u0430\u0431\u043b\u043e\u043d\u0430 \u0443\u0432\u0435\u0434\u043e\u043c\u043b\u0435\u043d\u0438\u044f \u043f\u0440\u0438 \u0441\u0433\u043e\u0440\u0430\u043d\u0438\u0438 \u0431\u043e\u043d\u0443\u0441\u0430 \u0438\u043b\u0438 \u0441\u043a\u0438\u0434\u043a\u0438")
    loyalty_card_types: list[LoyaltyCardType2] | None = Field(default=None, description="\u0422\u0438\u043f \u043a\u0430\u0440\u0442, \u0434\u043b\u044f \u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u0434\u0435\u0439\u0441\u0442\u0432\u0443\u0435\u0442 \u0430\u043a\u0446\u0438\u044f (\u043f\u043e \u0437\u0430\u043f\u0440\u043e\u0441\u0443)")
    on_changed_notification_template: LoyaltyNotificationMessageTemplate2 | None = Field(default=None)
    on_expiration_notification_template: LoyaltyNotificationMessageTemplate2 | None = Field(default=None)
    rules: list[LoyaltyProgramRule2] | None = Field(default=None, description="\u041f\u0440\u0430\u0432\u0438\u043b\u0430 \u0434\u043b\u044f \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u044f \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u0431\u043e\u043d\u0443\u0441\u0430 \u0438\u043b\u0438 \u0441\u043a\u0438\u0434\u043a\u0438 (\u0434\u043e\u043f\u0443\u0441\u0442\u0438\u043c\u043e \u0442\u043e\u043b\u044c\u043a\u043e \u043e\u0434\u043d\u043e \u043f\u0440\u0430\u0432\u0438\u043b\u043e \u0434\u043b\u044f \u0444\u0438\u043a\u0441\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0445 \u0430\u043a\u0446\u0438\u0439) (\u043f\u043e \u0437\u0430\u043f\u0440\u043e\u0441\u0443)")
    companies: list[Company2] | None = Field(default=None, description="\u0424\u0438\u043b\u0438\u0430\u043b\u044b, \u0432 \u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u0434\u0435\u0439\u0441\u0442\u0432\u0443\u0435\u0442 \u0430\u043a\u0446\u0438\u044f (\u043f\u043e \u0437\u0430\u043f\u0440\u043e\u0441\u0443)")
    applicable_items: list[LoyaltyEntityAttendanceItem2] | None = Field(default=None, description="\u0421\u0432\u044f\u0437\u0430\u043d\u043d\u044b\u0435 \u0441\u0443\u0449\u043d\u043e\u0441\u0442\u0438 \u0434\u043b\u044f \u0432\u044b\u0431\u043e\u0440\u043e\u0447\u043d\u043e\u0433\u043e \u043f\u0440\u0438\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u0430\u043a\u0446\u0438\u0438 (\u043f\u043e \u0437\u0430\u043f\u0440\u043e\u0441\u0443)")


class LoyaltyProgramCreateRequest2(BaseModel):
    """Тело запроса на создание акции лояльности
    Схема спеки: Root Type for LoyaltyProgramCreateRequest
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    title: str = Field(description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0430\u043a\u0446\u0438\u0438")
    type_: Literal["discount_static", "discount_accumulative_visits", "discount_accumulative_sold", "discount_accumulative_paid", "cashback_static_sold", "cashback_static_paid", "cashback_accumulative_paid", "cashback_accumulative_sold", "cashback_accumulative_paid_visits", "cashback_accumulative_sold_visits", "cashback_sold_visits", "cashback_paid_visits", "package_discount"] = Field(alias="type", description="\u0422\u0438\u043f \u0430\u043a\u0446\u0438\u0438")
    service_item_type: Literal["any_allowed", "not_allowed", "custom_allowed"] = Field(description="\u0422\u0438\u043f \u043f\u0440\u0438\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u043a \u0443\u0441\u043b\u0443\u0433\u0430\u043c")
    good_item_type: Literal["any_allowed", "not_allowed", "custom_allowed"] = Field(description="\u0422\u0438\u043f \u043f\u0440\u0438\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u043a \u0442\u043e\u0432\u0430\u0440\u0430\u043c")
    value_unit: Literal["percent", "amount"] = Field(description="\u0415\u0434\u0438\u043d\u0438\u0446\u0430 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f \u0431\u043e\u043d\u0443\u0441\u0430 \u0438\u043b\u0438 \u0441\u043a\u0438\u0434\u043a\u0438 (\u043f\u0440\u043e\u0446\u0435\u043d\u0442, \u0444\u0438\u043a\u0441\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u0430\u044f \u0441\u0443\u043c\u043c\u0430)")
    usage_limit: int | None = Field(default=None, description="\u041e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u0435 \u043f\u043e \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u0443 \u043f\u0440\u0438\u043c\u0435\u043d\u0435\u043d\u0438\u0439 (\u0442\u043e\u043b\u044c\u043a\u043e \u0434\u043b\u044f \u043a\u044d\u0448\u0431\u0435\u043a\u0430)")
    visit_multiplicity: int | None = Field(default=None, description="\u041a\u0440\u0430\u0442\u043d\u043e\u0441\u0442\u044c \u043f\u0440\u0438\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u043f\u043e \u0432\u0438\u0437\u0438\u0442\u0430\u043c (\u0442\u043e\u043b\u044c\u043a\u043e \u0434\u043b\u044f \u043a\u044d\u0448\u0431\u0435\u043a\u0430)")
    sold_items_multiplicity: int | None = Field(default=None, description="\u0421\u043a\u043e\u043b\u044c\u043a\u043e \u0443\u0441\u043b\u0443\u0433 \u043d\u0443\u0436\u043d\u043e \u043e\u043f\u043b\u0430\u0442\u0438\u0442\u044c, \u0447\u0442\u043e\u0431\u044b \u043f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0441\u043a\u0438\u0434\u043a\u0443 \u043d\u0430 \u0430\u043a\u0446\u0438\u043e\u043d\u043d\u044b\u0435 \u0443\u0441\u043b\u0443\u0433\u0438 (\u0442\u043e\u043b\u044c\u043a\u043e \u0434\u043b\u044f \u0442\u0438\u043f\u0430 \u0430\u043a\u0446\u0438\u0438 \"\u0421\u043a\u0438\u0434\u043a\u0430 \u043f\u043e \u0443\u0441\u043b\u043e\u0432\u0438\u044e\")")
    expiration_timeout: int | None = Field(default=None, description="\u0421\u0440\u043e\u043a \u0441\u0433\u043e\u0440\u0430\u043d\u0438\u044f \u0431\u043e\u043d\u0443\u0441\u043e\u0432 \u0438\u043b\u0438 \u0441\u043a\u0438\u0434\u043a\u0438")
    expiration_timeout_unit: Literal["day", "week", "month", "year"] | None = Field(default=None, description="\u0415\u0434\u0438\u043d\u0438\u0446\u0430 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f \u0441\u0440\u043e\u043a\u0430 \u0441\u0433\u043e\u0440\u0430\u043d\u0438\u044f \u0431\u043e\u043d\u0443\u0441\u043e\u0432 \u0438\u043b\u0438 \u0441\u043a\u0438\u0434\u043a\u0438")
    expiration_notification_timeout: int | None = Field(default=None, description="\u0417\u0430 \u0441\u043a\u043e\u043b\u044c\u043a\u043e \u0434\u043d\u0435\u0439 \u0434\u043e \u043d\u0430\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u044f \u0441\u0440\u043e\u043a\u0430 \u0441\u0433\u043e\u0440\u0430\u043d\u0438\u044f \u0431\u043e\u043d\u0443\u0441\u0430 \u0438\u043b\u0438 \u0441\u043a\u0438\u0434\u043a\u0438 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u043e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u043a\u043b\u0438\u0435\u043d\u0442\u0443 \u0443\u0432\u0435\u0434\u043e\u043c\u043b\u0435\u043d\u0438\u0435")
    params_source_type: Literal["loyalty_card", "active_companies", "chain"] | None = Field(default=None, description="\u041e\u0442\u043a\u0443\u0434\u0430 \u0431\u0440\u0430\u0442\u044c \u0438\u0441\u0442\u043e\u0440\u0438\u044e \u043a\u043b\u0438\u0435\u043d\u0442\u0430 \u0434\u043b\u044f \u0440\u0430\u0441\u0447\u0435\u0442\u0430 \u0440\u0430\u0437\u043c\u0435\u0440\u0430 \u0431\u043e\u043d\u0443\u0441\u0430 \u0438\u043b\u0438 \u0441\u043a\u0438\u0434\u043a\u0438 (\u0434\u043b\u044f \u043d\u0430\u043a\u043f\u043e\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0445 \u0430\u043a\u0446\u0438\u0439 \u0438\u043b\u0438 \u0441\u043a\u0438\u0434\u043a\u0438 \u043f\u043e \u0443\u0441\u043b\u043e\u0432\u0438\u044e)")
    history_start_date: str | None = Field(default=None, description="\u0421 \u043a\u0430\u043a\u043e\u0439 \u0434\u0430\u0442\u044b \u0443\u0447\u0438\u0442\u044b\u0432\u0430\u0442\u044c \u0438\u0441\u0442\u043e\u0440\u0438\u044e \u043a\u043b\u0438\u0435\u043d\u0442\u0430 \u0434\u043b\u044f \u0440\u0430\u0441\u0447\u0435\u0442\u0430 \u0440\u0430\u0437\u043c\u0435\u0440\u0430 \u0431\u043e\u043d\u0443\u0441\u0430 \u0438\u043b\u0438 \u0441\u043a\u0438\u0434\u043a\u0438 (\u0434\u043b\u044f \u043d\u0430\u043a\u043e\u043f\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0445 \u0430\u043a\u0446\u0438\u0439 \u0438\u043b\u0438 \u0441\u043a\u0438\u0434\u043a\u0438 \u043f\u043e \u0443\u0441\u043b\u043e\u0432\u0438\u044e)")
    loyalty_card_type_ids: list[int] | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440\u044b \u0442\u0438\u043f\u043e\u0432 \u043a\u0430\u0440\u0442, \u0434\u043b\u044f \u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u0434\u0435\u0439\u0441\u0442\u0432\u0443\u0435\u0442 \u0430\u043a\u0446\u0438\u044f")
    on_changed_notification_template: LoyaltyNotificationMessageTemplateRequest2 | None = Field(default=None)
    on_expiration_notification_template: LoyaltyNotificationMessageTemplateRequest2 | None = Field(default=None)
    rules: list[LoyaltyProgramRuleRequest2] = Field(description="\u041f\u0440\u0430\u0432\u0438\u043b\u0430 \u0434\u043b\u044f \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u044f \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u0431\u043e\u043d\u0443\u0441\u0430 \u0438\u043b\u0438 \u0441\u043a\u0438\u0434\u043a\u0438 (\u0434\u043e\u043f\u0443\u0441\u0442\u0438\u043c\u043e \u0442\u043e\u043b\u044c\u043a\u043e \u043e\u0434\u043d\u043e \u043f\u0440\u0430\u0432\u0438\u043b\u043e \u0434\u043b\u044f \u0444\u0438\u043a\u0441\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0445 \u0430\u043a\u0446\u0438\u0439)")
    company_ids: list[int] = Field(description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440\u044b \u0444\u0438\u043b\u0438\u0430\u043b\u043e\u0432, \u0432 \u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u0434\u0435\u0439\u0441\u0442\u0432\u0443\u0435\u0442 \u0430\u043a\u0446\u0438\u044f")
    allowed_service_ids: list[int] | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440\u044b \u0443\u0441\u043b\u0443\u0433 \u0438 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0439 \u0443\u0441\u043b\u0443\u0433 (\u0435\u0441\u043b\u0438 \u0437\u0430\u0434\u0430\u043d \u0442\u0438\u043f \u043f\u0440\u0438\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u0434\u043b\u044f \u043d\u0435\u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u0443\u0441\u043b\u0443\u0433)")
    allowed_good_ids: list[int] | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440\u044b \u0442\u043e\u0432\u0430\u0440\u043e\u0432 (\u0435\u0441\u043b\u0438 \u0437\u0430\u0434\u0430\u043d \u0442\u0438\u043f \u043f\u0440\u0438\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u0434\u043b\u044f \u043d\u0435\u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u0442\u043e\u0432\u0430\u0440\u043e\u0432)")
    allowed_good_category_ids: list[int] | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440\u044b \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0439 \u0442\u043e\u0432\u0430\u0440\u043e\u0432 (\u0435\u0441\u043b\u0438 \u0437\u0430\u0434\u0430\u043d \u0442\u0438\u043f \u043f\u0440\u0438\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u0434\u043b\u044f \u043d\u0435\u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u0442\u043e\u0432\u0430\u0440\u043e\u0432)")


class LoyaltyProgramUpdateRequest2(BaseModel):
    """Тело запроса на изменение акции лояльности
    Схема спеки: Root Type for LoyaltyProgramUpdateRequest
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    title: str | None = Field(default=None, description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0430\u043a\u0446\u0438\u0438")
    usage_limit: int | None = Field(default=None, description="\u041e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u0435 \u043f\u043e \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u0443 \u043f\u0440\u0438\u043c\u0435\u043d\u0435\u043d\u0438\u0439 (\u0442\u043e\u043b\u044c\u043a\u043e \u0434\u043b\u044f \u043a\u044d\u0448\u0431\u0435\u043a\u0430)")
    expiration_timeout: int | None = Field(default=None, description="\u0421\u0440\u043e\u043a \u0441\u0433\u043e\u0440\u0430\u043d\u0438\u044f \u0431\u043e\u043d\u0443\u0441\u043e\u0432 \u0438\u043b\u0438 \u0441\u043a\u0438\u0434\u043a\u0438")
    expiration_timeout_unit: Literal["day", "week", "month", "year"] | None = Field(default=None, description="\u0415\u0434\u0438\u043d\u0438\u0446\u0430 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f \u0441\u0440\u043e\u043a\u0430 \u0441\u0433\u043e\u0440\u0430\u043d\u0438\u044f \u0431\u043e\u043d\u0443\u0441\u043e\u0432 \u0438\u043b\u0438 \u0441\u043a\u0438\u0434\u043a\u0438")
    expiration_notification_timeout: int | None = Field(default=None, description="\u0417\u0430 \u0441\u043a\u043e\u043b\u044c\u043a\u043e \u0434\u043d\u0435\u0439 \u0434\u043e \u043d\u0430\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u044f \u0441\u0440\u043e\u043a\u0430 \u0441\u0433\u043e\u0440\u0430\u043d\u0438\u044f \u0431\u043e\u043d\u0443\u0441\u0430 \u0438\u043b\u0438 \u0441\u043a\u0438\u0434\u043a\u0438 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u043e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u043a\u043b\u0438\u0435\u043d\u0442\u0443 \u0443\u0432\u0435\u0434\u043e\u043c\u043b\u0435\u043d\u0438\u0435")
    loyalty_card_type_ids: list[int] | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440\u044b \u0442\u0438\u043f\u043e\u0432 \u043a\u0430\u0440\u0442, \u0434\u043b\u044f \u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u0434\u0435\u0439\u0441\u0442\u0432\u0443\u0435\u0442 \u0430\u043a\u0446\u0438\u044f")
    on_changed_notification_template: LoyaltyNotificationMessageTemplateRequest2 | None = Field(default=None)
    on_expiration_notification_template: LoyaltyNotificationMessageTemplateRequest2 | None = Field(default=None)
    rules: list[LoyaltyProgramRuleRequest2] | None = Field(default=None, description="\u041f\u0440\u0430\u0432\u0438\u043b\u0430 \u0434\u043b\u044f \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u044f \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u0431\u043e\u043d\u0443\u0441\u0430 \u0438\u043b\u0438 \u0441\u043a\u0438\u0434\u043a\u0438 (\u0434\u043e\u043f\u0443\u0441\u0442\u0438\u043c\u043e \u0442\u043e\u043b\u044c\u043a\u043e \u043e\u0434\u043d\u043e \u043f\u0440\u0430\u0432\u0438\u043b\u043e \u0434\u043b\u044f \u0444\u0438\u043a\u0441\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0445 \u0430\u043a\u0446\u0438\u0439)")
    company_ids: list[int] | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440\u044b \u0444\u0438\u043b\u0438\u0430\u043b\u043e\u0432, \u0432 \u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u0434\u0435\u0439\u0441\u0442\u0432\u0443\u0435\u0442 \u0430\u043a\u0446\u0438\u044f")
    allowed_service_ids: list[int] | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440\u044b \u0443\u0441\u043b\u0443\u0433 \u0438 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0439 \u0443\u0441\u043b\u0443\u0433 (\u0435\u0441\u043b\u0438 \u0437\u0430\u0434\u0430\u043d \u0442\u0438\u043f \u043f\u0440\u0438\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u0434\u043b\u044f \u043d\u0435\u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u0443\u0441\u043b\u0443\u0433)")
    allowed_good_ids: list[int] | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440\u044b \u0442\u043e\u0432\u0430\u0440\u043e\u0432 (\u0435\u0441\u043b\u0438 \u0437\u0430\u0434\u0430\u043d \u0442\u0438\u043f \u043f\u0440\u0438\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u0434\u043b\u044f \u043d\u0435\u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u0442\u043e\u0432\u0430\u0440\u043e\u0432)")
    allowed_good_category_ids: list[int] | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440\u044b \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0439 \u0442\u043e\u0432\u0430\u0440\u043e\u0432 (\u0435\u0441\u043b\u0438 \u0437\u0430\u0434\u0430\u043d \u0442\u0438\u043f \u043f\u0440\u0438\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u0434\u043b\u044f \u043d\u0435\u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u0442\u043e\u0432\u0430\u0440\u043e\u0432)")


class MasterWithPosition(BaseModel):
    """Схема спеки: Объект модели "Сотрудник с Должностью"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430.")
    name: str | None = Field(default=None, description="\u0418\u043c\u044f \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430.")
    company_id: float | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0444\u0438\u043b\u0438\u0430\u043b\u0430, \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u043c \u0441\u043e\u0437\u0434\u0430\u043d \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a.")
    specialization: str | None = Field(default=None, description="\u0421\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430.")
    avatar: str | None = Field(default=None, description="\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0430\u0432\u0430\u0442\u0430\u0440 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430 (\u0443\u043c\u0435\u043d\u044c\u0448\u0435\u043d\u043d\u044b\u0439).")
    avatar_big: str | None = Field(default=None, description="\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0430\u0432\u0430\u0442\u0430\u0440 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430 (\u043e\u0440\u0438\u0433\u0438\u043d\u0430\u043b\u044c\u043d\u044b\u0439).")
    position: dict[str, Any] | None = Field(default=None, description="\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c, \u043a \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u043f\u0440\u0438\u0432\u044f\u0437\u0430\u043d \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a.")


class SalaryPayrollCalculationItemContainer(BaseModel):
    """Схема спеки: Объект позиции начисления заработной платы
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    date: str | None = Field(default=None, description="\u0414\u0430\u0442\u0430.")
    time: str | None = Field(default=None, description="\u0412\u0440\u0435\u043c\u044f.")
    item_id: float | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0441\u0443\u0449\u043d\u043e\u0441\u0442\u0438, \u0437\u0430 \u0447\u0442\u043e \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0441\u044f \u043d\u0430\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u0435 (\u043d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0437\u0430\u043f\u0438\u0441\u0438 \u0438\u043b\u0438 \u043f\u0440\u043e\u0434\u0430\u0436\u0438 \u0442\u043e\u0432\u0430\u0440\u0430).")
    item_type_slug: Literal["periodic", "sale", "record", "bonus", "penalty", "retro_bonus", "activity"] | None = Field(default=None, description="\u0422\u0438\u043f \u0441\u0443\u0449\u043d\u043e\u0441\u0442\u0438, \u0437\u0430 \u0447\u0442\u043e \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0441\u044f \u043d\u0430\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u0435 (\u043d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, \u0437\u0430\u043f\u0438\u0441\u044c \u0438\u043b\u0438 \u043f\u0440\u043e\u0434\u0430\u0436\u0430 \u0442\u043e\u0432\u0430\u0440\u0430).")
    salary_sum: str | None = Field(default=None, description="\u0421\u0443\u043c\u043c\u0430 \u043d\u0430\u0447\u0438\u0441\u043b\u0435\u043d\u043d\u043e\u0439 \u0437\u0430\u0440\u0430\u0431\u043e\u0442\u043d\u043e\u0439 \u043f\u043b\u0430\u0442\u044b.")
    record_id: float | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0437\u0430\u043f\u0438\u0441\u0438.")
    client_id: float | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043a\u043b\u0438\u0435\u043d\u0442\u0430.")
    cost: str | None = Field(default=None, description="\u0411\u0430\u0437\u043e\u0432\u0430\u044f \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c.")
    paid: dict[str, Any] | None = Field(default=None, description="\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e\u0431 \u043e\u043f\u043b\u0430\u0442\u0435.")
    salary_calculation_info: SalaryPayrollCalculationItemInfoContainer | None = Field(default=None, description="\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u043f\u0440\u0438\u043c\u0435\u043d\u0451\u043d\u043d\u043e\u043c \u043f\u0440\u0430\u0432\u0438\u043b\u0435 \u0440\u0430\u0441\u0447\u0451\u0442\u0430 \u0437\u0430\u0440\u043f\u043b\u0430\u0442\u044b.")
    targets: list[SalaryPayrollCalculationItemTargetContainer] | None = Field(default=None)
    salary_discrepancy: dict[str, Any] | None = Field(default=None, description="\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0440\u0430\u0441\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u044f\u0445 \u0432 \u043d\u0430\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u0438 \u0437\u0430\u0440\u043f\u043b\u0430\u0442\u044b.")


class SalaryStaffPeriodDaily(BaseModel):
    """Получение расчёта за период по конкретному сотруднику с группировкой по дате.
    Схема спеки: Расчёт за период по конкретному сотруднику с группировкой по дате
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    period_calculation_daily: list[dict[str, Any]] | None = Field(default=None)
    currency: Currency2 | None = Field(default=None, description="\u0412\u0430\u043b\u044e\u0442\u0430.")


class ServiceCategoryTitle2(BaseModel):
    """Название категории услуг
    Схема спеки: Root Type for ServiceCategoryTitle
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0443\u0441\u043b\u0443\u0433")
    title: str | None = Field(default=None, description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0443\u0441\u043b\u0443\u0433")
    services: list[ServiceTitle2] | None = Field(default=None, description="\u0423\u0441\u043b\u0443\u0433\u0438 \u0432 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 (\u043f\u043e \u0437\u0430\u043f\u0440\u043e\u0441\u0443)")


class TimetableEventScheduleEvent2(BaseModel):
    """Данные по сущности конкретной записи или события в рамках расписания.
    Схема спеки: Объект модели "Сущность записи/события в Расписании"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0441\u0443\u0449\u043d\u043e\u0441\u0442\u0438 \u0437\u0430\u043f\u0438\u0441\u0438/\u0441\u043e\u0431\u044b\u0442\u0438\u044f \u0432 \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0438.")
    created_at: str | None = Field(default=None, description="\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f \u0441\u0443\u0449\u043d\u043e\u0441\u0442\u0438 \u0437\u0430\u043f\u0438\u0441\u0438/\u0441\u043e\u0431\u044b\u0442\u0438\u044f \u0432 \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0438.")
    updated_at: str | None = Field(default=None, description="\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0433\u043e \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f \u0441\u0443\u0449\u043d\u043e\u0441\u0442\u0438 \u0437\u0430\u043f\u0438\u0441\u0438/\u0441\u043e\u0431\u044b\u0442\u0438\u044f \u0432 \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0438.")
    deleted_at: str | None = Field(default=None, description="\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0443\u0434\u0430\u043b\u0435\u043d\u0438\u044f \u0441\u0443\u0449\u043d\u043e\u0441\u0442\u0438 \u0437\u0430\u043f\u0438\u0441\u0438/\u0441\u043e\u0431\u044b\u0442\u0438\u044f \u0432 \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0438.")
    event_status: Literal["stable", "event_created", "event_changed", "event_changed_force", "event_deleted", "entity_deleted", "entity_failed"] | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0441\u0443\u0449\u043d\u043e\u0441\u0442\u0438 \u0437\u0430\u043f\u0438\u0441\u0438/\u0441\u043e\u0431\u044b\u0442\u0438\u044f \u0432 \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0438: `stable` - \u0441\u0443\u0449\u043d\u043e\u0441\u0442\u044c \u0441\u0442\u0430\u0431\u0438\u043b\u044c\u043d\u0430; `event_created` - \u0441\u0443\u0449\u043d\u043e\u0441\u0442\u044c \u0442\u043e\u043b\u044c\u043a\u043e \u0447\u0442\u043e \u0441\u043e\u0437\u0434\u0430\u043d\u0430, \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u044e\u0449\u0430\u044f \u0437\u0430\u043f\u0438\u0441\u044c/\u0441\u043e\u0431\u044b\u0442\u0438\u0435 \u0435\u0449\u0435 \u043d\u0435 \u0441\u043e\u0437\u0434\u0430\u043d\u043e; `event_changed` - \u0441\u0443\u0449\u043d\u043e\u0441\u0442\u044c ...")
    event_datetime: str | None = Field(default=None, description="\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u0437\u0430\u043f\u0438\u0441\u0438/\u0441\u043e\u0431\u044b\u0442\u0438\u044f, \u0441\u043e\u0433\u043b\u0430\u0441\u043d\u043e \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f.")
    event_entity_type: Literal["record", "activity"] | None = Field(default=None, description="\u0422\u0438\u043f \u0441\u0443\u0449\u043d\u043e\u0441\u0442\u0438, \u0441\u043e\u0437\u0434\u0430\u043d\u043d\u043e\u0439 \u0432 \u0440\u0430\u043c\u043a\u0430\u0445 \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f.")
    event_entity_id: float | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0441\u0443\u0449\u043d\u043e\u0441\u0442\u0438, \u0441\u043e\u0437\u0434\u0430\u043d\u043d\u043e\u0439 \u0432 \u0440\u0430\u043c\u043a\u0430\u0445 \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f.")
    is_entity_master_changed: bool | None = Field(default=None, description="\u0424\u043b\u0430\u0433 \u0440\u0443\u0447\u043d\u043e\u0433\u043e \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430, \u043e\u043a\u0430\u0437\u044b\u0432\u0430\u044e\u0449\u0435\u0433\u043e \u0443\u0441\u043b\u0443\u0433\u0438 \u0432 \u0440\u0430\u043c\u043a\u0430\u0445 \u043a\u043e\u043d\u043a\u0440\u0435\u0442\u043d\u043e\u0439 \u0437\u0430\u043f\u0438\u0441\u0438/\u0441\u043e\u0431\u044b\u0442\u0438\u044f.")
    is_entity_datetime_changed: bool | None = Field(default=None, description="\u0424\u043b\u0430\u0433 \u0440\u0443\u0447\u043d\u043e\u0433\u043e \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u0434\u0430\u0442\u044b \u0438 \u0432\u0440\u0435\u043c\u0435\u043d\u0438 \u043a\u043e\u043d\u043a\u0440\u0435\u0442\u043d\u043e\u0439 \u0437\u0430\u043f\u0438\u0441\u0438/\u0441\u043e\u0431\u044b\u0442\u0438\u044f.")
    is_entity_duration_changed: bool | None = Field(default=None, description="\u0424\u043b\u0430\u0433 \u0440\u0443\u0447\u043d\u043e\u0433\u043e \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u0434\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u0438 \u043a\u043e\u043d\u043a\u0440\u0435\u0442\u043d\u043e\u0439 \u0437\u0430\u043f\u0438\u0441\u0438/\u0441\u043e\u0431\u044b\u0442\u0438\u044f.")
    is_entity_labels_changed: bool | None = Field(default=None, description="\u0424\u043b\u0430\u0433 \u0440\u0443\u0447\u043d\u043e\u0433\u043e \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0439, \u043f\u0440\u0438\u0432\u044f\u0437\u0430\u043d\u043d\u044b\u0445 \u043a \u043a\u043e\u043d\u043a\u0440\u0435\u0442\u043d\u043e\u0439 \u0437\u0430\u043f\u0438\u0441\u0438/\u0441\u043e\u0431\u044b\u0442\u0438\u044e.")
    is_entity_resource_instances_changed: bool | None = Field(default=None, description="\u0424\u043b\u0430\u0433 \u0440\u0443\u0447\u043d\u043e\u0433\u043e \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u044d\u043a\u0437\u0435\u043c\u043f\u043b\u044f\u0440\u043e\u0432 \u0440\u0435\u0441\u0443\u0440\u0441\u043e\u0432, \u043f\u0440\u0438\u0432\u044f\u0437\u0430\u043d\u043d\u044b\u0445 \u043a \u043a\u043e\u043d\u043a\u0440\u0435\u0442\u043d\u043e\u0439 \u0437\u0430\u043f\u0438\u0441\u0438/\u0441\u043e\u0431\u044b\u0442\u0438\u044e.")
    entity_master: dict[str, Any] | None = Field(default=None, description="\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a, \u043e\u043a\u0430\u0437\u044b\u0432\u0430\u044e\u0449\u0438\u0439 \u0443\u0441\u043b\u0443\u0433\u0438 \u0432 \u0440\u0430\u043c\u043a\u0430\u0445 \u043a\u043e\u043d\u043a\u0440\u0435\u0442\u043d\u043e\u0439 \u0437\u0430\u043f\u0438\u0441\u0438/\u0441\u043e\u0431\u044b\u0442\u0438\u044f \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f.")
    entity_datetime: str | None = Field(default=None, description="\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u0437\u0430\u043f\u0438\u0441\u0438/\u0441\u043e\u0431\u044b\u0442\u0438\u044f, \u0430\u043a\u0442\u0443\u0430\u043b\u044c\u043d\u044b\u0435 \u043d\u0430 \u0442\u0435\u043a\u0443\u0449\u0438\u0439 \u043c\u043e\u043c\u0435\u043d\u0442.")
    entity_duration: str | None = Field(default=None, description="\u0414\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u0438/\u0441\u043e\u0431\u044b\u0442\u0438\u044f, \u0430\u043a\u0442\u0443\u0430\u043b\u044c\u043d\u0430\u044f \u043d\u0430 \u0442\u0435\u043a\u0443\u0449\u0438\u0439 \u043c\u043e\u043c\u0435\u043d\u0442.")
    entity_labels: list[Label] | None = Field(default=None, description="\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438, \u043f\u0440\u0438\u0432\u044f\u0437\u0430\u043d\u043d\u044b\u0435 \u043a \u0437\u0430\u043f\u0438\u0441\u0438/\u0441\u043e\u0431\u044b\u0442\u0438\u044e, \u0430\u043a\u0442\u0443\u0430\u043b\u044c\u043d\u044b\u0435 \u043d\u0430 \u0442\u0435\u043a\u0443\u0449\u0438\u0439 \u043c\u043e\u043c\u0435\u043d\u0442.")
    entity_resource_instances: list[ResourceInstance] | None = Field(default=None, description="\u042d\u043a\u0437\u0435\u043c\u043f\u043b\u044f\u0440\u044b \u0440\u0435\u0441\u0443\u0440\u0441\u043e\u0432, \u043f\u0440\u0438\u0432\u044f\u0437\u0430\u043d\u043d\u044b\u0435 \u043a \u0437\u0430\u043f\u0438\u0441\u0438/\u0441\u043e\u0431\u044b\u0442\u0438\u044e, \u0430\u043a\u0442\u0443\u0430\u043b\u044c\u043d\u044b\u0435 \u043d\u0430 \u0442\u0435\u043a\u0443\u0449\u0438\u0439 \u043c\u043e\u043c\u0435\u043d\u0442.")


class GetApplicationApplicationIdResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: GetApplicationApplicationIdResponse200Data | None = Field(default=None, alias="data")
    meta: dict[str, Any] | None = Field(default=None)


class GetApplicationIdTariffsResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: list[GetApplicationIdTariffsResponse200DataItem] | None = Field(default=None, alias="data", description="\u0421\u043f\u0438\u0441\u043e\u043a \u0442\u0430\u0440\u0438\u0444\u043e\u0432")
    meta: dict[str, Any] | None = Field(default=None)


class GetClientIdCommentsResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: list[ClientCommentContainer] | None = Field(default=None, alias="data")
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
    active: float = Field(description="\u0410\u043a\u0442\u0438\u0432\u043d\u0430 \u043b\u0438 \u043b\u0438\u0446\u0435\u043d\u0437\u0438\u044f")
    deactivation_date: str = Field(description="\u0414\u0430\u0442\u0430 \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f \u0441\u0440\u043e\u043a\u0430 \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f \u043b\u0438\u0446\u0435\u043d\u0437\u0438\u0438")
    id_: float = Field(alias="id", description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043b\u0438\u0446\u0435\u043d\u0437\u0438\u0438")
    name: str = Field(description="\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u043b\u0438\u0446\u0435\u0437\u043d\u0438\u0438")
    options: list[dict[str, Any]] = Field(description="\u041e\u043f\u0446\u0438\u0438 \u043b\u0438\u0446\u0435\u043d\u0437\u0438\u0438")
    salon_id: float = Field(description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438")
    staff_limit: float = Field(description="\u041b\u0438\u043c\u0438\u0442 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u043e\u0432")
    start_date: str = Field(description="\u0414\u0430\u0442\u0430 \u043d\u0430\u0447\u0430\u043b\u0430 \u0441\u0440\u043e\u043a\u0430 \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f \u043b\u0438\u0446\u0435\u043d\u0437\u0438\u0438")


class GetSettingsTimeslotsResponse200Data(BaseModel):
    """Объект модели "Настройки таймслотов".
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    is_enabled: bool | None = Field(default=None, description="\u041f\u0440\u0438\u0437\u043d\u0430\u043a \u0432\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f \u0442\u0430\u0439\u043c\u0441\u043b\u043e\u0442\u043e\u0432.")
    weekdays_settings: CompanyGridWeekdaysContainer | None = Field(default=None)
    dates_settings: list[dict[str, Any]] | None = Field(default=None)


class GetStaffIdPeriodResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: Any | None = Field(default=None, alias="data")
    meta: dict[str, Any] | None = Field(default=None)


class PostActivityIdRecordsRequestClient(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: int | None = Field(default=None, alias="id", description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043a\u043b\u0438\u0435\u043d\u0442\u0430.")
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

    title: str = Field(description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0442\u0438\u043f\u0430 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430.")
    salon_group_id: float = Field(description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0441\u0435\u0442\u0438.")
    cost: float = Field(description="\u0426\u0435\u043d\u0430 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430")
    salon_ids: list[float] | None = Field(default=None, description="\u0421\u043f\u0438\u0441\u043e\u043a ID \u0444\u0438\u043b\u0438\u0430\u043b\u043e\u0432.")
    period: float | None = Field(default=None, description="\u041f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u043f\u0435\u0440\u0438\u043e\u0434\u0430 \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f.")
    period_unit_id: int | None = Field(default=None, description="\u0422\u0438\u043f \u0435\u0434\u0438\u043d\u0438\u0446 (1 - \u0434\u0435\u043d\u044c, 2 - \u043d\u0435\u0434\u0435\u043b\u044f, 3 - \u043c\u0435\u0441\u044f\u0446, 4 - \u0433\u043e\u0434).")
    allow_freeze: bool | None = Field(default=None, description="\u0412\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u044c \u0437\u0430\u043c\u043e\u0440\u043e\u0437\u043a\u0438.")
    freeze_limit: int | None = Field(default=None, description="\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u044b\u0439 \u043e\u0431\u0449\u0438\u0439 \u043f\u0435\u0440\u0438\u043e\u0434 \u0437\u0430\u043c\u043e\u0440\u043e\u0437\u043a\u0438")
    freeze_limit_unit_id: int | None = Field(default=None, description="\u0415\u0434\u0438\u043d\u0438\u0446\u0430 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f \u0441\u0440\u043e\u043a\u0430 \u0437\u0430\u043c\u043e\u0440\u043e\u0437\u043a\u0438 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430 (1 - \u0434\u0435\u043d\u044c, 2 - \u043d\u0435\u0434\u0435\u043b\u044f, 3 - \u043c\u0435\u0441\u044f\u0446, 4 - \u0433\u043e\u0434).")
    service_price_correction: bool | None = Field(default=None, description="\u0412\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u044c \u043a\u043e\u0440\u0440\u0435\u043a\u0442\u0438\u0440\u043e\u0432\u043a\u0438 \u0446\u0435\u043d\u044b \u0443\u0441\u043b\u0443\u0433\u0438 \u043f\u0440\u0438 \u043f\u0440\u0438\u043c\u0435\u043d\u0435\u043d\u0438\u0438 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430.")
    expiration_type_id: int | None = Field(default=None, description="\u0422\u0438\u043f \u0430\u043a\u0442\u0438\u0432\u0430\u0446\u0438\u0438 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430 (1 - \u043f\u0440\u0438 \u043f\u0440\u043e\u0434\u0430\u0436\u0435, 2 - \u043f\u0440\u0438 \u043f\u0435\u0440\u0432\u043e\u043c \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u0438, 3 - \u0441 \u043a\u043e\u043d\u043a\u0440\u0435\u0442\u043d\u043e\u0439 \u0434\u0430\u0442\u044b).")
    is_allow_empty_code: bool | None = Field(default=None, description="\u041e\u0431\u0449\u0438\u0439 \u0438\u043b\u0438 \u0438\u043c\u0435\u043d\u043d\u043e\u0439 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442. true - \u0438\u043c\u0435\u043d\u043d\u043e\u0439 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442 \u043f\u043e\u043b\u044c\u0437\u0443\u0435\u0442\u0441\u044f \u0442\u043e\u043b\u044c\u043a\u043e \u043e\u0434\u0438\u043d \u0447\u0435\u043b\u043e\u0432\u0435\u043a, \u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u0435\u0433\u043e \u043a\u0443\u043f\u0438\u043b. false - \u043c\u043e\u0433\u0443\u0442 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c\u0441\u044f \u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u043e \u0447\u0435\u043b\u043e\u0432\u0435\u043a \u043f\u043e \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u044c\u043d\u043e\u043c\u0443 \u043a\u043e\u0434\u0443.")
    is_united_balance: bool = Field(description="\u041f\u0440\u0438\u0437\u043d\u0430\u043a \u043e\u0431\u0449\u0435\u0433\u043e \u0431\u0430\u043b\u0430\u043d\u0441\u0430 (true - \u043e\u0431\u0449\u0438\u0439 \u0431\u0430\u043b\u0430\u043d\u0441, false - \u0440\u0430\u0437\u0434\u0435\u043b\u044c\u043d\u044b\u0439).")
    united_balance_services_count: int = Field(description="\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u0439 \u043f\u0440\u0438 \u043e\u0431\u0449\u0435\u043c \u0431\u0430\u043b\u0430\u043d\u0441\u0435.")
    balance_edit_type_id: int | None = Field(default=None, description="\u0422\u0438\u043f \u043a\u043e\u0440\u0440\u0435\u043a\u0442\u0438\u0440\u043e\u0432\u043a\u0438 \u0431\u0430\u043b\u0430\u043d\u0441\u0430 (0 - \u043a\u043e\u0440\u0440\u0435\u043a\u0442\u0438\u0440\u043e\u0432\u043a\u0430 \u0437\u0430\u043f\u0440\u0435\u0449\u0435\u043d\u0430, 1 - \u0432 \u0444\u0438\u043b\u0438\u0430\u043b\u0435 \u0433\u0434\u0435 \u0431\u044b\u043b \u043f\u0440\u043e\u0434\u0430\u043d \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442, 2 - \u0432\u043e \u0432\u0441\u0435\u0445 \u0444\u0438\u043b\u0438\u0430\u043b\u0430\u0445).")
    is_online_sale_enabled: bool | None = Field(default=None, description="\u041e\u043d\u043b\u0430\u0439\u043d \u043f\u0440\u043e\u0434\u0430\u0436\u0430 (true - \u0440\u0430\u0437\u0440\u0435\u0448\u0435\u043d\u0430, false - \u0437\u0430\u043f\u0440\u0435\u0449\u0435\u043d\u0430). \u0415\u0441\u043b\u0438 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u043f\u0435\u0440\u0435\u0434\u0430\u043d \u0440\u0430\u0432\u043d\u044b\u043c true, \u0442\u043e \u0442\u043e\u0433\u0434\u0430 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 online_sale_price \u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u0435\u043d.")
    online_sale_title: str | None = Field(default=None, description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430 \u043f\u0440\u0438 \u043e\u043d\u043b\u0430\u0439\u043d \u043f\u0440\u043e\u0434\u0430\u0436\u0435.")
    online_sale_description: str | None = Field(default=None, description="\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430 \u043f\u0440\u0438 \u043e\u043d\u043b\u0430\u0439\u043d \u043f\u0440\u043e\u0434\u0430\u0436\u0435.")
    online_sale_price: float | None = Field(default=None, description="\u0426\u0435\u043d\u0430 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430 \u043f\u0440\u0438 \u043e\u043d\u043b\u0430\u0439\u043d \u043f\u0440\u043e\u0434\u0430\u0436\u0435.")
    online_image: str | None = Field(default=None, description="\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430 \u043f\u0440\u0438 \u043e\u043d\u043b\u0430\u0439\u043d \u043f\u0440\u043e\u0434\u0430\u0436\u0435.")
    autoactivation_period: int | None = Field(default=None, description="\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u044b\u0439 \u043f\u0435\u0440\u0438\u043e\u0434 \u0430\u0432\u0442\u043e\u0430\u043a\u0442\u0438\u0432\u0430\u0446\u0438\u0438.")
    autoactivation_time_in_days: int | None = Field(default=None, description="\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0435\u0434\u0438\u043d\u0438\u0446 \u0432\u0440\u0435\u043c\u0435\u043d\u0438 \u0434\u043b\u044f \u0430\u0432\u0442\u043e\u0430\u043a\u0442\u0438\u0432\u0430\u0446\u0438\u0438 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430.")
    autoactivation_time_unit_id: int | None = Field(default=None, description="\u0415\u0434\u0438\u043d\u0438\u0446\u044b \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f \u0434\u043b\u044f \u0430\u0432\u0442\u043e\u0430\u043a\u0442\u0438\u0432\u0430\u0446\u0438\u0438 (1 - \u0434\u043d\u0438, 2 - \u043d\u0435\u0434\u0435\u043b\u0438, 3 - \u043c\u0435\u0441\u044f\u0446\u044b, 4 - \u0433\u043e\u0434\u044b).")
    is_archived: bool | None = Field(default=None, description="\u041f\u0440\u0438\u0437\u043d\u0430\u043a \u0430\u0440\u0445\u0438\u0432\u0430\u0446\u0438\u0438 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430.")
    services: list[int] | None = Field(default=None, description="\u0421\u043f\u0438\u0441\u043e\u043a ID \u0443\u0441\u043b\u0443\u0433.")
    service_categories: list[int] = Field(description="\u0421\u043f\u0438\u0441\u043e\u043a ID \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0439 \u0443\u0441\u043b\u0443\u0433.")
    availability: list[PostLoyaltyAbonementTypesRequestAvailabilityItem] | None = Field(default=None, description="\u0421\u043f\u0438\u0441\u043e\u043a \u0443\u0441\u043b\u043e\u0432\u0438\u0439 \u0432\u0440\u0435\u043c\u0435\u043d\u0438 \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430, \u043f\u0440\u0438 \u043f\u0443\u0441\u0442\u043e\u043c \u043c\u0430\u0441\u0441\u0438\u0432\u0435 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442 \u0434\u0435\u0439\u0441\u0442\u0432\u0443\u0435\u0442 \u0432 \u043b\u044e\u0431\u043e\u0435 \u0432\u0440\u0435\u043c\u044f.")


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

    title: str = Field(description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0442\u0438\u043f\u0430 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430.")
    salon_group_id: float = Field(description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0441\u0435\u0442\u0438.")
    cost: float = Field(description="\u0426\u0435\u043d\u0430 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430.")
    salon_ids: list[float] | None = Field(default=None, description="\u0421\u043f\u0438\u0441\u043e\u043a ID \u0444\u0438\u043b\u0438\u0430\u043b\u043e\u0432.")
    period: float | None = Field(default=None, description="\u041f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u043f\u0435\u0440\u0438\u043e\u0434\u0430 \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f.")
    period_unit_id: int | None = Field(default=None, description="\u0422\u0438\u043f \u0435\u0434\u0438\u043d\u0438\u0446 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f \u043f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u0438 \u043f\u0435\u0440\u0438\u043e\u0434\u0430 \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f \u0442\u0438\u043f\u0430 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430 (1 - \u0434\u0435\u043d\u044c, 2 - \u043d\u0435\u0434\u0435\u043b\u044f, 3 - \u043c\u0435\u0441\u044f\u0446, 4 - \u0433\u043e\u0434).")
    allow_freeze: bool | None = Field(default=None, description="\u0412\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u044c \u0437\u0430\u043c\u043e\u0440\u043e\u0437\u043a\u0438.")
    freeze_limit: int | None = Field(default=None, description="\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u044b\u0439 \u043e\u0431\u0449\u0438\u0439 \u043f\u0435\u0440\u0438\u043e\u0434 \u0437\u0430\u043c\u043e\u0440\u043e\u0437\u043a\u0438.")
    freeze_limit_unit_id: int | None = Field(default=None, description="\u0415\u0434\u0438\u043d\u0438\u0446\u0430 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f \u0441\u0440\u043e\u043a\u0430 \u0437\u0430\u043c\u043e\u0440\u043e\u0437\u043a\u0438 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430 (1 - \u0434\u0435\u043d\u044c, 2 - \u043d\u0435\u0434\u0435\u043b\u044f, 3 - \u043c\u0435\u0441\u044f\u0446, 4 - \u0433\u043e\u0434).")
    service_price_correction: bool | None = Field(default=None, description="\u0412\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u044c \u043a\u043e\u0440\u0440\u0435\u043a\u0442\u0438\u0440\u043e\u0432\u043a\u0438 \u0446\u0435\u043d\u044b \u0443\u0441\u043b\u0443\u0433\u0438 \u043f\u0440\u0438 \u043f\u0440\u0438\u043c\u0435\u043d\u0435\u043d\u0438\u0438 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430.")
    expiration_type_id: int | None = Field(default=None, description="\u0422\u0438\u043f \u0430\u043a\u0442\u0438\u0432\u0430\u0446\u0438\u0438 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430 (1 - \u043f\u0440\u0438 \u043f\u0440\u043e\u0434\u0430\u0436\u0435, 2 - \u043f\u0440\u0438 \u043f\u0435\u0440\u0432\u043e\u043c \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u0438, 3 - \u0441 \u043a\u043e\u043d\u043a\u0440\u0435\u0442\u043d\u043e\u0439 \u0434\u0430\u0442\u044b).")
    is_allow_empty_code: bool | None = Field(default=None, description="\u041e\u0431\u0449\u0438\u0439 \u0438\u043b\u0438 \u0438\u043c\u0435\u043d\u043d\u043e\u0439 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442. true - \u0438\u043c\u0435\u043d\u043d\u043e\u0439 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442 \u043f\u043e\u043b\u044c\u0437\u0443\u0435\u0442\u0441\u044f \u0442\u043e\u043b\u044c\u043a\u043e \u043e\u0434\u0438\u043d \u0447\u0435\u043b\u043e\u0432\u0435\u043a, \u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u0435\u0433\u043e \u043a\u0443\u043f\u0438\u043b. false - \u043c\u043e\u0433\u0443\u0442 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c\u0441\u044f \u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u043e \u0447\u0435\u043b\u043e\u0432\u0435\u043a \u043f\u043e \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u044c\u043d\u043e\u043c\u0443 \u043a\u043e\u0434\u0443.")
    is_united_balance: bool = Field(description="\u041f\u0440\u0438\u0437\u043d\u0430\u043a \u043e\u0431\u0449\u0435\u0433\u043e \u0431\u0430\u043b\u0430\u043d\u0441\u0430 (true - \u043e\u0431\u0449\u0438\u0439 \u0431\u0430\u043b\u0430\u043d\u0441, false - \u0440\u0430\u0437\u0434\u0435\u043b\u044c\u043d\u044b\u0439).")
    united_balance_services_count: int = Field(description="\u041a\u043e\u043b-\u0432\u043e \u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u0439 \u043f\u0440\u0438 \u043e\u0431\u0449\u0435\u043c \u0431\u0430\u043b\u0430\u043d\u0441\u0435.")
    balance_edit_type_id: int | None = Field(default=None, description="\u0422\u0438\u043f \u043a\u043e\u0440\u0440\u0435\u043a\u0442\u0438\u0440\u043e\u0432\u043a\u0438 \u0431\u0430\u043b\u0430\u043d\u0441\u0430 (0 - \u043a\u043e\u0440\u0440\u0435\u043a\u0442\u0438\u0440\u043e\u0432\u043a\u0430 \u0437\u0430\u043f\u0440\u0435\u0449\u0435\u043d\u0430, 1 - \u0432 \u0444\u0438\u043b\u0438\u0430\u043b\u0435 \u0433\u0434\u0435 \u0431\u044b\u043b \u043f\u0440\u043e\u0434\u0430\u043d \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442, 2 - \u0432\u043e \u0432\u0441\u0435\u0445 \u0444\u0438\u043b\u0438\u0430\u043b\u0430\u0445).")
    is_online_sale_enabled: bool | None = Field(default=None, description="\u041e\u043d\u043b\u0430\u0439\u043d \u043f\u0440\u043e\u0434\u0430\u0436\u0430 (true - \u0440\u0430\u0437\u0440\u0435\u0448\u0435\u043d\u0430, false - \u0437\u0430\u043f\u0440\u0435\u0449\u0435\u043d\u0430).")
    online_sale_title: str | None = Field(default=None, description="\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430 \u043f\u0440\u0438 \u043e\u043d\u043b\u0430\u0439\u043d \u043f\u0440\u043e\u0434\u0430\u0436\u0435.")
    online_sale_description: str | None = Field(default=None, description="\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430 \u043f\u0440\u0438 \u043e\u043d\u043b\u0430\u0439\u043d \u043f\u0440\u043e\u0434\u0430\u0436\u0435.")
    online_sale_price: float | None = Field(default=None, description="\u0426\u0435\u043d\u0430 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430 \u043f\u0440\u0438 \u043e\u043d\u043b\u0430\u0439\u043d \u043f\u0440\u043e\u0434\u0430\u0436\u0435.")
    online_image: str | None = Field(default=None, description="\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430 \u043f\u0440\u0438 \u043e\u043d\u043b\u0430\u0439\u043d \u043f\u0440\u043e\u0434\u0430\u0436\u0435.")
    autoactivation_period: int | None = Field(default=None, description="\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u044b\u0439 \u043f\u0435\u0440\u0438\u043e\u0434 \u0430\u0432\u0442\u043e\u0430\u043a\u0442\u0438\u0432\u0430\u0446\u0438\u0438.")
    autoactivation_time: int | None = Field(default=None, description="\u041a\u043e\u043b-\u0432\u043e \u0435\u0434\u0438\u043d\u0438\u0446 \u0432\u0440\u0435\u043c\u0435\u043d\u0438 \u0434\u043b\u044f \u0430\u0432\u0442\u043e\u0430\u043a\u0442\u0438\u0432\u0430\u0446\u0438\u0438 \u0442\u0438\u043f\u0430 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430.")
    autoactivation_time_unit_id: int | None = Field(default=None, description="\u0415\u0434\u0438\u043d\u0438\u0446\u044b \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f \u0434\u043b\u044f \u0430\u0432\u0442\u043e\u0430\u043a\u0442\u0438\u0432\u0430\u0446\u0438\u0438 (1 - \u0434\u043d\u0438, 2 - \u043d\u0435\u0434\u0435\u043b\u0438, 3 - \u043c\u0435\u0441\u044f\u0446\u044b, 4 - \u0433\u043e\u0434\u044b).")
    is_archived: bool | None = Field(default=None, description="\u041f\u0440\u0438\u0437\u043d\u0430\u043a \u0430\u0440\u0445\u0438\u0432\u0430\u0446\u0438\u0438 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430.")
    services: list[int] | None = Field(default=None, description="\u0421\u043f\u0438\u0441\u043e\u043a ID \u0443\u0441\u043b\u0443\u0433 \u043f\u0440\u0438\u0432\u044f\u0437\u0430\u043d\u043d\u044b\u0445 \u043a \u0442\u0438\u043f\u0443 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430.")
    service_categories: list[int] = Field(description="\u0421\u043f\u0438\u0441\u043e\u043a ID \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0439 \u0443\u0441\u043b\u0443\u0433 \u043f\u0440\u0438\u0432\u044f\u0437\u0430\u043d\u043d\u044b\u0445 \u043a \u0442\u0438\u043f\u0443 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430.")
    availability: list[PutAbonementTypesLoyaltyAbonementTypeIdRequestAvailabilityItem] | None = Field(default=None, description="\u0421\u043f\u0438\u0441\u043e\u043a \u0443\u0441\u043b\u043e\u0432\u0438\u0439 \u0432\u0440\u0435\u043c\u0435\u043d\u0438 \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430, \u043f\u0440\u0438 \u043f\u0443\u0441\u0442\u043e\u043c \u043c\u0430\u0441\u0441\u0438\u0432\u0435 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442 \u0434\u0435\u0439\u0441\u0442\u0432\u0443\u0435\u0442 \u0432 \u043b\u044e\u0431\u043e\u0435 \u0432\u0440\u0435\u043c\u044f.")


class PutStaffScheduleRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    schedules_to_set: list[PutStaffScheduleRequestSchedulesToSetItem] | None = Field(default=None, description="\u041c\u0430\u0441\u0441\u0438\u0432 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432 \u0441 \u0433\u0440\u0430\u0444\u0438\u043a\u0430\u043c\u0438 \u0440\u0430\u0431\u043e\u0442\u044b \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u043e\u0432 \u043d\u0430 \u043a\u043e\u043d\u043a\u0440\u0435\u0442\u043d\u044b\u0435 \u0434\u0430\u0442\u044b.")
    schedules_to_delete: list[PutStaffScheduleRequestSchedulesToDeleteItem] | None = Field(default=None, description="\u041c\u0430\u0441\u0441\u0438\u0432 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432 \u0441 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430\u043c\u0438 \u0443\u0434\u0430\u043b\u0435\u043d\u0438\u044f \u0433\u0440\u0430\u0444\u0438\u043a\u043e\u0432 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u043e\u0432 \u043d\u0430 \u043a\u043e\u043d\u043a\u0440\u0435\u0442\u043d\u044b\u0435 \u0434\u0430\u0442\u044b.")


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


class ClientVisitsHistoryGoodsTransaction(BaseModel):
    """Данные о продаже товара.
    Схема спеки: Объект модели "Продажа товара в истории посещений клиента"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u0438 \u043f\u043e \u043f\u0440\u043e\u0434\u0430\u0436\u0435 \u0442\u043e\u0432\u0430\u0440\u0430.")
    comment: str | None = Field(default=None, description="\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439.")
    date: str | None = Field(default=None, description="\u0414\u0430\u0442\u0430 \u043f\u0440\u043e\u0434\u0430\u0436\u0438.")
    visit_id: float | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0432\u0438\u0437\u0438\u0442\u0430. \u0420\u0430\u0432\u043d\u043e `0`, \u0435\u0441\u043b\u0438 \u043d\u0435\u0442 \u0441\u0432\u044f\u0437\u0438 \u0441 \u0432\u0438\u0437\u0438\u0442\u043e\u043c.")
    record_id: float | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0437\u0430\u043f\u0438\u0441\u0438. \u0420\u0430\u0432\u043d\u043e `0`, \u0435\u0441\u043b\u0438 \u043d\u0435\u0442 \u0441\u0432\u044f\u0437\u0438 \u0441 \u0437\u0430\u043f\u0438\u0441\u044c\u044e.")
    goods: list[ClientVisitsHistoryGoodsTransactionGood] | None = Field(default=None, description="\u0421\u043f\u0438\u0441\u043e\u043a \u043f\u0440\u043e\u0434\u0430\u043d\u043d\u044b\u0445 \u0442\u043e\u0432\u0430\u0440\u043e\u0432.")
    staff: dict[str, Any] | None = Field(default=None, description="\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a, \u043f\u0440\u043e\u0434\u0430\u0432\u0448\u0438\u0439 \u0442\u043e\u0432\u0430\u0440.")
    company: dict[str, Any] | None = Field(default=None, description="\u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0441\u0430\u043b\u043e\u043d\u0435, \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u043c \u0431\u044b\u043b \u043f\u0440\u043e\u0434\u0430\u043d \u0442\u043e\u0432\u0430\u0440.")


class ClientVisitsHistoryRecord(BaseModel):
    """Данные по записи клиента.
    Схема спеки: Объект модели "Запись в истории посещений клиента"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0437\u0430\u043f\u0438\u0441\u0438.")
    comment: str | None = Field(default=None, description="\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439.")
    date: str | None = Field(default=None, description="\u0414\u0430\u0442\u0430 \u0437\u0430\u043f\u0438\u0441\u0438.")
    visit_id: float | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0432\u0438\u0437\u0438\u0442\u0430.")
    attendance: float | None = Field(default=None, description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0437\u0430\u043f\u0438\u0441\u0438 \u0432 \u0432\u0438\u0437\u0438\u0442\u0435")
    services: list[ClientVisitsHistoryRecordService] | None = Field(default=None, description="\u0423\u0441\u043b\u0443\u0433\u0438 \u0432 \u0437\u0430\u043f\u0438\u0441\u0438.")
    staff: dict[str, Any] | None = Field(default=None, description="\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a, \u043e\u043a\u0430\u0437\u0430\u0432\u0448\u0438\u0439 \u0443\u0441\u043b\u0443\u0433\u0443.")
    company: dict[str, Any] | None = Field(default=None, description="\u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0441\u0430\u043b\u043e\u043d\u0435, \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u043c \u0431\u044b\u043b \u043f\u0440\u043e\u0434\u0430\u043d \u0442\u043e\u0432\u0430\u0440.")
    tips: TipsReduce | TipsReduceWithFullInfo | None = Field(default=None, description="\u0414\u0430\u043d\u043d\u044b\u0435 \u043e \u0447\u0430\u0435\u0432\u044b\u0445. \u0418\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u044e\u0442\u0441\u044f \u0440\u0430\u0437\u043d\u044b\u0435 \u043c\u043e\u0434\u0435\u043b\u0438 \u0432 \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438 \u043e\u0442 \u0442\u043e\u0433\u043e, \u044f\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u043b\u0438 \u0442\u0435\u043a\u0443\u0449\u0438\u0439 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c \u043c\u0430\u0441\u0442\u0435\u0440\u043e\u043c \u0432 \u0437\u0430\u043f\u0438\u0441\u0438.")
    comer: dict[str, Any] | None = Field(default=None, description="\u0414\u0430\u043d\u043d\u044b\u0435 \u043e \u043f\u043e\u0441\u0435\u0442\u0438\u0442\u0435\u043b\u0435. \u0415\u0441\u043b\u0438 \u043f\u043e\u0441\u0435\u0442\u0438\u0442\u0435\u043b\u044c \u043d\u0435 \u0443\u043a\u0430\u0437\u0430\u043d, \u0442\u043e \u043f\u043e\u043b\u0435 \u043d\u0435 \u0432\u044b\u0432\u043e\u0434\u0438\u0442\u0441\u044f.")


class TimetableEventScheduleDay2(BaseModel):
    """Данные по существующей в филиале серии расписания.
    Схема спеки: Объект модели "Серия Расписания"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0441\u0435\u0440\u0438\u0438 \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f.")
    created_at: str | None = Field(default=None, description="\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f \u0441\u0435\u0440\u0438\u0438 \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f.")
    updated_at: str | None = Field(default=None, description="\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0433\u043e \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f \u0441\u0435\u0440\u0438\u0438 \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f.")
    deleted_at: str | None = Field(default=None, description="\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0443\u0434\u0430\u043b\u0435\u043d\u0438\u044f \u0441\u0435\u0440\u0438\u0438 \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f.")
    timetable_event_schedule_id: float | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f, \u043a \u043a\u043e\u0442\u043e\u0440\u043e\u043c\u0443 \u043f\u0440\u0438\u0432\u044f\u0437\u0430\u043d\u0430 \u0434\u0430\u043d\u043d\u0430\u044f \u0441\u0435\u0440\u0438\u044f \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f.")
    day_of_week: Literal["mon", "tue", "wed", "thu", "fri", "sat", "sun"] | None = Field(default=None, description="\u0414\u0435\u043d\u044c \u043d\u0435\u0434\u0435\u043b\u0438 \u0441\u0435\u0440\u0438\u0438 \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f.")
    events_time: str | None = Field(default=None, description="\u0412\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u0437\u0430\u043f\u0438\u0441\u0435\u0439 \u0438\u043b\u0438 \u0441\u043e\u0431\u044b\u0442\u0438\u0439 \u0432 \u0440\u0430\u043c\u043a\u0430\u0445 \u0441\u0435\u0440\u0438\u0438 \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f.")
    events_duration: float | None = Field(default=None, description="\u0414\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u0435\u0439 \u0438\u043b\u0438 \u0441\u043e\u0431\u044b\u0442\u0438\u0439 \u0432 \u0440\u0430\u043c\u043a\u0430\u0445 \u0441\u0435\u0440\u0438\u0438 \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f. \u26a0\ufe0f \u0411\u0435\u0437 \u0443\u0447\u0451\u0442\u0430 \u0442\u0435\u0445.\u043f\u0435\u0440\u0435\u0440\u044b\u0432\u0430")
    event_technical_break_duration: float | None = Field(default=None, description="\u0414\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0442\u0435\u0445\u043d\u0438\u0447\u0435\u0441\u043a\u043e\u0433\u043e \u043f\u0435\u0440\u0435\u0440\u044b\u0432\u0430")
    events_master: dict[str, Any] | None = Field(default=None, description="\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a, \u043e\u043a\u0430\u0437\u044b\u0432\u0430\u044e\u0449\u0438\u0439 \u0443\u0441\u043b\u0443\u0433\u0438 \u0432 \u0440\u0430\u043c\u043a\u0430\u0445 \u0441\u0435\u0440\u0438\u0438 \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f. \u0412\u043e\u0437\u0432\u0440\u0430\u0449\u0430\u0435\u0442\u0441\u044f \u0432 \u043e\u0442\u0432\u0435\u0442\u0435, \u0435\u0441\u043b\u0438 \u0432 \u0437\u0430\u043f\u0440\u043e\u0441\u0435 \u0443\u043a\u0430\u0437\u0430\u043d \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 `include` \u0441 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u043c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435\u043c.")
    events_labels: list[Label] | None = Field(default=None, description="\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0438\u043d\u0434\u0438\u0432\u0438\u0434\u0443\u0430\u043b\u044c\u043d\u044b\u0445 \u0437\u0430\u043f\u0438\u0441\u0435\u0439 \u0438\u043b\u0438 \u0433\u0440\u0443\u043f\u043f\u043e\u0432\u044b\u0445 \u0441\u043e\u0431\u044b\u0442\u0438\u0439, \u043f\u0440\u0438\u0432\u044f\u0437\u0430\u043d\u043d\u044b\u0435 \u043a \u0437\u0430\u043f\u0438\u0441\u044f\u043c \u0438\u043b\u0438 \u0441\u043e\u0431\u044b\u0442\u0438\u044f\u043c \u0432 \u0440\u0430\u043c\u043a\u0430\u0445 \u0441\u0435\u0440\u0438\u0438 \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f. \u0412\u043e\u0437\u0432\u0440\u0430\u0449\u0430\u044e\u0442\u0441\u044f \u0432 \u043e\u0442\u0432\u0435\u0442\u0435, \u0435\u0441\u043b\u0438 \u0432 \u0437\u0430\u043f\u0440\u043e\u0441\u0435 \u0443\u043a\u0430\u0437\u0430\u043d \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 `include` \u0441 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u044e\u0449...")
    events_resource_instances: list[ResourceInstance] | None = Field(default=None, description="\u042d\u043a\u0437\u0435\u043c\u043f\u043b\u044f\u0440\u044b \u0440\u0435\u0441\u0443\u0440\u0441\u043e\u0432, \u043f\u0440\u0438\u0432\u044f\u0437\u0430\u043d\u043d\u044b\u0435 \u043a \u0437\u0430\u043f\u0438\u0441\u044f\u043c \u0438\u043b\u0438 \u0441\u043e\u0431\u044b\u0442\u0438\u044f\u043c \u0432 \u0440\u0430\u043c\u043a\u0430\u0445 \u0441\u0435\u0440\u0438\u0438 \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f. \u0412\u043e\u0437\u0432\u0440\u0430\u0449\u0430\u044e\u0442\u0441\u044f \u0432 \u043e\u0442\u0432\u0435\u0442\u0435, \u0435\u0441\u043b\u0438 \u0432 \u0437\u0430\u043f\u0440\u043e\u0441\u0435 \u0443\u043a\u0430\u0437\u0430\u043d \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 `include` \u0441 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u043c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435\u043c.")
    events: list[TimetableEventScheduleEvent2] | None = Field(default=None, description="\u0421\u0443\u0449\u043d\u043e\u0441\u0442\u0438 \u0437\u0430\u043f\u0438\u0441\u0435\u0439 \u0438\u043b\u0438 \u0441\u043e\u0431\u044b\u0442\u0438\u0439 \u0432 \u0440\u0430\u043c\u043a\u0430\u0445 \u0441\u0435\u0440\u0438\u0438 \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f. \u0412\u043e\u0437\u0432\u0440\u0430\u0449\u0430\u044e\u0442\u0441\u044f \u0432 \u043e\u0442\u0432\u0435\u0442\u0435, \u0435\u0441\u043b\u0438 \u0432 \u0437\u0430\u043f\u0440\u043e\u0441\u0435 \u0443\u043a\u0430\u0437\u0430\u043d \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 `include` \u0441 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u043c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435\u043c.")


class GetCalculationCalculationIdResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: Any | None = Field(default=None, alias="data")
    meta: dict[str, Any] | None = Field(default=None)


class GetCompanyIdGoodIdResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    loyalty_generate_code200_option: LoyaltyGenerateCode200Option2 | None = Field(default=None, alias="LoyaltyGenerateCode200Option")
    data_: LoyaltyGenerateCode200DataOption2 = Field(alias="data")
    meta: list[dict[str, Any]]
    success: bool


class GetSettingsTimeslotsResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: GetSettingsTimeslotsResponse200Data | None = Field(default=None, alias="data")
    meta: dict[str, Any] | None = Field(default=None)


class PatchDaysDayIdResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: TimetableEventScheduleDay2 | None = Field(default=None, alias="data")
    meta: dict[str, Any] | None = Field(default=None)


class PostActivityIdRecordsRequest(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    client_id: int | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043a\u043b\u0438\u0435\u043d\u0442\u0430.")
    comer_id: int | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043f\u043e\u0441\u0435\u0442\u0438\u0442\u0435\u043b\u044f.")
    client_: PostActivityIdRecordsRequestClient = Field(alias="client")
    comer: PostActivityIdRecordsRequestComer | None = Field(default=None)
    labels: list[int] | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440\u044b \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0439 \u0437\u0430\u043f\u0438\u0441\u0438.")
    clients_count: int = Field(description="\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u043e\u0441\u0435\u0442\u0438\u0442\u0435\u043b\u0435\u0439.")


class PostScheduleIdDaysResponse201(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: TimetableEventScheduleDay2 | None = Field(default=None, alias="data")
    meta: dict[str, Any] | None = Field(default=None)


class ClientVisitsHistory(BaseModel):
    """Данные по визитам клиента, включая записи и продажи товаров.
    Схема спеки: Объект модели "История посещений клиента"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    goods_transactions: list[ClientVisitsHistoryGoodsTransaction] | None = Field(default=None, description="\u0421\u043f\u0438\u0441\u043e\u043a \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u0439 \u043f\u043e \u043f\u0440\u043e\u0434\u0430\u0436\u0430\u043c \u0442\u043e\u0432\u0430\u0440\u043e\u0432.")
    records: list[ClientVisitsHistoryRecord] | None = Field(default=None, description="\u0421\u043f\u0438\u0441\u043e\u043a \u0437\u0430\u043f\u0438\u0441\u0435\u0439 \u043a\u043b\u0438\u0435\u043d\u0442\u0430.")


class CompanyAnalyticsOverallDataType(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data_: AnalyticsReportOverallStats2 = Field(alias="data")
    meta: list[dict[str, Any]] = Field(description="\u041c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435")
    success: bool = Field(description="\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (true)")


class TimetableEventSchedule2(BaseModel):
    """Данные по существующему в филиале расписанию записей или событий.
    Схема спеки: Объект модели "Расписание"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f.")
    created_at: str | None = Field(default=None, description="\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f.")
    updated_at: str | None = Field(default=None, description="\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0433\u043e \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f.")
    deleted_at: str | None = Field(default=None, description="\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0443\u0434\u0430\u043b\u0435\u043d\u0438\u044f \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f.")
    original_entity_type: Literal["record", "activity"] | None = Field(default=None, description="\u0422\u0438\u043f \u0441\u0443\u0449\u043d\u043e\u0441\u0442\u0438, \u043d\u0430 \u043e\u0441\u043d\u043e\u0432\u0435 \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u0431\u044b\u043b\u043e \u0441\u043e\u0437\u0434\u0430\u043d\u043e \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0435.")
    original_entity_id: float | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0441\u0443\u0449\u043d\u043e\u0441\u0442\u0438, \u043d\u0430 \u043e\u0441\u043d\u043e\u0432\u0435 \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u0431\u044b\u043b\u043e \u0441\u043e\u0437\u0434\u0430\u043d\u043e \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0435.")
    date_start: str | None = Field(default=None, description="\u0414\u0430\u0442\u0430 \u043d\u0430\u0447\u0430\u043b\u0430 \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f.")
    date_end: str | None = Field(default=None, description="\u0414\u0430\u0442\u0430 \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f.")
    days: list[TimetableEventScheduleDay2] | None = Field(default=None, description="\u0421\u0435\u0440\u0438\u0438 \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f, \u043f\u0440\u0438\u0432\u044f\u0437\u0430\u043d\u043d\u044b\u0435 \u043a \u0434\u0430\u043d\u043d\u043e\u043c\u0443 \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044e. \u0412\u043e\u0437\u0432\u0440\u0430\u0449\u0430\u044e\u0442\u0441\u044f \u0432 \u043e\u0442\u0432\u0435\u0442\u0435, \u0435\u0441\u043b\u0438 \u0432 \u0437\u0430\u043f\u0440\u043e\u0441\u0435 \u0443\u043a\u0430\u0437\u0430\u043d \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 `include` \u0441 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u043c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435\u043c.")


class TimetableEventScheduleClientSchedule(BaseModel):
    """Данные по существующему в филиале графику посещений клиента.
    Схема спеки: Объект модели "График посещений клиента"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0433\u0440\u0430\u0444\u0438\u043a\u0430 \u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u0439 \u043a\u043b\u0438\u0435\u043d\u0442\u0430.")
    loyalty_abonement_id: float | None = Field(default=None, description="\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0430\u0431\u043e\u043d\u0435\u043c\u0435\u043d\u0442\u0430, \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u043d\u043e\u0433\u043e \u0432 \u0433\u0440\u0430\u0444\u0438\u043a\u0435 \u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u0439 \u043a\u043b\u0438\u0435\u043d\u0442\u0430.")
    final_day: str | None = Field(default=None, description="\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f \u0433\u0440\u0430\u0444\u0438\u043a\u0430 \u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u0439 \u043a\u043b\u0438\u0435\u043d\u0442\u0430.")
    finish_date_type: Literal["end", "fixed", "abonement"] | None = Field(default=None, description="\u0422\u0438\u043f \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f")
    days: list[TimetableEventScheduleDay2] | None = Field(default=None, description="\u0421\u0435\u0440\u0438\u0438 \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u044f, \u043f\u0440\u0438\u0432\u044f\u0437\u0430\u043d\u043d\u044b\u0435 \u043a \u0434\u0430\u043d\u043d\u043e\u043c\u0443 \u0433\u0440\u0430\u0444\u0438\u043a\u0443 \u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u0439 \u043a\u043b\u0438\u0435\u043d\u0442\u0430.")


class GetEntityTypeEntityIdResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: TimetableEventSchedule2 | None = Field(default=None, alias="data")
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
