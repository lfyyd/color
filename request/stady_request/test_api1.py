import pytest
from request.commons.send_request import send

# 药品
from request.data.opne_yaml import read_yaml


class TestApi1:
    id = ""

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", read_yaml('../data/login.yaml'))
    def test_login(self, data):
        urls = data[0]["request"]["url"]
        datas = data[0]["request"]["datas"]
        method = data[0]["request"]["method"]
        result = send().send_requsts(method=method, url=urls, data=datas)
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

        result = send().send_requsts("post", url=urls, json=datas)
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

        result = send().send_requsts("put", url=urls, json=datas)
        print(result.json())

    def test_delect(self):
        urls = 'http://127.0.0.1/api/mgr/medicines'
        datas = {
            "action": "del_medicine",
            "id": TestApi1.id
        }

        result = send().send_requsts("delete", url=urls, json=datas)
        print(result.json())

    def test_client(self):
        urls = 'http://127.0.0.1/api/mgr/medicines'
        params = {
            "action": "list_medicine",
            "pagenum": "1",
            "pagesize": "5",
            "keywords": "",
            "_": "1659424270591"
        }

        result = send().send_requsts("get", url=urls, params=params)
        print(result.json())
