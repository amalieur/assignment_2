import time
from locust import HttpUser, task, between


class quickstartUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/numericalintegralservice/0/3.14159")
