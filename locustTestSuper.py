from locust import HttpUser, task, SequentialTaskSet, constant, events
from s import s  # Предполагается, что `s` импортируется корректно из вашего модуля

class SearchTasks(SequentialTaskSet):
    
    headers = {
        "cookie": "mindboxDeviceUUID=3939b2f7-a832-42a5-b531-00d7e8d481b9"
    }
    
    index = 0

    @task(1)
    def search(self):
        batch_size = 10
        total_urls = len(s)
        
        while self.index < total_urls:
            batch_urls = s[self.index:self.index+batch_size]
            self.index += batch_size
            
            self.execute_requests(batch_urls)
            
            # Wait for the first 10 requests to complete before proceeding
            self.wait()

    def execute_requests(self, urls):
        requests = []
        
        for url in urls:
            with self.client.get(url, headers=self.headers, catch_response=True) as response:
                if response.status_code == 200:
                    response.success()
                else:
                    response.failure(f"Received non-200 status code {response.status_code}")

@events.quitting.add_listener
def stop_locust(environment, **kwargs):
    environment.runner.quit()

class UserFS(HttpUser):
    tasks = [SearchTasks]
    wait_time = constant(1)
