from locust import HttpUser, task, between
import random
# import ssl

class UserFS(HttpUser): 
    host = 'https://preprod.fstravel.com'
   # host = 'https://stage-service-api.fstravel.com/'
    # host = 'https://fstravel.com'
    wait_time = between(1, 3)

    # ssl_verify = False

    # request_count = 0
    min_nights_count = 2
    max_nights_count = 8

    @task(1)
    def searchTurkey(self):
        
        headers = {
            # "accept": "text/plain",
            # "X-TUI-ClientId": "b2c:ru",
            # "X-User-Agent": "FUNSAN",
            "cookie": "mindboxDeviceUUID=3939b2f7-a832-42a5-b531-00d7e8d481b9"
         }
        
        # Рандом после 10 запросов
        # self.request_count += 1
        # if self.request_count % 10 == 0:
        #     self.min_nights_count = random.randint(2, 14)
        #     self.max_nights_count = random.randint(self.min_nights_count, min(self.min_nights_count + 7, 14))

        min_nights_count = random.randint(2, 14)
        max_nights_count = random.randint(min_nights_count, min(min_nights_count + 7, 14))

        url = f"/api/service-api/f-s/search/get-by-country?departureCityId=274286&arrivalCountryId=18803&minStartDate=2024-07-11&maxStartDate=2024-07-11&minNightsCount={min_nights_count}&maxNightsCount={max_nights_count}&adults=2&flightTypes=all&sort=recommendations_FS"

        self.client.get(url, headers=headers)

        
         