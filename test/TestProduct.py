from unittest import TestCase
from ProductSearcher import ProductSearcher

class TestProductClass(TestCase):
    def setUp(self):
        self.product = ProductSearcher('nesspresso')


    def test_search_product(self):
        entity = self.product.search_product_details('nesspresso')
        # assert False
