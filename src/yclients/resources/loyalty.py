"""LoyaltyApi -- сгенерированные методы API."""

from __future__ import annotations

from typing import Any, Literal

from yclients._base import BaseClient
from yclients.models.schemas import (
    CompanyAnalyticsLoyaltyProgramsIncomeDataTypesData,
    CompanyAnalyticsLoyaltyProgramsStaffDataTypesDataItem,
    CompanyAnalyticsLoyaltyProgramsVisitsDataTypesData,
    CompanyLoyaltyProgramsSearchDataTypesDataItem,
    LoyaltyAbonementsTypeSearchResponseDataTypesDataItem,
    LoyaltyCertificateTypeSearchResponseDataTypesDataItem,
    LoyaltyGenerateCode200DataOption2,
    LoyaltyNotificationMessageTemplate2,
    LoyaltyProgram2,
    LoyaltyTransaction2,
)


class LoyaltyApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def list_programs(
        self,
        chain_id: int,
        extra_query: dict[str, Any] | None = None
    ) -> list[LoyaltyNotificationMessageTemplate2]:
        """Получить список шаблонов уведомлений лояльности
        """
        return await self._client.request(
            "GET",
            "/api/v1/chain/{chain_id}/loyalty/notification_message_templates/programs",
            path_params={"chain_id": chain_id},
            response_model=list[LoyaltyNotificationMessageTemplate2],
            extra_query=extra_query,
        )

    async def create_program(
        self,
        chain_id: int,
        data: dict[str, Any],
        *,
        include: str | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> LoyaltyProgram2:
        """Создать акцию в сети
        """
        return await self._client.request(
            "POST",
            "/api/v1/chain/{chain_id}/loyalty/programs/",
            path_params={"chain_id": chain_id},
            params={"include": include},
            json_body=data,
            response_model=LoyaltyProgram2,
            extra_query=extra_query,
        )

    async def get(
        self,
        chain_id: int,
        loyalty_program_id: int,
        *,
        include: str | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> LoyaltyProgram2:
        """Получить акцию в сети
        """
        return await self._client.request(
            "GET",
            "/api/v1/chain/{chain_id}/loyalty/programs/{loyalty_program_id}",
            path_params={"chain_id": chain_id, "loyalty_program_id": loyalty_program_id},
            params={"include": include},
            response_model=LoyaltyProgram2,
            extra_query=extra_query,
        )

    async def update(
        self,
        chain_id: int,
        loyalty_program_id: int,
        data: dict[str, Any],
        *,
        include: str | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> LoyaltyProgram2:
        """Изменить акцию в сети
        """
        return await self._client.request(
            "PUT",
            "/api/v1/chain/{chain_id}/loyalty/programs/{loyalty_program_id}",
            path_params={"chain_id": chain_id, "loyalty_program_id": loyalty_program_id},
            params={"include": include},
            json_body=data,
            response_model=LoyaltyProgram2,
            extra_query=extra_query,
        )

    async def delete(
        self,
        chain_id: int,
        loyalty_program_id: int,
        *,
        include: str | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Удалить акцию в сети
        """
        return await self._client.request(
            "DELETE",
            "/api/v1/chain/{chain_id}/loyalty/programs/{loyalty_program_id}",
            path_params={"chain_id": chain_id, "loyalty_program_id": loyalty_program_id},
            params={"include": include},
            extra_query=extra_query,
        )

    async def get_transactions(
        self,
        chain_id: int,
        *,
        created_after: str | None = None,
        created_before: str | None = None,
        types: list[Literal["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]] | None = None,
        company_ids: list[int] | None = None,
        visit_ids: list[int] | None = None,
        loyalty_card_id: int | None = None,
        page_: int | None = None,
        count_: int | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> LoyaltyTransaction2:
        """Получить список транзакций лояльности в сети
        """
        return await self._client.request(
            "GET",
            "/api/v1/chain/{chain_id}/loyalty/transactions",
            path_params={"chain_id": chain_id},
            params={"created_after": created_after, "created_before": created_before, "types": types, "company_ids": company_ids, "visit_ids": visit_ids, "loyalty_card_id": loyalty_card_id, "page": page_, "count": count_},
            response_model=LoyaltyTransaction2,
            extra_query=extra_query,
        )

    async def generate_code(
        self,
        company_id: float,
        good_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> LoyaltyGenerateCode200DataOption2:
        """Генерация кода сертификата/абонемента
        + Параметры
        + salonId (required, number, `1`) - ID салона
        + goodId (required, number, `1`) - ID товара (сертификат/абонемент)
        """
        return await self._client.request(
            "GET",
            "/api/v1/loyalty/generate_code/{company_id}/{good_Id}",
            path_params={"company_id": company_id, "good_Id": good_id},
            response_model=LoyaltyGenerateCode200DataOption2,
            extra_query=extra_query,
        )

    async def search(
        self,
        company_id: float,
        *,
        title: str | None = None,
        page_: float | None = None,
        page_size: float | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> list[LoyaltyAbonementsTypeSearchResponseDataTypesDataItem]:
        """Получить список доступных типов абонементов
        Список **типов абонементов**, доступных в филиале, можно получить, сделав запрос с указанием идентификатора филиала.
        Список можно отфильтровать по названию типа абонемента, передав параметр `title`.
        Поддерживается постраничный вывод, задаваемый параметрами `page` и `page_size`.
        Список представляет собой массив [типов абонементов](#loyalty-abonement-type).
        <a name="loyalty-abonement-type"></a>
        **Тип абонемента** имеет следующую структуру:
        | Поле                           | Тип     | Описание                                                                                                                         |
        | -------------------------------| ------- | -------------------------------------------------------------------------------------------------------------------------------- |
        |  id                            | number  | Идентификатор типа абонемента                                                                                                    |
        |  title                         | string  | Название типа абонемента                                                                                                         |
        |  allow_freeze                  | boolean | Допускается ли заморозка абонементов? true - допускается, false - не допускается                                                 |
        |  freeze_limit                  | number  | Максимальный общий период заморозки (дни)                                                                                        |
        |  salon_group_id                | number  | Идентификатор сети, в которой действует тип абонемента                                                                           |
        """
        return await self._client.request(
            "GET",
            "/api/v1/company/{company_id}/loyalty/abonement_types/search",
            path_params={"company_id": company_id},
            params={"title": title, "page": page_, "page_size": page_size},
            response_model=list[LoyaltyAbonementsTypeSearchResponseDataTypesDataItem],
            extra_query=extra_query,
        )

    async def fetch_abonement_types(
        self,
        company_id: float,
        *,
        ids: float | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> list[LoyaltyAbonementsTypeSearchResponseDataTypesDataItem]:
        """Получить список типов абонементов по идентификатору
        Список **типов абонементов**, доступных в филиале, можно получить, сделав запрос с указанием идентификатора филиала и идентификаторов типов абонементов.
        Список представляет собой массив [типов абонементов](#loyalty-abonement-type).
        ### Получить список типов абонементов по идентификатору
        + Parameters
        + company_id (required, number) - ID компании
        + id: 1 (optional, number) - ID типа абонемента (можно указать несколько дополнительными параметрами `&ids[]={id}`
        """
        return await self._client.request(
            "GET",
            "/api/v1/company/{company_id}/loyalty/abonement_types/fetch",
            path_params={"company_id": company_id},
            params={"ids[]": ids},
            response_model=list[LoyaltyAbonementsTypeSearchResponseDataTypesDataItem],
            extra_query=extra_query,
        )

    async def search_certificate_types(
        self,
        company_id: float,
        *,
        title: str | None = None,
        page_: float | None = None,
        page_size: float | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> list[LoyaltyCertificateTypeSearchResponseDataTypesDataItem]:
        """Получить список доступных типов сертификатов
        Список **типов сертификатов**, доступных в филиале, можно получить, сделав запрос с указанием идентификатора филиала.
        Список можно отфильтровать по названию типа сертификата, передав параметр `title`.
        Поддерживается постраничный вывод, задаваемый параметрами `page` и `page_size`.
        Список представляет собой массив [типов сертификатов](#loyalty-certificate-type).
        <a name="loyalty-certificate-type"></a>
        **Тип сертификата** имеет следующую структуру:
        | Поле                        | Тип     | Описание                                                                                                                                              |
        | ----------------------------| ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
        |  id                         | number  | Идентификатор типа сертификата                                                                                                                        |
        |  title                      | string  | Название типа сертификата                                                                                                                             |
        |  balance                    | number  | Номинал сертификата                                                                                                                                   |
        |  is_multi                   | boolean | Тип списания: true - многократное списание, false - однократное списание                                                                              |
        |  company_group_id           | number  | Идентификатор сети, в которой действует тип сертификата                                                                                               |
        """
        return await self._client.request(
            "GET",
            "/api/v1/company/{company_id}/loyalty/certificate_types/search",
            path_params={"company_id": company_id},
            params={"title": title, "page": page_, "page_size": page_size},
            response_model=list[LoyaltyCertificateTypeSearchResponseDataTypesDataItem],
            extra_query=extra_query,
        )

    async def fetch_certificate_types(
        self,
        company_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> list[LoyaltyCertificateTypeSearchResponseDataTypesDataItem]:
        """Получить список типов сертификатов по идентификатору
        Список **типов сертификатов**, доступных в филиале, можно получить, сделав запрос с указанием идентификатора филиала и идентификаторов типов сертификатов.
        Список представляет собой массив [типов сертификатов](#loyalty-certificate-type).
        """
        return await self._client.request(
            "GET",
            "/api/v1/company/{company_id}/loyalty/certificate_types/fetch",
            path_params={"company_id": company_id},
            response_model=list[LoyaltyCertificateTypeSearchResponseDataTypesDataItem],
            extra_query=extra_query,
        )

    async def search_programs(
        self,
        company_id: float,
        *,
        include: str | None = None,
        type_: str | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> list[CompanyLoyaltyProgramsSearchDataTypesDataItem]:
        """Получить список акций, действующих в филиале
        Метод позволяет получить список акций, которые активны для указанного филиала.
        """
        return await self._client.request(
            "GET",
            "/api/v1/company/{company_id}/loyalty/programs/search",
            path_params={"company_id": company_id},
            params={"include": include, "type": type_},
            response_model=list[CompanyLoyaltyProgramsSearchDataTypesDataItem],
            extra_query=extra_query,
        )

    async def get_visits(
        self,
        company_id: float,
        *,
        date_to: str | None = None,
        date_from: str | None = None,
        loyalty_program_id: str | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> CompanyAnalyticsLoyaltyProgramsVisitsDataTypesData:
        """Получить статистику по клиентам
        Метод позволяет получить статистику по вернувшимся, новым и потерянным клиентам
        """
        return await self._client.request(
            "GET",
            "/api/v1/company/{company_id}/analytics/loyalty_programs/visits",
            path_params={"company_id": company_id},
            params={"date_to": date_to, "date_from": date_from, "loyalty_program_id": loyalty_program_id},
            response_model=CompanyAnalyticsLoyaltyProgramsVisitsDataTypesData,
            extra_query=extra_query,
        )

    async def get_income(
        self,
        company_id: float,
        *,
        date_to: str | None = None,
        date_from: str | None = None,
        loyalty_program_id: str | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> CompanyAnalyticsLoyaltyProgramsIncomeDataTypesData:
        """Получить статистику по выручке
        Метод позволяет получить статистику по выручке.
        """
        return await self._client.request(
            "GET",
            "/api/v1/company/{company_id}/analytics/loyalty_programs/income/",
            path_params={"company_id": company_id},
            params={"date_to": date_to, "date_from": date_from, "loyalty_program_id": loyalty_program_id},
            response_model=CompanyAnalyticsLoyaltyProgramsIncomeDataTypesData,
            extra_query=extra_query,
        )

    async def list_staff(
        self,
        company_id: float,
        *,
        date_to: str | None = None,
        date_from: str | None = None,
        loyalty_program_id: str | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> list[CompanyAnalyticsLoyaltyProgramsStaffDataTypesDataItem]:
        """Получить возвращаемость по сотруднику
        Метод позволяет получить статистику возвращаемости по сотруднику
        """
        return await self._client.request(
            "GET",
            "/api/v1/company/{company_id}/analytics/loyalty_programs/staff/",
            path_params={"company_id": company_id},
            params={"date_to": date_to, "date_from": date_from, "loyalty_program_id": loyalty_program_id},
            response_model=list[CompanyAnalyticsLoyaltyProgramsStaffDataTypesDataItem],
            extra_query=extra_query,
        )
