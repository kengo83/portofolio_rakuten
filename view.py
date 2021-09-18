import eel
import desktop
import item_info
from common import execute_api

API_Endpoint = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706'
ApplicationId = 1089791896465980338

app_name="html"
end_point="main.html"
size=(2250,1500)

@eel.expose
def get_name_and_price(keyword,ng_keyword,sort,dir_name,csv_name):
    item_info.get_name_and_price(keyword,ng_keyword,sort,dir_name,csv_name)

@eel.expose
def create_each_list(keyword,ng_keyword,sort):
    max_page = 10
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
        picture_list = []
        names_list = []
        urls_list = []
        for obj in result["Items"]:
            picture_url = obj["Item"]["smallImageUrls"][0]
            picture_list.append(picture_url)
            names = obj["Item"]["itemName"]
            names_list.append(names)
            urls = obj["Item"]["itemUrl"]
            urls_list.append(urls)
        pic_url = [p.get('imageUrl') for p in picture_list]
        items = dict(zip(pic_url,urls_list))
        print(items)
        return items,names_list
    
    
@eel.expose
def get_name_and_price_no_ng_keyword(keyword,sort,dir_name,csv_name):
    item_info.get_name_and_price_no_ng_keyword(keyword,sort,dir_name,csv_name)

@eel.expose
def create_list_no_ng_keyword(keyword,sort):
    max_page = 10
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
        picture_list = []
        names_list = []
        urls_list = []
        for obj in result["Items"]:
            picture_url = obj["Item"]["smallImageUrls"][0]
            picture_list.append(picture_url)
            names = obj["Item"]["itemName"]
            names_list.append(names)
            urls = obj["Item"]["itemUrl"]
            urls_list.append(urls)
        pic_url = [p.get('imageUrl') for p in picture_list]
        items = dict(zip(pic_url,urls_list))
        return items,names_list
    


desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)