import random
from datetime import datetime
from pprint import pprint
import variables


class GenerateQuoteInfor:
    @staticmethod
    def create_response_quote_infor(data_test):
        response = {
            "response": {
                "sxt_func_ack": {"sxt_func_ack": []},
                "sxapi_oehdr": {
                    "sxapi_oehdr": [
                        {
                            "invoiceDt": "",
                            "invNr": data_test.get('invNr'),
                            "invSuf": "00",
                            "custPo": str(random.randint(1000, 2000)),
                            "invType": "",
                            "refer": "",
                            "partnerId": "",
                            "buyParty": "",
                            "dept": "",
                            "orderDisp": "",
                            "event": "",
                            "vendNo2": "",
                            "cancelDt": datetime.now().strftime("%m/%d/%y"),
                            "shipDt": "",
                            "promiseDt": datetime.now().strftime("%m/%d/%y"),
                            "reqShipDt": datetime.now().strftime("%m/%d/%y"),
                            "shipVia": "",
                            "poIssDt": "",
                            "enterDt": datetime.now().strftime("%m/%d/%y"),
                            "pkgId": "",
                            "ackType": "AD",
                            "currentDt": datetime.now().strftime("%m/%d/%y"),
                            "user1": "",
                            "user2": "",
                            "user3": "",
                            "userInv": "",
                            "transType": data_test.get('transType'),
                            "shipInstr": "",
                            "placedBy": "",
                            "whse": str(random.randint(10, 20)),
                            "coreChg": "",
                            "datcCost": "",
                            "downPmt": "",
                            "specDiscAmt": "",
                            "restockAmt": "",
                            "taxAmt": '{:.2f}'.format(random.randint(10, 20) * 0.01).zfill(10),
                            "gstTaxAmt": "",
                            "pstTaxAmt": "",
                            "woDiscAmt": "",
                            "termsDiscAmt": '{:.2f}'.format(random.randint(10, 20) * 0.1).zfill(13),
                            "coNo": str(random.randint(1, 10))
                        }
                    ]
                },
                "sxapi_oeitm": {"sxapi_oeitm": []},
                "cErrorMessage": ""
            }
        }

        return response


if __name__ == '__main__':
    g = GenerateQuoteInfor()
    data = variables.data_quote_infor[0]

    x = g.create_response_quote_infor(data)
    pprint(x)
