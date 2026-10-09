"""BookingApi -- сгенерированные методы API."""

from __future__ import annotations

from typing import Any

from yclients._base import BaseClient
from yclients.models.schemas import (
    ActivityCompanyidActivityidBookResponseDataTypesData,
    BookCheckCompanyidRequestDataTypes,
    BookCheckCompanyidResponse201DataTypes,
    BookCodeCompanyidDataTypeResponse,
    BookCodeCompanyidDataTypesRequest,
    BookDatesCompanyidDataTypesData,
    BookformIdInfoDataTypesData,
    BookRecordCompanyidRecordidRecordhashResponseDataTypes,
    BookRecordCompanyidRecordRequestDataTypes,
    BookRecordCompanyidRecordResponseDataTypesData,
    BookRecordCompanyidRequestDataTypes,
    BookRecordCompanyidResponseDataTypesDataItem,
    BookServicesCompanyidDataTypesData,
    BookStaffCompanyidDataTypesDataItem,
    BookStaffSeancesCompanyidStaffidDataTypesData,
    BookTimesCompanyidDataTypesDataItem,
    GetSettingsTimeslotsResponse200Data,
    I18nLangInfoDataTypes,
)


class BookingApi:
    """Сгенерированные методы домена."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    async def get(
        self,
        id_: float,
        extra_query: dict[str, Any] | None = None
    ) -> BookformIdInfoDataTypesData:
        """Получить настройки формы бронирования
        Каждый клиент сервиса YCLIENTS, может создать неограниченное количество форм онлайн-записи с разным дизайном и для разных сценариев записи.
        Обычно, id формы бронирования хранится в поддомене, например: https://w123.yclients.ru, где 123 - id формы записи. С помощью этого параметра можно получить все остальные необходимые для реализации онлайн-записи параметры, понять, будет происходить запись в конкретную компанию или в сеть компаний.
        Для сетевого виджета необходимо будет дополнительно обратится к методу [GET] /companies с фильтром company_id и получить список копаний, в которые будет производиться запись.
        Объект содержащий настройки формы бронирование имеет следующие поля:
        | Поле | Тип | Описание |
        | ------------- | ------------- | ------------- |
        | steps  | Массив объектов  | Шаги формы бронирования со своими настройками  |
        | style  | Object  | Настройки дизайна формы бронирования  |
        | group_id  | number  | Идентификатор сети компаний (0 - если форма записи для несетевой компании)  |
        | company_id  | number  | Идентификатор компании (возвращается всегда, используется для получения дополнительных настроек) |
        | phone_confirmation  | boolean  | Нужно ли подтверждать телефон по смс (если groupid = 0 (не групповая форма), иначе смотреть в настройки каждой компании отдельно)
        | lang  | string  | Язык формы бронирования (код из массива langs)  |
        | langs  | array of object  | Список языков виджета
        """
        return await self._client.request(
            "GET",
            "/api/v1/bookform/{id}",
            path_params={"id": id_},
            response_model=BookformIdInfoDataTypesData,
            extra_query=extra_query,
        )

    async def get_i18n(
        self,
        lang_code: str,
        extra_query: dict[str, Any] | None = None
    ) -> I18nLangInfoDataTypes:
        """Получить параметры интернационализации
        Перевод доступен на один из языков:
        - Русский - 'ru-RU'
        - Латвийский - 'lv-LV'
        - Английский - 'en-US'
        - Эстонский - 'ee-EE'
        - Литовский - 'lt-LT'
        - Немецкий - 'de-DE'
        - Украинский - 'uk-UK'
        """
        return await self._client.request(
            "GET",
            "/api/v1/i18n/{langCode}",
            path_params={"langCode": lang_code},
            response_model=I18nLangInfoDataTypes,
            extra_query=extra_query,
        )

    async def send_code(
        self,
        company_id: float,
        data: BookCodeCompanyidDataTypesRequest,
        extra_query: dict[str, Any] | None = None
    ) -> BookCodeCompanyidDataTypeResponse:
        """Отправить СМС код подтверждения номера телефона
        + Тело запроса
        + phone (required, string, '79991234567') - телефон, на который будет отправлен код
        + fullname (option, sring, `Вася`) - Имя клиента
        """
        return await self._client.request(
            "POST",
            "/api/v1/book_code/{company_id}",
            path_params={"company_id": company_id},
            json_body=data,
            response_model=BookCodeCompanyidDataTypeResponse,
            extra_query=extra_query,
        )

    async def check(
        self,
        company_id: float,
        data: BookCheckCompanyidRequestDataTypes,
        extra_query: dict[str, Any] | None = None
    ) -> BookCheckCompanyidResponse201DataTypes:
        """Проверить параметры записи
        После формирования параметров записи(ей) можно проверить их на возможность создание записей.
        JSON-Объект содержащий параметры онлайн записи имеет следующие поля:
        | Поле | Тип | Обязательный | Описание |
        | ------------- | ------------- | ------------- | ------------- |
        | appointments  | Массив объектов  |  ДА  | Параметры записи (услуги, специалисты...) |
        Массив appointments состоит из объектов, которые имеют следующие поля:
        | Поле | Тип | Обязательный | Описание |
        | ------------- | ------------- | ------------- | ------------- |
        | id  | number  |  Да  | Идентификатор записи для обратной связи после сохранения (смотри ответ на запрос).
        | services  | array of numbers  | НЕТ  |  Массив идентификаторов услуг, на которые клиент хочет записаться |
        | staff_id  | number  |  ДА  | Идентификатор специалиста, к которому клиент хочет записаться (0 если выбран любой мастер)  |
        | datetime  | datetime  |  ДА  | Дата и время сеанса в формате ISO8601 (передается для каждого сеанса в ресурсе book_times)|
        В ответ на запрос проверки параметров придет пустой ответ с кодом 201 если параметры записи в порядке и записи могут быть созданы:
        """
        return await self._client.request(
            "POST",
            "/api/v1/book_check/{company_id}",
            path_params={"company_id": company_id},
            json_body=data,
            response_model=BookCheckCompanyidResponse201DataTypes,
            extra_query=extra_query,
        )

    async def create(
        self,
        company_id: float,
        data: BookRecordCompanyidRequestDataTypes,
        extra_query: dict[str, Any] | None = None
    ) -> list[BookRecordCompanyidResponseDataTypesDataItem]:
        """Создать запись на сеанс
        JSON-Объект содержащий параметры онлайн записи имеет следующие поля:
        | Поле | Тип | Обязательный | Описание |
        | ------------- | ------------- | ------------- | ------------- |
        | phone  | string  | ДА  |  Телефон клиента (например 79161502239)  |
        | fullname  | string  |  ДА  | Имя клиента  |
        | email  | string  |  ДА  | Почтовый адрес клиента  |
        | appointments  | Массив объектов  |  ДА  | Параметры записи (услуги, специалисты...) |
        | code  | string  |  НЕТ  |  Код подтверждения номера телефона, высланный по СМС (нужен только в случае необходимости подтверждения номера)  |
        | notify_by_sms  | number  |  НЕТ  |  За какое кол-во часов отправить смс напоминание о записи (0 если не нужно напоминать)  |
        | notify_by_email  | number  |  НЕТ  |  За какое кол-во часов отправить email напоминание о записи (0 если не нужно напоминать)  |
        | comment  | string  |  НЕТ  | Комментарий к записи  |
        | api_id  | string  |  НЕТ  | Внешний идентификатор записи  |
        | custom_fields | key-value object | НЕТ | Значения дополнительных полей карточки клиента, которые сохраняются вместе с записью |
        """
        return await self._client.request(
            "POST",
            "/api/v1/book_record/{company_id}",
            path_params={"company_id": company_id},
            json_body=data,
            response_model=list[BookRecordCompanyidResponseDataTypesDataItem],
            extra_query=extra_query,
        )

    async def update(
        self,
        company_id: float,
        record_id: float,
        data: BookRecordCompanyidRecordRequestDataTypes,
        extra_query: dict[str, Any] | None = None
    ) -> BookRecordCompanyidRecordResponseDataTypesData:
        """Перенести запись на сеанс
        """
        return await self._client.request(
            "PUT",
            "/api/v1/book_record/{company_id}/{record_id}",
            path_params={"company_id": company_id, "record_id": record_id},
            json_body=data,
            response_model=BookRecordCompanyidRecordResponseDataTypesData,
            extra_query=extra_query,
        )

    async def get_record(
        self,
        company_id: float,
        record_id: float,
        record_hash: str,
        extra_query: dict[str, Any] | None = None
    ) -> BookRecordCompanyidRecordidRecordhashResponseDataTypes:
        """Получить запись на сеанс
        """
        return await self._client.request(
            "GET",
            "/api/v1/book_record/{company_id}/{record_id}/{record_hash}",
            path_params={"company_id": company_id, "record_id": record_id, "record_hash": record_hash},
            response_model=BookRecordCompanyidRecordidRecordhashResponseDataTypes,
            extra_query=extra_query,
        )

    async def book(
        self,
        company_id: float,
        activity_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> ActivityCompanyidActivityidBookResponseDataTypesData:
        """Создать запись в групповом событии
        """
        return await self._client.request(
            "POST",
            "/api/v1/activity/{company_id}/{activity_id}/book",
            path_params={"company_id": company_id, "activity_id": activity_id},
            response_model=ActivityCompanyidActivityidBookResponseDataTypesData,
            extra_query=extra_query,
        )

    async def get_book_dates(
        self,
        company_id: float,
        *,
        service_ids: list[float] | None = None,
        staff_id: float | None = None,
        date: str | None = None,
        date_from: str | None = None,
        date_to: str | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> BookDatesCompanyidDataTypesData:
        """Получить список дат доступных для бронирования
        Объект даты, доступные для бронирования имеет следующие поля:
        | Поле  | Тип | Описание |
        | ------------- | ------------- | ------------- |
        |  working_days  |  массив рабочих дней сгруппированных по месяцам   | Рабочие дни сотрудника/организации  |
        |  working_dates  | array of dates  | Массив дат, когда работает сотрудник/организация  |
        |  booking_days  |  массив дней, когда есть свободные сеансы  | Массив дней, которые доступны для бронирования на указанные услуги   |
        |  booking_dates  | array of dates  | Массив дат, когда есть свободные сеансы на услугу к выбранному сотруднику/организации   |
        working days и booking_days имеют одинаковый формат:
        месяц:[массив дней в этом месяце]
        Например такой booking_days:
        "9": [
        "4",
        "5"]
        """
        return await self._client.request(
            "GET",
            "/api/v1/book_dates/{company_id}",
            path_params={"company_id": company_id},
            params={"service_ids": service_ids, "staff_id": staff_id, "date": date, "date_from": date_from, "date_to": date_to},
            response_model=BookDatesCompanyidDataTypesData,
            extra_query=extra_query,
        )

    async def get_book_services(
        self,
        company_id: float,
        *,
        staff_id: float | None = None,
        datetime: float | None = None,
        service_ids: list[float] | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> BookServicesCompanyidDataTypesData:
        """Получить список услуг доступных для бронирования
        Объект услуг, доступных для бронирования имеет следующие поля:
        | Поле  | Тип | Описание |
        | ------------- | ------------- | ------------- |
        |  categories  | массив объектов  | Массив категорий услуг (забронировать категорию нельзя)  |
        |  services  | массив объектов  | Услуги, доступные для бронирования, с указанием категории  |
        Объект из массива categories, имеет следующие поля:
        | Поле  | Тип | Описание |
        | ------------- | ------------- | ------------- |
        |  id  |  number  |  Идентификатор категории  |
        |  title  | string  |  Название категории  |
        |  sex  | number  |  Принадлежность категории к полу (1 - мужской, 2 - женский, 0 - не задано)  |
        |  weight  | number  |  Вес категории. При выводе категории сортируются по весу, сначала более тяжелые  |
        |  api_id  | string  |  Внешний идентификатор категории  |
        """
        return await self._client.request(
            "GET",
            "/api/v1/book_services/{company_id}",
            path_params={"company_id": company_id},
            params={"staff_id": staff_id, "datetime": datetime, "service_ids": service_ids},
            response_model=BookServicesCompanyidDataTypesData,
            extra_query=extra_query,
        )

    async def list_seances(
        self,
        company_id: float,
        staff_id: float,
        *,
        service_ids: list[float] | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> BookStaffSeancesCompanyidStaffidDataTypesData:
        """Получить список ближайших доступных сеансов
        Объект ближайших сеансов сотрудника имеет следующие поля:
        | Поле | Тип | Описание |
        | ------------- | ------------- | ------------- |
        |  seance_date  |  string   | Ближайшая дата с доступными сеансами   |
        |  seances  | Array  | Список доступных сеансов  |
        """
        return await self._client.request(
            "GET",
            "/api/v1/book_staff_seances/{company_id}/{staff_id}/",
            path_params={"company_id": company_id, "staff_id": staff_id},
            params={"service_ids": service_ids},
            response_model=BookStaffSeancesCompanyidStaffidDataTypesData,
            extra_query=extra_query,
        )

    async def list_staff(
        self,
        company_id: float,
        *,
        service_ids: list[float] | None = None,
        datetime: float | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> list[BookStaffCompanyidDataTypesDataItem]:
        """Получить список сотрудников доступных для бронирования
        Каждый объект из массива сотрудников, доступных для бронирования имеет следующие поля:
        | Поле  | Тип | Описание |
        | ------------- | ------------- | ------------- |
        |  id  |  number  |  Идентификатор сотрудника  |
        |  name  | string  |  Имя сотрудника  |
        |  specialization  | string  |  Специализация сотрудника  |
        |  position  | object  |  Должность сотрудника  |
        |  bookable  | boolean  |  Есть ли у сотрудника сеансы, доступные для бронирования  |
        |  weight  | number  |  Вес сотрудника. При выводе сотрудники сортируются по весу, сначала более тяжелые  |
        |  show_rating  | number  |  Показывать ли рейтинг сотрудника (1 - показывать, 0 - не показывать)  |
        |  rating  | number  |  Рейтинг сотрудника  |
        |  votes_count  | number  |  Кол-во голосов, оценивших сотрудника  |
        |  comments_count  | number  |  Кол-во комментариев к сотруднику  |
        """
        return await self._client.request(
            "GET",
            "/api/v1/book_staff/{company_id}",
            path_params={"company_id": company_id},
            params={"service_ids": service_ids, "datetime": datetime},
            response_model=list[BookStaffCompanyidDataTypesDataItem],
            extra_query=extra_query,
        )

    async def list_times(
        self,
        company_id: float,
        staff_id: float,
        date: str,
        *,
        service_ids: list[float] | None = None,
        extra_query: dict[str, Any] | None = None
    ) -> list[BookTimesCompanyidDataTypesDataItem]:
        """Получить список сеансов доступных для бронирования
        Объект сеансы, доступные для бронирования имеет следующие поля:
        | Поле  | Тип | Описание |
        | ------------- | ------------- | ------------- |
        |  time  |  string   | Время сеанса (17:30 например)   |
        |  seance_length  | number  | Длительность сеанса в секундах  |
        |  datetime  |  datetime  | Дата и время сеанса в формате ISO8601 (нужно передавать при создании записи)   |
        Доступны следующие фильтры:
        + service_ids: Массив ID услуг. Если нужны сеансы, когда можно забронировать указанные услуги
        """
        return await self._client.request(
            "GET",
            "/api/v1/book_times/{company_id}/{staff_id}/{date}",
            path_params={"company_id": company_id, "staff_id": staff_id, "date": date},
            params={"service_ids": service_ids},
            response_model=list[BookTimesCompanyidDataTypesDataItem],
            extra_query=extra_query,
        )

    async def get_timeslots(
        self,
        company_id: float,
        extra_query: dict[str, Any] | None = None
    ) -> GetSettingsTimeslotsResponse200Data:
        """Получить настройки таймслотов филиала
        Получение настроек таймслотов филиала. Интервалы слотов указываются в секундах, в ответе возвращаются настройки по каждому дню недели.
        """
        return await self._client.request(
            "GET",
            "/api/v1/company/{company_id}/settings/timeslots",
            path_params={"company_id": company_id},
            response_model=GetSettingsTimeslotsResponse200Data,
            extra_query=extra_query,
        )
