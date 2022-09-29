import json
import requests
import os
import logging as logger
from requests_oauthlib import OAuth1

from my_apitest.src.configs.hosts_config import API_HOSTS
from my_apitest.src.utilities.credentials_utils import CredentialsUtils


class RequestsUtils(object):

    def __init__(self):
        wc_creds = CredentialsUtils.get_wc_api_keys()
        self.env = os.environ.get('ENV', 'test')
        self.base_url = API_HOSTS[self.env]
        self.auth = OAuth1(client_key=wc_creds['wc_key'], client_secret=wc_creds['wc_secret'])
        self.response_status_code = None
        self.expected_status_code = None
        self.url = None
        self.response_json_string = None

    def assert_status_code(self):
        assert self.response_status_code == self.expected_status_code, \
            f"Bad status code" \
            f" | expected: {self.expected_status_code} | actual: {self.response_status_code}" \
            f" | URL: {self.url} | response JSON: {self.response_json_string}"

    def post(self, endpoint, payload=None, headers=None, expected_status_code=200):
        if not headers:
            headers = {"Content-Type": "application/json"}
        self.url = self.base_url + endpoint
        self.expected_status_code = expected_status_code
        response = requests.post(url=self.url, data=json.dumps(payload), headers=headers, auth=self.auth)
        self.response_json_string = response.json()
        self.response_status_code = response.status_code
        self.assert_status_code()
        logger.debug("API response: %s", self.response_json_string)
        return self.response_json_string

    def get(self):
        pass
