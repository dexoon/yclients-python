"""Базовый пример: компании и клиенты.

Запуск:
    PARTNER_TOKEN=... USER_TOKEN=... .venv/bin/python examples/basic.py
"""

import asyncio
import os

from yclients import YclientsApiError, YclientsClient

PARTNER_TOKEN = os.environ["PARTNER_TOKEN"]
USER_TOKEN = os.environ.get("USER_TOKEN")


async def main() -> None:
    async with YclientsClient(PARTNER_TOKEN, USER_TOKEN) as client:
        # список моих компаний
        companies = await client.companies.list(my=1)
        for company in companies[:5]:
            print(f"{company['id']}: {company.get('title')}")

        if not companies:
            return

        company_id = companies[0]["id"]

        # клиенты компании (параметры count/page у этого эндпоинта с суффиксом _)
        clients_list = await client.clients.list(company_id, count_=5, page_=1)
        print(f"Получено клиентов: {len(clients_list)}")

        # услуги компании
        services = await client.services.list(company_id)
        print(f"Услуг: {len(services)}")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except YclientsApiError as exc:
        print(f"Ошибка API: {exc}")
