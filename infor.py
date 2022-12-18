class GenerateInforOrderStatusV2:
    response = {
        "response": {
            "cErrorMessage": "",
            "tFieldlist": {
                "t-fieldlist": None
            },
            "tOelineitemV3": {
                "t-oelineitemV3": None
            },
            "tOetaxsa": {
                "t-oetaxsa": [
                    {
                        "seqno": 1,
                        "locallabels": "State",
                        "taxcode": "IN",
                        "localdescrip": "IN - State",
                        "taxgroupnm": "STANDARD",
                        "taxamt": "14.72",
                        "taxsaleamt": "210.23"
                    }
                ]
            },
            "tOetaxar": {
                "t-oetaxar": []
            }
        }
    }

    online_field = {
        "lineNo": 1,
        "specNsType": "",
        "prod": "ARINNMLT10",
        "desc1": "ARL NMLT10 1\" NMLT PUSH",
        "desc2": "IN CONN",
        "unit": "EA",
        "price": 312,
        "discAmt": 0,
        "discType": "%",
        "netOrd": 402.48,
        "netAmt": 0,
        "sortFld": "2",
        "rushfl": False,
        "botype": "y",
        "promisedt": "2021-12-14",
        "reqshipdt": "2021-12-14",
        "ordertype": "",
        "orderaltno": 0,
        "tiedorder": "",
        "bono": 2,
    }

    @staticmethod
    def generate_resp_infor(data_infor, field_online, response):
        qty = data_infor.get('qty')
        qty_stk = data_infor.get('qty_stk')

        fields = [{'fieldName': k, 'fieldValue': v, 'seqNo': '1'} for k, v in data_infor.items()
                  if k in ['orderno', 'ordersuf', 'stage', 'custpo']]
        field_online.update({'qtyOrd': qty, 'qtyShip': qty, 'stkqtyord': qty_stk, 'stkqtyship': qty_stk})

        response['response']['tFieldlist']['t-fieldlist'] = fields
        response['response']['tOelineitemV3']['t-oelineitemV3'] = [field_online]

        return response

    @staticmethod
    def get_data_order_infor(order, data_infor):
        return [data for data in data_infor if str(order) == str(data.get('orderno'))][0]


if __name__ == '__main__':
    infor = GenerateInforOrderStatusV2()

    resp = infor.response
    online_field = infor.online_field

    x = {'orderno': '21982806', 'ordersuf': '03', 'stage': 'Pd', 'custpo': 'SRX VMI', 'qty': 50, 'qty_stk': 30}

    data_infor = [
        {'orderno': '21982806', 'ordersuf': '03', 'stage': 'Pd', 'custpo': 'SRX VMI', 'qty': 50, 'qty_stk': 30},
        {'orderno': '21982807', 'ordersuf': '03', 'stage': 'Pd', 'custpo': 'SRX VMI', 'qty': 40, 'qty_stk': 20},
    ]

    order = '21982806'

    # y = infor.generate_resp_infor(x, online_field, resp)
    # print(y)

    z = infor.get_data_order_infor(order, data_infor)
    print(z)
