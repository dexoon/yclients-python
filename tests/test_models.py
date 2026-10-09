"""Модели: generic-страница, алиасы, extra-поля."""

from __future__ import annotations

import pytest
from pydantic import ValidationError as PydanticValidationError

from yclients.models import (
    AuthRequest2,
    AuthResponse2,
    ClientCommentContainer,
    Page,
    ValidationErrorItem,
)


def test_page_is_generic() -> None:
    page = Page[ClientCommentContainer].model_validate(
        {"data": [{"id": 1, "text": "ок", "type": "default"}], "count": 5}
    )
    assert page.count == 5
    assert isinstance(page.data[0], ClientCommentContainer)
    assert page.data[0].id_ == 1


def test_page_without_meta() -> None:
    page = Page[int].model_validate({"data": [1, 2, 3]})
    assert page.count is None
    assert page.data == [1, 2, 3]


def test_alias_field_populated_from_api_name() -> None:
    auth = AuthResponse2.model_validate({"id": 42, "user_token": "tok", "name": "Илья"})
    assert auth.id_ == 42
    assert auth.user_token == "tok"


def test_alias_serialized_back() -> None:
    comment = ClientCommentContainer(type_="default", text="текст")
    dumped = comment.model_dump(mode="json", by_alias=True, exclude_none=True)
    assert dumped == {"type": "default", "text": "текст"}


def test_extra_fields_allowed() -> None:
    company = AuthResponse2.model_validate({"id": 1, "new_api_field": "значение"})
    assert company.model_extra == {"new_api_field": "значение"}


def test_missing_required_field_raises() -> None:
    # у AuthRequest2 поля login и password обязательные
    with pytest.raises(PydanticValidationError):
        AuthRequest2.model_validate({})


def test_validation_error_item() -> None:
    item = ValidationErrorItem.model_validate(
        {"field": "name", "message": "обязательное поле"}
    )
    assert item.field == "name"
    assert item.message == "обязательное поле"
