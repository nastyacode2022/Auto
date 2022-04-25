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


    def assert_status_code(self):

        assert self.status_code == self.expected_status_code, f'Bad status code'\
        f'Expected {self.expected_status_code}, Actual status code {self.status_code},'\
        f'URL: {self.url}, Response JSON: {self.rs_json}'


    def post(self, endpoint, payload=None, headers=None, expected_status_code=200):

        if not headers:
            headers = {"Content-Type": "application/json; charset=UTF-8"}
        self.url = self.base_url + endpoint
        rs_api = requests.post(url=self.url, data=json.dumps(payload), headers=headers, auth=self.auth, verify=False)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()
        logger.debug(f'API POST response {self.rs_json}')
        return self.rs_json


    def get(self, endpoint, payload=None, headers=None, expected_status_code=200):

        if not headers:
            headers = {"Content-Type": "application/json; charset=UTF-8"}
        self.url = self.base_url + endpoint
        rs_api = requests.get(url=self.url, data=json.dumps(payload), headers=headers, auth=self.auth, verify=False)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()
        logger.debug(f'API GET response {self.rs_json}')
        return self.rs_json


    def delete(self):
        pass

    def update(self):
        pass

