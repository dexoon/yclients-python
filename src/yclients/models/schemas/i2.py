"""Модели YCLIENTS API (i2: I).

Сгенерировано scripts/generate.py -- не редактируйте вручную.
"""

from __future__ import annotations

from datetime import date, datetime
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class I18nLangInfoDataTypesUserDataForm(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    loyalty_phone_tip: str | None = Field(default=None, alias="loyalty-phone-tip")
    name_required: str | None = Field(default=None, alias="name-required")
    email_required: str | None = Field(default=None, alias="email-required")
    loyalty_email: str | None = Field(default=None, alias="loyalty-email")
    agreement_link: str | None = Field(default=None, alias="agreement-link")
    data_processing_link: str | None = Field(default=None, alias="data-processing-link")
    terms_prefix: str | None = Field(default=None, alias="terms-prefix")
    proceed: str | None = Field(default=None)
    pay: str | None = Field(default=None)
    phone_code: str | None = Field(default=None, alias="phone-code")
    phone: str | None = Field(default=None)
    invalid_phone: str | None = Field(default=None, alias="invalid-phone")


class Image2(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float = Field(alias="id", description="id изображения")
    path: str = Field(description="Путь к изображению")
    width: float = Field(description="Ширина изображения")
    height: float = Field(description="Высота изображения")
    type_: str = Field(alias="type", description="Тип изображения")
    image_group_id: float = Field(description="Id группы изображений")
    version: str = Field(description="Версия изображения")


class I18nLangInfoDataTypesActivity(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    places_left: str | None = Field(default=None)
    filters: I18nLangInfoDataTypesActivityFilters | None = Field(default=None)


class I18nLangInfoDataTypesCity(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    town_abbreviation: str | None = Field(default=None)
    service_count: str | None = Field(default=None)
    select_filial: str | None = Field(default=None)
    not_found_cities: str | None = Field(default=None)
    search_cities: str | None = Field(default=None)
    affiliate: I18nLangInfoDataTypesCityAffiliate | None = Field(default=None)


class I18nLangInfoDataTypesConfirmErrors(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    name: I18nLangInfoDataTypesConfirmErrorsName | None = Field(default=None)
    company: I18nLangInfoDataTypesConfirmErrorsCompany | None = Field(default=None)
    phone: I18nLangInfoDataTypesConfirmErrorsPhone | None = Field(default=None)
    email: I18nLangInfoDataTypesConfirmErrorsEmail | None = Field(default=None)
    agreement: I18nLangInfoDataTypesConfirmErrorsAgreement | None = Field(default=None)
    agreement_privacy_and_terms_of_use: I18nLangInfoDataTypesConfirmErrorsAgreementPrivacyAndTermsOfUse | None = Field(default=None)
    comment_default: I18nLangInfoDataTypesConfirmErrorsCommentDefault | None = Field(default=None)
    comment: I18nLangInfoDataTypesConfirmErrorsComment | None = Field(default=None)
    code: I18nLangInfoDataTypesConfirmErrorsCode | None = Field(default=None)


class I18nLangInfoDataTypesConfirmOrderErrors(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    unknown: str | None = Field(default=None)
    server: str | None = Field(default=None)
    code_400: str | None = Field(default=None)
    code_404: str | None = Field(default=None)
    code_422: str | None = Field(default=None)
    code_437: str | None = Field(default=None)
    code_433: str | None = Field(default=None)
    code_436: str | None = Field(default=None)
    code_438: str | None = Field(default=None)
    code_501: str | None = Field(default=None)
    big_letter: I18nLangInfoDataTypesConfirmOrderErrorsBigLetter | None = Field(default=None, alias="bigLetter")


class I18nLangInfoDataTypesDate(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    day_of: str | None = Field(default=None)
    no_record: str | None = Field(default=None)
    have_record: str | None = Field(default=None)
    by_month_num: I18nLangInfoDataTypesDateByMonthNum | None = Field(default=None)
    by_month_short: I18nLangInfoDataTypesDateByMonthShort | None = Field(default=None)


class I18nLangInfoDataTypesLogin(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    login: str | None = Field(default=None)
    sms_auth: str | None = Field(default=None)
    input_code_confirm: str | None = Field(default=None)
    input_phone_num: str | None = Field(default=None)
    input_login_and_password: str | None = Field(default=None)
    code_confirm: str | None = Field(default=None)
    come_in: str | None = Field(default=None)
    sms_not_send_with_colon: str | None = Field(default=None)
    sms_not_send: str | None = Field(default=None)
    sms_not_send_next_try: str | None = Field(default=None)
    request_new_sms_code: str | None = Field(default=None)
    change_phone_num: str | None = Field(default=None)
    get_code: str | None = Field(default=None)
    or_: str | None = Field(default=None, alias="or")
    authorized_as: str | None = Field(default=None)
    come_in_with_login_and_pass: str | None = Field(default=None)
    phone_or_email: str | None = Field(default=None)
    pass_: str | None = Field(default=None, alias="pass")
    come_in_with_sms_authorise: str | None = Field(default=None)
    errors: I18nLangInfoDataTypesLoginErrors | None = Field(default=None)


class I18nLangInfoDataTypesLoyaltyPrograms(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    item_type_id: I18nLangInfoDataTypesLoyaltyProgramsItemTypeId | None = Field(default=None)
    determined_action_settings: str | None = Field(default=None)


class I18nLangInfoDataTypesMaster(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    master: str | None = Field(default=None)
    skip_select_master: str | None = Field(default=None)
    skip_select: str | None = Field(default=None)
    near_session: str | None = Field(default=None)
    nearest_time: str | None = Field(default=None)
    no_record: str | None = Field(default=None)
    no_record_new: str | None = Field(default=None)
    no_master: str | None = Field(default=None)
    any_master: str | None = Field(default=None)
    record_is_available: str | None = Field(default=None)
    reviews: I18nLangInfoDataTypesMasterReviews | None = Field(default=None)
    prepaid: I18nLangInfoDataTypesMasterPrepaid | None = Field(default=None)


class I18nLangInfoDataTypesProfile(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    name: I18nLangInfoDataTypesProfileName | None = Field(default=None)
    no_future_records: str | None = Field(default=None, alias="noFutureRecords")
    no_past_records: str | None = Field(default=None, alias="noPastRecords")
    phone: I18nLangInfoDataTypesProfilePhone | None = Field(default=None)
    email: I18nLangInfoDataTypesProfileEmail | None = Field(default=None)
    password: I18nLangInfoDataTypesProfilePassword | None = Field(default=None)
    error: str | None = Field(default=None)
    saved: str | None = Field(default=None)
    contacts_details: str | None = Field(default=None, alias="contactsDetails")
    your_records: str | None = Field(default=None)


class I18nLangInfoDataTypesRegistration(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    registration: str | None = Field(default=None)
    form: I18nLangInfoDataTypesRegistrationForm | None = Field(default=None)


class I18nLangInfoDataTypesService(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    selected: str | None = Field(default=None)
    selected_service_count: str | None = Field(default=None)
    no_services_and_events: str | None = Field(default=None, alias="noServicesAndEvents")
    no_more_services: str | None = Field(default=None, alias="noMoreServices")
    no_more_service: str | None = Field(default=None, alias="noMoreService")
    search: str | None = Field(default=None)
    sale: str | None = Field(default=None)
    services: str | None = Field(default=None)
    add: str | None = Field(default=None)
    add_short: str | None = Field(default=None)
    currency_short: str | None = Field(default=None)
    services_pref: I18nLangInfoDataTypesServiceServicesPref | None = Field(default=None)
    order_on: str | None = Field(default=None)
    price: str | None = Field(default=None)
    price_not_available: str | None = Field(default=None)
    price_from: str | None = Field(default=None)
    price_to: str | None = Field(default=None)
    unavailable_service: str | None = Field(default=None)
    unavailable_services: str | None = Field(default=None)


class I18nLangInfoDataTypesSteps(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    date_and_time: str | None = Field(default=None)
    staff: I18nLangInfoDataTypesStepsStaff | None = Field(default=None)
    service: str | None = Field(default=None)
    time: str | None = Field(default=None)


class I18nLangInfoDataTypesTime(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    hour_cased: I18nLangInfoDataTypesTimeHourCased | None = Field(default=None, alias="hourCased")
    week_cased: I18nLangInfoDataTypesTimeWeekCased | None = Field(default=None, alias="weekCased")
    month_cased: I18nLangInfoDataTypesTimeMonthCased | None = Field(default=None, alias="monthCased")
    year_cased: I18nLangInfoDataTypesTimeYearCased | None = Field(default=None, alias="yearCased")
    day_cased: I18nLangInfoDataTypesTimeDayCased | None = Field(default=None, alias="dayCased")
    minute_cased: I18nLangInfoDataTypesTimeMinuteCased | None = Field(default=None, alias="minuteCased")
    second_cased: I18nLangInfoDataTypesTimeSecondCased | None = Field(default=None, alias="secondCased")
    at_o_clock: str | None = Field(default=None)
    no_times: str | None = Field(default=None, alias="noTimes")
    the_part_of_day: I18nLangInfoDataTypesTimeThePartOfDay | None = Field(default=None)
    by_week_day: I18nLangInfoDataTypesTimeByWeekDay | None = Field(default=None)
    by_full_week_day: I18nLangInfoDataTypesTimeByFullWeekDay | None = Field(default=None)


class I18nLangInfoDataTypesTips(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    terms: I18nLangInfoDataTypesTipsTerms | None = Field(default=None)
    review_sent: str | None = Field(default=None, alias="review-sent")
    your_mark: str | None = Field(default=None, alias="your-mark")
    leave_a_review: str | None = Field(default=None, alias="leave-a-review")
    leave_a_tip_to_a_specialist: str | None = Field(default=None, alias="leave-a-tip-to-a-specialist")
    credited: str | None = Field(default=None)
    visit_amount: str | None = Field(default=None, alias="visit-amount")
    will_be_written_off: str | None = Field(default=None, alias="will-be-written-off")
    at_time: str | None = Field(default=None, alias="at-time")
    rate_specialist_to_sent_feedback: str | None = Field(default=None, alias="rate-specialist-to-sent-feedback")
    title: str | None = Field(default=None)
    tips_required: str | None = Field(default=None, alias="tips-required")
    review_or_tips_required: str | None = Field(default=None, alias="review-or-tips-required")
    enter_sum: str | None = Field(default=None, alias="enter-sum")
    custom_sum: str | None = Field(default=None, alias="custom-sum")
    cancel_tips: str | None = Field(default=None, alias="cancel-tips")
    bad_sum: str | None = Field(default=None, alias="bad-sum")


class ImageGroup2(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float = Field(alias="id", description="id группы изображений")
    entity: str | None = Field(default=None, description="Название сущности, к которой привязана группа")
    entity_id: float | None = Field(default=None, description="Id сущности")
    images: Image2
    image_binded: bool = Field(description="Статус привязки изображений к сущности")
    image_group: dict[str, Any] = Field(description="Объект группа изображений")


class I18nLangInfoDataTypesConfirm(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    confirm: str | None = Field(default=None)
    show_order_details: str | None = Field(default=None)
    order_details: str | None = Field(default=None)
    sms_notify: str | None = Field(default=None, alias="smsNotify")
    dont_send: str | None = Field(default=None, alias="dontSend")
    order_on: str | None = Field(default=None)
    service_sale: str | None = Field(default=None)
    license_text: str | None = Field(default=None)
    accept: str | None = Field(default=None)
    i_accept: str | None = Field(default=None)
    i_agree: str | None = Field(default=None)
    accept_inline: str | None = Field(default=None)
    accept_personal_data_inline: str | None = Field(default=None)
    and_accept: str | None = Field(default=None)
    terms_of_agreement: str | None = Field(default=None)
    terms_of_agreement_inline: str | None = Field(default=None)
    how_my_personal_data_will_be_processed: str | None = Field(default=None)
    first_name: str | None = Field(default=None)
    phone: str | None = Field(default=None)
    will_be_used_to_confirm: str | None = Field(default=None)
    comment: str | None = Field(default=None)
    email: str | None = Field(default=None)
    recording: str | None = Field(default=None)
    code_and_phone_num: str | None = Field(default=None)
    phone_confirm_short: str | None = Field(default=None)
    phone_already_exists: str | None = Field(default=None)
    phone_confirm: str | None = Field(default=None)
    phone_confirm_button: str | None = Field(default=None)
    default_error: str | None = Field(default=None, alias="defaultError")
    you_want_to_book: str | None = Field(default=None)
    your_master: str | None = Field(default=None)
    waiting_for_you_at_the_address: str | None = Field(default=None)
    until_visit: I18nLangInfoDataTypesConfirmUntilVisit | None = Field(default=None, alias="untilVisit")
    order_errors_actions: I18nLangInfoDataTypesConfirmOrderErrorsActions | None = Field(default=None, alias="orderErrorsActions")
    order_errors: I18nLangInfoDataTypesConfirmOrderErrors | None = Field(default=None, alias="orderErrors")
    errors: I18nLangInfoDataTypesConfirmErrors | None = Field(default=None)


class I18nLangInfoDataTypesLoyalty(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    empty_list: str | None = Field(default=None, alias="empty-list")
    points: I18nLangInfoDataTypesLoyaltyPoints | None = Field(default=None)
    no_cards: str | None = Field(default=None)
    no_certificate: str | None = Field(default=None)
    no_subscription: str | None = Field(default=None)
    discount: str | None = Field(default=None)
    cashback: str | None = Field(default=None)
    paid_amount: str | None = Field(default=None)
    sold_amount: str | None = Field(default=None)
    visit_count: str | None = Field(default=None)
    balance: str | None = Field(default=None)
    certificate: I18nLangInfoDataTypesLoyaltyCertificate | None = Field(default=None)
    subscription: I18nLangInfoDataTypesLoyaltySubscription | None = Field(default=None)
    subscriptions: I18nLangInfoDataTypesLoyaltySubscriptions | None = Field(default=None)
    programs: I18nLangInfoDataTypesLoyaltyPrograms | None = Field(default=None)


class I18nLangInfoDataTypes(BaseModel):
    """Интернационализация вормы бронирования.
    Схема спеки: Root Type for i18n_lang_info
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    param_404: I18nLangInfoDataTypesParam404 | None = Field(default=None, alias="404")
    action: I18nLangInfoDataTypesAction | None = Field(default=None)
    tips: I18nLangInfoDataTypesTips | None = Field(default=None)
    payment_status: I18nLangInfoDataTypesPaymentStatus | None = Field(default=None, alias="payment-status")
    user_data_form: I18nLangInfoDataTypesUserDataForm | None = Field(default=None, alias="user-data-form")
    and_: str | None = Field(default=None, alias="and")
    terms_of_agreement: str | None = Field(default=None, alias="terms-of-agreement")
    data_processing: str | None = Field(default=None, alias="data-processing")
    license_agreement: str | None = Field(default=None, alias="license-agreement")
    personal_data: str | None = Field(default=None, alias="personal-data")
    buy_for: str | None = Field(default=None, alias="buy-for")
    group_booking: I18nLangInfoDataTypesGroupBooking | None = Field(default=None)
    geo: I18nLangInfoDataTypesGeo | None = Field(default=None)
    tooltips: I18nLangInfoDataTypesTooltips | None = Field(default=None)
    prepaid: I18nLangInfoDataTypesPrepaid | None = Field(default=None)
    back: str | None = Field(default=None)
    back_city: str | None = Field(default=None, alias="backCity")
    back_filials: str | None = Field(default=None, alias="backFilials")
    back_record_type: str | None = Field(default=None, alias="backRecordType")
    filials: str | None = Field(default=None)
    my_profile: str | None = Field(default=None)
    about_us: str | None = Field(default=None)
    record: I18nLangInfoDataTypesRecord | None = Field(default=None)
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
    address: I18nLangInfoDataTypesAddress | None = Field(default=None)
    common: I18nLangInfoDataTypesCommon | None = Field(default=None)
    notification: I18nLangInfoDataTypesNotification | None = Field(default=None)
    header: I18nLangInfoDataTypesHeader | None = Field(default=None)
    loyalty: I18nLangInfoDataTypesLoyalty | None = Field(default=None)
    save: str | None = Field(default=None)
    proceed: str | None = Field(default=None)
    profile: I18nLangInfoDataTypesProfile | None = Field(default=None)
    registration: I18nLangInfoDataTypesRegistration | None = Field(default=None)
    menu: I18nLangInfoDataTypesMenu | None = Field(default=None)
    footer: I18nLangInfoDataTypesFooter | None = Field(default=None)
    city: I18nLangInfoDataTypesCity | None = Field(default=None)
    company: I18nLangInfoDataTypesCompany | None = Field(default=None)
    steps: I18nLangInfoDataTypesSteps | None = Field(default=None)
    master: I18nLangInfoDataTypesMaster | None = Field(default=None)
    cart: I18nLangInfoDataTypesCart | None = Field(default=None)
    reviews: I18nLangInfoDataTypesReviews | None = Field(default=None)
    date: I18nLangInfoDataTypesDate | None = Field(default=None)
    time: I18nLangInfoDataTypesTime | None = Field(default=None)
    service: I18nLangInfoDataTypesService | None = Field(default=None)
    confirm: I18nLangInfoDataTypesConfirm | None = Field(default=None)
    login: I18nLangInfoDataTypesLogin | None = Field(default=None)
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
    activity: I18nLangInfoDataTypesActivity | None = Field(default=None)
    button: I18nLangInfoDataTypesButton | None = Field(default=None)
    landscape: str | None = Field(default=None)

__all__ = [
    "I18nLangInfoDataTypes",
    "I18nLangInfoDataTypesActivity",
    "I18nLangInfoDataTypesCity",
    "I18nLangInfoDataTypesConfirm",
    "I18nLangInfoDataTypesConfirmErrors",
    "I18nLangInfoDataTypesConfirmOrderErrors",
    "I18nLangInfoDataTypesDate",
    "I18nLangInfoDataTypesLogin",
    "I18nLangInfoDataTypesLoyalty",
    "I18nLangInfoDataTypesLoyaltyPrograms",
    "I18nLangInfoDataTypesMaster",
    "I18nLangInfoDataTypesProfile",
    "I18nLangInfoDataTypesRegistration",
    "I18nLangInfoDataTypesService",
    "I18nLangInfoDataTypesSteps",
    "I18nLangInfoDataTypesTime",
    "I18nLangInfoDataTypesTips",
    "I18nLangInfoDataTypesUserDataForm",
    "Image2",
    "ImageGroup2"
]
