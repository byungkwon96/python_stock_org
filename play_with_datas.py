import json
import heapq

with open("stocks_by_sectors.json") as f:
    companies_names_sectors = json.load(f)  # get stocks_by sectors

with open("./data/2022_Aug_8.json") as f:
    companies_info = json.load(f)
