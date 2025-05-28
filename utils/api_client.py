from playwright.sync_api import sync_playwright

from utils import config_reader as cr


class ApiClient:
    def __init__(self):
        self.api_details = cr.get_api_details()

    def get(self, endpoint, token, headers=None, params=None):
        with sync_playwright() as p:
            api_request_context = p.request.new_context(
                ignore_https_errors=self.api_details["ignore_https_errors"]
            )
            headers = {
                "Authorization": f"Bearer {token}",
                "Referer": self.api_details["referer"],
                "Accept": self.api_details["accept"],
            }
            response = api_request_context.get(
                cr.get_api_url(endpoint),
                headers=headers,
            )
        return response

    def post(self, endpoint, data=None, headers=None):
        with sync_playwright() as p:
            api_request_context = p.request.new_context(
                ignore_https_errors=cr.get_api_ignore_https_errors_status()
            )
            response = api_request_context.post(
                cr.get_api_url(endpoint),
                headers=cr.get_api_header_auth(),
                data=cr.get_api_request_data(),
            )

    # def put(self, endpoint, data=None, headers=None):
    #     return requests.put(url=self.base_url + endpoint, data=data, headers=headers)

    # def patch(self, endpoint, data=None, headers=None):
    #     return requests.patch(url=self.base_url + endpoint, data=data, headers=headers)

    # def delete(self, endpoint, headers=None):
    #     return requests.delete(url=self.base_url + endpoint, headers=headers)
