import json

# load data from etf_name.json
etf_name = {}
with open("./data/etf/etf_name.json", "r") as f:
    etf_name = json.load(f)

# organize companies by etf creater
etf_companies = {}
for k, v in etf_name.items():
    names = v["itemname"].split()
    company = names[0]
    if company not in etf_companies.keys():
        etf_companies[company] = [k]
    else:
        etf_companies[company].append(k)


# sort the dictionary so faster in search
for k in etf_companies.keys():
    etf_companies[k].sort()

with open("./data/etf/sorted_etf_by_company.json", "w") as f:
    f.write(json.dumps(etf_companies, ensure_ascii=False, indent=6))
