def shifts(line, n):
    s = line[n % len(line):] + line[:n % len(line)]
    return s

print(shifts('TheQuickBrownFoxJumpsOverTheLazyDog',3))