"""ClientsApi -- сгенерированные методы API."""

from __future__ import annotations

import builtins
from typing import Any

from yclients._base import BaseClient
from yclients.models.common import Page
from yclients.models.schemas import (
    ClientCommentContainer,
    ClientVisitsHistory,
    CompanyCompanyidClientsSearchRequestDataTypes,
    PostClientIdCommentsRequest,
    PostVisitsSearchRequest,
)


class ClientsApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def search(
        self,
        company_id: float,
        data: CompanyCompanyidClientsSearchRequestDataTypes,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[dict[str, Any]]:
        """Получить список клиентов
        """
        return await self._client.request(
            "POST",
            "/api/v1/company/{company_id}/clients/search",
            path_params={"company_id": company_id},
            json_body=data,
            response_model=builtins.list[dict[str, Any]],
            extra_query=extra_query,
        )

    async def list(
        self,
        company_id: float,
        *,
        fullname: str | None = None,
        phone: str | None = None,
        email: str | None = None,
        paid_min: float | None = None,
        paid_max: float | None = None,
        page_: float | None = None,
        count_: float | None = None,
        id_: float | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[dict[str, Any]]:
        """Устаревшее. Получить список клиентов
        + Параметр
        + company_id (required, number, `1`) - ID компании
        + page (number, `1`) - Номер страницы
        + count (number, `20`) - Количество клиентов на странице
        #### Фильтрация клиентов
        + fullname:Joh (optional, string) - Имя (часть имени) для фильтрации клиентов
        + phone:7916 (optional, string) - Телефон (часть номера) для фильтрации клиентов
        + email:test@ (optional, string) - Email (часть) для фильтрации клиентов
        + card:5663rt (optional, string) - Card (часть) для фильтрации клиентов по номеру карты лояльности
        + paid_min:100 (optional, number) - Минимально оплачено в кассу, для фильтрации клиентов по сумме оплат
        + paid_max:0 (optional, number) - Максимально оплачено в кассу, для фильтрации клиентов по сумме оплат
        + paid_max:0 (optional, number) - Максимально оплачено в кассу, для фильтрации клиентов по сумме оплат
        + id:66 (optional, number) - ID одного клиента для фильтрации клиентов
        """
        return await self._client.request(
            "GET",
            "/api/v1/clients/{company_id}",
            path_params={"company_id": company_id},
            params={"fullname": fullname, "phone": phone, "email": email, "paid_min": paid_min, "paid_max": paid_max, "page": page_, "count": count_, "id": id_},
            response_model=builtins.list[dict[str, Any]],
            extra_query=extra_query,
        )

    async def create(
        self,
        company_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Добавить клиента
        """
        return await self._client.request(
            "POST",
            "/api/v1/clients/{company_id}",
            path_params={"company_id": company_id},
            extra_query=extra_query,
        )

    async def bulk(
        self,
        company_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Массовое добавление клиентов
        """
        return await self._client.request(
            "POST",
            "/api/v1/clients/{company_id}/bulk",
            path_params={"company_id": company_id},
            extra_query=extra_query,
        )

    async def list_files(
        self,
        company_id: float,
        client_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> builtins.list[dict[str, Any]]:
        """Пример запроса на получение списка файлов клиента
        Список загруженных **файлов клиента** можно получить, сделав запрос с указанием идентификатора филиала и идентификатора клиента, для которого необходимо получить список.
        Идентификатор клиента можно получить из коллекции клиентов.
        Список представляет собой массив [файлов клиента](#client-file).
        <a name="client-file"></a>
        **Файл клиента** имеет следующую структуру:
        | Поле             | Тип     | Описание                                                                    |
        | -----------------| ------- | --------------------------------------------------------------------------- |
        |  id              | number  | Идентификатор файла                                                         |
        |  client_id       | number  | Идентификатор клиента                                                       |
        |  name            | string  | Имя файла с расширением                                                     |
        |  description     | string  | Описание файла                                                              |
        |  extension       | string  | Расширение имени файла                                                      |
        |  mime            | string  | MIME-тип файла                                                              |
        """
        return await self._client.request(
            "GET",
            "/api/v1/company/{company_id}/clients/files/{client_id}",
            path_params={"company_id": company_id, "client_id": client_id},
            response_model=builtins.list[dict[str, Any]],
            extra_query=extra_query,
        )

    async def delete_file(
        self,
        company_id: float,
        client_id: float,
        file_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Пример запроса на удаление
        """
        return await self._client.request(
            "DELETE",
            "/api/v1/company/{company_id}/clients/files/{client_id}/{file_id}",
            path_params={"company_id": company_id, "client_id": client_id, "file_id": file_id},
            extra_query=extra_query,
        )

    async def search_visits(
        self,
        company_id: float,
        data: PostVisitsSearchRequest,
        extra_query: dict[str, Any] | None = None
    ) -> ClientVisitsHistory:
        """Поиск по истории посещений клиента
        Выводит записи из истории посещений клиента по его идентификатору или номеру телефона. В ответ попадают записи и
        продажи товаров, объединенные по визитам, отфильтрованные по статусу посещения и статусу оплаты визита. Результат
        сортируется по дате и разбивается на страницы по 25 элементов (или более, если дата последней записи совпадает с
        датой следующей записи). Идентификация клиента происходит по входному параметру `client_id` либо по `client_phone`.
        Остальные параметры могут иметь пустое значение.
        Для получения данных на следующей странице необходимо выполнить запрос с параметрами `from` и `to`,
        полученными в результате текущего запроса в поле `meta`.
        """
        return await self._client.request(
            "POST",
            "/api/v1/company/{company_id}/clients/visits/search",
            path_params={"company_id": company_id},
            json_body=data,
            response_model=ClientVisitsHistory,
            extra_query=extra_query,
        )

    async def get(
        self,
        company_id: float,
        id_: float,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Получить клиента
        """
        return await self._client.request(
            "GET",
            "/api/v1/client/{company_id}/{id}",
            path_params={"company_id": company_id, "id": id_},
            extra_query=extra_query,
        )

    async def update(
        self,
        company_id: float,
        id_: float,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Редактировать клиента
        """
        return await self._client.request(
            "PUT",
            "/api/v1/client/{company_id}/{id}",
            path_params={"company_id": company_id, "id": id_},
            extra_query=extra_query,
        )

    async def delete(
        self,
        company_id: float,
        id_: float,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Удалить клиента
        """
        return await self._client.request(
            "DELETE",
            "/api/v1/client/{company_id}/{id}",
            path_params={"company_id": company_id, "id": id_},
            extra_query=extra_query,
        )

    async def list_comments(
        self,
        company_id: float,
        client_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> Page[ClientCommentContainer]:
        """Получение списка комментариев к клиенту
        Возвращает список комментариев к клиенту, а также историю загрузки файлов в карточку клиента в виде комментариев.
        """
        return await self._client.request(
            "GET",
            "/api/v1/company/{company_id}/clients/{client_id}/comments",
            path_params={"company_id": company_id, "client_id": client_id},
            response_model=Page[ClientCommentContainer],
            extra_query=extra_query,
        )

    async def create_comment(
        self,
        company_id: float,
        client_id: float,
        data: PostClientIdCommentsRequest,
        extra_query: dict[str, Any] | None = None
    ) -> ClientCommentContainer:
        """Добавление комментария к клиенту
        Создает новый текстовый комментарий к клиенту.
        """
        return await self._client.request(
            "POST",
            "/api/v1/company/{company_id}/clients/{client_id}/comments",
            path_params={"company_id": company_id, "client_id": client_id},
            json_body=data,
            response_model=ClientCommentContainer,
            extra_query=extra_query,
        )

    async def delete_comments(
        self,
        company_id: float,
        client_id: float,
        comment_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Удаление комментария к клиенту
        Удаляет комментарий к клиенту; не удаляет загруженные в карточку клиента файлы, загрузка которых породила создание комментария.
        """
        return await self._client.request(
            "DELETE",
            "/api/v1/company/{company_id}/clients/{client_id}/comments/{comment_id}",
            path_params={"company_id": company_id, "client_id": client_id, "comment_id": comment_id},
            response_model=dict[str, Any],
            extra_query=extra_query,
        )
