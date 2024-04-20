def multipliers(n):
    arr = []
    divisor = 2
    while n != 1:
        count = 0
        while n % divisor == 0:
            n = n // divisor
            count += 1
        if count > 0:
            arr.append((divisor, count))
        divisor += 1
    return arr
