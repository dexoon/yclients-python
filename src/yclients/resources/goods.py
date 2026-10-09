"""GoodsApi -- сгенерированные методы API."""

from __future__ import annotations

import builtins
from typing import Any

from yclients._base import BaseClient
from yclients.models.schemas import (
    GoodsCompanyGoodsIdResponse200DataTypesDataItem,
    GoodsCompanyRequestDataType,
    GoodsCompanyRequestWithRulesDataType,
)


class GoodsApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def create(
        self,
        company_id: float,
        data: GoodsCompanyRequestDataType,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[GoodsCompanyGoodsIdResponse200DataTypesDataItem]:
        """Создать товар
        Метод позволяет создать товар
        """
        return await self._client.request(
            "POST",
            "/api/v1/goods/{company_id}",
            path_params={"company_id": company_id},
            json_body=data,
            response_model=builtins.list[GoodsCompanyGoodsIdResponse200DataTypesDataItem],
            extra_query=extra_query,
        )

    async def list(
        self,
        company_id: float,
        good_id: float,
        *,
        term: str | None = None,
        page_: float | None = None,
        count_: float | None = None,
        category_id: float | None = None,
        changed_after: str | None = None,
        changed_before: str | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[GoodsCompanyGoodsIdResponse200DataTypesDataItem]:
        """Получить товары
        + term: Наименование, артикул или штрих-код
        + page (number, `1`) - Номер страницы (не используется, если передан good_id)
        + count (number, `25`) - Количество товаров на странице (не используется, если передан good_id)
        + category_id (number, `777`) - Id категории товаров (не используется, если передан good_id)
        + changed_after (string) - фильтрация товаров, измененных/созданных начиная с конкретной даты и времени (не используется, если передан good_id)
        + changed_before (string) - фильтрация товаров, измененных/созданных до конкретной даты и времени (не используется, если передан good_id)
        """
        return await self._client.request(
            "GET",
            "/api/v1/goods/{company_id}/{good_id}",
            path_params={"company_id": company_id, "good_id": good_id},
            params={"term": term, "page": page_, "count": count_, "category_id": category_id, "changed_after": changed_after, "changed_before": changed_before},
            response_model=builtins.list[GoodsCompanyGoodsIdResponse200DataTypesDataItem],
            extra_query=extra_query,
        )

    async def update(
        self,
        company_id: float,
        good_id: float,
        data: GoodsCompanyRequestWithRulesDataType,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[GoodsCompanyGoodsIdResponse200DataTypesDataItem]:
        """Редактировать товар
        Метод позволяет изменить параметры товара.
        При редактировании единиц измерения у товара, по которому уже имеются складские операции, необходимо добавлять массив правил пересчета единиц измерения - correction_rules. В ином случае, массив является необязательным.
        """
        return await self._client.request(
            "PUT",
            "/api/v1/goods/{company_id}/{good_id}",
            path_params={"company_id": company_id, "good_id": good_id},
            json_body=data,
            response_model=builtins.list[GoodsCompanyGoodsIdResponse200DataTypesDataItem],
            extra_query=extra_query,
        )

    async def delete(
        self,
        company_id: float,
        good_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Удалить товар
        Метод позволяет удалить товар
        """
        return await self._client.request(
            "DELETE",
            "/api/v1/goods/{company_id}/{good_id}",
            path_params={"company_id": company_id, "good_id": good_id},
            extra_query=extra_query,
        )
