n = int(input())
dic = {}
for i in range(n):
    commands, bill = input().split()
    c1, c2 = commands.split('-')
    b1, b2 = [int(x) for x in bill.split(':')]
    if b1 > b2:
        dic[c1] = dic.get(c1,0) + 3
    elif b1 == b2:
        dic[c1] = dic.get(c1,0) + 1
        dic[c2] = dic.get(c2, 0) + 1
    else:
        dic[c2] = dic.get(c2, 0) + 3
print(dic)