from pytest import mark
from API_testing.src.utility.request_utility import RequestUtility
from API_testing.src.dao.products_dao import ProductsDAO
from API_testing.src.helpers.products_helper import ProductHelper
import logging as logger


@mark.smoke
@mark.products
@mark.test_4
def test_get_all_products():
    logger.info('Getting all products')
    rs_api = RequestUtility().get(endpoint='products')
    assert rs_api, f'Error - empty list of products'


@mark.smoke
@mark.products
@mark.test_5
def test_get_product_by_ID():
    ID = ProductsDAO().get_random_product_id_from_bd(1)[0]['id']
    logger.info('Getting product by random ID')
    rs_api = ProductHelper().get_product_by_id(id=ID)
    assert rs_api['id'] == ID, f'There is no such ID: {ID}'


