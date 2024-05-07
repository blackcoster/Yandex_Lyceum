K, B = -1.5, 6


def below(*args):
    result = []
    for arg in args:
        x, y = arg
        if y < x * K + B:
            result.append(arg)

    return sorted(result)