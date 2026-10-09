"""Генератор кода клиента YCLIENTS из OpenAPI-спеки.

Использование:
    python scripts/generate.py

Читает docs/openapi.json и перегенерирует:
    src/yclients/models/schemas/    -- pydantic-модели компонент спеки (пакет)
    src/yclients/resources/*.py     -- ресурсные классы по доменам
    src/yclients/client.py          -- фасад YclientsClient
"""

from __future__ import annotations

import json
import re
import shutil
import sys
from collections import defaultdict, deque
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPEC_PATH = ROOT / "docs" / "openapi.json"
SRC = ROOT / "src" / "yclients"

HTTP_METHODS = ("get", "post", "put", "patch", "delete")
PREFIXES = ("api/v1", "api/v2", "marketplace")

# Пути-артефакты документации (не вызываемые эндпоинты)
SKIP_PATHS = {"/api/v1/https://your-api.url"}

# --------------------------------------------------------------- домены (теги)

# Русский тег из спеки -> (модуль, класс, "свои" существительные пути)
TAG_MAP: dict[str, tuple[str, str, frozenset[str]]] = {
    "Авторизация": ("auth", "AuthApi", frozenset({"auth"})),
    "Онлайн-запись": ("booking", "BookingApi", frozenset({"book", "booking"})),
    "Записи пользователя": ("user_records", "UserRecordsApi", frozenset({"records", "record"})),
    "Пользователи онлайн-записи": ("booking_users", "BookingUsersApi", frozenset({"booking", "user"})),
    "Компании": ("companies", "CompaniesApi", frozenset({"companies", "company"})),
    "Категория услуг": ("service_categories", "ServiceCategoriesApi", frozenset({"service_categories", "service_category"})),
    "Услуги": ("services", "ServicesApi", frozenset({"services", "service"})),
    "Пользователи": ("users", "UsersApi", frozenset({"users", "user"})),
    "Пользователь": ("user", "UserApi", frozenset({"user"})),
    "Сотрудники": ("staff", "StaffApi", frozenset({"staff"})),
    "Должности": ("positions", "PositionsApi", frozenset({"positions", "position"})),
    "Клиенты": ("clients", "ClientsApi", frozenset({"clients", "client"})),
    "Сетевые клиенты": ("chain_clients", "ChainClientsApi", frozenset({"clients", "client"})),
    "Записи": ("records", "RecordsApi", frozenset({"records", "record"})),
    "Визиты": ("visits", "VisitsApi", frozenset({"visits", "visit", "attendance"})),
    "Групповые события": ("activities", "ActivitiesApi", frozenset({"activity", "activities"})),
    "Групповые события v2": ("activities_v2", "ActivitiesV2Api", frozenset({"activities", "activity"})),
    "Расписания записей/событий": ("schedules", "SchedulesApi", frozenset({"schedules", "schedule"})),
    "Лист ожидания": ("waiting_list", "WaitingListApi", frozenset({"waiting_list"})),
    "График работы сотрудника": ("staff_schedule", "StaffScheduleApi", frozenset({"schedule"})),
    "Даты для журнала": ("timetable_dates", "TimetableDatesApi", frozenset({"dates"})),
    "Сеансы для журнала": ("timetable_seances", "TimetableSeancesApi", frozenset({"seances"})),
    "Комментарии": ("comments", "CommentsApi", frozenset({"comments", "comment"})),
    "Пользователи компании": ("company_users", "CompanyUsersApi", frozenset({"users", "user"})),
    "Кассы": ("accounts", "AccountsApi", frozenset({"accounts"})),
    "Склады": ("storages", "StoragesApi", frozenset({"storages", "storage"})),
    "SMS рассылка": ("sms", "SmsApi", frozenset({"sms"})),
    "Email рассылка": ("email", "EmailApi", frozenset({"email"})),
    "ККМ транзакции": ("kkm_transactions", "KkmTransactionsApi", frozenset({"kkm_transactions"})),
    "Операция продажи": ("sales", "SalesApi", frozenset({"sale"})),
    "Финансовые транзакции": ("finance_transactions", "FinanceTransactionsApi", frozenset({"finance_transactions", "transactions", "transaction"})),
    "Интеграция с сетевой телефонией": ("voip", "VoipApi", frozenset({"voip"})),
    "Лояльность": ("loyalty", "LoyaltyApi", frozenset({"loyalty"})),
    "Карты лояльности": ("loyalty_cards", "LoyaltyCardsApi", frozenset({"cards", "card", "card_types"})),
    "Сертификаты": ("certificates", "CertificatesApi", frozenset({"certificates", "certificate"})),
    "Абонементы": ("abonements", "AbonementsApi", frozenset({"abonements", "abonement"})),
    "Типы абонементов": ("abonement_types", "AbonementTypesApi", frozenset({"abonement_types"})),
    "Применение лояльности в визите": ("visit_loyalty", "VisitLoyaltyApi", frozenset({"loyalty"})),
    "Справочники": ("references", "ReferencesApi", frozenset({"references"})),
    "Категории": ("labels", "LabelsApi", frozenset({"labels", "label"})),
    "Товары": ("goods", "GoodsApi", frozenset({"goods", "good"})),
    "Категории товаров": ("goods_categories", "GoodsCategoriesApi", frozenset({"goods_categories", "category_node"})),
    "Технологические карты и расходники": ("technological_cards", "TechnologicalCardsApi", frozenset({"technological_cards"})),
    "Товарные транзакции": ("goods_transactions", "GoodsTransactionsApi", frozenset({"goods_transactions", "transactions"})),
    "Складские операции": ("storage_operations", "StorageOperationsApi", frozenset({"storage_operations"})),
    "Документы складских операций": ("storage_documents", "StorageDocumentsApi", frozenset({"documents"})),
    "Личные счета": ("deposits", "DepositsApi", frozenset({"deposits", "deposit"})),
    "Страны": ("countries", "CountriesApi", frozenset({"countries", "country"})),
    "Города": ("cities", "CitiesApi", frozenset({"cities"})),
    "Изображения": ("images", "ImagesApi", frozenset({"images"})),
    "Сети салонов": ("chains", "ChainsApi", frozenset({"groups", "group"})),
    "Аналитика": ("analytics", "AnalyticsApi", frozenset({"analytics"})),
    "Z-Отчет": ("reports", "ReportsApi", frozenset({"reports", "report"})),
    "Дополнительные поля": ("custom_fields", "CustomFieldsApi", frozenset({"custom_fields"})),
    "Отправка СМС через операторов": ("sms_delivery", "SmsDeliveryApi", frozenset({"delivery"})),
    "Лицензии": ("licenses", "LicensesApi", frozenset({"license"})),
    "Правила обработки персональных данных": ("privacy_policy", "PrivacyPolicyApi", frozenset({"privacy_policy"})),
    "Валидация данных": ("validation", "ValidationApi", frozenset({"validation"})),
    "Фискализация чеков": ("fiscalization", "FiscalizationApi", frozenset({"kkm"})),
    "Отзывы и чаевые": ("reviews", "ReviewsApi", frozenset({"master_record_review"})),
    "Чаевые": ("tips", "TipsApi", frozenset({"tips"})),
    "Ресурсы": ("resources", "ResourcesApi", frozenset({"resources"})),
    "Расчёт зарплат": ("payroll", "PayrollApi", frozenset({"salary"})),
    "Уведомления": ("notifications", "NotificationsApi", frozenset({"notification_settings"})),
    "Настройки онлайн-записи": ("online_settings", "OnlineSettingsApi", frozenset({"settings"})),
    "Настройки журнала записи": ("timetable_settings", "TimetableSettingsApi", frozenset({"settings"})),
    "Настройки букформы": ("booking_forms", "BookingFormsApi", frozenset({"booking_forms"})),
    "Маркетплейс": ("marketplace", "MarketplaceApi", frozenset({"marketplace"})),
}

# Ручные переопределения имён методов: (method, path) -> имя
METHOD_OVERRIDES: dict[tuple[str, str], str] = {
    # базовые
    ("POST", "/api/v1/"): "send_sms",
    ("POST", "/api/v1/auth"): "login",
    ("POST", "/api/v1/book_code/{company_id}"): "send_code",
    ("GET", "/api/v1/booking/user/phone_confirmation"): "send_phone_confirmation_code",
    ("POST", "/api/v1/company/{company_id}/clients/visits/search"): "search_visits",
    ("GET", "/api/v1/visit/details/{salon_id}/{record_id}/{visit_id}"): "get_details",
    ("POST", "/api/v1/kkm_transactions/{company_id}/print_document_bill"): "print_bill",
    ("GET", "/api/v1/reports/z_report/{company_id}"): "get_z_report",
    ("GET", "/api/v1/loyalty/card_types/client/{company_id}/{phone}"): "get_client_card_types",
    ("GET", "/api/v1/loyalty/card_types/salon/{company_id}"): "get_salon_card_types",
    ("POST", "/api/v1/goods/search/{company_id}"): "search",
    ("GET", "/api/v1/goods/search/{company_id}"): "search",
    ("GET", "/api/v1/goods/category_node/{company_id}/{category_id}"): "get_category_node",
    ("POST", "/api/v1/validation/validate_phone/{phone}"): "validate_phone",
    ("GET", "/api/v1/validation/validate_phone/{phone}"): "validate_phone",
    # применение лояльности в визите
    ("POST", "/api/v1/visit/loyalty/apply_card_withdrawal/{company_id}/{card_id}"): "apply_card_withdrawal",
    ("POST", "/api/v1/visit/loyalty/apply_discount_program/{company_id}/{card_id}/{program_id}"): "apply_discount_program",
    ("POST", "/api/v1/visit/loyalty/apply_referral_program/{company_id}/{group_id}"): "apply_referral_program",
    ("POST", "/api/v1/visit/loyalty/cancel_card_withdrawal/{company_id}/{card_id}"): "cancel_card_withdrawal",
    ("POST", "/api/v1/visit/loyalty/cancel_discount_program/{company_id}/{card_id}/{program_id}"): "cancel_discount_program",
    # онлайн-запись
    ("POST", "/api/v1/book_check/{company_id}"): "check",
    ("GET", "/api/v1/book_staff/{company_id}"): "list_staff",
    ("GET", "/api/v1/book_times/{company_id}/{staff_id}/{date}"): "list_times",
    ("GET", "/api/v1/book_staff_seances/{company_id}/{staff_id}/"): "list_seances",
    ("POST", "/api/v1/booking/auth"): "auth_by_phone",
    ("GET", "/api/v1/booking/user/data"): "get_data",
    # пользователи
    ("GET", "/api/v1/company/{company_id}/users/{user_id}/roles"): "list_user_roles",
    ("GET", "/api/v1/company_users/{company_id}"): "list_deprecated",
    ("GET", "/api/v1/company/{company_id}/users"): "list",
    # категории услуг
    ("GET", "/api/v1/service_category/{company_id}/{id}"): "get",
    ("GET", "/api/v1/company/{company_id}/service_categories/{id}"): "list",
    ("GET", "/api/v1/service_categories/{company_id}/{id}"): "list_deprecated",
    # финансовые транзакции
    ("GET", "/api/v1/finance_transactions/{company_id}/{transaction_id}"): "get",
    # категории (labels)
    ("POST", "/api/v1/labels/{company_id}/clients/create"): "create_for_clients",
    ("POST", "/api/v1/labels/{company_id}"): "create",
    # личные счета
    ("GET", "/api/v1/deposits/chain/{chain_id}"): "list_chain",
    ("GET", "/api/v1/deposits/chain/{chain_id}/deposit_history/{deposit_id}"): "get_history",
    # SMS/Email-рассылки
    ("POST", "/api/v1/sms/clients/by_id/{company_id}"): "list_by_id",
    ("POST", "/api/v1/sms/clients/by_filter/{company_id}"): "list_by_filter",
    ("POST", "/api/v1/email/clients/by_id/{company_id}"): "list_by_id",
    ("POST", "/api/v1/email/clients/by_filter/{company_id}"): "list_by_filter",
    # отправка СМС через операторов
    ("POST", "/api/v1/delivery/status"): "get_delivery_status",
    # лояльность
    ("GET", "/api/v1/company/{company_id}/loyalty/abonement_types/fetch"): "fetch_abonement_types",
    ("GET", "/api/v1/company/{company_id}/loyalty/certificate_types/fetch"): "fetch_certificate_types",
    ("GET", "/api/v1/loyalty/generate_code/{company_id}/{good_Id}"): "generate_code",
    # абонементы и сертификаты
    ("GET", "/api/v1/chain/{chain_id}/loyalty/abonements"): "list",
    ("GET", "/api/v1/user/loyalty/abonements/"): "list_user",
    ("GET", "/api/v1/user/loyalty/certificates/"): "list_user",
    # групповые события
    ("POST", "/api/v1/activity/{company_id}/duplication_strategy/{strategy_id}"): "update_duplication_strategy",
    ("POST", "/api/v1/activity/{company_id}/{activity_id}/duplicate/"): "duplicate",
    # маркетплейс
    ("POST", "/marketplace/salon/{salon_id}/application/{application_id}/uninstall"): "uninstall",
    ("POST", "/marketplace_webhook"): "create_webhook",
    ("POST", "/marketplace/partner/payment/refund/{payment_id}"): "create_refund",
    # категории товаров и товары
    ("GET", "/api/v1/company/{company_id}/goods_categories/{parent_category_id}"): "list_by_company",
    ("GET", "/api/v1/goods_categories/{company_id}/{parent_category_id}"): "list",
    ("GET", "/api/v1/goods/{company_id}/{good_id}"): "list",
    # расчёт зарплат
    ("GET", "/api/v1/company/{company_id}/salary/payroll/staff/{staff_id}/calculation/"): "list_payroll_charges",
    ("GET", "/api/v1/company/{company_id}/salary/payroll/staff/{staff_id}/calculation/{calculation_id}"): "get_payroll_charge",
    ("GET", "/api/v1/company/{company_id}/salary/calculation/staff/{staff_id}/"): "get_settlements",
    ("GET", "/api/v1/company/{company_id}/salary/calculation/staff/daily/{staff_id}/"): "get_daily_settlements",
    ("GET", "/api/v1/company/{company_id}/salary/period/staff/{staff_id}/"): "get_period_payroll",
    ("GET", "/api/v1/company/{company_id}/salary/period/staff/daily/{staff_id}/"): "get_daily_period_payroll",
    ("GET", "/api/v1/company/{company_id}/salary/staff/{staff_id}/calculation/"): "get_own_settlements",
    ("GET", "/api/v1/company/{company_id}/salary/staff/{staff_id}/period/"): "get_own_period_payroll",
    ("GET", "/api/v1/company/{company_id}/salary/staff/{staff_id}/salary_schemes/"): "list_own_salary_schemes",
    ("GET", "/api/v1/company/{company_id}/salary/calculation/staff/{staff_id}/salary_schemes_count/"): "get_salary_schemes_count",
    # отзывы
    ("POST", "/api/v1/master_record_review/{recordToken}"): "submit_review",
    # записи пользователя
    ("GET", "/api/v1/user/records/{record_id}/{record_hash}"): "get",
    # лист ожидания
    ("GET", "/api/v2/companies/{company_id}/waiting_list"): "list",
    # технологические карты
    ("GET", "/api/v1/technological_cards/default_for_staff_and_service/{company_id}/{staffId}/{serviceId}/"): "get_staff_service_card",
    ("GET", "/api/v1/technological_cards/record_consumables/{company_id}/{record_id}/"): "list_record_consumables",
    ("PUT", "/api/v1/technological_cards/record_consumables/consumables/{company_id}/{record_id}/{service_id}/"): "update_record_consumables",
    ("DELETE", "/api/v1/technological_cards/record_consumables/technological_cards/{company_id}/{record_id}/{service_id}"): "delete_record_technological_card",
    # визиты
    ("GET", "/api/v1/attendance/receipt_print/{visit_id}"): "get_receipt_pdf",
    # клиенты
    ("DELETE", "/api/v1/client/{company_id}/{id}"): "delete",
    ("DELETE", "/api/v1/company/{company_id}/clients/files/{client_id}/{file_id}"): "delete_file",
}

# "Действия" -- литеральные сегменты, которые сами по себе являются глаголами
GET_ACTIONS = frozenset({
    "search", "filters", "data", "settings", "schedule", "phone_confirmation",
    "notification_types", "references", "statistics", "links", "duplication_strategy",
})
POST_ACTIONS = frozenset({
    "search", "auth", "book", "login", "logout", "validate", "print", "freeze",
    "unfreeze", "clone", "fetch", "callback", "redirect", "bulk", "search_dates",
    "search_dates_range", "copy_to_companies", "remove_from_companies", "set_balance",
    "set_period", "disable", "enable", "payment", "payment_link", "add_discount",
    "update_channel", "phone_confirmation", "data", "check", "confirm", "invite",
    "book_dates", "book_services", "book_times", "book_workers", "apply",
})
POST_LIST_ACTIONS = frozenset({"by_filter", "by_id"})

# Сегменты путей, которые не несут смысла в имени метода
SKIP_SEGMENTS = frozenset({"api", "v1", "v2", "marketplace", "company", "chain", "group"})

PYTHON_KEYWORDS = frozenset({
    "and", "as", "assert", "async", "await", "break", "class", "continue", "def",
    "del", "elif", "else", "except", "finally", "for", "from", "global", "if",
    "import", "in", "is", "lambda", "nonlocal", "not", "or", "pass", "raise",
    "return", "try", "while", "with", "yield", "None", "True", "False", "id",
    "type", "data", "input", "filter", "list", "dict", "set", "str", "int",
    "float", "bool", "any", "all", "next", "object", "format", "property",
    "items", "keys", "values", "copy", "count", "page", "client", "request",
})

BUILTIN_ANNOTATION_NAMES = frozenset({
    "Any", "Literal", "Page", "dict", "list", "str", "int", "float", "bool", "None",
})


# ------------------------------------------------------------------ утилиты

def to_snake(name: str) -> str:
    """CamelCase / kebab / смешанные имена -> snake_case."""
    name = re.sub(r"[^0-9a-zA-Z]+", "_", str(name))
    name = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "_", name)
    name = re.sub(r"([A-Z]+)(?=[A-Z][a-z])", r"\1_", name)
    name = re.sub(r"_+", "_", name).strip("_").lower()
    if not name:
        name = "field"
    if name[0].isdigit():
        name = "param_" + name
    return name


def to_snake_param(name: str) -> str:
    """snake_case для параметров с уходом от ключевых слов Python."""
    result = to_snake(name)
    if result in PYTHON_KEYWORDS:
        result += "_"
    return result


def to_camel(name: str) -> str:
    """Имя схемы -> CamelCase-идентификатор класса."""
    parts = re.split(r"[^0-9a-zA-Z]+", name)
    result = "".join(p[:1].upper() + p[1:] for p in parts if p)
    if not result:
        result = "Model"
    if result[0].isdigit():
        result = "M" + result
    return result


def singularize(name: str) -> str:
    """Наивное единственное число для имён методов create_*/delete_*."""
    if len(name) > 3 and name.endswith("s") and not name.endswith("ss"):
        return name[:-1]
    return name


def docstring_lines(*texts: str | None) -> list[str]:
    lines: list[str] = []
    for text in texts:
        if not text:
            continue
        lines.extend(t.rstrip() for t in text.strip().splitlines())
    return lines


# --------------------------------------------------- нормализация inline-схем

class SpecNormalizer:
    """Выносит inline-объекты из путей в именованные компоненты."""

    def __init__(self, spec: dict) -> None:
        self.spec = spec
        self.components: dict = spec.setdefault("components", {}).setdefault("schemas", {})
        self.counter: dict[str, int] = defaultdict(int)

    def unique_name(self, base: str) -> str:
        name, i = base, 1
        while name in self.components:
            i += 1
            name = f"{base}_{i}"
        self.counter[base] = i
        return name

    def normalize(self) -> None:
        self.normalize_paths()
        self.normalize_components()

    def normalize_paths(self) -> None:
        for path, path_item in self.spec.get("paths", {}).items():
            if path in SKIP_PATHS:
                continue
            for method in HTTP_METHODS:
                op = path_item.get(method)
                if not op:
                    continue
                op_code = self.op_code(path, method)
                body = op.get("requestBody", {})
                for content in body.get("content", {}).values():
                    if "schema" in content:
                        content["schema"] = self.inline_to_ref(
                            content["schema"], f"{op_code}Request"
                        )
                for status, resp in op.get("responses", {}).items():
                    if not isinstance(resp, dict):
                        continue
                    content_map = resp.get("content")
                    if not isinstance(content_map, dict):
                        continue
                    for content_type, content in content_map.items():
                        if (
                            not isinstance(content, dict)
                            or "json" not in content_type
                            or "schema" not in content
                        ):
                            continue
                        code = str(status).replace(" ", "")
                        content["schema"] = self.inline_to_ref(
                            content["schema"], f"{op_code}Response{code}"
                        )

    def normalize_components(self) -> None:
        """Выносит inline-объекты из свойств самих компонентов в именованные компоненты.

        Без этого вложенные объекты (свойства, элементы массивов, ветки anyOf)
        остаются ``dict[str, Any]`` в полях моделей.
        """
        for name in list(self.components):
            schema = self.components[name]
            if not isinstance(schema, dict) or "$ref" in schema:
                continue
            props = schema.get("properties")
            if isinstance(props, dict):
                for key, value in props.items():
                    if isinstance(value, dict) and "$ref" not in value:
                        props[key] = self.inline_to_ref(
                            value, f"{name}_{to_snake(str(key))}"
                        )
            items = schema.get("items")
            if isinstance(items, dict) and "$ref" not in items:
                schema["items"] = self.inline_to_ref(items, f"{name}Item")
            for key in ("oneOf", "anyOf", "allOf"):
                variants = schema.get(key)
                if isinstance(variants, list):
                    schema[key] = [
                        self.inline_to_ref(v, f"{name}Variant{i}")
                        if isinstance(v, dict) and "$ref" not in v
                        else v
                        for i, v in enumerate(variants)
                    ]

    def inline_to_ref(self, schema: dict, base_name: str) -> dict:
        """Рекурсивно заменяет inline-объекты/массивы-объекты на $ref."""
        if not isinstance(schema, dict) or "$ref" in schema:
            return schema

        kind = self._shape(schema)

        if kind == "object" and schema.get("properties"):
            name = self.unique_name(to_camel(base_name))
            new_schema = {k: v for k, v in schema.items() if k != "properties"}
            new_schema["properties"] = {
                key: self.inline_to_ref(value, f"{base_name}_{to_snake(key)}")
                for key, value in schema["properties"].items()
            }
            self.components[name] = new_schema
            return {"$ref": f"#/components/schemas/{name}"}

        if kind == "object" and "additionalProperties" in schema:
            ap = schema["additionalProperties"]
            if isinstance(ap, dict) and "$ref" not in ap:
                schema = {
                    **schema,
                    "additionalProperties": self.inline_to_ref(ap, f"{base_name}Value"),
                }
            return schema

        if kind == "array":
            items = schema.get("items")
            if isinstance(items, dict) and "$ref" not in items:
                schema = {
                    **schema,
                    "items": self.inline_to_ref(items, f"{base_name}Item"),
                }
            return schema

        for key in ("oneOf", "anyOf", "allOf"):
            if key in schema:
                schema = {
                    **schema,
                    key: [
                        self.inline_to_ref(v, f"{base_name}Variant{i}")
                        for i, v in enumerate(schema[key])
                    ],
                }
        return schema

    @staticmethod
    def _shape(schema: dict) -> str | None:
        if schema.get("type") == "object" or (not schema.get("type") and schema.get("properties")):
            return "object"
        if schema.get("type") == "array" or (not schema.get("type") and schema.get("items")):
            return "array"
        return None

    @staticmethod
    def op_code(path: str, method: str) -> str:
        """Осмысленное имя операции для синтетических схем."""
        segs = [s for s in path.strip("/").split("/") if s]
        while segs and (segs[0] in PREFIXES or to_snake(segs[0]) in SKIP_SEGMENTS):
            segs.pop(0)
        tail = [to_camel(to_snake(s.strip("{}"))) for s in segs[-2:]]
        return method.capitalize() + "".join(tail)


# ------------------------------------------------------------- модель операций

class Operation:
    """Одна операция API, привязанная к домену по первому тегу."""

    def __init__(self, method: str, path: str, op: dict) -> None:
        self.method = method.upper()
        self.path = path
        self.op = op
        self.summary: str | None = op.get("summary")
        self.description: str | None = op.get("description")
        self.parameters: list[dict] = []
        self.request_schema: dict | None = None
        self.data_is_array = False

    @property
    def path_param_names(self) -> list[str]:
        return [
            to_snake_param(p["name"]) for p in self.parameters if p.get("in") == "path"
        ]


# --------------------------------------------------------- типы из JSON-схемы

class TypeMapper:
    def __init__(
        self,
        components: dict,
        model_classes: dict[str, str],
    ) -> None:
        self.components = components
        self.model_classes = model_classes  # только схемы, порождающие классы

    def resolve(self, schema: dict) -> dict:
        seen: set[str] = set()
        while isinstance(schema, dict) and "$ref" in schema:
            ref = schema["$ref"]
            if ref in seen:
                break
            seen.add(ref)
            schema = self.components.get(ref.split("/")[-1], {})
        return schema if isinstance(schema, dict) else {}

    def annotation(self, schema: dict | None) -> str:
        """Аннотация типа Python для JSON-схемы."""
        if not isinstance(schema, dict):
            return "Any"
        if "$ref" in schema:
            name = schema["$ref"].split("/")[-1]
            if name in self.model_classes:
                return self.model_classes[name]
            return self.annotation(self.components.get(name, {}))

        if "oneOf" in schema or "anyOf" in schema:
            anns: list[str] = []
            for variant in schema.get("oneOf") or schema.get("anyOf") or []:
                ann = self.annotation(variant)
                if ann != "Any" and ann not in anns:
                    anns.append(ann)
            # dict[...] принимает любое object: ставим его последним,
            # чтобы smart-union pydantic предпочёл конкретную модель
            anns.sort(key=lambda a: a.startswith("dict["))
            return " | ".join(anns) if anns else "Any"

        if "enum" in schema:
            values = schema["enum"]
            if values and all(
                isinstance(v, (str, int, float)) and not isinstance(v, bool)
                for v in values
            ):
                lits = ", ".join(json.dumps(v, ensure_ascii=False) for v in values)
                return f"Literal[{lits}]"
            return "Any"

        json_type = schema.get("type")

        if json_type == "string":
            return "str"
        if json_type == "boolean":
            return "bool"
        if json_type == "integer":
            return "int"
        if json_type == "number":
            return "float"
        if json_type == "null":
            return "None"
        if json_type == "array":
            item = self.annotation(schema.get("items") or {})
            return f"list[{item}]"
        if json_type == "object" or schema.get("properties"):
            if not schema.get("properties"):
                ap = schema.get("additionalProperties")
                if isinstance(ap, dict):
                    return f"dict[str, {self.annotation(ap)}]"
                return "dict[str, Any]"
            # объект с описанными свойствами, но без собственного класса
            return "dict[str, Any]"
        return "Any"

    def is_array(self, schema: dict) -> bool:
        schema = self.resolve(schema) if "$ref" in schema else schema
        return (schema.get("type") == "array" or schema.get("items") is not None) and bool(
            schema.get("items")
        )

    def param_annotation(self, schema: dict | None) -> str:
        """Аннотация для query/path-параметров: без Literal, только базовые типы."""
        ann = self.annotation(schema)
        if ann.startswith("Literal["):
            values: list[object] = []
            match = re.search(r"Literal\[(.*)\]", ann)
            if match:
                values = [
                    json.loads(v)
                    for v in re.findall(r'"[^"]*"|\'[^\']*\'|-?\d+(?:\.\d+)?', match.group(1))
                ]
            if values and all(isinstance(v, (int, float)) for v in values):
                return "float" if any(isinstance(v, float) for v in values) else "int"
            return "str"
        return ann


# ------------------------------------------------------ генерация pydantic-моделей

class ModelGenerator:
    def __init__(self, spec: dict) -> None:
        self.components: dict = spec["components"]["schemas"]
        self.used: set[str] = set()
        self.class_names = self._assign_class_names()
        self.model_classes = {
            name: cls
            for name, cls in self.class_names.items()
            if self._emits_class(self.components.get(name, {}))
        }
        self.mapper = TypeMapper(self.components, self.model_classes)

    @staticmethod
    def _emits_class(schema: dict) -> bool:
        return isinstance(schema, dict) and bool(schema.get("properties"))

    def _assign_class_names(self) -> dict[str, str]:
        names: dict[str, str] = {}
        taken: set[str] = set()
        for schema_name in sorted(self.components):
            base = to_camel(schema_name)
            name, i = base, 1
            while name in taken:
                i += 1
                name = f"{base}{i}"
            taken.add(name)
            names[schema_name] = name
        return names

    def mark_used_from_schema(self, schema: dict) -> None:
        """Помечает схемы, реально используемые операциями (транзитивно)."""
        if not isinstance(schema, dict):
            return
        if "$ref" in schema:
            ref = schema["$ref"].split("/")[-1]
            if ref in self.used:
                return
            self.used.add(ref)
            self.mark_used_from_schema(self.components.get(ref, {}))
            return
        if isinstance(schema.get("properties"), dict):
            for value in schema["properties"].values():
                self.mark_used_from_schema(value)
        for key in ("items", "additionalProperties"):
            if isinstance(schema.get(key), dict):
                self.mark_used_from_schema(schema[key])
        for key in ("oneOf", "anyOf", "allOf"):
            for variant in schema.get(key) or []:
                self.mark_used_from_schema(variant)

    # -- аннотации полей

    def _field_annotation(self, prop: dict, required: bool) -> str:
        ann = self.mapper.annotation(prop)
        parts = [p for p in ann.split(" | ") if p and p != "None"]
        ann = " | ".join(parts)
        if required:
            return ann
        if ann == "Any":
            return "Any"
        return ann

    # -- эмиссия

    def generate_modules(self) -> dict[str, str]:
        """Код моделей, разбитый на модули пакета schemas: {имя файла: код}.

        Модели группируются по первой букве класса; слишком большие группы
        дробятся. Ссылки на модели из других модулей разрешаются отложенно --
        schemas/__init__.py после импорта вызывает model_rebuild().
        """
        ordered = self._topological_order()
        emitted: list[str] = []
        for schema_name in ordered:
            if schema_name in self.used and self._model(schema_name):
                emitted.append(schema_name)
        self.generated_count = len(emitted)

        # группировка по первой букве; крупные буквы дробим на части
        groups: dict[str, list[str]] = defaultdict(list)
        for schema_name in emitted:
            letter = self.class_names[schema_name][0].lower()
            groups[letter if letter.isalpha() else "misc"].append(schema_name)

        max_per_module = 60
        modules: dict[str, list[str]] = defaultdict(list)
        for letter in sorted(groups):
            names = groups[letter]
            parts = range(1, len(names) // max_per_module + 2)
            for part in parts:
                chunk = names[(part - 1) * max_per_module : part * max_per_module]
                modules[letter + (str(part) if len(parts) > 1 else "")] = chunk

        result: dict[str, str] = {}
        for module_name, chunk in modules.items():
            title = ", ".join(
                sorted({self.class_names[n][0].upper() for n in chunk})
            )
            lines = [
                f'"""Модели YCLIENTS API ({module_name}: {title}).',
                "",
                "Сгенерировано scripts/generate.py -- не редактируйте вручную.",
                '"""',
                "",
                "from __future__ import annotations",
                "",
                "from datetime import date, datetime",
                "from typing import Any, Literal",
                "",
                "from pydantic import BaseModel, ConfigDict, Field",
            ]
            class_names: list[str] = []
            for schema_name in chunk:
                code = self._model(schema_name)
                if code:
                    lines.append("")
                    lines.append("")
                    lines.append(code)
                    class_names.append(self.class_names[schema_name])
            lines.append("")
            lines.append(f"__all__ = {json.dumps(class_names, indent=4)}")
            lines.append("")
            result[f"{module_name}.py"] = "\n".join(lines)
        self.module_classes = {name: [] for name in result}
        for module_name, chunk in modules.items():
            self.module_classes[f"{module_name}.py"] = [
                self.class_names[n] for n in chunk
            ]
        return result

    @staticmethod
    def build_package_init(modules: dict[str, list[str]]) -> str:
        """Код schemas/__init__.py: реэкспорт всех моделей + отложенный rebuild."""
        imports = "\n".join(
            f"from .{name.removesuffix('.py')} import *" for name in sorted(modules)
        )
        all_names = [cls for name in sorted(modules) for cls in modules[name]]
        all_lines = "\n".join(f'    "{cls}",' for cls in all_names)
        return f'''"""Модели YCLIENTS API, сгенерированы из docs/openapi.json.

Не редактируйте вручную: запустите scripts/generate.py.
"""

from pydantic import BaseModel as _BaseModel

{imports}

_namespaces = dict(globals())
# ссылки на модели из соседних модулей пакета разрешаются здесь, когда
# уже импортированы все модули; несколько заходов -- для цепочек зависимостей
for _round in range(5):
    _incomplete = [
        _obj
        for _obj in _namespaces.values()
        if isinstance(_obj, type)
        and issubclass(_obj, _BaseModel)
        and _obj is not _BaseModel
        and not _obj.__pydantic_complete__
    ]
    if not _incomplete:
        break
    for _model in _incomplete:
        _model.model_rebuild(_types_namespace=_namespaces)
else:
    raise RuntimeError(
        "Не удалось разрешить ссылки моделей: "
        + ", ".join(_obj.__name__ for _obj in _incomplete)
    )

__all__ = [
{all_lines}
]
'''

    def _topological_order(self) -> list[str]:
        deps: dict[str, set[str]] = {}

        def collect(schema: dict, acc: set[str], guard: set[str]) -> None:
            if not isinstance(schema, dict):
                return
            if "$ref" in schema:
                ref = schema["$ref"].split("/")[-1]
                if ref not in guard:
                    acc.add(ref)
                    guard.add(ref)
                    collect(self.components.get(ref, {}), acc, guard)
                return
            for value in (schema.get("properties") or {}).values():
                collect(value, acc, guard)
            for key in ("items", "additionalProperties"):
                if isinstance(schema.get(key), dict):
                    collect(schema[key], acc, guard)
            for key in ("oneOf", "anyOf", "allOf"):
                for variant in schema.get(key) or []:
                    collect(variant, acc, guard)

        for name, schema in self.components.items():
            acc: set[str] = set()
            collect(schema, acc, {name})
            deps[name] = acc

        ordered: list[str] = []
        emitted: set[str] = set()
        pending = deque(sorted(deps))
        while pending:
            next_round: deque[str] = deque()
            progressed = False
            for name in pending:
                if all(d in emitted for d in deps.get(name, ())):
                    ordered.append(name)
                    emitted.add(name)
                    progressed = True
                else:
                    next_round.append(name)
            pending = next_round
            if not progressed:
                ordered.extend(n for n in pending if n not in emitted)
                break
        return ordered

    def _model(self, schema_name: str) -> str:
        schema = self.components[schema_name]
        class_name = self.class_names[schema_name]
        if not isinstance(schema, dict) or not schema.get("properties"):
            return ""

        title = schema.get("title")
        description = schema.get("description")
        lines = [f"class {class_name}(BaseModel):"]
        doc = docstring_lines(description)
        if title and title != class_name and title not in (description or ""):
            doc.append(f"Схема спеки: {title}")
        if doc:
            clean = [d.replace('"""', "'''").strip() for d in doc]
            clean = [d for d in clean if d][:12]
            lines.append(f'    """{clean[0]}')
            for extra in clean[1:]:
                lines.append(f"    {extra}")
            lines.append('    """')
        lines.append("")
        lines.append('    model_config = ConfigDict(populate_by_name=True, extra="allow")')
        lines.append("")

        required = set(schema.get("required") or [])
        field_lines: list[str] = []
        used_field_names: set[str] = set()
        for prop_name, prop in schema["properties"].items():
            if not isinstance(prop, dict):
                prop = {}
            py_name = to_snake_param(str(prop_name))
            if py_name in used_field_names:
                # в спеке бывают дубли вида "ImageGroup" и "image_group"
                i = 2
                while f"{py_name}_{i}" in used_field_names:
                    i += 1
                py_name = f"{py_name}_{i}"
            used_field_names.add(py_name)
            ann = self._field_annotation(prop, prop_name in required)
            args: list[str] = []
            if str(prop_name) != py_name:
                args.append(f"alias={json.dumps(str(prop_name), ensure_ascii=False)}")
            if prop.get("description"):
                desc = " ".join(str(prop["description"]).split())
                if len(desc) > 200:
                    desc = desc[:197] + "..."
                args.append(
                    f"description={json.dumps(desc, ensure_ascii=False)}"
                )
            if prop_name in required:
                if args:
                    field_lines.append(f"    {py_name}: {ann} = Field({', '.join(args)})")
                else:
                    field_lines.append(f"    {py_name}: {ann}")
            else:
                args.insert(0, "default=None")
                field_lines.append(f"    {py_name}: {ann} | None = Field({', '.join(args)})")

        lines.extend(field_lines if field_lines else ["    pass"])
        return "\n".join(lines)


# ------------------------------------------------------------- имена методов

def strip_prefix(path: str) -> list[str]:
    path = path.split("?", 1)[0]
    segs = [s for s in path.strip("/").split("/") if s]
    while segs and segs[0] in PREFIXES:
        segs.pop(0)
    return segs


def significant_segments(segs: list[str], class_nouns: frozenset[str]) -> list[str]:
    """Значимые сегменты слева направо (без служебных и 'своих' существительных)."""
    result: list[str] = []
    for seg in segs:
        if seg.startswith("{"):
            name = to_snake(seg.strip("{}"))
            name = name[:-3] if name.endswith("_id") and len(name) > 4 else name
            if name in PYTHON_KEYWORDS:
                name += "_"
            result.append(name)
        else:
            s = to_snake(seg)
            if s in SKIP_SEGMENTS or s in class_nouns:
                continue
            result.append(s)
    return result


def method_name(
    op: Operation,
    class_nouns: frozenset[str],
    path_has_put: bool,
) -> str:
    clean_path = op.path.split("?", 1)[0]
    override = METHOD_OVERRIDES.get((op.method, clean_path))
    if override:
        return override

    segs = strip_prefix(clean_path)
    if not segs:
        return "request"
    last_is_param = segs[-1].startswith("{")
    last_lit = to_snake(segs[-1]) if not last_is_param else None

    if last_is_param:
        if op.method == "GET":
            return "list" if op.data_is_array else "get"
        if op.method in ("PUT", "PATCH"):
            return "update"
        if op.method == "DELETE":
            return "delete"
        return "update" if path_has_put else "create"

    assert last_lit is not None
    if op.method == "GET":
        if last_lit in GET_ACTIONS:
            return last_lit
        if op.data_is_array:
            return "list" if last_lit in class_nouns else "list_" + last_lit
        return "get" if last_lit in class_nouns else "get_" + last_lit
    if op.method == "POST":
        if last_lit in POST_LIST_ACTIONS:
            return "search" if last_lit == "search" else "list_" + last_lit
        if last_lit in POST_ACTIONS:
            return last_lit
        if last_lit == "create" or last_lit in class_nouns:
            return "create"
        return "create_" + singularize(last_lit)
    if op.method in ("PUT", "PATCH"):
        return "update" if last_lit in class_nouns else "update_" + last_lit
    if op.method == "DELETE":
        return "delete" if last_lit in class_nouns else "delete_" + singularize(last_lit)
    return last_lit


def unique_method_name(
    base: str,
    op: Operation,
    class_nouns: frozenset[str],
    used: dict[str, Operation],
) -> str:
    """Базовое имя метода; при коллизии удлиняет значимыми сегментами пути."""
    if base not in used:
        return base
    segs = strip_prefix(op.path)
    for seg in reversed(significant_segments(segs[:-1], class_nouns)):
        candidate = f"{base}_{seg}"
        if candidate not in used:
            return candidate
    for pair in (
        f"{base}_{a}_{b}"
        for a in significant_segments(segs[:-1], class_nouns)
        for b in significant_segments(segs[:-1], class_nouns)
        if a != b
    ):
        if pair not in used:
            return pair
    i = 2
    while f"{base}_{i}" in used:
        i += 1
    return f"{base}_{i}"


# ------------------------------------------------------------- генерация ресурсов

class ResourceGenerator:
    def __init__(self, spec: dict, models: ModelGenerator) -> None:
        self.spec = spec
        self.models = models
        self.mapper = models.mapper
        self.components = spec["components"]["schemas"]
        self.parameters = spec["components"].get("parameters", {})

    # -- разбор операций по доменам

    def collect_operations(self) -> dict[str, list[Operation]]:
        domains: dict[str, list[Operation]] = defaultdict(list)
        seen: set[tuple[str, str]] = set()
        for path, path_item in self.spec.get("paths", {}).items():
            if path in SKIP_PATHS:
                continue
            shared_params = path_item.get("parameters", [])
            for method in HTTP_METHODS:
                op = path_item.get(method)
                if not op or (path, method) in seen:
                    continue
                seen.add((path, method))
                tag = (op.get("tags") or ["misc"])[0]
                module = TAG_MAP.get(tag, ("misc", "MiscApi", frozenset()))[0]
                operation = Operation(method, path, op)
                operation.parameters = self._resolve_params(
                    shared_params + op.get("parameters", [])
                )
                operation.request_schema = self._request_schema(op)
                operation.data_is_array = self._data_is_array(op)
                domains[module].append(operation)
        return domains

    def _resolve_params(self, params: list[dict]) -> list[dict]:
        resolved: list[dict] = []
        for prm in params:
            if "$ref" in prm:
                prm = self.parameters.get(prm["$ref"].split("/")[-1], prm)
            if isinstance(prm, dict) and prm.get("in") in ("path", "query"):
                resolved.append(prm)
        return resolved

    def _request_schema(self, op: dict) -> dict | None:
        body = op.get("requestBody") or {}
        content = body.get("content", {}).get("application/json", {})
        return content.get("schema")

    def _response_schemas(self, op: dict) -> list[tuple[str, dict]]:
        """(HTTP-статус, схема) для всех 2xx-ответов с JSON."""
        result: list[tuple[str, dict]] = []
        for status, resp in (op.get("responses") or {}).items():
            if not str(status).startswith("2") or not isinstance(resp, dict):
                continue
            content_map = resp.get("content")
            if not isinstance(content_map, dict):
                continue
            json_content = content_map.get("application/json")
            if not isinstance(json_content, dict):
                continue
            schema = json_content.get("schema")
            if schema:
                result.append((str(status), schema))
        return sorted(result)

    def _envelope_parts(self, schema: dict) -> tuple[dict | None, str | None]:
        """(схема data, имя ref схемы meta), если ответ - конверт success/data/meta."""
        target = schema
        if "$ref" in schema:
            target = self.components.get(schema["$ref"].split("/")[-1], {})
        props = target.get("properties") or {}
        if "success" in props and "data" in props:
            meta = props.get("meta", {})
            meta_name = meta.get("$ref", "").split("/")[-1] if isinstance(meta, dict) else None
            return props["data"], meta_name
        return None, None

    def _data_is_array(self, op: dict) -> bool:
        for _, schema in self._response_schemas(op):
            data, _ = self._envelope_parts(schema)
            if data is None:
                data = schema
            if self.mapper.is_array(data):
                return True
        return False

    def response_annotation(self, op: dict) -> str:
        """Python-аннотация ответа метода (по всем 2xx)."""
        schemas = self._response_schemas(op.op)
        if not schemas:
            return "Any"
        anns: list[str] = []
        page_anns: list[str] = []
        for _, schema in schemas:
            ann, page_ann = self._single_response_annotation(schema)
            if ann and ann not in anns:
                anns.append(ann)
            if page_ann and page_ann not in page_anns:
                page_anns.append(page_ann)
        if page_anns and len(anns) == 1 and anns[0] == page_anns[0]:
            return anns[0]
        # dict[...] всеяден: ставим его в конец, иначе pydantic всегда выберет его,
        # и типизированные ветки юниона никогда не будут построены
        anns.sort(key=lambda a: a.startswith("dict["))
        return " | ".join(anns) if anns else "Any"

    def _single_response_annotation(self, schema: dict) -> tuple[str | None, str | None]:
        data, meta_name = self._envelope_parts(schema)
        if data is None:
            ann = self.mapper.annotation(schema)
            return (ann if ann != "None" else "Any"), None

        is_page = meta_name == "response_meta_count_object" and self.mapper.is_array(data)

        if "$ref" in data:
            name = data["$ref"].split("/")[-1]
            cls = self.models.model_classes.get(name)
            ann = cls or self.mapper.annotation(self.components.get(name, {}))
        else:
            if self.mapper.is_array(data):
                item_ann = self.mapper.annotation(data.get("items") or {})
                ann = f"list[{item_ann}]"
            else:
                ann = self.mapper.annotation(data)

        if is_page and ann.startswith("list["):
            item = ann[5:-1]
            return f"Page[{item}]", f"Page[{item}]"
        return ann, None

    def request_annotation(self, op: dict) -> str | None:
        schema = op.request_schema
        if not schema:
            return None
        if "oneOf" in schema or "anyOf" in schema:
            names: list[str] = []
            for v in schema.get("oneOf") or schema.get("anyOf") or []:
                if isinstance(v, dict) and "$ref" in v:
                    cls = self.models.model_classes.get(v["$ref"].split("/")[-1])
                    names.append(cls or "dict[str, Any]")
                else:
                    names.append("dict[str, Any]")
            names = sorted(set(names), key=names.index)
            # модели важнее словаря: dict[str, Any] валидирует всё подряд
            names.sort(key=lambda n: n == "dict[str, Any]")
            return " | ".join(names)
        if "$ref" in schema:
            cls = self.models.model_classes.get(schema["$ref"].split("/")[-1])
            return cls or "dict[str, Any]"
        return "dict[str, Any]"

    # -- импорты моделей

    def _model_imports(self, operations: list[Operation]) -> tuple[set[str], bool]:
        imports: set[str] = set()
        page_used = False
        for op in operations:
            resp_ann = self.response_annotation(op)
            req_ann = self.request_annotation(op)
            for ann in (resp_ann, req_ann):
                if not ann:
                    continue
                if "Page[" in ann:
                    page_used = True
                for ident in re.findall(r"[A-Za-z_][A-Za-z0-9_]*", ann):
                    if ident not in BUILTIN_ANNOTATION_NAMES:
                        imports.add(ident)
        return imports, page_used

    # -- эмиссия домена

    def generate_domain(
        self,
        class_name: str,
        class_nouns: frozenset[str],
        operations: list[Operation],
    ) -> str:
        # уникальные имена методов
        used: dict[str, Operation] = {}
        names: dict[int, str] = {}
        paths_with_put = {o.path for o in operations if o.method == "PUT"}
        for op in operations:
            base = method_name(op, class_nouns, op.path in paths_with_put)
            name = unique_method_name(base, op, class_nouns, used)
            used[name] = op
            names[id(op)] = name

        model_imports, page_used = self._model_imports(operations)

        lines = [
            f'"""{class_name} -- сгенерированные методы API."""',
            "",
            "from __future__ import annotations",
            "",
            "from typing import Any",
            "",
            "from yclients._base import BaseClient",
        ]
        if page_used or model_imports:
            lines.append("")
        if page_used:
            lines.append("from yclients.models.common import Page")
        if model_imports:
            lines.append(
                f"from yclients.models.schemas import {', '.join(sorted(model_imports))}"
            )
        lines += [
            "",
            "",
            f"class {class_name}:",
            '    """Сгенерированные методы домена."""',
            "",
            "    def __init__(self, client: BaseClient) -> None:",
            "        self._client = client",
            "",
        ]

        for op in operations:
            lines.append(self._method(op, names[id(op)], paths_with_put))
            lines.append("")

        code = "\n".join(lines).rstrip() + "\n"
        # метод list() затеняет builtin в области видимости класса -- используем
        # builtins.list в аннотациях, чтобы mypy не путался (рантайму это не нужно)
        if re.search(r"def list\(", code):
            code = re.sub(r"(?<![.\w])list\[", "builtins.list[", code)
            if "builtins.list[" in code and "import builtins" not in code:
                code = code.replace(
                    "from typing import Any", "import builtins\n\nfrom typing import Any", 1
                )
        if "Literal[" in code:
            code = code.replace(
                "from typing import Any", "from typing import Any, Literal", 1
            )
        return code

    def _method(self, op: Operation, name: str, paths_with_put: set[str]) -> str:
        args: list[str] = ["self"]

        # Некоторые пути спеки содержат "?key={param}" -- отделяем их:
        # реальные query-параметры передаются через params=, не через путь.
        clean_path = op.path.split("?", 1)[0]
        embedded_query_placeholders = re.findall(r"[?&][A-Za-z0-9_]+=\{([^{}]+)\}", op.path)

        # Параметры пути берём из плейсхолдеров пути: в спеке есть ошибки, где
        # у разных плейсхолдеров указано одно и то же имя параметра.
        placeholders = list(dict.fromkeys(re.findall(r"\{([^{}]+)\}", clean_path)))
        path_by_name = {
            str(p.get("name")): p for p in op.parameters if p.get("in") == "path"
        }
        path_by_lower = {k.lower(): v for k, v in path_by_name.items()}

        path_params: list[tuple[str, str]] = []
        used_param_names: set[str] = set()
        for ph in placeholders:
            prm = path_by_name.get(ph) or path_by_lower.get(ph.lower())
            if prm is not None:
                used_param_names.add(str(prm.get("name")))
            ann = self.mapper.param_annotation((prm or {}).get("schema") or {})
            if ann in ("None", "Any"):
                ann = "str"
            py = to_snake_param(ph)
            path_params.append((py, ph))
            args.append(f"{py}: {ann}")

        query_params: list[tuple[str, str, str]] = []
        for prm in op.parameters:
            orig = str(prm.get("name"))
            if prm.get("in") != "query" or orig in used_param_names:
                continue
            py = to_snake_param(orig)
            ann = self.mapper.param_annotation(prm.get("schema") or {})
            if ann == "None":
                ann = "Any"
            query_params.append((py, orig, ann))

        # Query-параметры, замусоренные в шаблоне пути, но не объявленные в спеке
        declared_query = {orig for _, orig, _ in query_params}
        for ph in embedded_query_placeholders:
            if ph in declared_query or ph in used_param_names:
                continue
            query_params.append((to_snake_param(ph), ph, "str"))

        body_ann = self.request_annotation(op)
        has_body = body_ann is not None
        if has_body:
            args.append(f"data: {body_ann}")

        if query_params:
            args.append("*")
        for py, _, ann in query_params:
            args.append(f"{py}: {ann} | None = None")
        args.append("extra_query: dict[str, Any] | None = None")

        resp_ann = self.response_annotation(op)
        if " | " in resp_ann:
            resp_ann = f"({resp_ann})"

        lines = [f"    async def {name}("]
        for i, arg in enumerate(args):
            comma = "," if i < len(args) - 1 else ""
            lines.append(f"        {arg}{comma}")
        lines.append(f"    ) -> {resp_ann}:")

        doc = docstring_lines(op.summary, op.description if op.summary else None)
        clean = [d.strip().replace('"""', "'''") for d in doc if d.strip()][:14]
        if clean:
            lines.append("        \"\"\"" + clean[0])
            for extra in clean[1:]:
                lines.append("        " + extra)
            lines.append('        """')

        lines.append("        return await self._client.request(")
        lines.append(f'            "{op.method}",')
        lines.append(f'            "{clean_path}",')
        if path_params:
            mapping = ", ".join(f'"{orig}": {py}' for py, orig in path_params)
            lines.append(f"            path_params={{{mapping}}},")
        if query_params:
            mapping = ", ".join(f'"{q_orig}": {q_py}' for q_py, q_orig, _ in query_params)
            lines.append(f"            params={{{mapping}}},")
        if has_body:
            lines.append("            json_body=data,")
        if resp_ann != "Any":
            lines.append(f"            response_model={resp_ann},")
        lines.append("            extra_query=extra_query,")
        lines.append("        )")
        return "\n".join(lines)


# ---------------------------------------------------------------------- main

def main() -> int:
    spec = json.loads(SPEC_PATH.read_text(encoding="utf-8"))

    normalizer = SpecNormalizer(spec)
    normalizer.normalize()

    models = ModelGenerator(spec)
    resources = ResourceGenerator(spec, models)
    domains = resources.collect_operations()

    for ops in domains.values():
        for op in ops:
            if op.request_schema:
                models.mark_used_from_schema(op.request_schema)
            for _, schema in resources._response_schemas(op.op):
                models.mark_used_from_schema(schema)

    schemas_modules = models.generate_modules()
    schemas_dir = SRC / "models" / "schemas"
    if schemas_dir.exists():
        shutil.rmtree(schemas_dir)
    old_schemas_file = SRC / "models" / "schemas.py"
    if old_schemas_file.exists():
        old_schemas_file.unlink()
    schemas_dir.mkdir(parents=True)
    for filename, code in schemas_modules.items():
        (schemas_dir / filename).write_text(code, encoding="utf-8")
    (schemas_dir / "__init__.py").write_text(
        models.build_package_init(models.module_classes), encoding="utf-8"
    )

    tag_by_module: dict[str, tuple[str, frozenset[str]]] = {}
    for _tag, (module, class_name, nouns) in TAG_MAP.items():
        tag_by_module.setdefault(module, (class_name, nouns))

    exports: list[tuple[str, str]] = []
    total_ops = 0
    for module in sorted(tag_by_module):
        class_name, nouns = tag_by_module[module]
        ops = domains.get(module, [])
        if not ops:
            continue
        total_ops += len(ops)
        code = resources.generate_domain(class_name, nouns, ops)
        (SRC / "resources" / f"{module}.py").write_text(code, encoding="utf-8")
        exports.append((class_name, module))

    # resources/__init__.py
    init_lines = ['"""Ресурсные классы API, сгенерированы из docs/openapi.json."""', ""]
    for class_name, module in exports:
        init_lines.append(f"from yclients.resources.{module} import {class_name}")
    init_lines += ["", "__all__ = ["]
    init_lines += [f'    "{c}",' for c, _ in sorted(exports)]
    init_lines += ["]", ""]
    (SRC / "resources" / "__init__.py").write_text("\n".join(init_lines), encoding="utf-8")

    (SRC / "client.py").write_text(
        build_facade(exports, models.model_classes.get("auth_request-2")),
        encoding="utf-8",
    )

    lint_generated_code()

    missing = set(domains) - {m for _, m in exports}
    print(f"Сгенерировано: {models.generated_count} моделей, {len(exports)} ресурсов, {total_ops} операций")
    if missing:
        print(f"!! Домены без TAG_MAP: {missing}")
        return 1
    return 0


def lint_generated_code() -> None:
    """Прогоняет ruff --fix по сгенерированному коду (если ruff доступен)."""
    import shutil
    import subprocess

    commands: list[list[str]] = [[sys.executable, "-m", "ruff"]]
    found = shutil.which("ruff")
    if found:
        commands.append([found])
    for cmd in commands:
        if subprocess.run([*cmd, "--version"], capture_output=True).returncode == 0:
            subprocess.run([*cmd, "check", "--fix", str(SRC)], capture_output=True)
            return
    # ruff не установлен - не критично


def build_facade(exports: list[tuple[str, str]], auth_body_cls: str | None) -> str:
    lines = [
        '"""Фасад клиента YCLIENTS API (генерируется scripts/generate.py)."""',
        "",
        "from __future__ import annotations",
        "",
        "from typing import Any",
        "",
        "import httpx",
        "",
        "from ._base import DEFAULT_BASE_URL, DEFAULT_TIMEOUT, BaseClient",
    ]
    if auth_body_cls:
        lines.append("from .models.schemas import " + auth_body_cls)
    for class_name, module in exports:
        lines.append(f"from .resources.{module} import {class_name}")
    lines.append("")
    lines.append("__all__ = [")
    lines.append("    'YclientsClient',")
    for class_name, _module in exports:
        lines.append(f"    '{class_name}',")
    lines.append("]")
    lines += [
        "",
        "",
        "class YclientsClient:",
        '    """Асинхронный клиент YCLIENTS REST API.',
        "",
        "    Атрибуты -- домены API: ``client.companies``, ``client.clients``,",
        "    ``client.records`` и т.д.",
        "",
        "    Пример:",
        '        async with YclientsClient(partner_token="...") as client:',
        "            companies = await client.companies.list(my=1)",
        '    """',
        "",
        "    def __init__(",
        "        self,",
        "        partner_token: str,",
        "        user_token: str | None = None,",
        "        *,",
        "        base_url: str = DEFAULT_BASE_URL,",
        "        timeout: float = DEFAULT_TIMEOUT,",
        "        headers: dict[str, str] | None = None,",
        "        max_retries: int = 2,",
        "        retry_backoff: float = 0.5,",
        "        http_client: httpx.AsyncClient | None = None,",
        "    ) -> None:",
        "        self._base = BaseClient(",
        "            partner_token,",
        "            user_token,",
        "            base_url=base_url,",
        "            timeout=timeout,",
        "            headers=headers,",
        "            max_retries=max_retries,",
        "            retry_backoff=retry_backoff,",
        "            http_client=http_client,",
        "        )",
    ]
    for class_name, module in exports:
        lines.append(f"        self.{module} = {class_name}(self._base)")
    lines += [
        "",
        "    async def aclose(self) -> None:",
        '        """Закрывает HTTP-клиент."""',
        "        await self._base.aclose()",
        "",
        "    async def __aenter__(self) -> YclientsClient:",
        "        return self",
        "",
        "    async def __aexit__(self, *exc_info: object) -> None:",
        "        await self.aclose()",
        "",
        "    # -------------------------------------------------------------- auth",
        "",
        "    @property",
        "    def user_token(self) -> str | None:",
        '        """Текущий User-токен (если авторизован)."""',
        "        return self._base.user_token",
        "",
        "    def set_user_token(self, user_token: str | None) -> None:",
        '        """Задаёт User-токен вручную."""',
        "        self._base.set_user_token(user_token)",
        "",
        "    async def login(self, login: str, password: str) -> Any:",
        '        """Авторизует пользователя и сохраняет его User-токен.',
        "",
        "        При включённой 2FA вернёт ответ с необходимостью кода подтверждения --",
        "        тогда повторите вызов с кодом через ``client.auth.login()`` и",
        "        передайте полученный токен в ``client.set_user_token()``.",
        '        """',
        "        result = await self.auth.login("
        + (
            f"{auth_body_cls}(login=login, password=password)"
            if auth_body_cls
            else '{"login": login, "password": password}'
        )
        + ")",
        "        token = result.get('user_token') if isinstance(result, dict) else getattr(result, 'user_token', None)",
        "        if token:",
        "            self._base.set_user_token(token)",
        "        return result",
        "",
    ]
    return "\n".join(lines)


if __name__ == "__main__":
    sys.exit(main())
