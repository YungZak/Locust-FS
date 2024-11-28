import json
from locust import HttpUser, task, between, events
import time
import logging

logger = logging.getLogger("locust")

total_bytes_sent = 0
total_bytes_received = 0
start_time = time.time()


# Подсчет трафика
@events.request.add_listener
def track_traffic(
    request_type, name, response_time, response_length, exception, context, **kwargs
):
    global total_bytes_sent, total_bytes_received, start_time
    # Учитываем размер отправленных данных
    if context and "request_size" in context:
        total_bytes_sent += context["request_size"]

    # Учитываем размер полученных данных
    if response_length:
        total_bytes_received += response_length

    # Печатаем данные каждую секунду
    elapsed_time = time.time() - start_time
    if elapsed_time >= 1:
        sent_per_sec_mb = (total_bytes_sent * 8) / 1_000_000
        received_per_sec_mb = (total_bytes_received * 8) / 1_000_000

        # Логируем трафик
        logger.info(
            f"Трафик в секунду: Отправлено: {sent_per_sec_mb:.2f} Мбит/сек, Получено: {received_per_sec_mb:.2f} Мбит/сек"
        )

        # Сброс времени для следующего отсчета
        start_time = time.time()
        total_bytes_sent = 0
        total_bytes_received = 0


class FSOneFront(HttpUser):
    host = "https://stage-fsone.fstravel.com"
    wait_time = between(1, 3)

    def on_start(self):
        self.client.cookies.set(
            "XSRF-TOKEN",
            "eyJpdiI6IkNwYW91T3NrU1c0bGIzTDFIVUhhZXc9PSIsInZhbHVlIjoiMXNYWHpRaTVKZTNVaUZJRldoTHRjcTk2cHRid21aRWZqNmFJZHVZSllxY2Zuc0Q0T01JMUpNZ21iQlZBWnkwMmUzQU9jZG5GMkwwMFc3WnN4OGFNNm5qby9tOVFQL0xMaWFkaGl6eTRjUlBibHEzeVZyeWQySEFBUDhJSG5pQUoiLCJtYWMiOiI2MTM3OTlmM2MzZDZlMzc1YWRjYTVhM2Q1ZWZiODVkMzNhNGQ2OGNlYTM2Zjk2ZWU2NWY4N2FmYTQyYmM3YjU3IiwidGFnIjoiIn0%3D",
        )
        self.client.cookies.set(
            "fs_one_admin_session",
            "eyJpdiI6Ik9RRHBUMU1PZzgzTE1HWks5b3c1QWc9PSIsInZhbHVlIjoiSXlHczJ4b2Yzclg0NDhqVkNiYnpMRGExSU14ZXQ0ZWNWT0lwcUszN0JJclF0aXBQcWhpR3dXVGdUOW1PQnRETGxWclVGUFJBMzF3ZlNWMVRKdjN1RGs3bG1oMVVqdEpVY0xpdFQvQXhESmxuSzltOURpR05FZnlwMnZlaHZiOTciLCJtYWMiOiJiN2FlY2M0NmU0MThlMzRkZmM2MjY1NjM5NzZiMDNlNGU3YTRlODdkYTc0MjYxOWFmMWU5M2FmMGZjZmI5OTQ1IiwidGFnIjoiIn0%3D",
        )

        with open("payloadAnalyseFront.json", "r") as file:
            self.payload = json.load(file)

    @task
    def post_request(self):

        with self.client.post(
            url="/api/tours/get-analytical-data",
            json=self.payload,
            headers={"Content-Type": "application/json"},
            catch_response=True,
        ) as response:
            if response.status_code:
                if response.status_code == 200:
                    response.success()
                else:
                    response.failure(f"Ошибка {response.status_code}: {response.text}")
            else:
                response.failure(
                    f"Ответ без статуса: {response.text or 'пустой ответ'}"
                )
                print("Ответ без статуса:", response.text or "пустой ответ")
