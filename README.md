# yclients-python

Асинхронный типизированный Python-клиент для [YCLIENTS REST API](https://developers.yclients.com/ru/).

Клиент сгенерирован из официальной OpenAPI-спеки: **303 операции**, **66 доменов**, ~900 pydantic-моделей
(включая вложенные структуры, вынесенные из inline-схем).

## Возможности

- Полностью асинхронный (`httpx.AsyncClient`), поддержка `async with`
- Типизированные методы для всех эндпоинтов API, типизированные ответы (pydantic v2)
- Авторизация Partner/User-токенами, встроенный `login()` c сохранением User-токена
- Разбор конверта `{success, data, meta}`: методы возвращают `data` уже провалидированной моделью
- Постраничные ответы через `Page[T]` (`data` + `count`)
- Иерархия исключений по HTTP-статусам: 401/403/404/422/429/5xx
- Автоматические повторные попытки на 429/502/503/504 (с учётом `Retry-After`)

## Установка

```bash
pip install yclients
```

Требуется Python 3.10+, `httpx`, `pydantic` — ставятся автоматически.

## Быстрый старт

```python
import asyncio

from yclients import YclientsClient


async def main() -> None:
    async with YclientsClient(partner_token="ВАШ_PARTNER_TOKEN") as client:
        # Список компаний (ответ -- list[Company] и т.п.)
        companies = await client.companies.list(my=1)
        for company in companies:
            print(company.id, company.title)

        # Авторизация пользователя: User-токен сохранится в клиенте
        me = await client.login("+79000000000", "password")
        print(me.name, me.email)

        # Клиенты компании, первая страница с количеством
        page = await client.clients.list(companies[0].id, page=1, count=20)
        print(page.count, len(page.data))


asyncio.run(main())
```

User-токен можно передать и сразу, без `login()`:

```python
client = YclientsClient(partner_token="...", user_token="...")
```

## Структура клиента

Домены API доступны как атрибуты клиента (соответствуют разделам документации):

| Атрибут | Домен |
|---|---|
| `client.auth` | Авторизация |
| `client.booking` | Онлайн-запись |
| `client.booking_users` | Пользователи онлайн-записи |
| `client.companies` | Компании |
| `client.services` / `client.service_categories` | Услуги и их категории |
| `client.staff` / `client.positions` | Сотрудники и должности |
| `client.clients` | Клиенты |
| `client.records` / `client.visits` | Записи и визиты |
| `client.activities` / `client.activities_v2` | Групповые события |
| `client.schedules` | Расписания записей/событий |
| `client.waiting_list` | Лист ожидания |
| `client.loyalty` / `client.loyalty_cards` | Лояльность и карты лояльности |
| `client.abonements` / `client.abonement_types` | Абонементы |
| `client.certificates` | Сертификаты |
| `client.goods` / `client.goods_categories` | Товары |
| `client.storage_operations` / `client.storages` | Склад |
| `client.finance_transactions` / `client.sales` | Финансы |
| `client.payroll` | Расчёт зарплат |
| `client.analytics` / `client.reports` | Аналитика |
| `client.sms` / `client.email` / `client.sms_delivery` | Рассылки |
| `client.marketplace` | Маркетплейс |
| ... | полный список в `yclients/resources/__init__.py` |

Примеры методов:

```python
await client.companies.get(company_id)             # GET  /company/{id}
await client.companies.create(CompanyCreateRequest(title="Салон", country_id=1))
await client.staff.list(company_id)                # GET  /staff/{company_id}
await client.clients.search(company_id, full_name="Иван")
await client.records.list(company_id, start_date="2026-01-01", end_date="2026-01-31")
await client.activities.book(company_id, activity_id, ...)   # запись на групповое событие
```

## Обработка ошибок

```python
from yclients import (
    YclientsApiError,
    YclientsAuthError,
    YclientsNotFoundError,
    YclientsRateLimitError,
    YclientsValidationError,
)

try:
    company = await client.companies.get(12345)
except YclientsNotFoundError as e:
    print("не найдена:", e.message)
except YclientsValidationError as e:
    print("ошибки валидации:", e.errors)
except YclientsAuthError:
    print("неверный partner/user токен")
except YclientsApiError as e:
    print("ошибка API:", e.status_code, e.message, e.meta)
```

Конверт ответа `{success: false}` превращается в исключение независимо от HTTP-статуса.
`meta` и полное тело ответа доступны в атрибутах `meta` и `body` исключения.

## Лимиты

YCLIENTS ограничивает **200 запросов в минуту (5 в секунду) на IP**. При получении 429
клиент автоматически повторяет запрос (по умолчанию до 2 раз, с учётом `Retry-After`).
Настройка: `YclientsClient(..., max_retries=3, retry_backoff=0.5)`.

## Кастомизация HTTP

```python
import httpx

http = httpx.AsyncClient(
    base_url="https://api.yclients.ru",
    proxy="http://localhost:8080",
)
client = YclientsClient(partner_token="...", http_client=http)
```

## Перегенерация кода

Клиент генерируется из спеки `docs/openapi.json` (извлечена с developers.yclients.com):

```bash
python scripts/generate.py
```

Ручные правки в `src/yclients/models/schemas/`, `src/yclients/resources/*` и
`src/yclients/client.py` будут потеряны -- правьте генератор.

## Примеры

В каталоге [`examples/`](examples/) -- рабочие скрипты: список компаний и клиентов
([basic.py](examples/basic.py)), авторизация и обработка ошибок валидации
([login.py](examples/login.py)).

```bash
PARTNER_TOKEN=... USER_TOKEN=... .venv/bin/python examples/basic.py
```

## Разработка

```bash
python -m venv .venv && .venv/bin/pip install -e '.[dev]'
.venv/bin/ruff check src tests scripts examples
.venv/bin/mypy
.venv/bin/pytest
```

## Примечания

- Спека YCLIENTS местами неточна (нетипизированные поля `Any`, дубли имён параметров) --
  в спорных местах клиент возвращает `dict[str, Any]`, а для неописанных полей моделей
  включён режим `extra="allow"`, так что данные из API не теряются.
- `docs/openapi.json` -- копия официальной спеки с https://developers.yclients.com/ru/
