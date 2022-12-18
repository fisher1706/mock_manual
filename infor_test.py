import requests
from utils import UtilsServerIlx
from variables import data_infor

headers = {'Authorization': 'a552945a85364af89653fe94d91bd57f'}
url = 'https://api.qa.integrationlogix.com/external-api/a568e5d3-38d4-4cd1-9aa1-3484afa78a0f/' \
      'infor_final/infor_final'

if __name__ == '__main__':

    for data in data_infor:
        order_id = data.get('orderno')
        resp = requests.get(url=UtilsServerIlx.generate_url(url, case=order_id), headers=headers)
        # print(resp.json())
        print(resp)
