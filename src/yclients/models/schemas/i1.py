"""Модели YCLIENTS API (i1: I).

Сгенерировано scripts/generate.py -- не редактируйте вручную.
"""

from __future__ import annotations

from datetime import date, datetime
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class I18nLangInfoDataTypesAction(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    send: str | None = Field(default=None)


class I18nLangInfoDataTypesActivityFilters(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    select: str | None = Field(default=None)
    reset: str | None = Field(default=None)
    apply: str | None = Field(default=None)


class I18nLangInfoDataTypesAddress(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    about: str | None = Field(default=None)
    address: str | None = Field(default=None)
    phone: str | None = Field(default=None)
    phones: str | None = Field(default=None)
    schedule: str | None = Field(default=None)
    site: str | None = Field(default=None)
    date_and_time: str | None = Field(default=None)
    photos: str | None = Field(default=None)
    details: str | None = Field(default=None)


class I18nLangInfoDataTypesButton(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    select: str | None = Field(default=None)
    select_time: str | None = Field(default=None)
    all_right: str | None = Field(default=None)
    get_sms: str | None = Field(default=None)
    back: str | None = Field(default=None)
    add_more: str | None = Field(default=None)
    remove_from_record: str | None = Field(default=None, alias="remove-from-record")
    continue_: str | None = Field(default=None, alias="continue")
    confirm: str | None = Field(default=None)
    canceling: str | None = Field(default=None)
    more_reviews: str | None = Field(default=None)


class I18nLangInfoDataTypesCart(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    title: str | None = Field(default=None)
    confirm: str | None = Field(default=None)
    go_to_pay: str | None = Field(default=None, alias="go-to-pay")
    confirmed: str | None = Field(default=None)
    pay_success: str | None = Field(default=None, alias="pay-success")


class I18nLangInfoDataTypesCityAffiliate(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    param_1: str | None = Field(default=None, alias="1")
    param_2: str | None = Field(default=None, alias="2")
    param_3: str | None = Field(default=None, alias="3")


class I18nLangInfoDataTypesCommon(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    information: str | None = Field(default=None)
    reviews: str | None = Field(default=None)
    contacts: str | None = Field(default=None)


class I18nLangInfoDataTypesCompany(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    list_: str | None = Field(default=None, alias="list")
    on_map: str | None = Field(default=None)
    no_companies_text_1: str | None = Field(default=None)
    lk: str | None = Field(default=None)
    no_companies_text_2: str | None = Field(default=None)
    no_companies: str | None = Field(default=None)
    near_session: str | None = Field(default=None)
    active_master: str | None = Field(default=None)
    at_o_clock: str | None = Field(default=None)
    find_companies: str | None = Field(default=None)
    not_found_companies: str | None = Field(default=None)
    look_at_the_map: str | None = Field(default=None)


class I18nLangInfoDataTypesConfirmErrorsAgreement(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    required: str | None = Field(default=None)


class I18nLangInfoDataTypesConfirmErrorsAgreementPrivacyAndTermsOfUse(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    required: str | None = Field(default=None)


class I18nLangInfoDataTypesConfirmErrorsCode(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    incorrect: str | None = Field(default=None)


class I18nLangInfoDataTypesConfirmErrorsComment(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    required: str | None = Field(default=None)


class I18nLangInfoDataTypesConfirmErrorsCommentDefault(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    required: str | None = Field(default=None)


class I18nLangInfoDataTypesConfirmErrorsCompany(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    required: str | None = Field(default=None)


class I18nLangInfoDataTypesConfirmErrorsEmail(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    required: str | None = Field(default=None)
    invalid: str | None = Field(default=None)


class I18nLangInfoDataTypesConfirmErrorsName(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    required: str | None = Field(default=None)


class I18nLangInfoDataTypesConfirmErrorsPhone(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    required: str | None = Field(default=None)
    incorrect: str | None = Field(default=None)


class I18nLangInfoDataTypesConfirmOrderErrorsActions(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    change_service: str | None = Field(default=None, alias="changeService")
    change_time: str | None = Field(default=None, alias="changeTime")
    change_record: str | None = Field(default=None, alias="changeRecord")
    delete_record: str | None = Field(default=None, alias="deleteRecord")


class I18nLangInfoDataTypesConfirmOrderErrorsBigLetter(BaseModel):

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


class I18nLangInfoDataTypesConfirmUntilVisit(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    postfix: str | None = Field(default=None)
    prefix: str | None = Field(default=None)


class I18nLangInfoDataTypesDateByMonthNum(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    param_1: str | None = Field(default=None, alias="1")
    param_2: str | None = Field(default=None, alias="2")
    param_3: str | None = Field(default=None, alias="3")
    param_4: str | None = Field(default=None, alias="4")
    param_5: str | None = Field(default=None, alias="5")
    param_6: str | None = Field(default=None, alias="6")
    param_7: str | None = Field(default=None, alias="7")
    param_10: str | None = Field(default=None, alias="10")
    param_11: str | None = Field(default=None, alias="11")
    param_12: str | None = Field(default=None, alias="12")
    param_08: str | None = Field(default=None, alias="08")
    param_09: str | None = Field(default=None, alias="09")


class I18nLangInfoDataTypesDateByMonthShort(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

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


class I18nLangInfoDataTypesFooter(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    worked_on: str | None = Field(default=None)
    worked_on_company_name: str | None = Field(default=None)


class I18nLangInfoDataTypesGeo(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    geo_timeout_error: str | None = Field(default=None)
    geo_timeout_error_android: str | None = Field(default=None)
    geo_access_error: str | None = Field(default=None)


class I18nLangInfoDataTypesGroupBooking(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    personal_booking: str | None = Field(default=None)
    group_booking: str | None = Field(default=None)
    choose_group_event: str | None = Field(default=None)
    group_events_available: str | None = Field(default=None)
    places: str | None = Field(default=None)
    group_events_is_not_available: str | None = Field(default=None)
    group_events_is_not_available_filial: str | None = Field(default=None)
    repeat: str | None = Field(default=None)
    duration: str | None = Field(default=None)
    no_space: str | None = Field(default=None)
    not_found: str | None = Field(default=None)


class I18nLangInfoDataTypesHeader(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    loyalty_cards: str | None = Field(default=None)
    widget_settings: str | None = Field(default=None)
    settings: str | None = Field(default=None)
    select_town: str | None = Field(default=None)
    select_company: str | None = Field(default=None)
    select_date: str | None = Field(default=None)
    select_master: str | None = Field(default=None)
    select_time: str | None = Field(default=None)
    select_service: str | None = Field(default=None)
    input_personal: str | None = Field(default=None)
    online_record: str | None = Field(default=None)
    selection_of: str | None = Field(default=None)
    contacts_form: str | None = Field(default=None)
    record_created: str | None = Field(default=None)
    login: str | None = Field(default=None)
    profile: str | None = Field(default=None)
    my_records: str | None = Field(default=None)
    record_create_disabled: str | None = Field(default=None)
    master_info: str | None = Field(default=None, alias="master-info")
    notification: str | None = Field(default=None)
    my_notifications: str | None = Field(default=None)
    none_notifications: str | None = Field(default=None)
    cart: str | None = Field(default=None)
    change_record: str | None = Field(default=None)
    you_booking: str | None = Field(default=None)
    you_data: str | None = Field(default=None)
    record: str | None = Field(default=None)
    actions: str | None = Field(default=None)
    cancel_record: str | None = Field(default=None, alias="cancel-record")
    booking_again: str | None = Field(default=None)
    choose_time: str | None = Field(default=None)
    choose_staff: str | None = Field(default=None)
    about_service: str | None = Field(default=None)
    records: str | None = Field(default=None)
    confirmation: str | None = Field(default=None)


class I18nLangInfoDataTypesLoginErrors(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    incorrect_login_password: str | None = Field(default=None)
    undefined_error: str | None = Field(default=None)


class I18nLangInfoDataTypesLoyaltyCertificate(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    services_includes: str | None = Field(default=None, alias="services-includes")
    no_restrictions: str | None = Field(default=None, alias="no-restrictions")
    restrictions_only_services: str | None = Field(default=None, alias="restrictions-only-services")
    any_goods: str | None = Field(default=None, alias="any-goods")
    without_goods: str | None = Field(default=None, alias="without-goods")
    without_services: str | None = Field(default=None, alias="without-services")
    validity: str | None = Field(default=None)
    validity_without_restrictions: str | None = Field(default=None, alias="validity-without-restrictions")
    validity_till: str | None = Field(default=None, alias="validity-till")
    validity_after_purchase: str | None = Field(default=None, alias="validity-after-purchase")
    use_type: str | None = Field(default=None, alias="use-type")
    use_type_multiple: str | None = Field(default=None, alias="use-type-multiple")
    use_type_single: str | None = Field(default=None, alias="use-type-single")
    where_to_use: str | None = Field(default=None, alias="where-to-use")
    where_to_use_show_more: str | None = Field(default=None, alias="where-to-use-show-more")
    where_to_use_all_group: str | None = Field(default=None, alias="where-to-use-all-group")
    allow_to_freeze: str | None = Field(default=None, alias="allow-to-freeze")
    title: str | None = Field(default=None)
    one_off_use: str | None = Field(default=None, alias="one-off-use")
    multi_use: str | None = Field(default=None, alias="multi-use")
    denomination: str | None = Field(default=None)
    balance: str | None = Field(default=None)


class I18nLangInfoDataTypesLoyaltyPoints(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    nominative: str | None = Field(default=None)
    genitive: str | None = Field(default=None)
    plural_genitive: str | None = Field(default=None, alias="plural-genitive")


class I18nLangInfoDataTypesLoyaltyProgramsItemTypeId(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    any_services_any_goods: str | None = Field(default=None)
    any_service_no_goods: str | None = Field(default=None)
    no_services_any_goods: str | None = Field(default=None)
    custom_services_no_goods: str | None = Field(default=None)
    custom_services_any_goods: str | None = Field(default=None)
    no_services_custom_goods: str | None = Field(default=None)
    any_services_custom_goods: str | None = Field(default=None)
    custom_services_custom_goods: str | None = Field(default=None)
    no_services_no_goods: str | None = Field(default=None)


class I18nLangInfoDataTypesLoyaltySubscription(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    validity_without_restrictions: str | None = Field(default=None, alias="validity-without-restrictions")
    title: str | None = Field(default=None)


class I18nLangInfoDataTypesLoyaltySubscriptions(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    all_services: str | None = Field(default=None, alias="all-services")
    from_: str | None = Field(default=None, alias="from")
    valid_until: str | None = Field(default=None)
    valid_unlimited: str | None = Field(default=None)
    unused: str | None = Field(default=None)
    online_sale_button_text: str | None = Field(default=None)


class I18nLangInfoDataTypesMasterPrepaid(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    forbidden: str | None = Field(default=None)
    allowed: str | None = Field(default=None)
    required: str | None = Field(default=None)


class I18nLangInfoDataTypesMasterReviews(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    nominative: str | None = Field(default=None)
    genitive: str | None = Field(default=None)
    plural_genitive: str | None = Field(default=None, alias="plural-genitive")


class I18nLangInfoDataTypesMenu(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    account: str | None = Field(default=None)
    change_filial: str | None = Field(default=None)
    change_city: str | None = Field(default=None)
    online_record: str | None = Field(default=None)
    about: str | None = Field(default=None)
    change_lang: str | None = Field(default=None)
    hide_menu: str | None = Field(default=None)
    login: str | None = Field(default=None)
    my_records: str | None = Field(default=None, alias="myRecords")
    on_line: str | None = Field(default=None, alias="on-line")
    logout: str | None = Field(default=None)
    my: str | None = Field(default=None)
    favorite: str | None = Field(default=None)
    change_password: str | None = Field(default=None)
    header: str | None = Field(default=None)
    profile: str | None = Field(default=None)
    loyalty: str | None = Field(default=None)
    loyalty_subscriptions: str | None = Field(default=None)
    loyalty_certificates: str | None = Field(default=None)


class I18nLangInfoDataTypesNotification(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    your_city: str | None = Field(default=None)
    yes_my_city: str | None = Field(default=None)
    no_my_city: str | None = Field(default=None)
    read_all: str | None = Field(default=None)
    delete_all: str | None = Field(default=None)
    deleted_record: str | None = Field(default=None)
    record: str | None = Field(default=None)
    news: str | None = Field(default=None)
    review: str | None = Field(default=None)
    notify: str | None = Field(default=None)
    sent: str | None = Field(default=None)


class I18nLangInfoDataTypesParam404(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    not_found: str | None = Field(default=None, alias="not-found")
    not_found_record: str | None = Field(default=None, alias="not-found-record")
    go_home: str | None = Field(default=None, alias="go-home")


class I18nLangInfoDataTypesPaymentStatus(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    payment_error: str | None = Field(default=None, alias="payment-error")
    payment_redirect: str | None = Field(default=None, alias="payment-redirect")
    payment_config_error: str | None = Field(default=None, alias="payment-config-error")
    contact_us_for_questions: str | None = Field(default=None, alias="contact-us-for-questions")
    contacts: str | None = Field(default=None)
    order_registered: str | None = Field(default=None, alias="order-registered")
    order_paid: str | None = Field(default=None, alias="order-paid")
    retry: str | None = Field(default=None)
    order_created_successfully: str | None = Field(default=None, alias="order-created-successfully")
    order_is_being_processed: str | None = Field(default=None, alias="order-is-being-processed")
    get_payment_data: str | None = Field(default=None, alias="get-payment-data")
    transaction_number: str | None = Field(default=None, alias="transaction-number")
    payment_transaction_info_1: str | None = Field(default=None, alias="payment-transaction-info-1")
    payment_transaction_info_2: str | None = Field(default=None, alias="payment-transaction-info-2")
    order_number_info: str | None = Field(default=None, alias="order-number-info")


class I18nLangInfoDataTypesPrepaid(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    required: str | None = Field(default=None)
    allowed: str | None = Field(default=None)
    prepaid_sum: str | None = Field(default=None)
    postpaid_sum: str | None = Field(default=None)


class I18nLangInfoDataTypesProfileEmail(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    info: str | None = Field(default=None)


class I18nLangInfoDataTypesProfileName(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    saved: str | None = Field(default=None)
    not_known: str | None = Field(default=None)


class I18nLangInfoDataTypesProfilePassword(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    info: str | None = Field(default=None)
    bad_password: str | None = Field(default=None, alias="badPassword")
    current: str | None = Field(default=None)
    new: str | None = Field(default=None)
    invalid_too_short: str | None = Field(default=None, alias="invalidTooShort")
    invalid_no_digit: str | None = Field(default=None, alias="invalidNoDigit")
    invalid_no_capital: str | None = Field(default=None, alias="invalidNoCapital")
    invalid_no_symbol: str | None = Field(default=None, alias="invalidNoSymbol")


class I18nLangInfoDataTypesProfilePhone(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    confirm: str | None = Field(default=None)


class I18nLangInfoDataTypesRecord(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    show_details: str | None = Field(default=None)
    is_canceled: str | None = Field(default=None)
    is_canceled_success: str | None = Field(default=None)
    record: str | None = Field(default=None)
    place: str | None = Field(default=None)
    master: str | None = Field(default=None)
    service: str | None = Field(default=None)
    services: str | None = Field(default=None)
    date: str | None = Field(default=None)
    past: str | None = Field(default=None)
    through: str | None = Field(default=None)
    time: str | None = Field(default=None)
    clients_count: str | None = Field(default=None)
    book_visit: str | None = Field(default=None)
    add_service: str | None = Field(default=None)
    add_master: str | None = Field(default=None)
    add_datetime: str | None = Field(default=None)
    cancel_record: str | None = Field(default=None)
    cancel_record_warning: str | None = Field(default=None)
    confirm_cancel_record: str | None = Field(default=None)
    error_cancel_record: str | None = Field(default=None)
    error_cancel_record_new1: str | None = Field(default=None)
    error_cancel_record_new2_1: str | None = Field(default=None)
    error_cancel_record_new2_2: str | None = Field(default=None)
    add_to_google_calendar: str | None = Field(default=None)
    booking_success: str | None = Field(default=None)
    create_new_record: str | None = Field(default=None)
    future_records: str | None = Field(default=None)
    past_records: str | None = Field(default=None)
    change_record_time: str | None = Field(default=None)
    error_change_record_time: str | None = Field(default=None)
    error_change_record_time2_1: str | None = Field(default=None)
    error_change_record_time2_2: str | None = Field(default=None)
    selected_services: str | None = Field(default=None)
    calculate_services: str | None = Field(default=None)
    change_record_fail: str | None = Field(default=None)
    continue_booking: str | None = Field(default=None)
    go_to_registration: str | None = Field(default=None)
    repeat: str | None = Field(default=None)
    is_deleted: str | None = Field(default=None)


class I18nLangInfoDataTypesRegistrationForm(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    name: str | None = Field(default=None)
    company_title: str | None = Field(default=None)
    i_know_promo: str | None = Field(default=None)
    confirm_oferta_1: str | None = Field(default=None)
    confirm_oferta_2: str | None = Field(default=None)
    submit: str | None = Field(default=None)
    promo: str | None = Field(default=None)
    unknown_error: str | None = Field(default=None, alias="unknownError")


class I18nLangInfoDataTypesReviews(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    cancel_add_review: str | None = Field(default=None, alias="cancelAddReview")
    later: str | None = Field(default=None)
    add_review: str | None = Field(default=None, alias="addReview")
    your_review_mark: str | None = Field(default=None, alias="yourReviewMark")
    review_field_label_text: str | None = Field(default=None, alias="reviewFieldLabelText")
    review_title: str | None = Field(default=None, alias="reviewTitle")
    review_message: str | None = Field(default=None, alias="reviewMessage")
    review_request_store_title: str | None = Field(default=None, alias="reviewRequestStoreTitle")
    review_button: str | None = Field(default=None, alias="reviewButton")
    thanks_for_review: str | None = Field(default=None, alias="thanksForReview")


class I18nLangInfoDataTypesServiceServicesPref(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    param_1: str | None = Field(default=None, alias="1")
    param_2: str | None = Field(default=None, alias="2")
    param_3: str | None = Field(default=None, alias="3")


class I18nLangInfoDataTypesStepsStaff(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    nominative: str | None = Field(default=None)
    genitive: str | None = Field(default=None)


class I18nLangInfoDataTypesTimeByFullWeekDay(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    monday: str | None = Field(default=None, alias="Monday")
    tuesday: str | None = Field(default=None, alias="Tuesday")
    wednesday: str | None = Field(default=None, alias="Wednesday")
    thursday: str | None = Field(default=None, alias="Thursday")
    friday: str | None = Field(default=None, alias="Friday")
    saturday: str | None = Field(default=None, alias="Saturday")
    sunday: str | None = Field(default=None, alias="Sunday")


class I18nLangInfoDataTypesTimeByWeekDay(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    mon: str | None = Field(default=None, alias="Mon")
    tue: str | None = Field(default=None, alias="Tue")
    wed: str | None = Field(default=None, alias="Wed")
    thu: str | None = Field(default=None, alias="Thu")
    fri: str | None = Field(default=None, alias="Fri")
    sat: str | None = Field(default=None, alias="Sat")
    sun: str | None = Field(default=None, alias="Sun")


class I18nLangInfoDataTypesTimeDayCased(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    nominative: str | None = Field(default=None)
    genitive: str | None = Field(default=None)
    plural_genitive: str | None = Field(default=None, alias="plural-genitive")


class I18nLangInfoDataTypesTimeHourCased(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    nominative: str | None = Field(default=None)
    genitive: str | None = Field(default=None)
    plural_genitive: str | None = Field(default=None, alias="plural-genitive")


class I18nLangInfoDataTypesTimeMinuteCased(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    nominative: str | None = Field(default=None)
    genitive: str | None = Field(default=None)
    accusative: str | None = Field(default=None)
    plural_genitive: str | None = Field(default=None, alias="plural-genitive")


class I18nLangInfoDataTypesTimeMonthCased(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    nominative: str | None = Field(default=None)
    genitive: str | None = Field(default=None)
    plural_genitive: str | None = Field(default=None, alias="plural-genitive")


class I18nLangInfoDataTypesTimeSecondCased(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    nominative: str | None = Field(default=None)
    genitive: str | None = Field(default=None)
    accusative: str | None = Field(default=None)
    plural_genitive: str | None = Field(default=None, alias="plural-genitive")


class I18nLangInfoDataTypesTimeThePartOfDay(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    morning: str | None = Field(default=None)
    day: str | None = Field(default=None)
    evening: str | None = Field(default=None)


class I18nLangInfoDataTypesTimeWeekCased(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    nominative: str | None = Field(default=None)
    genitive: str | None = Field(default=None)
    plural_genitive: str | None = Field(default=None, alias="plural-genitive")


class I18nLangInfoDataTypesTimeYearCased(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    nominative: str | None = Field(default=None)
    genitive: str | None = Field(default=None)
    plural_genitive: str | None = Field(default=None, alias="plural-genitive")


class I18nLangInfoDataTypesTipsTerms(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    prefix: str | None = Field(default=None)
    of_use: str | None = Field(default=None, alias="of-use")
    personal_policy: str | None = Field(default=None, alias="personal-policy")


class I18nLangInfoDataTypesTooltips(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    change_filial: str | None = Field(default=None)
    change_filial_back_button: str | None = Field(default=None)

__all__ = [
    "I18nLangInfoDataTypesAction",
    "I18nLangInfoDataTypesActivityFilters",
    "I18nLangInfoDataTypesAddress",
    "I18nLangInfoDataTypesButton",
    "I18nLangInfoDataTypesCart",
    "I18nLangInfoDataTypesCityAffiliate",
    "I18nLangInfoDataTypesCommon",
    "I18nLangInfoDataTypesCompany",
    "I18nLangInfoDataTypesConfirmErrorsAgreement",
    "I18nLangInfoDataTypesConfirmErrorsAgreementPrivacyAndTermsOfUse",
    "I18nLangInfoDataTypesConfirmErrorsCode",
    "I18nLangInfoDataTypesConfirmErrorsComment",
    "I18nLangInfoDataTypesConfirmErrorsCommentDefault",
    "I18nLangInfoDataTypesConfirmErrorsCompany",
    "I18nLangInfoDataTypesConfirmErrorsEmail",
    "I18nLangInfoDataTypesConfirmErrorsName",
    "I18nLangInfoDataTypesConfirmErrorsPhone",
    "I18nLangInfoDataTypesConfirmOrderErrorsActions",
    "I18nLangInfoDataTypesConfirmOrderErrorsBigLetter",
    "I18nLangInfoDataTypesConfirmUntilVisit",
    "I18nLangInfoDataTypesDateByMonthNum",
    "I18nLangInfoDataTypesDateByMonthShort",
    "I18nLangInfoDataTypesFooter",
    "I18nLangInfoDataTypesGeo",
    "I18nLangInfoDataTypesGroupBooking",
    "I18nLangInfoDataTypesHeader",
    "I18nLangInfoDataTypesLoginErrors",
    "I18nLangInfoDataTypesLoyaltyCertificate",
    "I18nLangInfoDataTypesLoyaltyPoints",
    "I18nLangInfoDataTypesLoyaltyProgramsItemTypeId",
    "I18nLangInfoDataTypesLoyaltySubscription",
    "I18nLangInfoDataTypesLoyaltySubscriptions",
    "I18nLangInfoDataTypesMasterPrepaid",
    "I18nLangInfoDataTypesMasterReviews",
    "I18nLangInfoDataTypesMenu",
    "I18nLangInfoDataTypesNotification",
    "I18nLangInfoDataTypesParam404",
    "I18nLangInfoDataTypesPaymentStatus",
    "I18nLangInfoDataTypesPrepaid",
    "I18nLangInfoDataTypesProfileEmail",
    "I18nLangInfoDataTypesProfileName",
    "I18nLangInfoDataTypesProfilePassword",
    "I18nLangInfoDataTypesProfilePhone",
    "I18nLangInfoDataTypesRecord",
    "I18nLangInfoDataTypesRegistrationForm",
    "I18nLangInfoDataTypesReviews",
    "I18nLangInfoDataTypesServiceServicesPref",
    "I18nLangInfoDataTypesStepsStaff",
    "I18nLangInfoDataTypesTimeByFullWeekDay",
    "I18nLangInfoDataTypesTimeByWeekDay",
    "I18nLangInfoDataTypesTimeDayCased",
    "I18nLangInfoDataTypesTimeHourCased",
    "I18nLangInfoDataTypesTimeMinuteCased",
    "I18nLangInfoDataTypesTimeMonthCased",
    "I18nLangInfoDataTypesTimeSecondCased",
    "I18nLangInfoDataTypesTimeThePartOfDay",
    "I18nLangInfoDataTypesTimeWeekCased",
    "I18nLangInfoDataTypesTimeYearCased",
    "I18nLangInfoDataTypesTipsTerms",
    "I18nLangInfoDataTypesTooltips"
]
