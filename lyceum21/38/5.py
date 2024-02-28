import json

with open('factory.txt') as in_file, open('processes.json', 'w') as out_file:
    lines = [x.rstrip().split('\t') for x in in_file]
    dic = {}
    for item in lines:
        if len(item) > 2:
            ids, cost, depend = item
            depend = depend.split(', ')
        else:
            ids, cost = item
            depend = []
        dic[ids] = {
            "cost": int(cost),
            "dependencies": depend
        }
    json.dump(dic, out_file)