import json
import heapq

with open("stocks_by_sectors.json") as f:
    companies_names_sectors = json.load(f)  # get stocks_by sectors

with open("./data/2022_Aug_8.json") as f:
    companies_info = json.load(f)

# organize data into 10 lowest per, 10 lowest pbr
per_l = []
personal_best = []

for k in companies_info.keys():
    temp_per = companies_info[k]["per"]
    if temp_per and temp_per < 7 and temp_per > 5:
        heapq.heappush(per_l, (temp_per, k))

    if (
        temp_per
        and temp_per > 0
        and companies_info[k]["pbr"]
        and companies_info[k]["pbr"] < 1
    ):
        heapq.heappush(personal_best, ((companies_info[k]["pbr"], temp_per, k)))

index = 0
while len(per_l) > 0 and index < 10:
    index += 1
    per, code = heapq.heappop(per_l)
    print(f"{index}. {companies_names_sectors[code]['name']}, per = {per}")


print("personal best")
index = 0
while len(personal_best) > 0 and index < 20:
    pbr_t, per_t, code = heapq.heappop(personal_best)
    index += 1
    print(
        f"{index}. {companies_names_sectors[code]['name']} = sectors: {companies_names_sectors[code]['industry']} \n per: {per_t} and pbr: {pbr_t}"
    )
