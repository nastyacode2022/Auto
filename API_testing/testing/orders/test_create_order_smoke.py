import pytest
from pytest import mark
from API_testing.src.dao.products_dao import ProductsDAO
from API_testing.src.helpers.order_helper import OrdersHelper
from API_testing.src.dao.orders_dao import OrdersDAO
from API_testing.src.helpers.customers_helper import CustomerHelper


@pytest.fixture(scope='module')
def my_orders_smoke_setup():

    random_product = ProductsDAO().get_random_product_id_from_bd()[0]['id']
    return random_product


@mark.orders
@mark.smoke
@mark.test_8
def test_create_paid_order_guest_user(my_orders_smoke_setup):

    info = {"line_items": [
        {
            "product_id": my_orders_smoke_setup,
            "quantity": 1
        }
    ]}
    order_json = OrdersHelper().create_order(add_args=info)
    assert order_json, 'Create order response is empty'
    assert order_json['customer_id'] == 0, 'Wrong customer id'
    assert len(order_json['line_items']) == 1, f'Expected only 1 product in order'
    assert OrdersDAO().get_order_by_id(id=order_json['id']), f'There is no order in db'


@mark.orders
@mark.smoke
@mark.test_9
def test_create_paid_order_new_created_customer(my_orders_smoke_setup):

    random_customer = CustomerHelper().create_customer()['id']
    info = {"line_items": [
        {
            "product_id": my_orders_smoke_setup,
            "quantity": 1
        }
    ],
            "customer_id": random_customer}
    order_json = OrdersHelper().create_order(add_args=info)
    assert order_json, 'Create order response is empty'
    assert order_json['customer_id'] == random_customer, 'Wrong customer id'
    assert len(order_json['line_items']) == 1, f'Expected only 1 product in order'
    assert OrdersDAO().get_order_by_id(id=order_json['id']), f'There is no order in db'