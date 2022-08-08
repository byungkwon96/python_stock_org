import json

# organize text to dic
def stock_org(l):
    temp = {"name": l[2]}
    for i in range(3, len(l)):
        data = ""
        for j in range(i + 1, len(l)):
            if l[j] == "코스닥" or l[j] == "코스피":
                break
            data += " " + l[j]
        temp["industry"] = data
        temp["main-item"] = " ".join(l[j + 1 :])
        temp["market"] = l[j]
        break
    return (l[0], temp)


# read file and organize in dictionary format
dic = {}
with open("test.txt", "r") as f:
    for ls in f.readlines():
        l = ls.split()
        if len(l) > 2:
            name, temp = stock_org(l)
            dic[name] = temp

# write in file
with open("stocks_by_sectors.txt", "w") as f:
    f.write(json.dumps(dic, ensure_ascii=False, indent=6))
