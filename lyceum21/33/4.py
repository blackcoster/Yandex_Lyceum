line = input()
dic = {}
for i in range(0,len(line) - 2 ):
    dic[line[i:i+3]] = dic.get(line[i:i+3],0) + 1
dic