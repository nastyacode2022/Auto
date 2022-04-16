from API_testing.src.utility import generic_utilities
from API_testing.src.utility.request_utility import RequestUtility

class CustomerHelper:

    def __init__(self):

        self.request_utility = RequestUtility()

    def create_customer(self, email=None, **kwargs):

        if not email:
            email = generic_utilities.generate_random_email()
        payload = dict()
        payload['email'] = email
        payload.update(kwargs)
        create_user_json = self.request_utility.post('customers', payload, expected_status_code=201)
        return create_user_json