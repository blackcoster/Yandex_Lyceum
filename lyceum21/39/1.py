with open('numbers.txt') as in_file:
    data = [int(x) for x in in_file]
    count = 0
    for i in range(1, len(data)):
        a, b = data[i - 1:i + 1]
        if a % 2 != b % 2:
            count += 1
    print(count)
