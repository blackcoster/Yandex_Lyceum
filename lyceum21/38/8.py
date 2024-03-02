import json

with open('names.txt', encoding='utf8') as in_file, open('cities.json', 'w', encoding='utf8') as out_file:
    cities = [x.rstrip() for x in in_file]
    dic = {}
    for city in cities:
        dic[city[0]] = dic.setdefault(city[0],[]) + [city]
        dic[city[0]].sort()
    json.dump(dic, out_file, ensure_ascii=False)

