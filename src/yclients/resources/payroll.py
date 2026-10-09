"""PayrollApi -- сгенерированные методы API."""

from __future__ import annotations

from typing import Any

from yclients._base import BaseClient
from yclients.models.common import Page
from yclients.models.schemas import (
    SalaryStaffCalculation,
    SalaryStaffCalculationDaily,
    SalaryStaffPeriodDaily,
    SalaryStaffScheme,
    SalaryStaffSchemesCount,
)


class PayrollApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def list_payroll_charges(
        self,
        company_id: float,
        staff_id: float,
        *,
        date_from: str | None = None,
        date_to: str | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> Page[SalaryStaffCalculation]:
        """Поиск начислений по сотруднику
        Метод позволяет владельцу получить список начислений зарплаты по сотруднику.
        """
        return await self._client.request(
            "GET",
            "/api/v1/company/{company_id}/salary/payroll/staff/{staff_id}/calculation/",
            path_params={"company_id": company_id, "staff_id": staff_id},
            params={"date_from": date_from, "date_to": date_to},
            response_model=Page[SalaryStaffCalculation],
            extra_query=extra_query,
        )

    async def get_payroll_charge(
        self,
        company_id: float,
        staff_id: float,
        calculation_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Получение данных о начислении по сотруднику
        Метод позволяет владельцу получить подробную информацию о конкретном начислении зарплаты.
        """
        return await self._client.request(
            "GET",
            "/api/v1/company/{company_id}/salary/payroll/staff/{staff_id}/calculation/{calculation_id}",
            path_params={"company_id": company_id, "staff_id": staff_id, "calculation_id": calculation_id},
            extra_query=extra_query,
        )

    async def get_salary_schemes_count(
        self,
        company_id: float,
        staff_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> SalaryStaffSchemesCount:
        """Получение количества схем расчёта зарплат у сотрудника
        Метод позволяет получить количество схем расчёта зарплат по сотруднику перед тем, как запрашивать данные о суммах.
        """
        return await self._client.request(
            "GET",
            "/api/v1/company/{company_id}/salary/calculation/staff/{staff_id}/salary_schemes_count/",
            path_params={"company_id": company_id, "staff_id": staff_id},
            response_model=SalaryStaffSchemesCount,
            extra_query=extra_query,
        )

    async def get_settlements(
        self,
        company_id: float,
        staff_id: float,
        *,
        date_from: str | None = None,
        date_to: str | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> SalaryStaffCalculation:
        """Получение взаиморасчётов с сотрудником
        Метод позволяет владельцу получить взаиморасчёты с сотрудником.
        """
        return await self._client.request(
            "GET",
            "/api/v1/company/{company_id}/salary/calculation/staff/{staff_id}/",
            path_params={"company_id": company_id, "staff_id": staff_id},
            params={"date_from": date_from, "date_to": date_to},
            response_model=SalaryStaffCalculation,
            extra_query=extra_query,
        )

    async def get_daily_settlements(
        self,
        company_id: float,
        staff_id: float,
        *,
        date_from: str | None = None,
        date_to: str | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> SalaryStaffCalculationDaily:
        """Получение взаиморасчётов с сотрудником в разрезе по дате
        Метод позволяет владельцу получить взаиморасчёты с сотрудником с группировкой по дате.
        """
        return await self._client.request(
            "GET",
            "/api/v1/company/{company_id}/salary/calculation/staff/daily/{staff_id}/",
            path_params={"company_id": company_id, "staff_id": staff_id},
            params={"date_from": date_from, "date_to": date_to},
            response_model=SalaryStaffCalculationDaily,
            extra_query=extra_query,
        )

    async def get_period_payroll(
        self,
        company_id: float,
        staff_id: float,
        *,
        date_from: str | None = None,
        date_to: str | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> SalaryStaffCalculation:
        """Получение расчёта зарплаты за период по сотруднику
        Метод позволяет владельцу получить расчёт зарплаты за период по сотруднику.
        """
        return await self._client.request(
            "GET",
            "/api/v1/company/{company_id}/salary/period/staff/{staff_id}/",
            path_params={"company_id": company_id, "staff_id": staff_id},
            params={"date_from": date_from, "date_to": date_to},
            response_model=SalaryStaffCalculation,
            extra_query=extra_query,
        )

    async def get_daily_period_payroll(
        self,
        company_id: float,
        staff_id: float,
        *,
        date_from: str | None = None,
        date_to: str | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> SalaryStaffPeriodDaily:
        """Получение расчёта зарплаты за период по сотруднику в разрезе по дате
        Метод позволяет владельцу получить расчёт зарплаты за период по сотруднику с группировкой по дате.
        """
        return await self._client.request(
            "GET",
            "/api/v1/company/{company_id}/salary/period/staff/daily/{staff_id}/",
            path_params={"company_id": company_id, "staff_id": staff_id},
            params={"date_from": date_from, "date_to": date_to},
            response_model=SalaryStaffPeriodDaily,
            extra_query=extra_query,
        )

    async def get_own_settlements(
        self,
        company_id: float,
        staff_id: float,
        *,
        date_from: str | None = None,
        date_to: str | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> SalaryStaffCalculation:
        """Получение собственных взаиморасчётов сотрудника с филиалом
        Метод позволяет получить собственные взаиморасчёты сотрудника с филиалом. В правах доступа пользователя должна быть указана галочка "Доступ к расчёту заработной платы только конкретного сотрудника".
        """
        return await self._client.request(
            "GET",
            "/api/v1/company/{company_id}/salary/staff/{staff_id}/calculation/",
            path_params={"company_id": company_id, "staff_id": staff_id},
            params={"date_from": date_from, "date_to": date_to},
            response_model=SalaryStaffCalculation,
            extra_query=extra_query,
        )

    async def list_own_salary_schemes(
        self,
        company_id: float,
        staff_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> Page[SalaryStaffScheme]:
        """Получение собственных схем расчёта зарплат
        Метод позволяет получить собственные схемы расчёта зарплат.
        В правах доступа пользователя должна быть указана галочка "Доступ к расчёту заработной платы только конкретного сотрудника".
        """
        return await self._client.request(
            "GET",
            "/api/v1/company/{company_id}/salary/staff/{staff_id}/salary_schemes/",
            path_params={"company_id": company_id, "staff_id": staff_id},
            response_model=Page[SalaryStaffScheme],
            extra_query=extra_query,
        )

    async def get_own_period_payroll(
        self,
        company_id: float,
        staff_id: float,
        *,
        date_from: str | None = None,
        date_to: str | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> Any:
        """Получение расчёта собственной зарплаты за период
        Метод позволяет получить расчёт собственной зарплаты за период.
        В правах доступа пользователя должна быть указана галочка "Доступ к расчёту заработной платы только конкретного сотрудника".
        """
        return await self._client.request(
            "GET",
            "/api/v1/company/{company_id}/salary/staff/{staff_id}/period/",
            path_params={"company_id": company_id, "staff_id": staff_id},
            params={"date_from": date_from, "date_to": date_to},
            extra_query=extra_query,
        )
