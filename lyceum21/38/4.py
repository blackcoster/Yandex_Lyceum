import json

with open('question.json') as in_file, open('response.json', 'w') as out_file:
    lines = json.load(in_file)
    result = sum(sum(row) for row in lines) - lines[len(lines) // 2][len(lines[0]) // 2]
    lines[len(lines) // 2][len(lines[0]) // 2] = result
    json.dump(lines, out_file)