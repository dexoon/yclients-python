"""FiscalizationApi -- сгенерированные методы API."""

from __future__ import annotations

from typing import Any

from yclients._base import BaseClient
from yclients.models.schemas import TaxSystemResponseDataTypes2


class FiscalizationApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def get(
        self,
        country_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> TaxSystemResponseDataTypes2:
        """Пример запроса на получение списка
        Список доступных для страны **систем налогообложения** и **НДС** можно получить, сделав запрос с указанием идентификатора страны, для которой необходимо получить список.
        Идентификатор страны можно получить из [списка стран](#countries).
        Список представляет собой массив [систем налогообложения](#fiscalization-tax) со вложенным массивом [НДС](#fiscalization-vat) для каждой системы налогообложения.
        **Cистема налогообложения** имеет следующую структуру:
        | Поле             | Тип              | Описание                 |
        | -----------------| ---------------- | ------------------------ |
        |  title           | string           | Название системы налогообложения |
        |  slug            | string           | Кодовое название системы налогообложения |
        |  vats            | Array of objects([Vat](#fiscalization-vat)[]) | Список доступных НДС для системы налогообложения |
        <a name="fiscalization-vat"></a>
        **НДС** имеет следующую структуру:
        | Поле             | Тип              | Описание                 |
        | -----------------| ---------------- | ------------------------ |
        """
        return await self._client.request(
            "GET",
            "/api/v1/integration/kkm/references/tax_system/{countryId}",
            path_params={"countryId": country_id},
            response_model=TaxSystemResponseDataTypes2,
            extra_query=extra_query,
        )

    async def callback(
        self,
        data: dict[str, Any],
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Пример запроса в случае успешной фискализации или в случае ошибка
        """
        return await self._client.request(
            "POST",
            "/api/v1/integration/kkm/callback/",
            json_body=data,
            extra_query=extra_query,
        )
