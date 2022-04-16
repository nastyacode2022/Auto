import requests
from API_testing.src.utility.credentialUtility import CredentialsUtility
import os
from API_testing.src.config.hosts_config import API_HOSTS
import json
from requests_oauthlib import OAuth1
import logging as logger

class RequestUtility:

    def __init__(self):

        self.venv = os.environ.get('ENV', 'test')
        self.base_url = API_HOSTS[self.venv]
        self.auth = OAuth1(CredentialsUtility.get_wc_api_keys()['wc_key'], CredentialsUtility.get_wc_api_keys()['wc_secret'])

    def post(self, endpoint, payload=None, headers=None, expected_status_code=200):

        if not headers:
            headers = {"Content-Type": "application/json; charset=UTF-8"}
        url = self.base_url + endpoint
        rs_api = requests.post(url=url, data=json.dumps(payload), headers=headers, auth=self.auth)
        self.status_code = rs_api.status_code
        assert self.status_code == int(expected_status_code), f'Expected status code {expected_status_code} actual status {self.status_code}'
        logger.debug(f'API response {rs_api.json()}')
        return rs_api.json()

    def get(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass

