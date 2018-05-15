import pandas
from amazon.api import AmazonAPI

class ProductSearcher(object):
    def __init__(self, product_name):
        self.product_name = product_name
        keys = pandas.read_csv('accessKeys.csv').iloc[0]
        self.amazon = AmazonAPI(keys['access_key'],
                                         keys['access_secret'],
                                         837361066829, region='US')
    def search(self):
        products = self.amazon.search(Keywords=self.product_name,
                                   SearchIndex='All')
        for product in products:
            print('product_title={}'.format(product.title))
