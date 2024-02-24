with open('lines.txt', encoding='utf8') as in_file, \
        open('transformed_lines.txt', 'w', encoding='utf8') as out_file:
    for item in in_file:
        line = item.rstrip()
        if len(line) % 3 == 0 and len(line) % 5 == 0:
            print(line.title(), file=out_file)
        elif len(line) % 3 == 0:
            print(line.upper(), file=out_file)
        elif len(line) % 5 == 0:
            print(line.lower(), file=out_file)
        else:
            print(line.swapcase(), file=out_file)