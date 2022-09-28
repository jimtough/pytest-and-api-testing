import json
import requests
import os
from requests_oauthlib import OAuth1

from my_apitest.src.configs.hosts_config import API_HOSTS
from my_apitest.src.utilities.credentials_utils import CredentialsUtils


class RequestsUtils(object):

    def __init__(self):
        wc_creds = CredentialsUtils.get_wc_api_keys()
        self.env = os.environ.get('ENV', 'test')
        self.base_url = API_HOSTS[self.env]
        self.auth = OAuth1(client_key=wc_creds['wc_key'], client_secret=wc_creds['wc_secret'])

    def post(self, endpoint, payload=None, headers=None, expected_status_code=200):
        if not headers:
            headers = {"Content-Type": "application/json"}

        url = self.base_url + endpoint

        rs_api = requests.post(url=url, data=json.dumps(payload), headers=headers, auth=self.auth)
        self.status_code = rs_api.status_code
        assert self.status_code == int(expected_status_code), \
            f"Expected status code {expected_status_code} but actual was {self.status_code}"

        return rs_api.json()

    def get(self):
        pass
