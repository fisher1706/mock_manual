import random
from utils import UtilsServerIlx as Utils


class GetPricingEclipse:
    currency = ['EUR', 'USD', 'UAH']

    def create_rep_price_eclipse(self, product, qnt):
        response = {
            "productId": product,
            "branch": Utils.random_str(size=3),
            "pricingPerQuantity": qnt,
            "pricingUOM": "c",
            "productUnitPrice": {
                "value": '{:.8f}'.format(random.randint(1000, 2000) * 0.01),
                "currency": random.choice(self.currency)
            },
            "quantityBreaks": []
        }

        return response


if __name__ == '__main__':
    g = GetPricingEclipse()

    prod = 100
    qnt = 200

    resp = g.create_rep_price_eclipse(prod, qnt)

    print(resp)
