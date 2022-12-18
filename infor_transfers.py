import random
from utils import UtilsServerIlx as Utils
from variables import *
from pprint import pprint


class InforTransfers:
    @staticmethod
    def get_resp_infor_transfers(data):
        response = {
            "cErrorMessage": data,
            "tFieldlist": {
                "t-fieldlist": [
                    {
                        "wtno": random.randint(1, 10),
                        "stage": "Ord",
                        "wtsuf": random.randint(1, 10),
                        "transtype": Utils.random_str(),
                        "shipfmwhse": Utils.random_str(),
                        "shiptowhse": Utils.random_str()
                    }
                ]
            },
            "tWtlineitemv2": {
                "t-wtlineitemv2": [
                    {
                        "bono": random.randint(1, 10),
                        "unit": Utils.random_str(),
                        "duedt": Utils.random_str(),
                        "lineno": random.randint(1, 10),
                        "netamt": random.randint(1, 10),
                        "netord": random.randint(1, 10),
                        "netrcv": random.randint(1, 10),
                        "qtyord": random.randint(1, 10),
                        "qtyrcv": random.randint(1, 10),
                        "qtyship": random.randint(1, 10),
                        "sortFld": Utils.random_str(),
                        "prodcost": random.randint(1, 10),
                        "shipprod": Utils.random_str(),
                        "unitconv": random.randint(1, 10),
                        "approvety": Utils.random_str(),
                        "ordertype": Utils.random_str(),
                        "proddesc": Utils.random_str(),
                        "proddesc2": Utils.random_str(),
                        "stkqtyord": random.randint(1, 10),
                        "stkqtyrcv": random.randint(1, 10),
                        "tiedorder": Utils.random_str(),
                        "nonstockty": Utils.random_str(),
                        "orderaltno": random.randint(1, 10),
                        "stkqtyship": random.randint(1, 10),
                        "prodinrcvfl": random.choice([True, False]),
                        "rcvunavailfl": random.choice([True, False])
                    }
                ]
            }
        }

        return response


if __name__ == '__main__':
    i = InforTransfers()
    mess = i.get_resp_infor_transfers(data_infor_transfers['cErrorMessage'])

    x = data_infor_transfers.pop('cErrorMessage')
    y = data_infor_transfers

    print(x)
    pprint(y)
    # pprint(mess)


