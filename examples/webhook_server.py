"""Пример приёма webhook-уведомлений YCLIENTS.

Запускает локальный HTTP-сервер, разбирает входящие уведомления через
yclients.parse_webhook() и печатает события по записям и клиентам.

Запуск:
    .venv/bin/python examples/webhook_server.py
Затем укажите http://<ваш-адрес>:8080/webhooks как URL webhook в настройках
филиала YCLIENTS (или туннелируйте через ngrok/cloudflared для локальной отладки).
"""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer

from yclients import RecordWebhook, parse_webhook


class WebhookHandler(BaseHTTPRequestHandler):
    def do_post(self) -> None:
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length)

        try:
            event = parse_webhook(body)
        except Exception:  # некорректное тело -- отвечаем 400
            self.send_response(400)
            self.end_headers()
            return

        print(event.company_id, event.resource, event.status)
        match event.resource:
            case "record":
                assert isinstance(event, RecordWebhook)
                if event.data is not None:
                    print("  запись", event.resource_id, "комментарий:", event.data.comment)
            case "client":
                if event.data is not None:
                    print("  клиент", event.data.display_name, event.data.phone)
            case _:
                print("  ", json.dumps(event.model_dump(mode="json"), ensure_ascii=False))

        # YCLIENTS считает доставку успешной при любом HTTP-ответе,
        # но лучше отвечать 200 как можно раньше и обрабатывать асинхронно
        self.send_response(200)
        self.end_headers()


def main() -> None:
    server = HTTPServer(("0.0.0.0", 8080), WebhookHandler)
    print("Слушаю webhook-и на http://0.0.0.0:8080/webhooks")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()


if __name__ == "__main__":
    main()
