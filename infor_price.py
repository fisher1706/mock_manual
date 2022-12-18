import random


class GetPricingInfor:

    @staticmethod
    def create_rep_price_infor(unit_price, prod_number, name):

        response = {
            "response": {
                "cErrorMessage": "",
                "price": unit_price,
                "discountAmount": random.randint(0, 10),
                "discountType": "%",
                "netAvailable": random.randint(0, 10),
                "specialCostType": "y",
                "priceCostPer": name,
                "unitsPerStocking": '{:.2f}'.format(random.randint(10, 20) * 0.01),
                "specialConversion": random.randint(0, 10),
                "specialCostRecordNumber": random.randint(0, 10),
                "stockingQuantityOrdered": random.randint(0, 10),
                "unitConversion": random.randint(0, 10),
                "pricingRecordNumber": prod_number,
                "promotionalFlag": random.choice([True, False]),
                "priceOriginCode": f'{random.randint(1, 10)}',
                "unitsPerStockingText": name,
                "extendedAmount": '{:.2f}'.format(random.randint(10, 20) * 0.01),
                "extendedDiscountAmount": random.randint(0, 10)
            }
        }

        return response
