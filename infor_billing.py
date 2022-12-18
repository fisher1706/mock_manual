from datetime import datetime


class GetBillingInfor:
    @staticmethod
    def create_resp_billing_infor(num):
        date_now = datetime.now().strftime('%d/%m/%y')

        response = {
            "response": {
                "sxt_func_ack": {
                    "sxt_func_ack": [
                        {
                            "coNo": 1,
                            "correlation_data": "",
                            "data1": f"{num}-00",
                            "errorNo": 0,
                            "msg": f"Order: {num}-00, has been created.",
                            "seqNo": 0,
                            "trxType": ""
                        }
                    ]
                },
                "sxapi_oehdr": {
                    "sxapi_oehdr": [
                        {
                            "invoiceDt": "",
                            "invNr": f"0{num}",
                            "invSuf": "00",
                            "custPo": "SX27714_32",
                            "invType": "",
                            "refer": "",
                            "partnerId": "IDCX_COMAU-01",
                            "buyParty": "",
                            "dept": "",
                            "orderDisp": "",
                            "event": "",
                            "vendNo2": "",
                            "cancelDt": "",
                            "shipDt": "",
                            "promiseDt": f"{date_now}",
                            "reqShipDt": "04/07/22",
                            "shipVia": "CAP WEST",
                            "poIssDt": "        ",
                            "enterDt": f"{date_now}",
                            "pkgId": "",
                            "ackType": "AD",
                            "currentDt": f"{date_now}",
                            "user1": "",
                            "user2": "",
                            "user3": "",
                            "userInv": "",
                            "transType": "SO",
                            "shipInstr": "",
                            "placedBy": "",
                            "whse": "X610",
                            "coreChg": "",
                            "datcCost": "",
                            "downPmt": "",
                            "specDiscAmt": "",
                            "restockAmt": "",
                            "taxAmt": "",
                            "gstTaxAmt": "",
                            "pstTaxAmt": "",
                            "woDiscAmt": "",
                            "termsDiscAmt": "",
                            "coNo": "1"
                        }
                    ]
                },
                "sxapi_oeitm": {
                    "sxapi_oeitm": [
                        {
                            "lineIden": "0001",
                            "qtyUom": "EA",
                            "prodSvcCd": "",
                            "sellerProd": "WOOD114030K12M005",
                            "buyerProd": "",
                            "descrip": "WOOD 114030K12M005 MC 4P",
                            "user1": "",
                            "user2": "",
                            "user3": "",
                            "user4": "",
                            "user5": "",
                            "ordStatCd": "",
                            "chgCd": "",
                            "boType": "y",
                            "user6": "",
                            "user7": "",
                            "user8": "",
                            "user9": "",
                            "user10": "",
                            "specCostTy": "Y",
                            "sCostUnit": "000001.000000",
                            "xrefProdTy": "",
                            "taxableFl": "n",
                            "taxableTy": "",
                            "taxGroup": "1",
                            "promiseDt": f"{date_now}",
                            "reqShipDt": f"{date_now}",
                            "specNsType": "s",
                            "upc": "",
                            "sxLineNo": "0001",
                            "qtyShip": "000001.00",
                            "price": "0000045.68000",
                            "discPct": "",
                            "qtyOrd": "000001.00",
                            "discAmt": "",
                            "taxAmt1": "0000000.00000",
                            "taxAmt2": "0000000.00000",
                            "taxAmt3": "0000000.00000",
                            "taxAmt4": "0000000.00000",
                            "upcSection1": "000000000000",
                            "upcSection2": "000000000000",
                            "upcSection3": "000000786788",
                            "upcSection4": "000000002291",
                            "upcSection5": "000000000000",
                            "upcSection6": "000000000000",
                            "restockChg": "000000000.00",
                            "spCostUnit": "EA"
                        }
                    ]
                },
                "cErrorMessage": ""
            }
        }

        return response


if __name__ == '__main__':
    g = GetBillingInfor()
    resp = g.create_resp_billing_infor(123)
    print(resp)
