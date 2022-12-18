import random
from utils import UtilsServerIlx as Utils


class GetPricingD1:

    @staticmethod
    def create_resp_price_d1(prod_id):
        response = {
            "unit": prod_id,
            "price": '{:.2f}'.format(random.randint(1000, 2000) * 0.01),
        }

        print(response)
        return response


if __name__ == '__main__':
    g = GetPricingD1()
    item = 'zapel'

    resp = g.create_resp_price_d1(item)

    print(resp)
