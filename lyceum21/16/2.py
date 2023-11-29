n = int(input())

a, b, c, d = n // 1000, n // 100 % 10, n // 10 % 10, n % 10

mi = min(a, b, c, d)
ma = max(a, b, c, d)

if a == mi and b == ma or b == mi and a == ma:
    print(b * 1000 + a * 100 + c * 10 + d)
elif a == mi and c == ma or c == mi and a == ma:
    print(c * 1000 + b * 100 + a * 10 + d)
elif a == mi and d == ma or d == mi and a == ma:
    print(d * 1000 + b * 100 + c * 10 + a)
elif b == mi and c == ma or c == mi and b == ma:
    print(a * 1000 + c * 100 + b * 10 + d)
elif b == mi and d == ma or d == mi and b == ma:
    print(a * 1000 + d * 100 + c * 10 + b)
elif c == mi and d == ma or d == mi and c == ma:
    print(a * 1000 + b * 100 + d * 10 + c)
