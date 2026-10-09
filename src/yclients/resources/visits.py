"""VisitsApi -- сгенерированные методы API."""

from __future__ import annotations

from typing import Any

from yclients._base import BaseClient


class VisitsApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def get(
        self,
        visit_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Получить визит
        """
        return await self._client.request(
            "GET",
            "/api/v1/visits/{visit_id}",
            path_params={"visit_id": visit_id},
            response_model=dict[str, Any],
            extra_query=extra_query,
        )

    async def get_details(
        self,
        salon_id: float,
        record_id: float,
        visit_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Получить детали визита
        **Блок "kkm_transaction_details_container"**
        Флаг  "last_operation_type"
        | Значение  | Описание |
        | ------------- | ------------- |
        |  0  | Распечатать чек возврата |
        |  1  | Распечатать чек продажи |
        Типы всех операций c ККМ
        | Значение  | Описание |
        | ------------- | ------------- |
        |  0  | Операция продажи  (активна для документа с типом "Визит") |
        |  1  | Операция возврата продажи (активна для документа с типом "Визит") |
        |  2  | Операция коррекции |
        |  4  | Операция открытия смены |
        """
        return await self._client.request(
            "GET",
            "/api/v1/visit/details/{salon_id}/{record_id}/{visit_id}",
            path_params={"salon_id": salon_id, "record_id": record_id, "visit_id": visit_id},
            response_model=dict[str, Any],
            extra_query=extra_query,
        )

    async def update(
        self,
        visit_id: float,
        record_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Изменить визит
        """
        return await self._client.request(
            "PUT",
            "/api/v1/visits/{visit_id}/{record_id}",
            path_params={"visit_id": visit_id, "record_id": record_id},
            extra_query=extra_query,
        )

    async def get_receipt_pdf(
        self,
        visit_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Чек PDF по визиту
        """
        return await self._client.request(
            "GET",
            "/api/v1/attendance/receipt_print/{visit_id}",
            path_params={"visit_id": visit_id},
            extra_query=extra_query,
        )
