from pytest import mark
from API_testing.src.utility.request_utility import RequestUtility
import logging as logger

@mark.test_2
def test_get_all_customers():

    req_helper = RequestUtility()
    rs_api = req_helper.get(endpoint='customers')
    assert rs_api, f'Error - empty list of customers'
