from utils import UtilsServerIlx as Utils
import random


class GetResponseGerrie:

    @staticmethod
    def generate_resp_gerrie(data_test):
        response = {
            'response': [
                {
                    "id": Utils.random_str(8),
                    "items": [
                        {
                            "dsku": str(random.randint(100, 500)),
                            "msku": str(random.randint(10, 50)),
                            "quantityOrdered": data_test.get("quantityOrdered"),
                            "quantityShipped": data_test.get("quantityShipped"),
                        }
                    ],
                    "release": Utils.random_str(10),
                    "poNumber": Utils.random_str(6),
                    "transactionType": data_test.get("type")
                }
            ]
        }

        return response


if __name__ == '__main__':
    g = GetResponseGerrie()
    data = {"quantityOrdered": 100,
            "quantityShipped": 200,
            "tran_type": "ORDERED"}

    x = g.generate_resp_gerrie(data)
    print(x)
