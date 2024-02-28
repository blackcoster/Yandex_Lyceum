import json

with open('numbers.json') as in_file, open('ready.json', 'w') as out_file:
    lines = json.load(in_file)
    result = list(set(lines))
    result.sort(reverse=True)
    json.dump(result, out_file)