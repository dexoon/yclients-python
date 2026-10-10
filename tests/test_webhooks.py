"""Тесты моделей webhook-уведомлений на примерах из документации YCLIENTS.

Примеры payload взяты из официальной документации webhooks:
https://support.yclients.ru/67-69-993--webhooks-v-yclients/
"""

import json
from typing import Any

import pytest
from pydantic import ValidationError

from yclients import (
    ClientWebhook,
    FinancesOperationWebhook,
    GoodsOperationsWebhook,
    GoodWebhook,
    RecordWebhook,
    ServiceCategoryWebhook,
    ServiceWebhook,
    StaffWebhook,
    UnknownWebhook,
    parse_webhook,
)

STAFF_CREATE = """{
    "company_id": 997441,
    "resource": "staff",
    "resource_id": 5058870,
    "status": "create",
    "data": {"id": 5058870, "name": "Test_2"}
}"""

GOOD_CREATE = {
    "company_id": 997441,
    "resource": "good",
    "resource_id": 46810311,
    "status": "create",
    "data": {
        "title": "new_goods",
        "value": "new_goods",
        "label": "new_goods",
        "article": "",
        "category": "test",
        "category_id": 1693647,
        "salon_id": 997441,
        "good_id": 46810311,
        "cost": 1000,
        "unit_id": 216760,
        "unit_short_title": "шт",
        "service_unit_id": 216763,
        "service_unit_short_title": "г",
        "actual_cost": 800,
        "unit_actual_cost": 80,
        "unit_actual_cost_format": "80 ₽",
        "unit_equals": 10,
        "barcode": "",
        "is_chain": False,
        "comment": "goods",
        "loyalty_abonement_type_id": 0,
        "loyalty_certificate_type_id": 0,
        "loyalty_certificate_type": None,
        "loyalty_allow_empty_code": 1,
        "loyalty_serial_number_limited": 0,
        "actual_amounts": [],
        "critical_amount": 0,
        "desired_amount": 0,
        "last_change_date": "2026-03-07T14:44:39+0400",
        "is_goods_mark_enabled": False,
    },
}

SERVICE_CREATE = {
    "company_id": 997441,
    "resource": "service",
    "resource_id": 27140007,
    "status": "create",
    "data": {
        "id": 27140007,
        "salon_service_id": 30950727,
        "title": "New_services",
        "booking_title": "New_services",
        "category_id": 26599596,
        "price_min": 1000,
        "price_max": 1000,
        "duration": 3600,
        "discount": 0,
        "comment": "",
        "weight": 0,
        "active": 1,
        "api_id": "0",
        "staff": [{"id": 5049378, "seance_length": 3600}],
        "image_group": [],
        "prepaid": "forbidden",
        "is_multi": False,
        "capacity": 0,
        "is_price_managed_only_in_chain": False,
        "is_comment_managed_only_in_chain": False,
    },
}

SERVICE_CATEGORY_CREATE = {
    "company_id": 997441,
    "resource": "service_category",
    "resource_id": 27140598,
    "status": "create",
    "data": {
        "id": 27140598,
        "salon_service_id": 30951402,
        "title": "New_categories",
        "weight": 0,
        "api_id": "",
        "staff": [],
        "is_chain": False,
    },
}

CLIENT_CREATE = {
    "company_id": 997441,
    "resource": "client",
    "resource_id": 371102091,
    "status": "create",
    "data": {
        "id": 371102091,
        "name": "New_Client",
        "surname": "",
        "patronymic": "",
        "display_name": "New_Client",
        "phone": "+79115566866",
        "email": "",
        "card": "",
        "birth_date": "",
        "comment": "test_1",
        "discount": 0,
        "visits": 0,
        "sex_id": 0,
        "sex": "Неизвестно",
        "sms_check": 0,
        "sms_bot": 0,
        "sms_not": 0,
        "spent": 0,
        "paid": 0,
        "balance": 0,
        "importance_id": 0,
        "importance": "Без класса важности",
        "categories": [],
        "last_change_date": "2026-03-07T16:55:56+0400",
        "custom_fields": {"text": "text!"},
    },
}

RECORD_CREATE = {
    "company_id": 997441,
    "resource": "record",
    "resource_id": 1561921428,
    "status": "create",
    "data": {
        "id": 1561921428,
        "company_id": 997441,
        "staff_id": 3094597,
        "date": "2026-03-07 18:00:00",
        "attendance": 0,
        "services": [{"id": 25184394, "title": "Мужская стрижка", "cost": 1300}],
    },
}

# payload частичный: только изменившиеся поля
RECORD_UPDATE = """{
    "company_id": 997441,
    "resource": "record",
    "resource_id": 1561921428,
    "status": "update",
    "data": {"id": 1561921428, "comment": "test"}
}"""

RECORD_DELETE = {
    "company_id": 997441,
    "resource": "record",
    "resource_id": 1561921428,
    "status": "delete",
    "data": {"id": 1561921428, "deleted": True},
}

SALE_CREATE = {
    "company_id": 997441,
    "resource": "goods_operations_sale",
    "resource_id": 1505139618,
    "status": "create",
    "data": {
        "id": 1505139618,
        "document_id": 1786795563,
        "type_id": 1,
        "type": "Продажа товара",
        "operation_unit_type": 1,
        "amount": -1,
        "create_date": "2026-03-10T14:50:58+0400",
        "cost_per_unit": 1000,
        "cost": 1000,
        "discount": 0,
        "comment": "",
        "record_id": 0,
        "last_change_date": "2026-03-10T14:51:26+04:00",
        "loyalty_abonement_id": 0,
        "loyalty_certificate_id": 0,
        "good": {"id": 46902813, "title": "Test_goods"},
        "unit": {"id": 216760, "title": "Штука", "short_title": "шт."},
        "storage": {"id": 2012214, "title": "Товары"},
        "client": {"id": 371127207, "name": "Test_YC", "phone": "79006464261"},
        "master": {"id": 3094597, "title": "Filipp Schigartcov"},
        "service": [],
        "supplier": [],
    },
}

RECEIPT_CREATE = {
    "company_id": 997441,
    "resource": "goods_operations_receipt",
    "resource_id": 1505181921,
    "status": "create",
    "data": {
        "id": 1505181921,
        "document_id": 1786846098,
        "type_id": 3,
        "type": "Приход товара",
        "operation_unit_type": 1,
        "amount": 1,
        "create_date": "2026-03-10T15:06:00+0400",
        "cost_per_unit": 800,
        "cost": 800,
        "discount": 0,
        "comment": "",
        "record_id": 0,
        "last_change_date": "2026-03-10T15:06:24+04:00",
        "loyalty_abonement_id": 0,
        "loyalty_certificate_id": 0,
        "good": {"id": 46902813, "title": "Test_goods"},
        "unit": {"id": 216760, "title": "Штука", "short_title": "шт."},
        "storage": {"id": 2012213, "title": "Расходники"},
        "client": [],
        "master": [],
        "service": [],
        "supplier": [],
    },
}

CONSUMABLE_CREATE = {
    "company_id": 997441,
    "resource": "goods_operations_consumable",
    "resource_id": 1505280765,
    "status": "create",
    "data": {
        "id": 1505280765,
        "document_id": 1786965060,
        "type_id": 2,
        "type": "Списание расходников",
        "operation_unit_type": 2,
        "amount": -1,
        "create_date": "2026-03-10T18:00:00+0400",
        "cost_per_unit": 0.17,
        "cost": 0.17,
        "record_id": 1566746583,
        "good": {"id": 41289912, "title": "test 123"},
        "unit": {"id": 216763, "title": "Грамм", "short_title": "г"},
        "storage": {"id": 2012213, "title": "Расходники"},
        "client": {"id": 241731761, "name": "Filipp", "phone": "79006464263"},
        "service": {"id": 25184394, "title": "Мужская стрижка"},
    },
}

STOLEN_CREATE = {
    "company_id": 997441,
    "resource": "goods_operations_stolen",
    "resource_id": 1505226180,
    "status": "create",
    "data": {
        "id": 1505226180,
        "document_id": 1786901040,
        "type_id": 4,
        "type": "Списание товара",
        "operation_unit_type": 2,
        "amount": -1,
        "create_date": "2026-03-10T15:22:00+0400",
        "cost_per_unit": 800,
        "cost": 800,
        "discount": 0,
        "comment": "",
        "record_id": 0,
        "last_change_date": "2026-03-10T15:23:03+04:00",
        "loyalty_abonement_id": 0,
        "loyalty_certificate_id": 0,
        "good": {"id": 46902813, "title": "Test_goods"},
        "unit": {"id": 216760, "title": "Штука", "short_title": "шт."},
        "storage": {"id": 2012213, "title": "Расходники"},
        "client": [],
        "master": [],
        "service": [],
        "supplier": [],
    },
}

# перемещение формирует две операции с одинаковым document_id
MOVE_OUT = {
    "company_id": 997441,
    "resource": "goods_operations_move",
    "resource_id": 1505320617,
    "status": "create",
    "data": {
        "id": 1505320617,
        "document_id": 1787013297,
        "type": "Перемещение товара",
        "amount": -1,
        "good": {"id": 46902813, "title": "Test_goods"},
        "storage": {"id": 2012213, "title": "Расходники"},
    },
}

MOVE_IN = {
    "company_id": 997441,
    "resource": "goods_operations_move",
    "resource_id": 1505320620,
    "status": "create",
    "data": {
        "id": 1505320620,
        "document_id": 1787013297,
        "type": "Перемещение товара",
        "amount": 1,
        "good": {"id": 46902813, "title": "Test_goods"},
        "storage": {"id": 2012214, "title": "Товары"},
    },
}

FINANCES_CREATE = {
    "company_id": 997441,
    "resource": "finances_operation",
    "resource_id": 1362847671,
    "status": "create",
    "data": {
        "id": 1362847671,
        "document_id": 1787082051,
        "date": "2026-03-12T12:55:00+0400",
        "amount": 1300,
        "expense": {"id": 5, "title": "Оказание услуг"},
        "account": {"id": 2038564, "title": "Основная касса"},
    },
}

FINANCES_UPDATE = {
    "company_id": 997441,
    "resource": "finances_operation",
    "resource_id": 1362842394,
    "status": "update",
    "data": {"id": 1362842394, "amount": 1200, "record_id": 1566746583},
}

FINANCES_DELETE = {
    "company_id": 997441,
    "resource": "finances_operation",
    "resource_id": 1362847671,
    "status": "delete",
    "data": {"id": 1362847671, "amount": 1300},
}


@pytest.mark.parametrize(
    ("payload", "expected_class"),
    [
        (STAFF_CREATE, StaffWebhook),
        (GOOD_CREATE, GoodWebhook),
        (SERVICE_CREATE, ServiceWebhook),
        (SERVICE_CATEGORY_CREATE, ServiceCategoryWebhook),
        (CLIENT_CREATE, ClientWebhook),
        (RECORD_CREATE, RecordWebhook),
        (RECORD_UPDATE, RecordWebhook),
        (RECORD_DELETE, RecordWebhook),
        (SALE_CREATE, GoodsOperationsWebhook),
        (RECEIPT_CREATE, GoodsOperationsWebhook),
        (CONSUMABLE_CREATE, GoodsOperationsWebhook),
        (STOLEN_CREATE, GoodsOperationsWebhook),
        (MOVE_OUT, GoodsOperationsWebhook),
        (MOVE_IN, GoodsOperationsWebhook),
        (FINANCES_CREATE, FinancesOperationWebhook),
        (FINANCES_UPDATE, FinancesOperationWebhook),
        (FINANCES_DELETE, FinancesOperationWebhook),
    ],
)
def test_dispatch_by_resource(
    payload: dict[str, Any] | str, expected_class: type
) -> None:
    event = parse_webhook(payload)
    assert isinstance(event, expected_class)
    assert event.company_id == 997441
    assert event.status in ("create", "update", "delete")


def test_json_and_bytes_input() -> None:
    from_json = parse_webhook(STAFF_CREATE)
    from_bytes = parse_webhook(STAFF_CREATE.encode())
    assert from_json == from_bytes
    assert isinstance(from_json, StaffWebhook)
    assert from_json.data is not None
    assert from_json.data.name == "Test_2"


def test_record_partial_update_keeps_only_sent_fields() -> None:
    event = parse_webhook(RECORD_UPDATE)
    assert isinstance(event, RecordWebhook)
    assert event.resource_id == 1561921428
    assert event.data is not None
    assert event.data.id_ == 1561921428
    assert event.data.comment == "test"
    assert event.data.staff_id is None  # поле не пришло в payload


def test_record_delete_flag() -> None:
    event = parse_webhook(RECORD_DELETE)
    assert isinstance(event, RecordWebhook)
    assert event.data is not None
    assert event.data.deleted is True


def test_extra_fields_are_preserved() -> None:
    # loyalty_serial_number_limited есть в примерах, но нет в таблице полей
    event = parse_webhook(GOOD_CREATE)
    assert isinstance(event, GoodWebhook)
    assert event.data is not None
    assert event.data.model_extra is not None
    assert event.data.model_extra["loyalty_serial_number_limited"] == 0
    # "1" в примере приходит числом, а не bool -- значение не искажается
    assert event.data.loyalty_allow_empty_code == 1


def test_sale_nested_objects() -> None:
    event = parse_webhook(SALE_CREATE)
    assert isinstance(event, GoodsOperationsWebhook)
    assert event.data is not None
    assert event.data.good is not None and event.data.good.title == "Test_goods"
    assert event.data.unit is not None and event.data.unit.short_title == "шт."
    client = event.data.client
    assert not isinstance(client, list)
    assert client is not None and client.phone == "79006464261"
    master = event.data.master
    assert not isinstance(master, list)
    assert master is not None and master.title == "Filipp Schigartcov"
    assert event.data.amount == -1


def test_receipt_client_and_master_are_arrays() -> None:
    event = parse_webhook(RECEIPT_CREATE)
    assert isinstance(event, GoodsOperationsWebhook)
    assert event.data is not None
    assert event.data.client == []
    assert event.data.master == []


def test_consumable_service_is_object() -> None:
    event = parse_webhook(CONSUMABLE_CREATE)
    assert isinstance(event, GoodsOperationsWebhook)
    assert event.data is not None
    service = event.data.service
    assert not isinstance(service, list)
    assert service is not None and service.title == "Мужская стрижка"


def test_move_pairs_share_document_id() -> None:
    out_event = parse_webhook(MOVE_OUT)
    in_event = parse_webhook(MOVE_IN)
    out = out_event.data
    inn = in_event.data
    assert out is not None and inn is not None
    assert out.document_id == inn.document_id
    assert (out.amount, inn.amount) == (-1, 1)


def test_client_custom_fields_dict() -> None:
    event = parse_webhook(CLIENT_CREATE)
    assert isinstance(event, ClientWebhook)
    assert event.data is not None
    assert event.data.custom_fields == {"text": "text!"}
    assert event.data.sex == "Неизвестно"


def test_record_create_services() -> None:
    event = parse_webhook(RECORD_CREATE)
    assert isinstance(event, RecordWebhook)
    assert event.data is not None
    assert event.data.services is not None
    service = event.data.services[0]
    assert service.title == "Мужская стрижка"
    assert service.cost == 1300


def test_finances_nested() -> None:
    event = parse_webhook(FINANCES_CREATE)
    assert isinstance(event, FinancesOperationWebhook)
    assert event.data is not None
    assert event.data.expense is not None and event.data.expense.title == "Оказание услуг"
    assert event.data.account is not None and event.data.account.id_ == 2038564


def test_unknown_resource_falls_back() -> None:
    payload = {
        "company_id": 997441,
        "resource": "brand_new_resource",
        "resource_id": 1,
        "status": "create",
        "data": {"foo": "bar"},
    }
    event = parse_webhook(payload)
    assert isinstance(event, UnknownWebhook)
    assert event.resource == "brand_new_resource"
    assert event.data == {"foo": "bar"}


def test_malformed_payload_raises() -> None:
    with pytest.raises(ValidationError):
        parse_webhook("not json")
    with pytest.raises(ValidationError):
        parse_webhook({"resource": "record"})  # нет company_id


def test_missing_data_is_allowed() -> None:
    event = parse_webhook(
        {"company_id": 1, "resource": "client", "resource_id": 2, "status": "delete"}
    )
    assert isinstance(event, ClientWebhook)
    assert event.data is None


def test_bad_status_rejected() -> None:
    with pytest.raises(ValidationError):
        parse_webhook(
            {
                "company_id": 1,
                "resource": "client",
                "resource_id": 2,
                "status": "explode",
                "data": {},
            }
        )


def test_json_string_matches_docs_example() -> None:
    # пример из документации "Изменение записи" -- сырой JSON
    raw = json.loads(RECORD_UPDATE)
    assert json.dumps(raw, ensure_ascii=False)  # тело валидно
    event = parse_webhook(RECORD_UPDATE)
    assert isinstance(event, RecordWebhook)
    assert event.status == "update"
