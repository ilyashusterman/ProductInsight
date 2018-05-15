from unittest import TestCase
from ProductSearcher import ProductSearcher

class TestProductClass(TestCase):
    def setUp(self):
        self.product = ProductSearcher('nesspresso capsules')


    def test_search_product(self):
        entity = self.product.search()
        assert False
