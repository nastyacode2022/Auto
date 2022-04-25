from pytest import mark
from API_testing.src.utility.request_utility import RequestUtility
from API_testing.src.dao.products_dao import ProductsDAO
from datetime import datetime, timedelta
import logging as logger


@mark.regression
class TestProductsWithFiler:

    @mark.test_7
    def test_product_with_filter_after(self):

        logger.info('Test_7 started - test_product_with_filter_after')
        after = datetime.now() - timedelta(5)
        get_call = RequestUtility().get(endpoint=f'products?after={after}')
        db_count = ProductsDAO().count_products_by_data(data=after)
        assert len(get_call) == (db_count[0]['count(*)'])-1, f"Wrong number of products with after filter"
