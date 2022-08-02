import pytest

# 客户
from request.commons.send_request import send


class TestApi2:
    ids = ""

    def test_creapt(self):
        urls = 'http://127.0.0.1/api/mgr/customers'
        datas = {
            "action": "add_customer",
            "data": {
                "name": "梁枫",
                "phonenumber": "17610372366",
                "address": "杭州市"
            }
        }

        result = send().send_requsts("post", url=urls, json=datas)
        TestApi2.ids = result.json()['id']
        print(result.json())

    def test_update(self):
        urls = 'http://127.0.0.1/api/mgr/customers'
        datas = {
            "action": "modify_customer",
            "id": TestApi2.ids,
            "newdata": {
                "address": "杭州市萧山区"
            }
        }

        result = send().send_requsts("put", url=urls, json=datas)
        print(result.json())

    def test_delect(self):
        urls = 'http://127.0.0.1/api/mgr/customers'
        datas = {
            "action": "del_customer",
            "id": TestApi2.ids
        }

        result = send().send_requsts("delete", url=urls, json=datas)
        print(result.json())

    def test_client(self):
        urls = 'http://127.0.0.1/api/mgr/customers'
        params = {
            "action": "list_customer",
            "pagenum": "1",
            "pagesize": "5",
            "keywords": "",
            "_": "1659443519681"
        }

        result = send().send_requsts("get", url=urls, params=params)
        print(result.json())
