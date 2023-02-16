import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def origin_destination(self):
        self.client.get('/api/v1/ticket/origin-dest')

    @task
    def available_offers(self):
        self.client.get('/api/v1/ticket/available-offers')
