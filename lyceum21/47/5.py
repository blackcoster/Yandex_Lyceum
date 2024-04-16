def triangle_square(a, b, c):
    side_a = distance(a, b)
    side_b = distance(b, c)
    side_c = distance(a, c)
    p = (side_a + side_b + side_c) / 2
    s = (p * (-side_a + p) * (-side_b + p) * (-side_c + p)) ** 0.5
    return s


def distance(m, n):
    return ((m[0] - n[0]) ** 2 + (m[1] - n[1]) ** 2) ** 0.5


