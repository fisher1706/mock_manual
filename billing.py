from utils import UtilsServerIlx
import random


class GenerateBilling:
    @staticmethod
    def generate_results(num):
        results = [{
            "referenceId": "test_" + str(i),
            "id": UtilsServerIlx.random_str(),
        } for i in range(num)]

        return results

    def generate_resp_billing(self, num):
        resp = {
            "hasErrors": random.choice([True, False]),
            "results": self.generate_results(num)
        }

        return resp


if __name__ == '__main__':
    g = GenerateBilling()

    x = g.generate_results(5)
    print(x)

    y = g.generate_resp_billing(5)
    print(y)
