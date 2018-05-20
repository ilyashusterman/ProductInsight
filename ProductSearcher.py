import pandas
from amazon.api import AmazonAPI

REGION = 'US'

class ProductSearcher(object):
    def __init__(self, product_name):
        self.product_name = product_name
        keys = pandas.read_csv('accessKeys.csv').iloc[0]
        self.amazon = AmazonAPI(keys['access_key'],
                                keys['access_secret'],
                                837361066829, region=REGION)

    def search_product_details(self, product_name=None):
        product_name = product_name if product_name is not None \
            else self.product_name
        products = self.amazon.search(Keywords=product_name,
                                      SearchIndex='All')
        for product in products:
            print('product_title={}'.format(product.title))
            print('price={}'.format(product.price_and_currency))
