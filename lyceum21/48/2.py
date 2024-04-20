from math import pi


def arc(r, a):
    l = pi * r * a / 180
    s = pi * r ** 2 * a / 360
    return l, s
