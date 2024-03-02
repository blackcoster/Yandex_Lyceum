with open('numbers.txt') as in_file, open('answer.txt', 'w') as out_file:
    line = in_file.readline().rstrip()
    count = 0
    template = '83?20*1*14?5'
    while line:
        if line[:3] == '83' and line[3:5] == '20' and line[-1] == '5' and \
                line[-4:-2] == '14' and ('1' in line[5:-4]):
            count += 1
        line = in_file.readline().rstrip()
    print(count, file = out_file)