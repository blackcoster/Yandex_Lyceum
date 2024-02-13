dic = {}
for _ in range(int(input())):
    num, theme = input().split(' - ')
    num = int(num)
    dic[theme] = dic.get(theme, []) + [num]
    dic[theme].sort()
names = sorted(dic)
for name in names:
    print(f"{name}: {', '.join([str(x) for x in dic[name]])}")
