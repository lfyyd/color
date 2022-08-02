import requests
import pytest


class TestApi1:
    cookie = ""
    id = ""

    def test_login(self):
        urls = 'http://127.0.0.1/api/mgr/signin'
        datas = {
            "username": "byhy",
            "password": "88888888"
        }

        result = requests.post(url=urls, data=datas)
        TestApi1.cookie = result.cookies
        print(result.json())

    def test_creapt(self):
        urls = 'http://127.0.0.1/api/mgr/medicines'
        datas = {
            "action": "add_medicine",
            "data": {
                "name": "枫谷",
                "sn": "1314521",
                "desc": "七夕大礼品"
            }
        }

        result = requests.post(url=urls, json=datas, cookies=TestApi1.cookie)
        TestApi1.id = result.json()['id']
        print(result.json())

    def test_update(self):
        urls = 'http://127.0.0.1/api/mgr/medicines'
        datas = {
            "action": "modify_medicine",
            "id": TestApi1.id,
            "newdata": {
                "name": "枫谷",
                "sn": "1314521",
                "desc": "七夕豪华礼品"
            }
        }

        result = requests.put(url=urls, json=datas, cookies=TestApi1.cookie)
        print(result.json())

    def test_delect(self):
        urls = 'http://127.0.0.1/api/mgr/medicines'
        datas = {
            "action": "del_medicine",
            "id": TestApi1.id
        }

        result = requests.delete(url=urls, json=datas, cookies=TestApi1.cookie)
        print(result.json())

    def test_client(self):
        urls = 'http://127.0.0.1/api/mgr/medicines'
        params = {
            "action": "list_medicine",
            "pagenum": "1",
            "pagesize": "5",
            "keywords": "",
            "_": "1659409989246"
        }

        result = requests.get(url=urls, params=params, cookies=TestApi1.cookie)
        print(result.json())



