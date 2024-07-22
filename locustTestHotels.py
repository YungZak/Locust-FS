from locust import HttpUser, task, between

class UserFS(HttpUser): 
   
    host = 'https://api.fstravel.com'
    wait_time = between(1, 3)
    whoRequest = "tours"
    

    @task(1) 
    def getArrivalMow(self):

        TOKEN = "f876b87654ec42c18e227161391a114a"
        headers = {
            
            "Accept-Encoding": "gzip, deflate, sdch",
            "User-Agent": "leveltravel",
        }
        url = f"/export/default.php?ADULT=2&CHECKIN_BEG=20240728&CHECKIN_END=20240801&CHILD=0&CURRENCY=1&FILTER=1&FREIGHT=1&HOTELS=781487%2C355421&HOTELTYPES=&MEAL=&NIGHTS_FROM=4&NIGHTS_TILL=8&PACKET=0&PRICEPAGE=1&SPOINC=0&STATEINC=210357&TOURINC=0&TOWNFROMINC=274286&TOWNTO=&action=SearchTour_PRICES&oauth_token={TOKEN}&page=search_tour&samo_action=api"

        self.client.get(url, headers=headers)
    
    @task(1) 
    def getArrivalMow(self):

        TOKEN = "f876b87654ec42c18e227161391a114a"
        headers = {
            
            "Accept-Encoding": "gzip, deflate, sdch",
            "User-Agent": "leveltravel",
        }
        url = f"/export/default.php?ADULT=2&CHECKIN_BEG=20240801&CHECKIN_END=20240801&CHILD=0&CURRENCY=1&FILTER=1&FREIGHT=1&HOTELS=30691&HOTELTYPES=&MEAL=&NIGHTS_FROM=5&NIGHTS_TILL=9&PACKET=0&PRICEPAGE=1&SPOINC=0&STATEINC=18803&TOURINC=0&TOWNFROMINC=274286&TOWNTO=&action=SearchTour_PRICES&oauth_token={TOKEN}&page=search_tour&samo_action=api"

        self.client.get(url, headers=headers)

    @task(1) 
    def getArrivalMow(self):

        TOKEN = "f876b87654ec42c18e227161391a114a"
        headers = {
            
            "Accept-Encoding": "gzip, deflate, sdch",
            "User-Agent": "leveltravel",
        }
        url = f"/export/default.php?ADULT=3&CHECKIN_BEG=20240801&CHECKIN_END=20240801&CHILD=0&CURRENCY=1&FILTER=1&FREIGHT=1&HOTELS=584040&HOTELTYPES=&MEAL=&NIGHTS_FROM=14&NIGHTS_TILL=14&PACKET=0&PRICEPAGE=1&SPOINC=0&STATEINC=18803&TOURINC=0&TOWNFROMINC=274286&TOWNTO=&action=SearchTour_PRICES&oauth_token={TOKEN}&page=search_tour&samo_action=api"

        self.client.get(url, headers=headers)

    @task(1) 
    def getArrivalMow(self):

        TOKEN = "f876b87654ec42c18e227161391a114a"
        headers = {
            
            "Accept-Encoding": "gzip, deflate, sdch",
            "User-Agent": "leveltravel",
        }
        url = f"/export/default.php?ADULT=3&CHECKIN_BEG=20240801&CHECKIN_END=20240801&CHILD=0&CURRENCY=1&FILTER=1&FREIGHT=1&HOTELS=584040&HOTELTYPES=&MEAL=&NIGHTS_FROM=14&NIGHTS_TILL=14&PACKET=0&PRICEPAGE=1&SPOINC=0&STATEINC=18803&TOURINC=0&TOWNFROMINC=274286&TOWNTO=&action=SearchTour_PRICES&oauth_token={TOKEN}&page=search_tour&samo_action=api"

        self.client.get(url, headers=headers)

    @task(1) 
    def getArrivalMow(self):

        TOKEN = "f876b87654ec42c18e227161391a114a"
        headers = {
            
            "Accept-Encoding": "gzip, deflate, sdch",
            "User-Agent": "leveltravel",
        }
        url = f"/export/default.php?ADULT=2&CHECKIN_BEG=20240826&CHECKIN_END=20240830&CHILD=0&CURRENCY=1&FILTER=1&FREIGHT=1&HOTELS=703276&HOTELTYPES=&MEAL=&NIGHTS_FROM=5&NIGHTS_TILL=9&PACKET=0&PRICEPAGE=1&SPOINC=0&STATEINC=18498&TOURINC=0&TOWNFROMINC=274286&TOWNTO=&action=SearchTour_PRICES&oauth_token={TOKEN}&page=search_tour&samo_action=api"

        self.client.get(url, headers=headers)

    

    

    