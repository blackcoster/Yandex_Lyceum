def factorization(n):
    res = []
    divisor = 2
    while n != 1:
        while n % divisor == 0:
            res.append(divisor)
            n = n // divisor
        divisor += 1
    return res
