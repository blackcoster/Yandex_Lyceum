with open('stone.txt') as file:
    numbers = [[int(x) for x in line.split()] for line in file]
    result = []
    for i in range(len(numbers)):
        if numbers[i][0] >= numbers[i][1]:
            numbers[i][0] = numbers[i][1] - 1
            result.append((i, 0))
        if numbers[i][-1] >= numbers[i][-2]:
            numbers[i][-1] = numbers[i][-2] - 1
            result.append((i, len(numbers[0]) - 1))
        print(*numbers[i], sep='\t')
    for item in result:
        print(item)
