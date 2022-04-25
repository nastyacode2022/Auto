import string
import random
from API_testing.src.dao.products_dao import ProductsDAO
from pytest import mark
from API_testing.src.utility.request_utility import RequestUtility
from API_testing.src.utility.generic_utilities import create_random_product_json


@mark.products
@mark.test_6
def test_create_one_simple_product():

    json_body = create_random_product_json()
    new_req = RequestUtility().post(endpoint='products', payload=json_body, expected_status_code=201)
    json_id = new_req['id']
    id_database = ProductsDAO().get_product_by_id(json_id)
    assert id_database


