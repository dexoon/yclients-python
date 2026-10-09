"""UserRecordsApi -- сгенерированные методы API."""

from __future__ import annotations

from typing import Any

from yclients._base import BaseClient


class UserRecordsApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def get(
        self,
        record_id: str,
        record_hash: str,
        extra_query: dict[str, Any] | None = None
    ) -> list[dict[str, Any]]:
        """Получить записи пользователя
        JSON-Объект содержащий параметры записи пользователя имеет следующие поля:
        | Поле | Тип | Обязательный | Описание |
        | ------------- | ------------- | ------------- | ------------- |
        | id  | number  | ДА  |  ID записи  |
        | services  | array of numbers  |  ДА  | Список ID услуг записи  |
        | company  | object  |  ДА  | Параметры компании  |
        | staff  | object  |  ДА  | Параметры специалиста, которые был забронирован |
        | clients_count  | int  |  ДА  |  Количество клиентов  |
        | date  | string  |  ДА  |  Дата сеанса  |
        | datetime  | string  |  ДА  |  Дата сеанса в формате |
        | create_date  | string  |  ДА  |  Дата создания записи  |
        | length  | number  |  ДА  | Длительность сеанса  |
        | deleted  | boolean  |  ДА  | Удалена ли запись (true если удалена)  |
        """
        return await self._client.request(
            "GET",
            "/api/v1/user/records/{record_id}/{record_hash}",
            path_params={"record_id": record_id, "record_hash": record_hash},
            response_model=list[dict[str, Any]],
            extra_query=extra_query,
        )

    async def delete(
        self,
        record_id: float,
        record_hash: str,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Удалить запись пользователя
        """
        return await self._client.request(
            "DELETE",
            "/api/v1/user/records/{record_id}/{record_hash}",
            path_params={"record_id": record_id, "record_hash": record_hash},
            extra_query=extra_query,
        )
