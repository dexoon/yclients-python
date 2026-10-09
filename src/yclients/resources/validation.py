"""ValidationApi -- сгенерированные методы API."""

from __future__ import annotations

from typing import Any

from yclients._base import BaseClient


class ValidationApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def validate_phone(
        self,
        phone: str,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Проверка формата номера телефона
        Происходит проверка переданного номера телефона на соответствие правилам YCLIENTS.
        """
        return await self._client.request(
            "GET",
            "/api/v1/validation/validate_phone/{phone}",
            path_params={"phone": phone},
            extra_query=extra_query,
        )
