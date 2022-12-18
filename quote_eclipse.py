from pprint import pprint
import variables


class GenerateQuoteEclipse:
    @staticmethod
    def create_response_quote_eclipse(data_test):
        response = {
            "results": [
                {
                    "generations": [
                        {
                            "status": data_test.get('orderStatus'),
                        }
                    ],
                    "id": data_test.get('productId')
                }
            ]
        }

        return response


if __name__ == '__main__':
    g = GenerateQuoteEclipse()
    data = variables.data_quote_eclipse[1]

    x = g.create_response_quote_eclipse(data)
    pprint(x)
