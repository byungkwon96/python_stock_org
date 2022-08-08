import requests
import json
import time

# BASE URL 네이버 파이낸스
BASE_URL = "https://api.finance.naver.com/service/itemSummary.nhn?itemcode="

# 오늘 날짜
l = time.ctime().split()
today = l[-1] + "_" + l[1] + "_" + l[2]

# lets try to find all the code number and save it into the list
stock_code = []  # 코스닥, 코스피 코드
with open("stock_codes.txt", "r") as f:
    stock_code = [l.rstrip("\n") for l in f]

# 날짜 파일에다 저장
data = {}  # 나중에 저장할 딕션어리 json (format)
with open(f"{today}.txt", "w") as f:
    for s in stock_code:
        url = BASE_URL + s
        response = requests.get(url)
        if response.status_code == 200:
            try:
                res = response.json()
                data[s] = res
            except:
                continue

    f.write(json.dumps(data, indent=6))
