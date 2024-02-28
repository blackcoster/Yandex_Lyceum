import json

line = [int(x) for x in input().split()]
dic = {}
for n in line:
    dic[n] = dic.get(n, 0) + 1
with open('counting.json', 'w') as file:
    json.dump(dic, file)