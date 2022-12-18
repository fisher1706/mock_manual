import random
from pprint import pprint


class GenerateVmiList:
    partNumbers = ["1 GAL CPLG", "1 HUB", "1 PAR CLMP", "1 PLUG", "1 RI AN CLMP"]
    locations = ["CABINET", "WIRE RACK", "SHELF", "CONDUIT RACK", "CRIB DRAWER"]

    def create_string_id(self, data_vmi):
        return f'"{data_vmi["customerId"]}~{random.choice(self.partNumbers)}~{data_vmi["productId"]}"'

    def create_items(self, data_vmi):
        items = [{
            "customerId": data_vmi["customerId"],
            "partNumber": random.choice(self.partNumbers),
            "location": random.choice(self.locations),
            "productId": data_vmi["productId"],
            "minQty": random.randint(100, 200),
            "maxQty": random.randint(100, 200),
            "id": self.create_string_id(data_vmi)
        } for _ in range(data_vmi["pageSize"])]

        return items

    def create_response_vmi(self, data_vmi):
        resp = {
            "metadata": {
                "startIndex": data_vmi["startIndex"],
                "pageSize": data_vmi["pageSize"],
                "totalItems": 100
            },

            "results": self.create_items(data_vmi)
        }

        return resp


if __name__ == '__main__':
    g = GenerateVmiList()

    data = {
        "customerId": 60428,
        "productId": 700,
        "pageSize": 5,
        "startIndex": 3,
    }

    x = g.create_string_id(data)
    print(x)

    y = g.create_items(data)
    pprint(y)

    z = g.create_response_vmi(data)
    pprint(z)
