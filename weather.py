import requests
import json
import pymongo
client = pymongo.MongoClient('localhost', 27017)
mydb = client["work"]
mycol = mydb["workpy"]
response = requests.get("https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-F495BF63-F249-4C4E-BED8-FE612E1BEEF1&format=JSON&elementName=&sort=time")
data=response.json()
l=data["records"]["location"]
records=[]
for la in l:
    for i in range(0,3):
        di={}    
        di["縣市名"]=la["locationName"]
        di["結束時間"]=la["weatherElement"][0]["time"][i]["endTime"]
        di["開始時間"]=la["weatherElement"][0]["time"][i]["startTime"]    
        di["狀態"]=la["weatherElement"][0]["time"][i]["parameter"]["parameterName"]
        di["降雨比例"]=la["weatherElement"][2]["time"][i]["parameter"]["parameterName"]
        di["低溫"]=la["weatherElement"][2]["time"][i]["parameter"]["parameterName"]
        di["舒適度"]=la["weatherElement"][3]["time"][i]["parameter"]["parameterName"]
        di["高溫"]=la["weatherElement"][4]["time"][i]["parameter"]["parameterName"]
        #print(a,st,et,b,c,d,e,f)
        records.append(di)        
print(records)
mycol.insert_many(records)

