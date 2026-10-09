"""MarketplaceApi -- сгенерированные методы API."""

from __future__ import annotations

from typing import Any

from yclients._base import BaseClient
from yclients.models.schemas import (
    GetApplicationApplicationIdResponse200Data,
    GetApplicationIdTariffsResponse200DataItem,
    GetApplicationPaymentLinkResponse200Data,
    PostApplicationAddDiscountRequest,
    PostApplicationUpdateChannelRequest,
    PostCallbackRedirectRequest,
    PostMarketplaceWebhookRequest,
    PostPartnerCallbackRequest,
    PostPartnerPaymentRequest,
    PostPartnerPaymentResponse200Data,
    PostPartnerShortNamesRequest,
)


class MarketplaceApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def redirect(
        self,
        data: PostCallbackRedirectRequest,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Адрес для редиректа пользователя после регистрации в сервисе-партнере
        На этот адрес необходимо перенаправить пользователя в браузере после прохождения регистрации с данными, которые необходимы сервису-партнеру
        """
        return await self._client.request(
            "POST",
            "/marketplace/partner/callback/redirect",
            json_body=data,
            extra_query=extra_query,
        )

    async def callback(
        self,
        data: PostPartnerCallbackRequest,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Установка приложения для филиала
        На этот адрес необходимо направить настройки интеграции сервиса-партнера, после чего будет произведена настройка и установка приложения в филиале
        """
        return await self._client.request(
            "POST",
            "/marketplace/partner/callback",
            json_body=data,
            extra_query=extra_query,
        )

    async def payment(
        self,
        data: PostPartnerPaymentRequest,
        extra_query: dict[str, Any] | None = None
    ) -> PostPartnerPaymentResponse200Data:
        """Уведомление YCLIENTS об успешном платеже
        На данный адрес необходимо присылать webhook-уведомление об успешной оплате услуг на стороне сервиса-партнера
        """
        return await self._client.request(
            "POST",
            "/marketplace/partner/payment",
            json_body=data,
            response_model=PostPartnerPaymentResponse200Data,
            extra_query=extra_query,
        )

    async def create_short_name(
        self,
        data: PostPartnerShortNamesRequest,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Оповещение YCLIENTS о доступных именах отправителя SMS-сообщений
        Этот адрес предназначен для отправки в YCLIENTS доступных пользователю именах отправителя SMS-сообщений. Пользователь будет иметь возможность выбрать любое доступное из переданных
        """
        return await self._client.request(
            "POST",
            "/marketplace/partner/short_names",
            json_body=data,
            extra_query=extra_query,
        )

    async def create_refund(
        self,
        payment_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Уведомление о возврате платежа
        Адрес предназначен для уведомления YCLIENTS о возврате платежа
        """
        return await self._client.request(
            "POST",
            "/marketplace/partner/payment/refund/{payment_id}",
            path_params={"payment_id": payment_id},
            extra_query=extra_query,
        )

    async def create_webhook(
        self,
        data: PostMarketplaceWebhookRequest,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Вебхук из YCLIENTS о событиях
        Это не действующий эндпойнт.
        Здесь описывается отправка вебхуков из YCLIENTS при возникновении определенных событий в процессе жизненного цикла "приложение - салон".
        В данный момент доступны события к получению:
        * uninstall - событие отправляется при отключении приложения на стороне YCLIENTS.
        * freeze - событие отправляется при заморозке интеграции вследствие экспирации.
        Настроить адрес для получения вебхуков можно в личном кабинете разработчика YCLIENTS.
        """
        return await self._client.request(
            "POST",
            "/marketplace_webhook",
            json_body=data,
            extra_query=extra_query,
        )

    async def get(
        self,
        salon_id: float,
        application_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> GetApplicationApplicationIdResponse200Data:
        """Данные о подключении приложения в салоне
        Данный эндпойнт предназначен для получения информации об установке приложения в конкретном салоне.
        """
        return await self._client.request(
            "GET",
            "/marketplace/salon/{salon_id}/application/{application_id}",
            path_params={"salon_id": salon_id, "application_id": application_id},
            response_model=GetApplicationApplicationIdResponse200Data,
            extra_query=extra_query,
        )

    async def list_salons(
        self,
        application_id: float,
        *,
        page_: float | None = None,
        count_: float | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> list[dict[str, Any]]:
        """Данные о салонах, подключивших приложение
        Данный эндпойнт предназначен для получения списка салонов, которые подключили некоторое приложение, с подробной информацией о них
        """
        return await self._client.request(
            "GET",
            "/marketplace/application/{application_id}/salons",
            path_params={"application_id": application_id},
            params={"page": page_, "count": count_},
            response_model=list[dict[str, Any]],
            extra_query=extra_query,
        )

    async def uninstall(
        self,
        salon_id: float,
        application_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Отключение приложения
        Данный эндпойнт предназначен для инициирования отключения приложения со стороны партнера.
        """
        return await self._client.request(
            "POST",
            "/marketplace/salon/{salon_id}/application/{application_id}/uninstall",
            path_params={"salon_id": salon_id, "application_id": application_id},
            response_model=dict[str, Any],
            extra_query=extra_query,
        )

    async def get_payment_link(
        self,
        *,
        salon_id: float | None = None,
        application_id: float | None = None,
        discount: float | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> GetApplicationPaymentLinkResponse200Data:
        """Генерация ссылки на оплату
        Эндпойнт предназначен для генерации ссылки на оплату приложения через YCLIENTS
        """
        return await self._client.request(
            "GET",
            "/marketplace/application/payment_link",
            params={"salon_id": salon_id, "application_id": application_id, "discount": discount},
            response_model=GetApplicationPaymentLinkResponse200Data,
            extra_query=extra_query,
        )

    async def list_tariffs(
        self,
        application_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> list[GetApplicationIdTariffsResponse200DataItem]:
        """Данные о тарифах приложения
        Данный эндпойнт предназначен для получения списка тарифов.
        """
        return await self._client.request(
            "GET",
            "/marketplace/application/{application_id}/tariffs",
            path_params={"application_id": application_id},
            response_model=list[GetApplicationIdTariffsResponse200DataItem],
            extra_query=extra_query,
        )

    async def add_discount(
        self,
        data: PostApplicationAddDiscountRequest,
        extra_query: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Установить скидку салонам на оплату
        Данный эндпойнт предназначен для установки скидки при оплате через YCLIENTS определенным салонам
        """
        return await self._client.request(
            "POST",
            "/marketplace/application/add_discount",
            json_body=data,
            response_model=dict[str, Any],
            extra_query=extra_query,
        )

    async def update_channel(
        self,
        data: PostApplicationUpdateChannelRequest,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Изменение доступности каналов отправки
        Только для приложений из категории Чат-Боты и СМС-агрегаторы. Позволяет изменить доступные каналы отправки уведомлений для приложения.
        """
        return await self._client.request(
            "POST",
            "/marketplace/application/update_channel",
            json_body=data,
            extra_query=extra_query,
        )
