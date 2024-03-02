with open('task.txt') as in_file:
    lines = [[int(x) for x in line.split()] for line in in_file]
    count = 0
    for item in lines:
        temp = item[:]
        temp.sort()
        if len(set(item)) == 3 and temp[0] < temp[1] and temp[-1] > temp[-2]:
            count += 1
    print(count)
