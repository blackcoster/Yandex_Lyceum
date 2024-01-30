numbers = input().split()
result = []
for n in numbers:
    while len(n) > 1:
        n = str(sum([int(x) for x in n]))
    result.append(n)
print('; '.join(result))