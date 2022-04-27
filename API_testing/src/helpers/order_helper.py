import json
import os
from API_testing.src.utility.request_utility import RequestUtility


class OrdersHelper:

    def __init__(self):

        self.file_dir = os.path.dirname(os.path.realpath(__file__))


    def create_order(self, add_args=None):

        payload_template = os.path.join(self.file_dir, '..', 'data', 'create_order.json')
        with open(payload_template) as f:
            payload = json.load(f)
        if add_args:
            assert isinstance(add_args, dict), f'Parameter add_args must be a dict'
            payload.update(add_args)
        rs_api = RequestUtility().post(endpoint='orders', payload=payload, expected_status_code=201)
        return rs_api
