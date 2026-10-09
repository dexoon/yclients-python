"""Модели YCLIENTS API (g2: G).

Сгенерировано scripts/generate.py -- не редактируйте вручную.
"""

from __future__ import annotations

from datetime import date, datetime
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class GetStaffIdPeriodResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: Any | None = Field(default=None, alias="data")
    meta: dict[str, Any] | None = Field(default=None)


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


class GetAbonementsSearchForActivityResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data_: list[SearchForActivityItem] | None = Field(default=None, alias="data")
    included: list[Any] | None = Field(default=None, description="Массив инклюдов (включений)")


class GetEntityTypeEntityIdResponse200(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None)
    data_: TimetableEventSchedule2 | None = Field(default=None, alias="data")
    meta: dict[str, Any] | None = Field(default=None)

__all__ = [
    "GetAbonementsSearchForActivityResponse200",
    "GetCalculationCalculationIdResponse200",
    "GetCompanyIdGoodIdResponse200",
    "GetEntityTypeEntityIdResponse200",
    "GetSettingsTimeslotsResponse200",
    "GetStaffIdPeriodResponse200"
]
