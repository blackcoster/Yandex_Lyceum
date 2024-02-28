with open('magnetic.txt') as file:
    result = []
    for line in file:
        date, array = line.rstrip().split(': ')
        values = [int(x) for x in array.split()]
        average = sum(values) / len(values)
        temp = []
        for i in range(len(values)):
            if values[i] > average:
                temp.append(values[i])
            else:
                if len(temp) >= 3:
                    result.append(date)
                    temp = []
                    break
                temp = []
        if len(temp) >= 3:
            result.append(date)
        print('\n'.join(result))