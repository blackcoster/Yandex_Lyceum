with open('data.txt') as in_file, open('answer.txt', 'w') as out_file:
    data = [int(x) for x in in_file]
    count = 0
    for i in range(1, len(data)):
        a, b = data[i - 1:i + 1]
        if a % 5 == 0 and b > a or b % 5 == 0 and a > b:
            count += 1
    print(count)
