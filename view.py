import eel
import desktop
import item_info


app_name="html"
end_point="main.html"
size=(2250,1500)

@eel.expose
def get_name_and_price(keyword,ng_keyword,sort,dir_name,csv_name):
    item_info.get_name_and_price(keyword,ng_keyword,sort,dir_name,csv_name)

@eel.expose
def get_name_and_price_no_ng_keyword(keyword,sort,dir_name,csv_name):
    item_info.get_name_and_price_no_ng_keyword(keyword,sort,dir_name,csv_name)


desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)