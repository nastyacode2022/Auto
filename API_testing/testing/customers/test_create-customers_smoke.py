from pytest import mark
import logging as logger
from API_testing.src.utility import generic_utilities
from API_testing.src.helpers import customers_helper

@mark.test_1
def test_create_customer_only_email():
    logger.info('Test: create new customer with email')
    email = generic_utilities.generate_random_email()
    logger.info(email)
    new_costumer_api = customers_helper.CustomerHelper().create_customer(email=email)
    assert new_costumer_api['email'] == email, f"Create customer API return wrong email. Email: {email}"
    assert new_costumer_api['first_name'] == '', f"Create customer API return value for the first_name, but it should be empty."