from pytest import mark


class TestCheckout:

    def test_product_get(self):
        print('Have no products')

    @mark.product
    def test_product_put(self):
        print('You added a product')

