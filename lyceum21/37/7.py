with open('mushroom_place.txt') as in_file:
    dic = {}
    data = [x.rstrip() for x in in_file.readlines()]
    for i in range(0, len(data), 2):
        name, count = data[i:i + 2]
        dic[name] = dic.setdefault(name, 0) + int(count)
    print(dic)