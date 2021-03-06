from pytest import mark
import logging as logger
from API_testing.src.utility import generic_utilities, request_utility
from API_testing.src.helpers import customers_helper
from API_testing.src.dao.customers_dao import CustomersDAO


@mark.smoke
@mark.customers
@mark.test_1
def test_create_customer_only_email():
    """
    Creating customer with random email, checking email in API response and DB
    """
    logger.info('Test: create new customer with email')
    email = generic_utilities.generate_random_email()
    logger.info(email)
    """
    Create customer with API with random email
    """
    new_customer_api = customers_helper.CustomerHelper().create_customer(email=email)
    """
    Assertion in json response
    """
    assert new_customer_api['email'] == email, f"Create customer API return \
    wrong email. Email: {email}"
    assert new_customer_api['first_name'] == '', f"Create customer API return value for \
    the first_name, but it should be empty."

    cust_dao = CustomersDAO()
    cust_info = cust_dao.get_customer_by_email(email)
    """
    Assertion in DB select response
    """
    id_in_api = new_customer_api['id']
    id_in_db = cust_info[0]['ID']
    assert id_in_db == id_in_api, f"Wrong customer id in response: {id_in_api} and db: {id_in_db}"\
                                f"Email:{email}"


@mark.smoke
@mark.test_3
@mark.customers
def test_create_customer_fail_for_existing_email():
    # get existing email from db
    cust_dao = CustomersDAO()
    existing_cust = cust_dao.get_random_customer_from_db()
    existing_email = existing_cust[0]['user_email']
    payload = {"email": existing_email}
    new_customer_api = request_utility.RequestUtility().post(endpoint='customers', payload=payload, expected_status_code=400)
    assert new_customer_api['code'] == 'registration-error-email-exists',\
        'Error with registation - email is already exist'
