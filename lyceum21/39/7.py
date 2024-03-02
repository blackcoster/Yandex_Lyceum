with open('numbers.txt') as in_file:
    line = in_file.readline().rstrip()
    k44 = 0  # количество чисел, которые делятся на 21
    k22 = 0  # количество чисел, которые не делятся на 21, но делятся на 7
    k11 = 0  # количество чисел, которые не делятся на 21, но делятся на 3
    k4 = 0
    k2 = 0

    count = 0
    while line:
        n = int(line)
        count += 1
        if n % 44 == 0:
            k44 += 1
        elif n % 22 == 0:
            k22 += 1
        elif n % 11 == 0:
            k11 += 1
        elif n % 4 == 0:
            k4 += 1
        elif n % 2 == 0:
            k2 += 1
        line = in_file.readline().rstrip()
    print(k44*(count-k44) + k44*(k44-1)//2 + k22*(k2+k4) + k22*(k22-1)//2 + k11*k4)
