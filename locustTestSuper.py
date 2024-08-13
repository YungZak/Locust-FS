from locust import HttpUser, task, SequentialTaskSet, constant, events
from s import s  # Предполагается, что `s` импортируется корректно из вашего модуля

class SearchTasks(SequentialTaskSet):
    
    headers = {
        "cookie": "mindboxDeviceUUID=3939b2f7-a832-42a5-b531-00d7e8d481b9"
    }
    
    index = 0
    batch_size = 80

    # @task(2)
    # def getDepartureCities(self):
    #     self.client.get("/api/service-api/f-s/fields/get-departure-cities")
    
    # @task(3) #Moscow
    # def getArrivalMow(self):

    #     headers = {
    #         "accept": "text/plain",
    #         "X-TUI-ClientId": "b2c:ru",
    #         "X-User-Agent": "FUNSAN",
    #     }
    #     url = f"/api/service-api/f-s/fields/get-arrival?departureCityId=274286&whoRequest=tours"
    #     url2 = f"/api/service-api/f-s/fields/get-available-checkins?arrivalCountryId=18803&departureCityId=274286&adultsCount=2"
    #     url3 = f"/api/service-api/f-s/fields/get-nights-by-freight-type?arrivalCountryId=18803&departureCityId=274286&checkinBeg=2024-08-15&checkinEnd=2024-08-17&adult=2&child=0&freightType=0"

    #     self.client.get(url, headers=headers)
    #     self.client.get(url2, headers=headers)
    #     self.client.get(url3, headers=headers)
    
    @task(1)
    def search(self):
        if self.index >= len(s):
            self.interrupt()  # Завершение задачи после обработки всех ссылок
            return
        
        headers = {
            "accept": "text/plain",
            "X-TUI-ClientId": "b2c:ru",
            "X-User-Agent": "FUNSAN",
        }

        batch_urls = s[self.index:self.index + self.batch_size]
        self.index += self.batch_size
        self.execute_requests(batch_urls, headers)

    def execute_requests(self, urls, headers):
        for url in urls:
            with self.client.get(url, headers=headers, catch_response=True) as response:
                if response.status_code == 200:
                    response.success()
                else:
                    response.failure(f"Received non-200 status code {response.status_code}")
        self.wait()  # Можно задать время ожидания после обработки каждого батча

@events.quitting.add_listener
def stop_locust(environment, **kwargs):
    environment.runner.quit()

class UserFS(HttpUser):
    tasks = [SearchTasks]
    wait_time = constant(1)
