import json
import requests
import os

from my_apitest.src.configs.hosts_config import API_HOSTS


class RequestsUtils(object):

    def __init__(self):
        self.env = os.environ.get('ENV', 'test')
        self.base_url = API_HOSTS[self.env]

    def post(self, endpoint, payload=None, headers=None):
        if not headers:
            headers = {"Content-Type": "application/json"}

        url = self.base_url + endpoint

        rs_api = requests.post(url=url, data=json.dumps(payload), headers=headers)
        # import pdb; pdb.set_trace()

    def get(self):
        pass
