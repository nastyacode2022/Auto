from API_testing.src.utility.request_utility import RequestUtility

class ProductHelper:

    def __init__(self):

        self.request_utility = RequestUtility()

    def get_product_by_id(self, id):

        return self.request_utility.get(endpoint=f'products/{id}')