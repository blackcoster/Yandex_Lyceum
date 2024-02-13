dic = {}
for i in range(int(input())):
    a, b = input().split()
    a = int(a)
    b = float(b)
    dic[a] = dic.get(a, []) + [b]

result = [(k, round(sum(v) / len(v), 1)) for k, v in dic.items()]
result.sort()
for a, b in result:
    print(a, b)
