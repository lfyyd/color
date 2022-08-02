import requests


class send:
    session = requests.session()

    def send_requsts(self, method, url, **kwargs):
        result = send.session.request(method, url, **kwargs)
        return result
