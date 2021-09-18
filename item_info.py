import requests
import os
from pprint import pprint
from common import execute_api
import numpy as np
import pandas as pd
import eel

EXP_CSV_PATH = "./{dir_name}/{csv_name}"
API_Endpoint = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706'
ApplicationId = 1089791896465980338


def get_name_and_price(keyword,ng_keyword,sort,dir_name,csv_name):
    max_page = 10
    item_list = []
    os.makedirs(dir_name,exist_ok=True)
    for page in range(1,max_page+1):
        params = {
            'keyword' : keyword,
            "NGKeyword":ng_keyword,
            'applicationId': ApplicationId,
            'format':'json',
            'hits':30,
            'page':page,
            'sort':sort
        }
        res = execute_api(API_Endpoint, params)
        result = res.json()
        for obj in result["Items"]:
            text = f'{obj["Item"]["itemName"]}'
            eel.view_picture(text)

        birth_list = ['itemName','itemPrice','itemCaption','itemUrl','postageFlag','shopName','shopCode','shopUrl']
        for i in range(0,len(result['Items'])):
            item_dict = {}
            elements = result['Items'][i]['Item']
            for key,value in elements.items():
                if key in birth_list:
                    item_dict[key] = value
            item_list.append(item_dict.copy())
        
        data = pd.DataFrame(item_list)
        data = data.reindex(columns=['itemName','itemPrice','itemUrl','itemCaption','postageFlag','shopName','shopCode','shopUrl'])
        data.columns = ['商品名', '値段', '商品url','商品説明','0:送料無し,1:送料あり','店舗名','店舗コード','店舗url']
        header = False if os.path.exists(EXP_CSV_PATH.format(dir_name=dir_name,csv_name=csv_name))else True
        data.to_csv(EXP_CSV_PATH.format(dir_name=dir_name,csv_name=csv_name),mode='a',index=False,header=header,encoding='utf_8_sig')
    
def get_name_and_price_no_ng_keyword(keyword,sort,dir_name,csv_name):
    max_page = 10
    item_list = []
    os.makedirs(dir_name,exist_ok=True)
    for page in range(1,max_page+1):
        params = {
            'keyword' : keyword,
            'applicationId': ApplicationId,
            'format':'json',
            'hits':30,
            'page':page,
            'sort':sort
        }
        res = execute_api(API_Endpoint, params)
        result = res.json()
        for obj in result["Items"]:
            text = f'{obj["Item"]["itemName"]}'
            eel.view_picture(text)

        birth_list = ['itemName','itemPrice','itemCaption','itemUrl','postageFlag','shopName','shopCode','shopUrl']
        for i in range(0,len(result['Items'])):
            item_dict = {}
            elements = result['Items'][i]['Item']
            for key,value in elements.items():
                if key in birth_list:
                    item_dict[key] = value
            item_list.append(item_dict.copy())
        
        data = pd.DataFrame(item_list)
        data = data.reindex(columns=['itemName','itemPrice','itemUrl','itemCaption','postageFlag','shopName','shopCode','shopUrl'])
        data.columns = ['商品名', '値段', '商品url','商品説明','0:送料無し,1:送料あり','店舗名','店舗コード','店舗url']
        header = False if os.path.exists(EXP_CSV_PATH.format(dir_name=dir_name,csv_name=csv_name))else True
        data.to_csv(EXP_CSV_PATH.format(dir_name=dir_name,csv_name=csv_name),mode='a',index=False,header=header,encoding='utf_8_sig')

# if __name__ == "__main__":
#     keyword = input('検索キーワードを入力して下さい:')
#     csv_name = input('csvファイル名を入力して下さい')
#     dir_name = input('フォルダ名を指定してください')
#     ng_keyword = input('ngキーワードを入力して下さい')
#     sort = 'standard'

#     get_name_and_price(keyword,ng_keyword,sort,dir_name,csv_name)



    

