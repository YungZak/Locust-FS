from locust import HttpUser, task, between
import itertools
import time

class UserFS(HttpUser):
    wait_time = between(1, 3)
    departure_values = []

    @task(1)
    def getDepartureCities(self):

        response =self.client.get("/api/service-api/f-s/fields/get-departure-cities")
        data = response.json()

        for item in data:
            ebg_node_id = item['ebgNodeId']
            self.departure_values.append(ebg_node_id)

    @task(1)
    def getArrival(self):

        if self.departure_values:
            ebg_node_id = self.departure_values.pop()

        headers = {
            "accept": "text/plain",
            "X-TUI-ClientId": "b2c:ru",
            "X-User-Agent": "FUNSAN"
        }
         
        whoRequest = "tours"
        
        url = f"/api/service-api/f-s/fields/get-arrival?departureCityId={ebg_node_id}&whoRequest={whoRequest}"

        self.client.get(url, headers=headers)


