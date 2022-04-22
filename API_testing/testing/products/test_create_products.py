import string
import random
from pytest import mark
from API_testing.src.utility.request_utility import RequestUtility


@mark.products
@mark.test_6
def test_create_one_simple_product():

    name = ''.join(random.choices(string.ascii_lowercase, k=5))
    desc = ''.join(random.choices(string.ascii_lowercase, k=10))
    price = str(float(random.choice(range(10, 1000))))
    json_body = dict()
    json_body['name'] = name
    json_body['description'] = desc
    json_body['regular_price'] = price
    new_req = RequestUtility().post(endpoint='products', payload=json_body, expected_status_code=201)

    import pdb; pdb.set_trace()
