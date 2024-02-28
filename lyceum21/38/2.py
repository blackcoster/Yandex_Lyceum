import json

with open('strings.json') as in_file:
    lines = json.load(in_file)
    average = sum([len(x) for x in lines]) / len(lines)
    result = [x for x in lines if len(x) >= average]
    result.sort()
    print(', '.join(result))