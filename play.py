import requests
import json

response = requests.get("https://finance.naver.com/api/sise/etfItemList.nhn")
data = json.loads(response.text)
dic = {}

for i in data["result"]["etfItemList"]:
    dic[i["itemcode"]] = {"itemname": i["itemname"], "total_num_stock": i["quant"]}


with open("./data/etf/etf_name.json", "w") as f:
    f.write(json.dumps(dic, ensure_ascii=False, indent=6))
