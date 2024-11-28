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


class FSOneBack(HttpUser):
    host = "http://10.130.4.24:30080"
    wait_time = between(1, 3)

    def on_start(self):

        with open("payloadGetPriceBack.json", "r") as file:
            self.payload = json.load(file)

    @task
    def post_request(self):

        with self.client.post(
            url="/api/tours/get-prices",
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
