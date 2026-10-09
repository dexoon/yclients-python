"""Авторизация пользователя и запись клиента.

Запуск:
    PARTNER_TOKEN=... LOGIN=... PASSWORD=... .venv/bin/python examples/login.py
"""

import asyncio
import os

from yclients import YclientsClient, YclientsValidationError

PARTNER_TOKEN = os.environ["PARTNER_TOKEN"]
LOGIN = os.environ["LOGIN"]
PASSWORD = os.environ["PASSWORD"]


async def main() -> None:
    async with YclientsClient(PARTNER_TOKEN) as client:
        # login() авторизует пользователя и сохранит его User-токен в клиенте
        user = await client.login(LOGIN, PASSWORD)
        print(f"Привет, {user.name} (user_token: {user.user_token[:8]}...)")

        # теперь доступны пользовательские методы
        companies = await client.companies.list(my=1)
        if not companies:
            return
        company_id = companies[0]["id"]

        # пример обработки ошибки валидации
        try:
            await client.clients.create(company_id)
        except YclientsValidationError as exc:
            print(f"Ожидаемая ошибка валидации: {exc.errors}")


if __name__ == "__main__":
    asyncio.run(main())
