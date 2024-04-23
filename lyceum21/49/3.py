f = s = 0


def supermoon(size):
    global f, s
    if f != 0 and s != 0 and size > s > f:
        res = 'Supermoon'
    else:
        res = 'Full moon'
    f, s = s, size
    return res
