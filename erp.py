import random
from __main__ import app

from flask import request

from billing import GenerateBilling as Billing
from d1_price import GetPricingD1
from eclipse_price import GetPricingEclipse as PriceEclipse
from electric import GetResponseGerrie as Gerrie
from infor import GenerateInforOrderStatusV2 as Infor
from infor_billing import GetBillingInfor
from infor_price import GetPricingInfor as PriceInfor
from infor_transfers import InforTransfers
from quote_eclipse import GenerateQuoteEclipse as EclipseQuote
from utils import UtilsServerIlx as ServUtils
from variables import *
from vmi import GenerateVmiList as Vmi
from quote_infor import GenerateQuoteInfor as InforQuote


@app.route('/external-api/test-full2/test-full2/syndicalist', methods=['GET'])
def vmi_list_sync():
    startIndex = request.args.get('startIndex')
    customerNumber = request.args.get('customerNumber')
    shipToNumber = request.args.get('shipToNumber')
    pageSize = request.args.get('pageSize')

    if startIndex is None or customerNumber is None or shipToNumber is None or pageSize is None:
        response = {
            "error": "error"
        }
        return response, 400
    else:
        response = {
            "results": [
                {
                    "dsku": "VIRTUAL 2",
                    "locationName1": "locationName",
                    "locationValue1": "value",
                    "csku": "VIRTUAL 2 updated2",
                    "min": 1,
                    "max": 101,
                    "id": "123"
                },
                {
                    "dsku": "BANANA DSKU",
                    "locationName1": "name",
                    "locationValue1": "value",
                    "csku": "Banana 98072376",
                    "min": 1,
                    "max": 99,
                    "id": "333"
                },
                {
                    "dsku": "APPLE DSKU",
                    "locationName1": "locationName 98072376",
                    "locationValue1": "value",
                    "csku": "Appl2",
                    "min": 1,
                    "max": 23,
                    "id": "234"
                },
                {
                    "dsku": "DERP",
                    "locationName1": "derp loc name 1",
                    "locationValue1": "loc value1",
                    "csku": "updated name derp(only 98072376)",
                    "min": 1,
                    "max": 11,
                    "id": "746837"
                },
                {
                    "dsku": "test",
                    "locationName1": "",
                    "locationValue1": "",
                    "csku": "ctest 98072376",
                    "min": 1,
                    "max": 11,
                    "id": "444"
                }

            ],
            "metadata": {
                "startIndex": int(startIndex),
                "pageSize": int(pageSize),
                "totalItems": 667
            }
        }
    return response, 200


# @app.route('/external-api/test-full2/test-full2', methods=['GET', 'POST'])
# def get_full2():
#     response = {
#         "data": [
#             "getPricing",
#             "quoteOrders",
#             "salesOrders",
#             "salesOrdersStatusV2",
#             "submitBilling",
#             "submitTransfer",
#             "submitBillingReturns",
#             "submitBillingDiscrepancies",
#             "vmilistsync",
#             "searchProduct",
#             "submitPma"
#         ],
#         "message": None,
#         "code": 200
#     }
#     return response


def random_int():
    return str(random.randint(100000, 999999))


@app.route('/external-api/test-full2/test-full2/<operation>', methods=['GET', 'POST'])
def sales_orders(operation):
    if operation == "salesOrders" or operation == "quoteOrders":
        transaction_type = "ORDERED" if operation == "salesOrders" else "QUOTED"
        body = request.get_json()
        ids = list()
        MIN = None
        if body is not None:
            if body.get("items") is not None:
                if isinstance(body["items"], list):
                    for item in body["items"]:
                        if "id" in item:
                            ids.append(item["id"])
                    if len(ids) > 0:
                        MIN = min(ids)
        response = {
            "transactionType": transaction_type,
            "id": MIN
        }
        return response
    elif operation == "getPricing":
        response = {
            "price": 100,
            "unitName": "EACH"
        }
        return response
    elif operation == "submitBilling":
        body = request.get_json()
        response = {
            "id": "issue" + random_int()
        }
        return response
    elif operation == "submitBillingDiscrepancies":
        body = request.get_json()
        response = {
            "id": random_int()
        }
        return response
    elif operation == "submitTransfer":
        body = request.get_json()
        response = {
            "id": random_int()
        }
        return response
    elif operation == "submitBillingReturns":
        body = request.get_json()
        response = {
            "id": "return" + random_int()
        }
        return response
    elif operation == "searchProduct":
        body = request.get_json()
        print('##################', body)

        if "dsku" in body:
            response = {
                "dsku": body["dsku"],
                "msku": "BT7LH-L0",
                "productExists": "true",
                "manufacturer": "PANDUIT CORP. TP-16",
                "roundBuy": "1",
                "labelDescription": "Label description",
                "shortDescription": "Short description",
                "upc": "02120043178"
            }
            return response
        else:
            response = {
                "sample-response"
            }
            return response


@app.route('/external-api/test-full2/test-full2/salesOrdersStatusV2', methods=['GET'])
def get_order_status_v2():
    args = request.args
    response = {
        "response": [
            {
                "id": f"{args['orderId']}",
                "release": "1",
                "transactionType": "ORDERED",
                "items": [
                    {
                        "dsku": "123",
                        "quantityOrdered": 30,
                        "quantityShipped": 0
                    },
                ]
            }
        ]
    }
    return response


@app.route('/external-api/test-full2/test-full2/SalesOrders/<order_id>', methods=['GET'])
def get_order(order_id):
    data = request.get_json()
    print(data)

    response = {
        "updateKey": "BDE70949B9362887889DD492808EA2B3",
        "id": order_id
    }

    error_response = {
        "error": "error"
    }

    if order_id == "SIQTE-42966-116440-001":
        generations, lines = ServUtils.create_data_order(data_case_1)
    elif order_id == "case2":
        generations, lines = ServUtils.create_data_order(data_case_2)
    elif order_id == "case3":
        generations, lines = ServUtils.create_data_order(data_case_3)
    elif order_id == "case4":
        generations, lines = ServUtils.create_data_order(data_case_4)
    elif order_id == "case5":
        generations, lines = ServUtils.create_data_order(data_case_5)
    elif order_id == "case6":
        generations, lines = ServUtils.create_data_order(data_case_6)
    elif order_id == "case7":
        generations, lines = ServUtils.create_data_order(data_case_7)
    elif order_id == "case8":
        generations, lines = ServUtils.create_data_order(data_case_8)
    elif order_id == "case10":
        generations, lines = ServUtils.create_data_order(data_case_10)
    elif order_id == "case11":
        generations, lines = ServUtils.create_data_order(data_case_11)
    else:
        return error_response, 400

    response.update({"generations": generations, "lines": lines})
    return response


@app.route('/external-api/test-full2/test-full2/sxapioegetsingleorderv3', methods=['GET', 'POST'])
def get_order_infor_qa():
    orderNumber = request.get_json().get('request').get('orderNumber')
    resp = Infor.response
    online_field = Infor.online_field

    response = {'error': f'orderNumber: {orderNumber} - not found'}

    for data in data_infor:
        if str(data.get('orderno')) == str(orderNumber):
            return Infor.generate_resp_infor(data, online_field, resp)

    return response, 400


@app.route('/external-api/test-full2/test-full2/CustomerPartNumbers', methods=['GET'])
def get_vmi_sync():
    customer_id = request.args['customerId']
    page_size = request.args['pageSize']

    print(f'customer_id: {customer_id}, page_size: {page_size}')

    response = {'error': f'incorrect data for customerId: {customer_id}'}

    for data in data_sync:
        if str(data['customerId']) == customer_id and str(data['pageSize']) == page_size:
            resp = Vmi().create_response_vmi(data)
            return resp

    return response, 400


@app.route('/fiix', methods=['GET', 'POST'])
def get_fiix():
    # print(f'data: {request}')
    response = {'message': f'it works'}

    return response, 400


@app.route('/external-api/test-full2/test-full2/', methods=['GET', 'POST'])
def get_fiix_new():
    # print(f'json: {request.json}')
    # print(f'json: {request}')
    response = {'message': 'it works'}

    if request.json:
        return response, 200
    else:
        return 'error', 400


@app.route('/external-api/test-full2/test-full2/vmilistsync', methods=['GET'])
def vmi_list_sync_test():
    startIndex = request.args.get('startIndex')
    customerNumber = request.args.get('customerNumber')
    pageSize = request.args.get('pageSize')
    if startIndex is None or customerNumber is None or pageSize is None:
        response = {
            "error": "error"
        }
        return response, 400
    else:
        response = {
            "results": [
                {
                    "dsku": "VIRTUAL 2",
                    "locationName1": "locationName 563356",
                    "locationValue1": "value222 656235",
                    "csku": "new virtual 4545434343454",
                    "min": 1,
                    "max": 33,
                    "id": "898"
                },
                {
                    "dsku": "BANANA DSKU",
                    "locationName1": "djdsfkf231",
                    "locationValue1": "djksjd31333333331",
                    "csku": "test banana73737",
                    "min": 1,
                    "max": 25,
                    "id": "434"
                },
                {
                    "dsku": "APPLE DSKU",
                    "locationName1": "stage22222ewedcd",
                    "locationValue1": "24",
                    "csku": "new Apple24242232",
                    "min": 1,
                    "max": 798,
                    "id": "232212"
                },
                {
                    "dsku": "DERP",
                    "locationName1": "stage",
                    "locationValue1": "324",
                    "csku": "new 75757",
                    "min": 1,
                    "max": 667,
                    "id": "2323"
                },
                {
                    "dsku": "test",
                    "locationName1": "",
                    "locationValue1": "",
                    "csku": "ctest erp223232",
                    "min": 1,
                    "max": 57,
                    "id": "2323121"
                },
                {
                    "dsku": "sync",
                    "locationName1": "34ddddddde3d",
                    "locationValue1": "er",
                    "csku": "sync erp2222",
                    "min": 1,
                    "max": 99,
                    "id": "3433"
                },
                {
                    "dsku": "sync2",
                    "locationName1": "12ololo",
                    "locationValue1": "39",
                    "csku": "new data eqwqwrp222",
                    "min": 1,
                    "max": 3767,
                    "id": "2323"
                },
                {
                    "dsku": "SKU_VALUE1",
                    "locationName1": "new namew",
                    "locationValue1": "wnew value",
                    "csku": "12345",
                    "min": 1,
                    "max": 2335,
                    "id": "34394"
                },
                {
                    "dsku": "Tomato",
                    "locationName1": "",
                    "locationValue1": "",
                    "csku": "tomato111",
                    "min": 1,
                    "max": 28,
                    "id": "34934"
                },
                {
                    "dsku": "Potato",
                    "locationName1": "Potato new location name",
                    "locationValue1": "Potato wnew location value",
                    "csku": "Potato sku222",
                    "min": 1,
                    "max": 28,
                    "id": "23"
                },
                {
                    "dsku": "Potato",
                    "locationName1": "Potato",
                    "locationValue1": "228",
                    "csku": "Potato ololo",
                    "min": 1,
                    "max": 28,
                    "id": "98765"
                },
                {
                    "dsku": "Cucumber",
                    "locationName1": "stage",
                    "locationValue1": "228",
                    "csku": "Cucumber Tea sku88383838",
                    "min": 1,
                    "max": 29,
                    "id": ""
                },
                {
                    "dsku": "Cucumber",
                    "locationName1": "c",
                    "locationValue1": "1",
                    "csku": "cucumber sku",
                    "min": 1,
                    "max": 29,
                    "id": "232323"
                },
                {
                    "dsku": "Testsync",
                    "locationName1": "test name2",
                    "locationValue1": "2",
                    "csku": "my Testsync sku2",
                    "min": 2,
                    "max": 22,
                    "id": ""
                }

            ],
            "metadata": {
                "startIndex": int(startIndex),
                "pageSize": int(pageSize),
                "totalItems": 10
            }
        }
    return response, 200


@app.route('/external-api/test-full2/test-full2/billing', methods=['GET', 'POST'])
def billing_line():
    """know request param"""
    # customer = request.get_json().get('records')[0].get('AcctSeed_Customer_c')
    # print('customer = ', customer)

    response = {'error': f"incorrect - data - for - customer: {request.url.split('/')[-1]}"}

    for data in data_billing:
        if data['customer'] in [request.url.split('/')[3], request.url.split('/')[4]]:
            resp = Billing().generate_resp_billing(data['number'])
            return resp

    return response, 400


@app.route('/external-api/test-full2/test-full2/pricing_eclipse', methods=['GET', 'POST'])
def price_eclipse():
    # customer = request.get_json().get('customerNumber')
    # qnt = request.get_json().get('dsku')

    print(request.content_type)

    customer = 100
    qnt = 200

    response = {'error': f'incorrect - data - for - customer: {customer}'}

    for data in data_price_eclipse:
        if data['customerNumber'] == customer:
            return PriceEclipse().create_rep_price_eclipse(customer, qnt)

    return response, 400


@app.route('/external-api/test-full2/test-full2/sxapioepricingv4', methods=['GET', 'POST'])
def price_infor():
    customer = request.get_json().get('request').get('customerNumber')
    response = {'error': f'incorrect - data - for - customer: {customer}'}

    for data in data_price_infor:
        if data['customerNumber'] == customer:
            return PriceInfor().create_rep_price_infor(data.get('price'), data.get('number'), data.get('name'))

    return response, 400


@app.route('/external-api/test-full2/test-full2/price/fetch/', methods=['GET', 'POST'])
def price_d1():
    customer = request.args.get('customer')
    print('customer')
    item = request.args.get('item')
    response = {'error': f'incorrect data for price_d1 - customer: {customer}, item: {item}'}

    for data in data_price_d1:
        if data.get('customer') == customer and data.get('item') == item:
            resp = GetPricingD1().create_resp_price_d1(item)
            return resp

    return response, 400


@app.route('/external-api/test-full2/test-full2/SalesOrders', methods=['GET', 'POST'])
def get_order_quote_eclipse():
    customer = request.get_json().get('customerPONumber')
    bill = request.get_json().get('shipToCustomer')

    response = {'error': f'incorrect data for test: customer - {customer}'}
    for data in data_quote_eclipse:
        if data['customer'] == customer or data['customer'] == bill:
            resp = EclipseQuote.create_response_quote_eclipse(data)
            return resp
    return response


@app.route('/external-api/test-full2/test-full2/sxapioefullordermntv6', methods=['GET', 'POST'])
def get_order_quote_infor():
    customer = request.get_json().get('request').get('sxt_shipto').get('sxt_shipto')[0].get('shipToNo')

    response = {'error': f'incorrect data for test: customer - {customer}'}
    for data in data_quote_infor:
        if data['custNo'] == str(customer):
            resp = InforQuote.create_response_quote_infor(data)
            return resp
    return response


@app.route('/external-api/test-full2/test-full2/oracle', methods=['GET', 'POST'])
def get_order_quote_error_oracle():
    response = {
        "error": "general decline"
    }

    return response


# @app.route('/external-api/test-full2/test-full2/create', methods=['GET', 'POST'])
# def get_order_quote_error_d1():
#     response = {
#         "error": "general decline"
#     }
#
#     return response


@app.route('/external-api/test-full2/test-full2/Quote/Create', methods=['GET', 'POST'])
def get_sales_order_error_oracle():
    response = {
        "QuoteNumber": "13510917QW00001",
        "TotalAmount": 345.88,
        "TaxAmount": 39.79,
        "FreightAmount": 0,
        "SubtotalAmount": 306.09,
        "ErrorCode": 0,
        "ErrorMessage": None,
        "OperationId": "00-b75ed489d75e6f4388a95272b91b909a-ceef6752d8cc4444-00",
        "FreightExplanation": "GlobalRate:10;CustFreight:0;T:0",
        "TaxAmounts": [
            39.7917
        ],
        "TaxCode": "hst",
        "PromotionCode": None,
        "PromotionAmount": None
    }

    return response


@app.route('/external-api/test-full2/test-full2/test', methods=['GET', 'POST'])
def get_order_history():
    customer_number = request.args['customerNumber']
    order_number = request.args['orderNumber']

    response = {'error': f'incorrect data for test: customer_number - {customer_number}, order_number - {order_number}'}

    for data in data_gerrie_electric:
        if data['orderNumber'] == order_number and data['customerNumber'] == customer_number:
            resp = Gerrie.generate_resp_gerrie(data)
            return resp

    return response, 400


@app.route('/external-api/test-full2/test-full2/sxapioefullordermntvbilling', methods=['GET', 'POST'])
def get_resp_infor_billing():
    data = request.get_json()
    ship_to_no = data.get("request").get("sxt_shipto").get("sxt_shipto")[0]
    sxt_item_v4 = data.get("request").get("sxt_itemV4").get("sxt_itemV4")[0]
    resp_data = dict(list(ship_to_no.items()) + list(sxt_item_v4.items()))

    if resp_data == data_infor_billing:
        resp = GetBillingInfor().create_resp_billing_infor(resp_data['shipToNo'])
        return resp
    else:
        resp = ServUtils.create_resp_error(resp_data, data_infor_billing)
        return resp, 400


# @app.route('/external-api/test-full2/test-full2/SalesOrders', methods=['GET', 'POST'])
# def get_sales_order_error_eclipse():
#     response = {
#         "error": "general decline"
#     }
#
#     return response

@app.route('/external-api/test-full2/test-full2/sxapiwtgetsingletransferorderv2', methods=['GET', 'POST'])
def get_infor_consignment_transfer():
    response = {
        "error": "incorrect-data-for-test"
    }

    data = request.get_json()
    data_resp = data_infor_transfers.copy()
    resp = InforTransfers.get_resp_infor_transfers(data_infor_transfers['cErrorMessage'])
    data_resp.pop('cErrorMessage')

    if data == data_resp:
        return resp
    else:
        return response, 400


@app.route('/external-api/test-full2/test-full2/Order/History', methods=['GET', 'POST'])
def get_sales_order_jd():
    response = {
        'Lines': {},
        'TaxAmounts': {},
        'Orders': {},
        'OperationId': '123',
        'ErrorCode': '',
        'ErrorMessage': ''
        }

    return response


@app.route('/external-api/test-search-icsw/test-search-icsw/', methods=['GET', 'POST'])
def search_product_icsw():
    data = request.get_json()
    prod = data['WhereClause'].split('=')[-1].replace("'", "").strip()

    response = {
        "ttblicsw": [
            {
                "arpvendno": 11171,
                "prod": prod,
                "prodline": "PAND",
                "vendprod": "BT7LH-L0",
                "whse": "7000",
            }
        ]
    }

    return response


@app.route('/external-api/test-search-apsv/test-search-apsv/', methods=['GET', 'POST'])
def search_product_apsv():
    response = {
        "ttblapsv": [
            {
                "name": "PANDUIT CORP. TP-16",
                "vendno": 11171,
            }
        ]
    }
    return response


@app.route('/external-api/test-search-apsv/test-search-icsp/', methods=['GET', 'POST'])
def search_product_icsp():
    response = {
        'ttblicsp': [
            {
                'user10': 'test',
                'sellmult': 1,
                "descrip": [
                    "PANDUITBT7LH-L0DOME-TOP",
                    "BARBTYCABLE"
                ]
            }
        ]
    }

    return response


@app.route('/external-api/test-search-apsv/test-search-icsv/', methods=['GET', 'POST'])
def search_product_icsv():
    # data = request.get_json()
    # print(data)

    response = {
        'ttblicsv': [
            {
                'section3': 1,
                'section4': 2
            }
        ]
    }

    return response


# @app.route('/external-api/seed-purchase-order/seed-purchase-order/', methods=['GET', 'POST'])
@app.route('/external-api/seed-purchase-order/seed-purchase-order/AcctSeedERP__Purchase_Order__c', methods=['GET', 'POST'])
def seed_purchase_order():
    data = request.get_json()
    print(data)

    # response = {
    #     "AcctSeedERP__Type__c": "Standard",
    #     "AcctSeedERP__Vendor__c": "0012E000028GUo7QAG",
    #     "AcctSeedERP__Comment__c": "ILX/Rest API Integration Test"
    # }

    response = {
        "success": True,
        "id": "0012E000028GUo7QAG",
    }

    return response


# @app.route('/external-api/seed-purchase-order/seed-purchase-order-line/', methods=['GET', 'POST'])
@app.route('/external-api/seed-purchase-order/seed-purchase-order-line/AcctSeedERP__Purchase_Order_Line__c',
           methods=['GET', 'POST'])
def seed_purchase_order_line():
    data = request.get_json()
    print(data)

    response = {
        'results': [
            {
                'id': '0012E000028GUo7QAG',
                'referenceId': '123'
            }
        ],
        'hasErrors': False
    }

    return response


# @app.route('/external-api/seed-purchase-order/seed-purchase-order-po-number/', methods=['GET', 'POST'])
@app.route('/external-api/seed-purchase-order/seed-purchase-order-po-number/AcctSeedERP__Purchase_Order__c/<sfOrderId>',
           methods=['GET', 'POST'])
def seed_purchase_order_po_number(sfOrderId):
    data = request.get_json()
    print(data)

    response = {
        "attributes": {
            "type": "AcctSeedERP__Purchase_Order__c",
            "url": "/services/data/v55.0/sobjects/AcctSeedERP__Purchase_Order__c/a1e4U00000EamBvQAJ"
        },
        "Name": "PO-00045",
        "Id": "a1e4U00000EamBvQAJ"
    }

    return response




