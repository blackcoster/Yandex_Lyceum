dic = {}

def see_a_comet(name):
    dic[name] = dic.get(name, 0) + 1
    return dic[name]