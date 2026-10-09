"""VoipApi -- сгенерированные методы API."""

from __future__ import annotations

from typing import Any

from yclients._base import BaseClient
from yclients.models.schemas import (
    GetIntegrationCallsRequest,
    GetIntegrationCallsResponse200DataItem,
    VoipIntegrationDisableRequestDataTypes,
    VoipIntegrationEnableRequestDataTypes,
    VoipIntegrationHistoryRequestDataTypes,
    VoipIntegrationNotificationRequestDataTypes,
)


class VoipApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def create_integration(
        self,
        data: VoipIntegrationEnableRequestDataTypes | VoipIntegrationDisableRequestDataTypes | VoipIntegrationHistoryRequestDataTypes | VoipIntegrationNotificationRequestDataTypes,
        extra_query: dict[str, Any] | None = None
    ) -> str:
        """События телефонии
        #### Подключить интеграцию
        Для использования api и активации доступа к настройкам в пользовательском интерфейсе необходимо активировать интеграцию, отправив запрос "Подключить интеграцию". После успешного подключения, в сетевом интерфейсе пользователя будет открыт доступ в раздел с настройками маршрутизации.
        #### Отключить интеграция
        Для отключения интеграции можно воспользоваться методом "Отключить интеграцию". После отключения интеграции закрывается доступ в раздел настроек пользовательского интерфейса, обработка запросов "Уведомление о звонке" и "Сохранение информации о звонке" не производится.
        #### Уведомление о звонке
        Для отображения уведомлений о входящем звонке используется метод "Уведомление о звонке", в параметрах указыватеся тип звонка ("incoming", "outgoing", "internal"), но на текущий момент уведомления отображаются только для значения "incoming". Уведомления отображаются для пользователей, определенных на основе настроек маршрутизации. При одновременном указании параметров "user" и "diversion" приоритетным при поиске маршрутов является "user".
        #### Сохранение информации о звонке
        Сохранение информации о звонке автоматически происходит в сетевую историю и в историю компаний сети в соответствии с настройками маршрутизации звонка.
        """
        return await self._client.request(
            "POST",
            "/api/v1/voip/integration",
            json_body=data,
            response_model=str,
            extra_query=extra_query,
        )

    async def list_calls(
        self,
        data: GetIntegrationCallsRequest,
        extra_query: dict[str, Any] | None = None
    ) -> list[GetIntegrationCallsResponse200DataItem]:
        """Получить список звонков филиала
        Данный эндпойнт предназначен для получения списка звонков в филиале с учетом фильтров и с пагинацией
        """
        return await self._client.request(
            "GET",
            "/api/v1/voip/integration/calls",
            json_body=data,
            response_model=list[GetIntegrationCallsResponse200DataItem],
            extra_query=extra_query,
        )
