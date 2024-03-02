with open('sequence.txt') as in_file:
    numbers = [int(x) for x in in_file]
    count = 0
    max_count = 0
    s = 0
    max_s = 0

    for n in numbers:
        if n % 3 == 1:
            count += 1
            s += n
        else:
            if count > max_count or count == max_count and s > max_s:
                max_count = count
                max_s = s
            count = 0
            s = 0
    if count > max_count or count == max_count and s > max_s:
        max_count = count
        max_s = s
    print(max_s)