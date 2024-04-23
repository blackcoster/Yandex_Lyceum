count = -1


def comet_bang():
    global count
    count += 1
    abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return f'A fragment {abc[count]} has fallen'
