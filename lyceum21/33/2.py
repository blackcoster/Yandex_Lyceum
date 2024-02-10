line = input()
dic = {}
for i in range(1,len(line)):
    if line[i-1]=='A':
        dic[line[i]] = dic.get(line[i], 0) + 1
print(dic)