with open('lines.txt') as in_file, open('sequence.txt') as out_file:
    max_seq = ''
    for line in in_file:
        line = line.rstrip()
        if line.count('D') >= 5:
            temp = line.split('D')
            for item in temp:
                if len(item) > len(max_seq) or len(item) == len(max_seq) and item > max_seq:
                    max_seq = item
    print(max_seq, file=out_file)

