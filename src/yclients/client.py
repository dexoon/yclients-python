"""Фасад клиента YCLIENTS API (генерируется scripts/generate.py)."""

from __future__ import annotations

from typing import Any

import httpx

from ._base import DEFAULT_BASE_URL, DEFAULT_TIMEOUT, BaseClient
from .models.schemas import AuthRequest2
from .resources.abonement_types import AbonementTypesApi
from .resources.abonements import AbonementsApi
from .resources.accounts import AccountsApi
from .resources.activities import ActivitiesApi
from .resources.activities_v2 import ActivitiesV2Api
from .resources.analytics import AnalyticsApi
from .resources.auth import AuthApi
from .resources.booking import BookingApi
from .resources.booking_forms import BookingFormsApi
from .resources.booking_users import BookingUsersApi
from .resources.certificates import CertificatesApi
from .resources.chain_clients import ChainClientsApi
from .resources.chains import ChainsApi
from .resources.cities import CitiesApi
from .resources.clients import ClientsApi
from .resources.comments import CommentsApi
from .resources.companies import CompaniesApi
from .resources.company_users import CompanyUsersApi
from .resources.countries import CountriesApi
from .resources.custom_fields import CustomFieldsApi
from .resources.deposits import DepositsApi
from .resources.email import EmailApi
from .resources.finance_transactions import FinanceTransactionsApi
from .resources.fiscalization import FiscalizationApi
from .resources.goods import GoodsApi
from .resources.goods_categories import GoodsCategoriesApi
from .resources.goods_transactions import GoodsTransactionsApi
from .resources.images import ImagesApi
from .resources.kkm_transactions import KkmTransactionsApi
from .resources.labels import LabelsApi
from .resources.licenses import LicensesApi
from .resources.loyalty import LoyaltyApi
from .resources.loyalty_cards import LoyaltyCardsApi
from .resources.marketplace import MarketplaceApi
from .resources.notifications import NotificationsApi
from .resources.online_settings import OnlineSettingsApi
from .resources.payroll import PayrollApi
from .resources.positions import PositionsApi
from .resources.privacy_policy import PrivacyPolicyApi
from .resources.records import RecordsApi
from .resources.references import ReferencesApi
from .resources.reports import ReportsApi
from .resources.resources import ResourcesApi
from .resources.reviews import ReviewsApi
from .resources.sales import SalesApi
from .resources.schedules import SchedulesApi
from .resources.service_categories import ServiceCategoriesApi
from .resources.services import ServicesApi
from .resources.sms import SmsApi
from .resources.sms_delivery import SmsDeliveryApi
from .resources.staff import StaffApi
from .resources.staff_schedule import StaffScheduleApi
from .resources.storage_documents import StorageDocumentsApi
from .resources.storage_operations import StorageOperationsApi
from .resources.storages import StoragesApi
from .resources.technological_cards import TechnologicalCardsApi
from .resources.timetable_dates import TimetableDatesApi
from .resources.timetable_seances import TimetableSeancesApi
from .resources.timetable_settings import TimetableSettingsApi
from .resources.tips import TipsApi
from .resources.user import UserApi
from .resources.user_records import UserRecordsApi
from .resources.users import UsersApi
from .resources.validation import ValidationApi
from .resources.visit_loyalty import VisitLoyaltyApi
from .resources.visits import VisitsApi
from .resources.voip import VoipApi
from .resources.waiting_list import WaitingListApi

__all__ = [
    'AbonementTypesApi',
    'AbonementsApi',
    'AccountsApi',
    'ActivitiesApi',
    'ActivitiesV2Api',
    'AnalyticsApi',
    'AuthApi',
    'BookingApi',
    'BookingFormsApi',
    'BookingUsersApi',
    'CertificatesApi',
    'ChainClientsApi',
    'ChainsApi',
    'CitiesApi',
    'ClientsApi',
    'CommentsApi',
    'CompaniesApi',
    'CompanyUsersApi',
    'CountriesApi',
    'CustomFieldsApi',
    'DepositsApi',
    'EmailApi',
    'FinanceTransactionsApi',
    'FiscalizationApi',
    'GoodsApi',
    'GoodsCategoriesApi',
    'GoodsTransactionsApi',
    'ImagesApi',
    'KkmTransactionsApi',
    'LabelsApi',
    'LicensesApi',
    'LoyaltyApi',
    'LoyaltyCardsApi',
    'MarketplaceApi',
    'NotificationsApi',
    'OnlineSettingsApi',
    'PayrollApi',
    'PositionsApi',
    'PrivacyPolicyApi',
    'RecordsApi',
    'ReferencesApi',
    'ReportsApi',
    'ResourcesApi',
    'ReviewsApi',
    'SalesApi',
    'SchedulesApi',
    'ServiceCategoriesApi',
    'ServicesApi',
    'SmsApi',
    'SmsDeliveryApi',
    'StaffApi',
    'StaffScheduleApi',
    'StorageDocumentsApi',
    'StorageOperationsApi',
    'StoragesApi',
    'TechnologicalCardsApi',
    'TimetableDatesApi',
    'TimetableSeancesApi',
    'TimetableSettingsApi',
    'TipsApi',
    'UserApi',
    'UserRecordsApi',
    'UsersApi',
    'ValidationApi',
    'VisitLoyaltyApi',
    'VisitsApi',
    'VoipApi',
    'WaitingListApi',
    'YclientsClient',
]


class YclientsClient:
    """Асинхронный клиент YCLIENTS REST API.

    Атрибуты -- домены API: ``client.companies``, ``client.clients``,
    ``client.records`` и т.д.

    Пример:
        async with YclientsClient(partner_token="...") as client:
            companies = await client.companies.list(my=1)
    """

    def __init__(
        self,
        partner_token: str,
        user_token: str | None = None,
        *,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float = DEFAULT_TIMEOUT,
        headers: dict[str, str] | None = None,
        max_retries: int = 2,
        retry_backoff: float = 0.5,
        http_client: httpx.AsyncClient | None = None,
    ) -> None:
        self._base = BaseClient(
            partner_token,
            user_token,
            base_url=base_url,
            timeout=timeout,
            headers=headers,
            max_retries=max_retries,
            retry_backoff=retry_backoff,
            http_client=http_client,
        )
        self.abonement_types = AbonementTypesApi(self._base)
        self.abonements = AbonementsApi(self._base)
        self.accounts = AccountsApi(self._base)
        self.activities = ActivitiesApi(self._base)
        self.activities_v2 = ActivitiesV2Api(self._base)
        self.analytics = AnalyticsApi(self._base)
        self.auth = AuthApi(self._base)
        self.booking = BookingApi(self._base)
        self.booking_forms = BookingFormsApi(self._base)
        self.booking_users = BookingUsersApi(self._base)
        self.certificates = CertificatesApi(self._base)
        self.chain_clients = ChainClientsApi(self._base)
        self.chains = ChainsApi(self._base)
        self.cities = CitiesApi(self._base)
        self.clients = ClientsApi(self._base)
        self.comments = CommentsApi(self._base)
        self.companies = CompaniesApi(self._base)
        self.company_users = CompanyUsersApi(self._base)
        self.countries = CountriesApi(self._base)
        self.custom_fields = CustomFieldsApi(self._base)
        self.deposits = DepositsApi(self._base)
        self.email = EmailApi(self._base)
        self.finance_transactions = FinanceTransactionsApi(self._base)
        self.fiscalization = FiscalizationApi(self._base)
        self.goods = GoodsApi(self._base)
        self.goods_categories = GoodsCategoriesApi(self._base)
        self.goods_transactions = GoodsTransactionsApi(self._base)
        self.images = ImagesApi(self._base)
        self.kkm_transactions = KkmTransactionsApi(self._base)
        self.labels = LabelsApi(self._base)
        self.licenses = LicensesApi(self._base)
        self.loyalty = LoyaltyApi(self._base)
        self.loyalty_cards = LoyaltyCardsApi(self._base)
        self.marketplace = MarketplaceApi(self._base)
        self.notifications = NotificationsApi(self._base)
        self.online_settings = OnlineSettingsApi(self._base)
        self.payroll = PayrollApi(self._base)
        self.positions = PositionsApi(self._base)
        self.privacy_policy = PrivacyPolicyApi(self._base)
        self.records = RecordsApi(self._base)
        self.references = ReferencesApi(self._base)
        self.reports = ReportsApi(self._base)
        self.resources = ResourcesApi(self._base)
        self.reviews = ReviewsApi(self._base)
        self.sales = SalesApi(self._base)
        self.schedules = SchedulesApi(self._base)
        self.service_categories = ServiceCategoriesApi(self._base)
        self.services = ServicesApi(self._base)
        self.sms = SmsApi(self._base)
        self.sms_delivery = SmsDeliveryApi(self._base)
        self.staff = StaffApi(self._base)
        self.staff_schedule = StaffScheduleApi(self._base)
        self.storage_documents = StorageDocumentsApi(self._base)
        self.storage_operations = StorageOperationsApi(self._base)
        self.storages = StoragesApi(self._base)
        self.technological_cards = TechnologicalCardsApi(self._base)
        self.timetable_dates = TimetableDatesApi(self._base)
        self.timetable_seances = TimetableSeancesApi(self._base)
        self.timetable_settings = TimetableSettingsApi(self._base)
        self.tips = TipsApi(self._base)
        self.user = UserApi(self._base)
        self.user_records = UserRecordsApi(self._base)
        self.users = UsersApi(self._base)
        self.validation = ValidationApi(self._base)
        self.visit_loyalty = VisitLoyaltyApi(self._base)
        self.visits = VisitsApi(self._base)
        self.voip = VoipApi(self._base)
        self.waiting_list = WaitingListApi(self._base)

    async def aclose(self) -> None:
        """Закрывает HTTP-клиент."""
        await self._base.aclose()

    async def __aenter__(self) -> YclientsClient:
        return self

    async def __aexit__(self, *exc_info: object) -> None:
        await self.aclose()

    # -------------------------------------------------------------- auth

    @property
    def user_token(self) -> str | None:
        """Текущий User-токен (если авторизован)."""
        return self._base.user_token

    def set_user_token(self, user_token: str | None) -> None:
        """Задаёт User-токен вручную."""
        self._base.set_user_token(user_token)

    async def login(self, login: str, password: str) -> Any:
        """Авторизует пользователя и сохраняет его User-токен.

        При включённой 2FA вернёт ответ с необходимостью кода подтверждения --
        тогда повторите вызов с кодом через ``client.auth.login()`` и
        передайте полученный токен в ``client.set_user_token()``.
        """
        result = await self.auth.login(AuthRequest2(login=login, password=password))
        token = result.get('user_token') if isinstance(result, dict) else getattr(result, 'user_token', None)
        if token:
            self._base.set_user_token(token)
        return result
