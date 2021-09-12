import requests


class SwaggerApiCallsClass:

    def test_get(self, credentials, get_requests, requests_path):
        """
        here we will run the "GET" requests
        """
        for x in get_requests:
            payload = {}
            url = requests_path + x
            headers = credentials
            response = requests.request("GET", url, headers=headers, data=payload)
            print(response.text)

    def test_post(self):
        return self

    def test_put(self):
        return self

    def test_delete(self):
        return self
