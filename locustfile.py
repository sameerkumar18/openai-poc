from locust import HttpUser, task, between


class ChatUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def chat(self):
        c = self.client.get("/test", params={'delay': 3})

# openai takes between 1 and 3 sec to respond
