from locust import HttpUser, task, between

class UserFS(HttpUser): 
    # host = 'https://fstravel.com'
    host = 'https://preprod.fstravel.com'
   # host = 'https://prerelease.fstravel.com'
    wait_time = between(1, 3)
    whoRequest = "tours"

    @task(2)
    def getDepartureCities(self):
        self.client.get("/api/service-api/f-s/fields/get-departure-cities")

    @task(9) #Moscow
    def getArrivalMow(self):

        headers = {
            "accept": "text/plain",
            "X-TUI-ClientId": "b2c:ru",
            "X-User-Agent": "FUNSAN",
        }
        url = f"/api/service-api/f-s/fields/get-arrival?departureCityId=274286&whoRequest={UserFS.whoRequest}"
        url2 = f"/api/service-api/f-s/fields/get-available-checkins?arrivalCountryId=18803&departureCityId=274286&adultsCount=2"
        url3 = f"/api/service-api/f-s/fields/get-nights-by-freight-type?arrivalCountryId=18803&departureCityId=274286&checkinBeg=2024-08-15&checkinEnd=2024-08-17&adult=2&child=0&freightType=0"

        self.client.get(url, headers=headers)
        self.client.get(url2, headers=headers)
        self.client.get(url3, headers=headers)

    @task(3) #Spb
    def getArrivalSpb(self):

        headers = {
            "accept": "text/plain",
            "X-TUI-ClientId": "b2c:ru",
            "X-User-Agent": "FUNSAN"
        }
        url = f"/api/service-api/f-s/fields/get-arrival?departureCityId=244707&whoRequest={UserFS.whoRequest}"
        url2 = f"/api/service-api/f-s/fields/get-available-checkins?arrivalCountryId=18803&departureCityId=244707&adultsCount=2"
        url3 = f"/api/service-api/f-s/fields/get-nights-by-freight-type?arrivalCountryId=18803&departureCityId=244707&checkinBeg=2024-08-15&checkinEnd=2024-08-17&adult=2&child=0&freightType=0"

        self.client.get(url, headers=headers)
        self.client.get(url2, headers=headers)
        self.client.get(url3, headers=headers)

    @task(5) #Ekb
    def getArrivalEkb(self):

        headers = {
            "accept": "text/plain",
            "X-TUI-ClientId": "b2c:ru",
            "X-User-Agent": "FUNSAN"
        }
        url = f"/api/service-api/f-s/fields/get-arrival?departureCityId=353556&whoRequest={UserFS.whoRequest}"
        url2 = f"/api/service-api/f-s/fields/get-available-checkins?arrivalCountryId=18803&departureCityId=353556&adultsCount=2"
        url3 = f"/api/service-api/f-s/fields/get-nights-by-freight-type?arrivalCountryId=18803&departureCityId=353556&checkinBeg=2024-08-15&checkinEnd=2024-08-17&adult=2&child=0&freightType=0"

        self.client.get(url, headers=headers)
        self.client.get(url2, headers=headers)
        self.client.get(url3, headers=headers)

    @task(4) #Kaz
    def getArrivalKaz(self):

        headers = {
            "accept": "text/plain",
            "X-TUI-ClientId": "b2c:ru",
            "X-User-Agent": "FUNSAN"
        }
        url = f"/api/service-api/f-s/fields/get-arrival?departureCityId=265062&whoRequest={UserFS.whoRequest}"
        url2 = f"/api/service-api/f-s/fields/get-available-checkins?arrivalCountryId=18803&departureCityId=265062&adultsCount=2"
        url3 = f"/api/service-api/f-s/fields/get-nights-by-freight-type?arrivalCountryId=18803&departureCityId=265062&checkinBeg=2024-08-15&checkinEnd=2024-08-17&adult=2&child=0&freightType=0"

        self.client.get(url, headers=headers)
        self.client.get(url2, headers=headers)
        self.client.get(url3, headers=headers)


