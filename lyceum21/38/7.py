import json

with open('names.json', encoding='utf-8') as in_file, open('data.json', 'w', encoding='utf-8') as out_file:
    lines = json.load(in_file)
    dic = {}

    for i, item in enumerate(lines, 1):
        sur, name, age = item.split()
        dic[i] = {'surname': sur,
                  'name': name,
                  'age': int(age)}
        json.dump(dic, out_file, ensure_ascii=False)
