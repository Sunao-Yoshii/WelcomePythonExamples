from locust import HttpLocust, TaskSet, task

import re


class UserBehavior(TaskSet):
    def on_start(self):
        self.login()

    def on_stop(self):
        self.logout()

    def login(self):
        # Cookie などを受け取る目的で
        self.client.get("/wp-login.php")
        parameters = {
            'log': 'TestAccount',
            'pwd': 'Fire!!1192',
            'redirect_to': 'http://localhost:9000/wp-admin/',
            'testcookie': '1'
        }

        self.client.post("/wp-login.php", parameters)

    def logout(self):
        response = self.client.get("/wp-admin/")
        # ログアウト用 URL 取得
        logout_url = re.search(
            r'<a class="screen-reader-shortcut" href="http:\/\/localhost\:9000(.+)">ログアウト</a>',
            response.text).group(1)
        self.client.get(logout_url)

    @task
    def top(self):
        self.client.get("/")

    @task(2)
    def mypage(self):
        with self.client.get("/wp-admin/customize.php", catch_response=True) as response:
            if response.status_code != 200:
                response.failure("not authenticated???")

    @task
    def projects(self):
        self.client.get("/wp-admin/")


class Wordpress(HttpLocust):
    task_set = UserBehavior
    min_wait = 500
    max_wait = 1000
