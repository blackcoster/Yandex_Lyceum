line = input()
dic = {}
while line != "That's all":
    dic[line] = dic.get(line, 0) + 1
    line = input()
print(dic)