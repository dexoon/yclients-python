"""Модели YCLIENTS API (u: U).

Сгенерировано scripts/generate.py -- не редактируйте вручную.
"""

from __future__ import annotations

from datetime import date, datetime
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class UserInviteResponseDataTypesMeta(BaseModel):
    """Метаданные (содержит сообщение о том, что данные сохранены)
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    message: str | None = Field(default=None)


class UserPermissionsResponseDataTypesDataClients(BaseModel):
    """Раздел Клиенты
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    clients_access: bool | None = Field(default=None, description="true - есть доступ к клиентской базе, false - нет доступа")
    client_phones_access: bool | None = Field(default=None, description="true - есть доступ к номерам телефонов в списке клиентов, false - нет доступа")
    clients_phones_email_access: bool | None = Field(default=None, description="true - есть доступ к номерам телефонов и email в списке клиентов, false - нет доступа")
    clients_card_phone_access: bool | None = Field(default=None, description="true - есть доступ к телефонам в карточке клиента, false - нет доступа")
    clients_delete_access: bool | None = Field(default=None, description="true - есть доступ к удалению клиентов, false - нет доступа")
    clients_excel_access: bool | None = Field(default=None, description="true - есть доступ к выгрузке списка клиентов в Excel, false - нет доступа")
    excel_access: bool | None = Field(default=None, description="1 - есть доступ к выгрузке списка клиентов в Excel, 0 - нет доступа")
    client_comments_list_access: bool | None = Field(default=None, description="true - есть доступ к просмотру комментарии, false - нет доступа")
    client_comments_add_access: bool | None = Field(default=None, description="true - есть доступ к добавлению комментарии, false - нет доступа")
    client_comments_own_edit_access: bool | None = Field(default=None, description="true - есть доступ к изменению/удалению своих комментарии, false - нет доступа")
    client_comments_other_edit_access: bool | None = Field(default=None, description="true - есть доступ к изменению/удалению чужих комментарии, false - нет доступа")
    client_files_list_access: bool | None = Field(default=None, description="true - есть доступ к просмотрам и скачиванию файлов, false - нет доступа")
    client_files_upload_access: bool | None = Field(default=None, description="true - есть доступ к загрузке файлов, false - нет доступа")
    client_files_delete_access: bool | None = Field(default=None, description="true - есть доступ к удалению файлов, false - нет доступа")
    clients_visit_master_id: float | None = Field(default=None, description="ID мастера по которому можно посмотреть клиентов посещавшие мастера, 0 - без ограничений")
    get_visit_master_id: float | None = Field(default=None, description="ID мастера по которому можно посмотреть клиентов посещавшие мастера, 0 - без ограничений")


class UserPermissionsResponseDataTypesDataDashboard(BaseModel):
    """Раздел Обзор
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    dashboard_access: bool | None = Field(default=None, description="true - есть доступ к разделу обзор, false - нет доступа")
    dash_access: bool | None = Field(default=None, description="true - есть доступ к разделу сводка, false - нет доступа")
    dash_phones_access: bool | None = Field(default=None, description="true - есть доступ к показу номера телефонов в сводке, false - нет доступа")
    dash_records_access: bool | None = Field(default=None, description="true - есть доступ к просмотру списка записей, false - нет доступа")
    dash_records_last_days_count: float | None = Field(default=None, description="-1 - есть доступ к просмотру списка записей за все время, >= 0 - доступ к просмотру списка записей за указанное количество дней прошлое")
    dash_records_excel_access: bool | None = Field(default=None, description="true - есть доступ к выгрузке списка записей в Excel, false - нет доступа")
    dash_records_phones_access: bool | None = Field(default=None, description="true - есть доступ к показу номера телефонов в записях, false - нет доступа")
    dash_message_access: bool | None = Field(default=None, description="true - есть доступ к просмотру детализаций сообщений, false - нет доступа")
    dash_message_excel_access: bool | None = Field(default=None, description="true - есть доступ к выгрузке детализаций сообщений в Excel, false - нет доступа")
    dash_message_phones_access: bool | None = Field(default=None, description="true - есть доступ к показу номера телефонов в сообщениях, false - нет доступа")
    dash_reviews_access: bool | None = Field(default=None, description="true - есть доступ к просмотру отзывов, false - нет доступа")
    dash_reviews_delete_access: bool | None = Field(default=None, description="true - есть доступ к удалению отзывов, false - нет доступа")
    dashboard_calls_access: bool | None = Field(default=None, description="true - есть доступ к разделу звонки, false - нет доступа")
    dashboard_calls_excel_access: bool | None = Field(default=None, description="true - есть доступ к выгрузке звонков Excel, false - нет доступа")
    dashboard_calls_phones_access: bool | None = Field(default=None, description="true - есть доступ к просмотру номера телефона у клиентов, false - нет доступа")


class UserPermissionsResponseDataTypesDataFinances(BaseModel):
    """Раздел Финансы
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    finances_access: bool | None = Field(default=None, description="true - есть доступ к финансам, false - нет доступа")
    finances_accounts_ids: list[dict[str, Any]] | None = Field(default=None, description="массив ID к выбранным кассам")
    finances_transactions_access: bool | None = Field(default=None, description="true - есть доступ к просмотру движений средств, false - нет доступа")
    finances_last_days_count: float | None = Field(default=None, description="-1 - есть доступ к просмотру движений средств за все время, >= 0 - доступ к просмотру движений средств за указанное количество дней прошлое")
    finances_create_transactions_access: bool | None = Field(default=None, description="true - есть доступ к созданию транзакций, false - нет доступа")
    finances_create_last_days_count: float | None = Field(default=None, description="-1 - есть доступ к созданию транзакций за все время, >= 0 - доступ к созданию транзакций за указанное количество дней прошлое")
    finances_edit_transactions_access: bool | None = Field(default=None, description="true - есть доступ к редактированию транзакций, false - нет доступа")
    finances_edit_last_days_count: float | None = Field(default=None, description="-1 - есть доступ к редактированию транзакций за все время, >= 0 - доступ к редактированию транзакций за указанное количество дней прошлое")
    finances_delete_transactions_access: bool | None = Field(default=None, description="true - есть доступ к удалению транзакций, false - нет доступа")
    finances_transactions_excel_access: bool | None = Field(default=None, description="true - есть доступ к выгрузке движений средств в Excel, false - нет доступа")
    finances_expenses_ids: list[dict[str, Any]] | None = Field(default=None, description="true - есть доступ к переводам между кассами, false - нет доступа")
    finances_accounts_access: bool | None = Field(default=None, description="true - есть доступ к счетам и кассам, false - нет доступа")
    finances_accounts_banalce_access: bool | None = Field(default=None, description="true - есть доступ к балансу, false - нет доступа")
    finances_suppliers_read_access: bool | None = Field(default=None, description="true - есть доступ к контрагентам, false - нет доступа")
    finances_suppliers_create_access: bool | None = Field(default=None, description="true - есть доступ к созданию контрагентов, false - нет доступа")
    finances_suppliers_update_access: bool | None = Field(default=None, description="true - есть доступ к изменению контрагентов, false - нет доступа")
    finances_suppliers_delete_access: bool | None = Field(default=None, description="true - есть доступ к удалению контрагентов, false - нет доступа")
    finances_suppliers_excel_access: bool | None = Field(default=None, description="true - есть доступ к выгрузке в Excel, false - нет доступа")
    finances_expenses_read_access: bool | None = Field(default=None, description="true - есть доступ к статье платежей, false - нет доступа")
    expenses_read_access: bool | None = Field(default=None, description="true - есть доступ к статье платежей, false - нет доступа")
    finances_expenses_create_access: bool | None = Field(default=None, description="true - есть доступ к созданию статьи платежа, false - нет доступа")
    expenses_create_access: bool | None = Field(default=None, description="true - есть доступ к созданию статьи платежа, false - нет доступа")
    finances_expenses_update_access: bool | None = Field(default=None, description="true - есть доступ к изменению статьи платежа, false - нет доступа")
    expenses_update_access: bool | None = Field(default=None, description="true - есть доступ к изменению статьи платежа, false - нет доступа")
    finances_expenses_delete_access: bool | None = Field(default=None, description="true - есть доступ к удалению статьи платежа, false - нет доступа")
    expenses_delete_access: bool | None = Field(default=None, description="true - есть доступ к удалению статьи платежа, false - нет доступа")
    finances_kkm_transactions_access: bool | None = Field(default=None, description="true - есть доступ к операциям с KKM, false - нет доступа")
    kkm_transactions_accounts_access: bool | None = Field(default=None, description="true - есть доступ к операциям с KKM, false - нет доступа")
    finances_kkm_settings_read_access: bool | None = Field(default=None, description="true - есть доступ к настройкам KKM, false - нет доступа")
    kkm_settings_reed_access: bool | None = Field(default=None, description="true - есть доступ к настройкам KKM, false - нет доступа")
    finances_kkm_settings_update_access: bool | None = Field(default=None, description="true - есть доступ к изменению KKM, false - нет доступа")
    kkm_settings_update_access: bool | None = Field(default=None, description="true - есть доступ к изменению KKM, false - нет доступа")
    finances_settings_invoicing_read_access: bool | None = Field(default=None, description="true - есть доступ к онлайн-оплатам, false - нет доступа")
    finances_settings_invoicing_update_access: bool | None = Field(default=None, description="true - есть доступ к изменению онлайн-оплат, false - нет доступа")
    settings_invoicing_read_access: bool | None = Field(default=None, description="true - есть доступ к онлайн-оплатам, false - нет доступа")
    settings_invoicing_update_access: bool | None = Field(default=None, description="true - есть доступ к изменению онлайн-оплат, false - нет доступа")
    finances_options_read_access: bool | None = Field(default=None, description="true - есть доступ к настройкам оплаты, false - нет доступа")
    finances_options_update_access: bool | None = Field(default=None, description="true - есть доступ к изменению настроек оплаты, false - нет доступа")
    options_update_access: bool | None = Field(default=None, description="true - есть доступ к изменению настроек оплаты, false - нет доступа")
    finances_salary_schemes_access: bool | None = Field(default=None, description="true - есть доступ к схемам расчета заработной платы, false - нет доступа")
    finances_salary_calc_access: bool | None = Field(default=None, description="true - есть доступ к расчету заработной платы, false - нет доступа")
    finances_salary_not_limitation_today_access: bool | None = Field(default=None, description="true - есть доступ к расчету заработной платы, false - доступ к расчету заработной платы за текущий день")
    finances_payroll_calculation_create_access: bool | None = Field(default=None, description="true - есть доступ к начислению заработной платы, false - нет доступа")
    finances_payroll_calculation_create_not_limitation_today_access: bool | None = Field(default=None, description="true - есть доступ к начислению заработной платы, false - доступ к начислению заработной платы за текущий день")
    finances_salary_access_master_checkbox: bool | None = Field(default=None, description="true - есть доступ к расчету заработной платы только конкретного сотрудника, false - полный доступ")
    finances_salary_access_master_id: float | None = Field(default=None, description="ID сотрудника к которому есть доступ на расчет заработной платы")
    get_salary_access_master_id: float | None = Field(default=None, description="ID сотрудника к которому есть доступ на расчет заработной платы")
    finances_salary_master_not_limitation_today_access: bool | None = Field(default=None, description="true - не ограничивать текущим днем, false - доступ только на сегодняшний день")
    finances_payroll_calculation_create_by_master_access: bool | None = Field(default=None, description="true - есть доступ к начислению заработной платы по конкретному сотруднику, false - без ограничений")
    calculation_create_by_master_not_limitation_today_access: bool | None = Field(default=None, description="true - есть доступ к начислению заработной платы, false - нет доступа")
    finances_period_report_access: bool | None = Field(default=None, description="true - есть доступ к отчету за период, false - нет доступа")
    finances_period_report_excel_access: bool | None = Field(default=None, description="true - есть доступ к выгрузке в Excel отчета за период, false - нет доступа")
    finances_year_report_access: bool | None = Field(default=None, description="true - есть доступ к годовому отчету, false - нет доступа")
    finances_year_report_excel_access: bool | None = Field(default=None, description="true - есть доступ к выгрузке в Excel годового отчета, false - нет доступа")
    finances_print_check_access: bool | None = Field(default=None, description="true - есть доступ к печати чека, false - нет доступа")
    finances_z_report_access: bool | None = Field(default=None, description="true - есть доступ к отчету по кассе за день, false - нет доступа")
    finances_z_report_no_limit_today_access: bool | None = Field(default=None, description="true - есть доступ к отчету по кассе, false - доступ к отчету по кассе за текущий день")
    finances_z_report_excel_access: bool | None = Field(default=None, description="true - есть доступ к выгрузке в Excel, false - нет доступа")


class UserPermissionsResponseDataTypesDataLoyalty(BaseModel):
    """Раздел Лояльность
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    loyalty_access: bool | None = Field(default=None, description="true - есть доступ к лояльности, false - нет доступа")
    has_loyalty_access: bool | None = Field(default=None, description="true - есть доступ к лояльности, false - нет доступа")
    loyalty_cards_manual_transactions_access: bool | None = Field(default=None, description="true - есть доступ к ручному пополнению/списанию с карт лояльности, false - нет доступа")
    has_loyalty_cards_manual_transactions_access: bool | None = Field(default=None, description="true - есть доступ к ручному пополнению/списанию с карт лояльности, false - нет доступа")
    loyalty_certificate_and_abonement_manual_transactions_access: bool | None = Field(default=None, description="true - есть доступ к оплате сертификатом и абонементом без кода, false - нет доступа")


class UserPermissionsResponseDataTypesDataNotification(BaseModel):
    """Настройки уведомлений
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    notification: bool | None = Field(default=None, description="true - есть доступ к Уведомления, false - нет доступа")
    web_push: bool | None = Field(default=None, description="true - есть доступ к показу Push уведомлений о записях в Web-версии, false - нет доступа")
    web_phone_push: bool | None = Field(default=None, description="true - есть доступ к показу Push уведомлений о звонках в Web-версии, false - нет доступа")
    notification_sms_ending_license: bool | None = Field(default=None, description="true - есть доступ к отправки SMS уведомлений о скором окончании лицензии, false - нет доступа")
    notification_sms_low_balance: bool | None = Field(default=None, description="true - есть доступ к отправки SMS уведомлений о низком балансе, false - нет доступа")
    notification_email_ending_license: bool | None = Field(default=None, description="true - есть доступ к отправки Email уведомлений о скором окончании лицензии, false - нет доступа")


class UserPermissionsResponseDataTypesDataOther(BaseModel):
    """Доступ к аналитике, биллингу, SMS-рассылкам и включение доступа в филиал по IP-адресу
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    stat_access: bool | None = Field(default=None, description="true - есть доступ к аналитике, false - нет доступа")
    billing_access: bool | None = Field(default=None, description="true - есть доступ к биллингу (раздел меню баланс), false - нет доступа")
    send_sms: bool | None = Field(default=None, description="true - есть доступ к SMS рассылки клиентам, false - нет доступа")
    auth_enable_check_ip: bool | None = Field(default=None, description="true - есть доступ к филиалу только с IP-адресов (v4, v6), false - нет доступа")
    auth_list_allowed_ip: list[dict[str, Any]] | None = Field(default=None, description="список IP адресов")


class UserPermissionsResponseDataTypesDataRecordForm(BaseModel):
    """Окно записи
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    record_form_access: bool | None = Field(default=None, description="true - есть доступ к окну записи, false - нет доступа")
    record_form_client_access: bool | None = Field(default=None, description="true - есть доступ к данным клиентов, false - нет доступа")
    records_autocomplete_access: bool | None = Field(default=None, description="true - есть доступ к выпадающему списку с данными о клиентах, false - нет доступа")
    create_records_access: bool | None = Field(default=None, description="true - есть доступ к созданию записей, false - нет доступа Создавать записи")
    edit_records_access: bool | None = Field(default=None, description="true - есть доступ к изменение записей, false - нет доступа")
    edit_records_attendance_access: bool | None = Field(default=None, description="true - есть доступ к записям со статусом визита \"клиент пришел\", false - нет доступа")
    records_services_cost_access: bool | None = Field(default=None, description="true - есть доступ к изменению стоимости услуг, false - нет доступа")
    records_services_discount_access: bool | None = Field(default=None, description="true - есть доступ к изменению скидки на услуги, false - нет доступа")
    record_edit_full_paid_access: bool | None = Field(default=None, description="true - есть доступ к редактированию оплаченной записи, false - нет доступа")
    delete_records_access: bool | None = Field(default=None, description="true - есть доступ к удалению записи, false - нет доступа")
    delete_customer_came_records_access: bool | None = Field(default=None, description="true - есть доступ к удалению записей со статусом \"клиент пришел\", false - нет доступа")
    delete_paid_records_access: bool | None = Field(default=None, description="true - есть доступ к удалению оплаченных записей, false - нет доступа")
    records_goods_access: bool | None = Field(default=None, description="true - есть доступ к продажам товаров, false - нет доступа")
    records_goods_create_transaction_access: bool | None = Field(default=None, description="true - есть доступ к созданию товарных транзакций, false - нет доступа")
    records_goods_create_last_days_count: float | None = Field(default=None, description="-1 - есть доступ к созданию товарных транзакций за все время, >= 0 - доступ к созданию товарных транзакций за указанное количество дней прошлое")
    records_goods_edit_transaction_access: bool | None = Field(default=None, description="true - есть доступ к редактированию товарных транзакций, false - нет доступа")
    records_goods_edit_last_days_count: float | None = Field(default=None, description="-1 - есть доступ к редактированию товарных транзакций за все время, >= 0 - доступ к редактированию товарных транзакций за указанное количество дней прошлое''")
    records_goods_cost_access: bool | None = Field(default=None, description="true - есть доступ к изменению стоимость товаров, false - нет доступа")
    records_goods_discount_access: bool | None = Field(default=None, description="true - есть доступ к изменению скидки на товары, false - нет доступа")
    records_finances_access: bool | None = Field(default=None, description="true - есть доступ к оплате, false - нет доступа")
    records_finances_last_days_count: float | None = Field(default=None, description="-1 - есть доступ к проведению оплаты в записях за все время, >= 0 - доступ к проведению оплаты в записях за указанное количество дней прошлое")
    records_finances_pay_from_deposits_access: bool | None = Field(default=None, description="true - есть доступ к проведению оплаты в записях с личного счета клиента, false - нет доступа")
    records_group_id_access: bool | None = Field(default=None, description="true - есть доступ к данным клиентов по сети, false - нет доступа")
    records_group_id: float | None = Field(default=None, description="ID сети к которой есть доступ к данным клиентов")


class UserPermissionsResponseDataTypesDataSettings(BaseModel):
    """Раздел Настройки
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    settings_access: bool | None = Field(default=None, description="true - есть доступ к разделу настройки, false - нет доступа")
    settings_basis_access: bool | None = Field(default=None, description="true - есть доступ к разделу Основные, false - нет доступа")
    settings_information_access: bool | None = Field(default=None, description="true - есть доступ к разделу Информация, false - нет доступа")
    users_access: bool | None = Field(default=None, description="true - есть доступ к управлению пользователями, false - нет доступа")
    delete_users_access: bool | None = Field(default=None, description="true - есть доступ к удалению пользователей, false - нет доступа")
    create_users_access: bool | None = Field(default=None, description="true - есть доступ к добавлению пользователей, false - нет доступа")
    edit_users_access: bool | None = Field(default=None, description="true - есть доступ к управлению правами пользователей, false - нет доступа")
    limited_users_access: bool | None = Field(default=None, description="true - есть доступ к управлению правами в рамках своего набора прав, false - нет доступа")
    settings_services_access: bool | None = Field(default=None, description="true - есть доступ к разделу Услуги, false - нет доступа")
    settings_services_create_access: bool | None = Field(default=None, description="true - есть доступ к созданию услуг, false - нет доступа")
    services_edit: bool | None = Field(default=None, description="true - есть доступ к редактированию услуг, false - нет доступа")
    settings_services_edit_title_access: bool | None = Field(default=None, description="true - есть доступ к названиям услуг и название для онлайн-записи, false - нет доступа")
    settings_services_relation_category_access: bool | None = Field(default=None, description="true - есть доступ к категориям услуги, false - нет доступа")
    settings_services_edit_price_access: bool | None = Field(default=None, description="true - есть доступ к ценам услуг, false - нет доступа")
    settings_services_edit_image_access: bool | None = Field(default=None, description="true - есть доступ к загрузкам и изменениям изображений, false - нет доступа")
    settings_services_edit_online_seance_date_time_access: bool | None = Field(default=None, description="true - есть доступ к отображениям услуг в виджете, false - нет доступа")
    settings_services_edit_online_pay_access: bool | None = Field(default=None, description="true - есть доступ к онлайн-оплате услуги, false - нет доступа")
    settings_services_edit_services_related_resource_access: bool | None = Field(default=None, description="true - есть доступ к ресурсам услуги, false - нет доступа")
    settings_positions_read: bool | None = Field(default=None, description="true - есть доступ к разделу должности, false - нет доступа")
    settings_positions_create: bool | None = Field(default=None, description="true - есть доступ к созданию должностей, false - нет доступа")
    settings_positions_delete: bool | None = Field(default=None, description="true - есть доступ к удалению должностей, false - нет доступа")
    edit_master_service_and_duration: bool | None = Field(default=None, description="true - есть доступ к изменению услуги сотрудников и их длительность, false - нет доступа")
    tech_card_edit: bool | None = Field(default=None, description="true - есть доступ к изменению технологической карты, false - нет доступа")
    services_delete: bool | None = Field(default=None, description="true - есть доступ к удалению услуг, false - нет доступа")
    settings_master_access: bool | None = Field(default=None, description="true - есть доступ к разделу Сотрудники, false - нет доступа")
    master_create: bool | None = Field(default=None, description="true - есть доступ к созданию сотрудников, false - нет доступа")
    master_edit: bool | None = Field(default=None, description="true - есть доступ к редактированию сотрудников, false - нет доступа")
    master_delete: bool | None = Field(default=None, description="true - есть доступ к удалению сотрудников, false - нет доступа")
    settings_master_dismiss_access: bool | None = Field(default=None, description="true - есть доступ к увольнению сотрудников, false - нет доступа")
    schedule_edit: bool | None = Field(default=None, description="true - есть доступ к редактированию графика работы, false - нет доступа")
    settings_notifications_access: bool | None = Field(default=None, description="true - есть доступ к разделу Sms уведомления, false - нет доступа")
    settings_email_notifications_access: bool | None = Field(default=None, description="true - есть доступ к разделу Email уведомления, false - нет доступа")
    settings_template_notifications_access: bool | None = Field(default=None, description="true - есть доступ к разделу Типы уведомлений, false - нет доступа")
    webhook_read_access: bool | None = Field(default=None, description="true - есть доступ к изменению настроек WebHook, false - нет доступа")


class UserPermissionsResponseDataTypesDataStorages(BaseModel):
    """Раздел Склад
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    storages_access: bool | None = Field(default=None, description="true - есть доступ к складу, false - нет доступа")
    storages_ids: list[dict[str, Any]] | None = Field(default=None, description="true - есть доступ к выбранным складам, false - нет доступа")
    storages_transactions_access: bool | None = Field(default=None, description="true - есть доступ к просмотру движений товаров, false - нет доступа")
    storages_last_days_count: float | None = Field(default=None, description="-1 - есть доступ к просмотру движений товаров за все время, >= 0 - доступ к просмотру движений товаров за указанное количество дней прошлое")
    storages_move_goods_access: bool | None = Field(default=None, description="true - есть доступ к перемещение товаров между складами, false - нет доступа")
    storages_create_transactions_access: bool | None = Field(default=None, description="true - есть доступ к созданию товарных транзакций, false - нет доступа")
    storages_create_last_days_count: float | None = Field(default=None, description="-1 - есть доступ к создание товарных транзакций за все время, >= 0 - доступ к создание товарных транзакций за указанное количество дней прошлое")
    storages_create_transactions_buy_access: bool | None = Field(default=None, description="true - есть доступ к оформлению прихода товаров, false - нет доступа")
    storages_create_transactions_sale_access: bool | None = Field(default=None, description="true - есть доступ к оформлению продаж товаров, false - нет доступа")
    storages_edit_transactions_access: bool | None = Field(default=None, description="true - есть доступ к редактированию товарных транзакций, false - нет доступа")
    storages_edit_last_days_count: float | None = Field(default=None, description="-1 - есть доступ к редактированию товарных транзакций за все время, >= 0 - доступ к редактированию товарных транзакций за указанное количество дней прошлое")
    storages_edit_transactions_buy_access: bool | None = Field(default=None, description="true - есть доступ к оформлению прихода товаров, false - нет доступа")
    storages_edit_transactions_sale_access: bool | None = Field(default=None, description="true - есть доступ к оформлению продаж товаров, false - нет доступа")
    storages_delete_transactions_access: bool | None = Field(default=None, description="true - есть доступ к удалению товарных транзакций, false - нет доступа")
    storages_transactions_excel_access: bool | None = Field(default=None, description="true - есть доступ к выгрузке движений товаров в Excel, false - нет доступа")
    storages_transactions_types: list[dict[str, Any]] | None = Field(default=None, description="true - есть доступ к выгрузке движений товаров в Excel, false - нет доступа")
    storages_inventory_access: bool | None = Field(default=None, description="true - есть доступ к инвентаризации, false - нет доступа")
    storages_inventory_create_edit_access: bool | None = Field(default=None, description="true - есть доступ к созданию и редактированию инвентаризации, false - нет доступа")
    storages_inventory_delete_access: bool | None = Field(default=None, description="true - есть доступ к удалению инвентаризации, false - нет доступа")
    storages_inventory_excel_access: bool | None = Field(default=None, description="true - есть доступ к выгрузке инвентаризации в Excel, false - нет доступа")
    storages_remnants_report_access: bool | None = Field(default=None, description="true - есть доступ к отчету остатков на складе, false - нет доступа")
    storages_remnants_report_excel_access: bool | None = Field(default=None, description="true - есть доступ к выгрузке остатков в Excel, false - нет доступа")
    storages_sales_report_access: bool | None = Field(default=None, description="true - есть доступ к отчету по продажам, false - нет доступа")
    storages_sales_report_excel_access: bool | None = Field(default=None, description="true - есть доступ к выгрузке отчета по продажам в Excel, false - нет доступа")
    storages_consumable_report_access: bool | None = Field(default=None, description="true - есть доступ к отчету по списанию расходников, false - нет доступа")
    storages_consumable_report_excel_access: bool | None = Field(default=None, description="true - есть доступ к выгрузке отчета по списанию расходников в Excel, false - нет доступа")
    storages_write_off_report_access: bool | None = Field(default=None, description="true - есть доступ к отчету по списанию товаров, false - нет доступа")
    storages_write_off_report_excel_access: bool | None = Field(default=None, description="true - есть доступ к выгрузке отчета по списанию товаров в Excel, false - нет доступа")
    storages_turnover_report_access: bool | None = Field(default=None, description="true - есть доступ к отчету по оборачиваемости, false - нет доступа")
    storages_turnover_report_excel_access: bool | None = Field(default=None, description="true - есть доступ к выгрузке отчета по оборачиваемости в Excel, false - нет доступа")
    storages_goods_crud_access: bool | None = Field(default=None, description="true - есть доступ к управлению товарами, false - нет доступа")
    storages_goods_create_access: bool | None = Field(default=None, description="true - есть доступ к созданию товаров, false - нет доступа")
    storages_goods_update_access: bool | None = Field(default=None, description="true - есть доступ к изменению товаров, false - нет доступа")
    storages_goods_title_edit_access: bool | None = Field(default=None, description="true - есть доступ к названию, Артикул, Штрих-код, false - нет доступа")
    storages_goods_category_edit_access: bool | None = Field(default=None, description="true - есть доступ к категориям, false - нет доступа")
    storages_goods_selling_price_edit_access: bool | None = Field(default=None, description="true - есть доступ к ценам продажи, false - нет доступа")
    storages_goods_cost_price_edit_access: bool | None = Field(default=None, description="true - есть доступ к себестоимости, false - нет доступа")
    storages_goods_units_edit_access: bool | None = Field(default=None, description="true - есть доступ к единицам измерения, false - нет доступа")
    storages_goods_critical_balance_edit_access: bool | None = Field(default=None, description="true - есть доступ к критичным остаткам, Желаемый остаток, false - нет доступа")
    storages_goods_masses_edit_access: bool | None = Field(default=None, description="true - есть доступ к массе, false - нет доступа")
    storages_goods_comment_edit_access: bool | None = Field(default=None, description="true - есть доступ к комментариям, false - нет доступа")
    storages_goods_archive_access: bool | None = Field(default=None, description="true - есть доступ к архивации и восстановлению товаров, false - нет доступа")
    storages_goods_delete_access: bool | None = Field(default=None, description="true - есть доступ к удалению товаров, false - нет доступа")


class UserPermissionsResponseDataTypesDataTimetable(BaseModel):
    """Журнал записи
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    timetable_access: bool | None = Field(default=None, description="true - есть доступ к журналу записи, false - нет доступа")
    master_id: float | None = Field(default=None, description="0 - если пользователь может просматривать расписание и записи всех сотрудников, иначе только того сотрудника, ID которого задан")
    position_id: float | None = Field(default=None, description="0 - если пользователь может просматривать расписание и записи всех сотрудников, иначе только ту должность, ID которого задан")
    last_days_count: float | None = Field(default=None, description="0 - не ограничить доступ к истории расписаний и записям")
    schedule_edit_access: bool | None = Field(default=None, description="true - есть доступ к графику работы сотрудника в журнале, false - нет доступа")
    timetable_phones_access: bool | None = Field(default=None, description="true - есть доступ к номеру телефона в журнале записи, false - нет доступа")
    timetable_transferring_record_access: bool | None = Field(default=None, description="true - есть доступ к переносу записей, false - нет доступа")
    timetable_statistics_access: bool | None = Field(default=None, description="true - есть доступ к просмотру статистики, false - нет доступа")


class UserRecordsResponseDataTypesDataItemCompany(BaseModel):
    """Параметры компании
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="ID копаниии")
    title: str | None = Field(default=None, description="Название компании")
    country_id: float | None = Field(default=None, description="ID страны")
    country: str | None = Field(default=None, description="Название страны, в которой расположены организация")
    city_id: float | None = Field(default=None, description="ID города")
    city: str | None = Field(default=None, description="Название города, в котором расположена организация")
    phone: str | None = Field(default=None, description="Телефон компании")
    phones: list[str] | None = Field(default=None)
    timezone: str | None = Field(default=None, description="Временная зона компании")
    address: str | None = Field(default=None, description="Адрес компании")
    coordinate_lat: float | None = Field(default=None, description="Широта")
    coordinate_lon: float | None = Field(default=None, description="Долгота")
    allow_delete_record: bool | None = Field(default=None)
    allow_change_record: bool | None = Field(default=None)
    site: str | None = Field(default=None)
    currency_short_title: str | None = Field(default=None)
    allow_change_record_delay_step: int | None = Field(default=None)
    allow_delete_record_delay_step: int | None = Field(default=None)


class UserRecordsResponseDataTypesDataItemServicesItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор услуги")
    title: str | None = Field(default=None, description="Название услуги")
    amount: int | None = Field(default=None, description="Количество заказанных услуг")
    seance_length: int | None = Field(default=None, description="Длительность оказания услуги в секундах (только если задан фильтр по сотруднику)")


class UserRecordsResponseDataTypesDataItemStaffPosition(BaseModel):
    """Должность сотрудника
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="ID должности")
    title: str | None = Field(default=None, description="Название должности")


class UserInviteResponseDataTypes(BaseModel):
    """Создание и отправка приглашения
    Схема спеки: Root Type for user_invite_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешной отправка (true)")
    data_: str | None = Field(default=None, alias="data", description="Имеет значение null")
    meta: UserInviteResponseDataTypesMeta | None = Field(default=None)


class UserNameAvatar(BaseModel):
    """Данные по существующему пользователю.
    Схема спеки: Объект модели "Пользователь с именем и аватаром"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="Идентификатор пользователя.")
    name: str | None = Field(default=None, description="Имя пользователя.")
    avatar: str | None = Field(default=None, description="Аватар пользователя.")


class UserRolePermissions(BaseModel):
    """Данные по правам и роли пользователя
    Схема спеки: Объект модели "Права и роль пользователя"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    user_role: Literal["worker", "administrator", "accountant", "manager", "owner"] | None = Field(default=None, description="Название роли")
    staff_id: float | None = Field(default=None, description="Идентификатор сотрудника привязанного к пользователю")
    is_editable: bool | None = Field(default=None, description="Доступны ли права и роль для редактирования")
    user_permissions: list[Any] | None = Field(default=None, description="Список значений прав пользователя")


class UserRoleWithSalonAndUser(BaseModel):
    """Данные по роли пользователя
    Схема спеки: Объект модели "Роль пользователя"
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    slug: Literal["worker", "administrator", "accountant", "manager", "owner"] | None = Field(default=None, description="Название роли")
    title: str | None = Field(default=None, description="Заголовок роли")
    description: str | None = Field(default=None, description="Описание роли")
    weight: float | None = Field(default=None, description="Вес роли, определяющий количество доступных прав")
    user_permissions: list[Any] | None = Field(default=None, description="Список прав этой роли Возвращается в ответе, если в запросе указан параметр `include` с соответствующим значением.")


class UserPermissionsResponseDataTypesData(BaseModel):
    """Объект с категориями прав доступа
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    timetable: UserPermissionsResponseDataTypesDataTimetable | None = Field(default=None)
    record_form: UserPermissionsResponseDataTypesDataRecordForm | None = Field(default=None)
    finances: UserPermissionsResponseDataTypesDataFinances | None = Field(default=None)
    clients: UserPermissionsResponseDataTypesDataClients | None = Field(default=None)
    dashboard: UserPermissionsResponseDataTypesDataDashboard | None = Field(default=None)
    notification: UserPermissionsResponseDataTypesDataNotification | None = Field(default=None)
    loyalty: UserPermissionsResponseDataTypesDataLoyalty | None = Field(default=None)
    storages: UserPermissionsResponseDataTypesDataStorages | None = Field(default=None)
    settings: UserPermissionsResponseDataTypesDataSettings | None = Field(default=None)
    other: UserPermissionsResponseDataTypesDataOther | None = Field(default=None)


class UserRecordsResponseDataTypesDataItemStaff(BaseModel):
    """Параметры сотрудника
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="ID сотрудника")
    name: str | None = Field(default=None, description="Имя сотрудника")
    specialization: str | None = Field(default=None, description="Специализация сотрудника")
    position: UserRecordsResponseDataTypesDataItemStaffPosition | None = Field(default=None)
    show_rating: bool | None = Field(default=None, description="Показывать ли рейтинг сотрудника")
    rating: float | None = Field(default=None, description="Рейтинг сотрудника (от 0 до 5)")
    votes_count: float | None = Field(default=None, description="Кол-во голосов, поставивших сотруднику оценку")
    avatar: str | None = Field(default=None, description="Путь к аватарке сотрудника")
    comments_count: float | None = Field(default=None, description="Кол-во комментариев сотруднику")


class UserPermissionsResponseDataTypes(BaseModel):
    """Получить список прав
    Схема спеки: Root Type for user_permissions_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: UserPermissionsResponseDataTypesData | None = Field(default=None, alias="data")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")


class UserRecordsResponseDataTypesDataItem(BaseModel):

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id_: float | None = Field(default=None, alias="id", description="ID записи")
    services: list[UserRecordsResponseDataTypesDataItemServicesItem] | None = Field(default=None, description="Список ID услуг")
    company: UserRecordsResponseDataTypesDataItemCompany | None = Field(default=None)
    staff: UserRecordsResponseDataTypesDataItemStaff | None = Field(default=None)
    clients_count: int | None = Field(default=None)
    date: str | None = Field(default=None, description="\"2025-01-01 12:00:00\" (required, string) - Дата сеанса")
    datetime: str | None = Field(default=None, description="Дата сеанса в ISO")
    create_date: str | None = Field(default=None, description="\"2025-01-01 12:00:00\" (required, string) - Дата создания записи")
    comment: str | None = Field(default=None, description="Комментарий к записи")
    deleted: bool | None = Field(default=None, description="Удалена ли запись (true если удалена)")
    attendance: float | None = Field(default=None, description="2 - Пользователь подтвердил запись, 1 - Пользователь пришел, услуги оказаны, 0 - ожидание пользователя, -1 - пользователь не пришел на визит")
    length: float | None = Field(default=None, description="Длительность сеанса")
    notify_by_sms: float | None = Field(default=None, description="За какое кол-во часов отправить смс напоминание о записи (0 если не нужно напоминать)")
    notify_by_email: float | None = Field(default=None, description="За какое кол-во часов отправить email напоминание о записи (0 если не нужно напоминать)")
    master_requested: bool | None = Field(default=None, description="Был ли указан определенный специалист при записи (false если был указан \"не имеет значения\")")
    online: bool | None = Field(default=None, description="Запись онлайновая или нет (false если запись внес администратор)")
    api_id: str | None = Field(default=None, description="Внешний идентификатор записи")
    last_change_date: str | None = Field(default=None, description="Дата последнего редактирования записи")
    prepaid: bool | None = Field(default=None, description="Доступна ли онлайн-оплата для записи")
    prepaid_confirmed: bool | None = Field(default=None, description="Статус online-оплаты")
    activity_id: float | None = Field(default=None, description="ID групповой записи")


class UserRecordsResponseDataTypes(BaseModel):
    """Получить записи пользователя
    Схема спеки: Root Type for user_records_response_data_types
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    success: bool | None = Field(default=None, description="Статус успешности выполнения (true)")
    data_: list[UserRecordsResponseDataTypesDataItem] | None = Field(default=None, alias="data", description="Массив объектов")
    meta: list[dict[str, Any]] | None = Field(default=None, description="Метаданные (пустой массив)")

__all__ = [
    "UserInviteResponseDataTypes",
    "UserInviteResponseDataTypesMeta",
    "UserNameAvatar",
    "UserPermissionsResponseDataTypes",
    "UserPermissionsResponseDataTypesData",
    "UserPermissionsResponseDataTypesDataClients",
    "UserPermissionsResponseDataTypesDataDashboard",
    "UserPermissionsResponseDataTypesDataFinances",
    "UserPermissionsResponseDataTypesDataLoyalty",
    "UserPermissionsResponseDataTypesDataNotification",
    "UserPermissionsResponseDataTypesDataOther",
    "UserPermissionsResponseDataTypesDataRecordForm",
    "UserPermissionsResponseDataTypesDataSettings",
    "UserPermissionsResponseDataTypesDataStorages",
    "UserPermissionsResponseDataTypesDataTimetable",
    "UserRecordsResponseDataTypes",
    "UserRecordsResponseDataTypesDataItem",
    "UserRecordsResponseDataTypesDataItemCompany",
    "UserRecordsResponseDataTypesDataItemServicesItem",
    "UserRecordsResponseDataTypesDataItemStaff",
    "UserRecordsResponseDataTypesDataItemStaffPosition",
    "UserRolePermissions",
    "UserRoleWithSalonAndUser"
]
