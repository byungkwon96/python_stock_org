import json

with open("stocks_by_sectors.json") as f:
    companies_names_sectors = json.load(f)  # get stocks_by sectors

print(companies_names_sectors["001120"])
