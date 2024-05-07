a, b, c, *rest = input().split()
result = [x for x in [a, b] + rest if not set(c) & set(x)]
print(*result, sep=', ')
