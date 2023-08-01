from locust import HttpUser, task, between


class ChatUser(HttpUser):
    wait_time = between(1, 3)

    # @task
    # def chat_delay_1(self):
    #     c = self.client.get("/test", params={'delay': 1})

    @task
    def chat_delay_3(self):
        c = self.client.get("/test", params={'delay': 3})
# openai takes between 1 and 3 sec to respond
