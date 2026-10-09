"""ReviewsApi -- сгенерированные методы API."""

from __future__ import annotations

from typing import Any

from yclients._base import BaseClient
from yclients.models.schemas import MasterRecordReviewPostRequest


class ReviewsApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def get(
        self,
        record_token: str,
        extra_query: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Получение статуса формы отзыва
        """
        return await self._client.request(
            "GET",
            "/api/v1/master_record_review/{recordToken}",
            path_params={"recordToken": record_token},
            response_model=dict[str, Any],
            extra_query=extra_query,
        )

    async def submit_review(
        self,
        record_token: str,
        data: MasterRecordReviewPostRequest,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Отправка формы отзыва
        """
        return await self._client.request(
            "POST",
            "/api/v1/master_record_review/{recordToken}",
            path_params={"recordToken": record_token},
            json_body=data,
            extra_query=extra_query,
        )
