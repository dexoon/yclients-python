"""GoodsCategoriesApi -- сгенерированные методы API."""

from __future__ import annotations

import builtins
from typing import Any

from yclients._base import BaseClient
from yclients.models.schemas import (
    GoodsCategoriesPostPutResponseDataTypesData,
    GoodsCategoriesRequestDataTypes,
    GoodsCategoriesResponse200DataTypesDataItem,
    GoodsCategoryNodeResponse200DataTypesData,
    GoodsSearchResponse200DataTypesDataItem,
)


class GoodsCategoriesApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def search(
        self,
        company_id: float,
        *,
        search_term: str | None = None,
        max_count: float | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[GoodsSearchResponse200DataTypesDataItem]:
        """Пример запроса на получение списка
        ### Список товаров и товарных категорий
        Список **товаров и товарных категорий** можно получить, сделав запрос с указанием идентификатора филиала.
        Список можно отфильтровать по названию или артикулу категории товаров, по названию, артикулу или штрихкоду товара, передав параметр `search_term`.
        Количество результатов ограничивается параметром `max_count`.
        Если `search_term` не передан, выводится список корневых категорий филиала без учета `max_count`. Если `search_term` передан, сначала производится поиск по категориям, затем (если найдено меньше, чем `max_count`) - по товарам
        Список представляет собой массив [элементов дерева товаров](#good-category-tree-node).
        <a name="good-category-tree-node"></a>
        **Элемент дерева товаров** имеет следующую структуру:
        | Поле          | Тип     | Описание                                                                                    |
        | --------------| ------- | ------------------------------------------------------------------------------------------- |
        |  parent_id    | number  | Идентификатор родительского элемента (0 для корневых элементов)                             |
        |  item_id      | number  | Идентификатор товара (0, если элемент - категория)                                          |
        |  category_id  | number  | Идентификатор товарной категории (0, если элемент - товар)                                  |
        """
        return await self._client.request(
            "GET",
            "/api/v1/goods/search/{company_id}",
            path_params={"company_id": company_id},
            params={"search_term": search_term, "max_count": max_count},
            response_model=builtins.list[GoodsSearchResponse200DataTypesDataItem],
            extra_query=extra_query,
        )

    async def get_category_node(
        self,
        company_id: float,
        category_id: float,
        *,
        page_: float | None = None,
        count_: float | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> GoodsCategoryNodeResponse200DataTypesData:
        """Пример запроса на получение состава категории
        ##№ Состав товарной категории
        Информацию по товарной категории и ее потомкам можно получить, сделав запрос с указанием идентификатора филиала и товарной категории.
        Поддерживается постраничный вывод, задаваемый параметрами `page` и `count`.
        **Состав товарной категории** имеет следующую структуру:
        | Поле            | Тип     | Описание                                                                                            |
        | ----------------| ------- | --------------------------------------------------------------------------------------------------- |
        |  parent_id      | number  | Идентификатор родительского элемента (0 для корневых элементов)                                     |
        |  item_id        | number  | Идентификатор товара (всегда 0)                                                                     |
        |  category_id    | number  | Идентификатор товарной категории                                                                    |
        |  title          | string  | Название товарной категории                                                                         |
        |  is_chain       | boolean | Является ли элемент привязанным к сети? true - элемент привязан к сети, false - не привязан         |
        |  is_category    | boolean | Является ли элемент категорией? всегда true                                                         |
        |  is_item        | boolean | Является ли элемент товаром? всегда false                                                           |
        """
        return await self._client.request(
            "GET",
            "/api/v1/goods/category_node/{company_id}/{category_id}",
            path_params={"company_id": company_id, "category_id": category_id},
            params={"page": page_, "count": count_},
            response_model=GoodsCategoryNodeResponse200DataTypesData,
            extra_query=extra_query,
        )

    async def list(
        self,
        company_id: float,
        parent_category_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[GoodsCategoriesResponse200DataTypesDataItem]:
        """Получить список категорий товаров
        """
        return await self._client.request(
            "GET",
            "/api/v1/goods_categories/{company_id}/{parent_category_id}",
            path_params={"company_id": company_id, "parent_category_id": parent_category_id},
            response_model=builtins.list[GoodsCategoriesResponse200DataTypesDataItem],
            extra_query=extra_query,
        )

    async def list_multiple(
        self,
        company_id: float,
        *,
        id_: float | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[GoodsCategoriesResponse200DataTypesDataItem]:
        """Получить список категорий товаров по идентификатору
        """
        return await self._client.request(
            "GET",
            "/api/v1/goods_categories/multiple/{company_id}",
            path_params={"company_id": company_id},
            params={"id": id_},
            response_model=builtins.list[GoodsCategoriesResponse200DataTypesDataItem],
            extra_query=extra_query,
        )

    async def list_by_company(
        self,
        company_id: float,
        parent_category_id: float,
        *,
        accept: str | None = None,
        content_type: str | None = None,
        authorization: str | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[GoodsCategoriesResponse200DataTypesDataItem]:
        """Пример запроса на получение категорий
        """
        return await self._client.request(
            "GET",
            "/api/v1/company/{company_id}/goods_categories/{parent_category_id}",
            path_params={"company_id": company_id, "parent_category_id": parent_category_id},
            params={"Accept": accept, "Content-Type": content_type, "Authorization": authorization},
            response_model=builtins.list[GoodsCategoriesResponse200DataTypesDataItem],
            extra_query=extra_query,
        )

    async def create(
        self,
        company_id: float,
        data: GoodsCategoriesRequestDataTypes,
        extra_query: dict[str, Any] | None = None
    ) -> GoodsCategoriesPostPutResponseDataTypesData:
        """Создать категорию товаров
        Метод позволяет создать категорию товаров.
        """
        return await self._client.request(
            "POST",
            "/api/v1/goods_categories/{company_id}",
            path_params={"company_id": company_id},
            json_body=data,
            response_model=GoodsCategoriesPostPutResponseDataTypesData,
            extra_query=extra_query,
        )

    async def update(
        self,
        company_id: float,
        category_id: float,
        data: GoodsCategoriesRequestDataTypes,
        extra_query: dict[str, Any] | None = None
    ) -> GoodsCategoriesPostPutResponseDataTypesData:
        """Редактировать категорию товаров
        Метод позволяет отредактировать категорию товаров
        """
        return await self._client.request(
            "PUT",
            "/api/v1/goods_categories/{company_id}/{category_id}",
            path_params={"company_id": company_id, "category_id": category_id},
            json_body=data,
            response_model=GoodsCategoriesPostPutResponseDataTypesData,
            extra_query=extra_query,
        )

    async def delete(
        self,
        company_id: float,
        category_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Удалить категорию товаров
        Метод позволяет удалить категорию товаров
        """
        return await self._client.request(
            "DELETE",
            "/api/v1/goods_categories/{company_id}/{category_id}",
            path_params={"company_id": company_id, "category_id": category_id},
            extra_query=extra_query,
        )
