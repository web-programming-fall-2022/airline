from locust import HttpUser, task, between


class AirlineUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def origin_destination(self):
        self.client.get('/api/v1/ticket/origin-dest?limit=20')

    @task
    def available_offers(self):
        self.client.get('/api/v1/ticket/available-offers?limit=100')

    @task
    def login_getinfo(self):
        auth_token = self.client.post('/api/v1/auth/login', json={
            'email': 'pouya@gmail.com',
            'password': '123456789',
        }).json()['authToken']
        self.client.post('/api/v1/auth/userinfo', json={
            'auth_token': auth_token
        })
