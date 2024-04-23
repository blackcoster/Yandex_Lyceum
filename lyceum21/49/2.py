G = 6.67e-11
M = 1.99e+30
PI = 3.14159


def nemesis(t):
    return (t ** 2 * G * M / (4 * PI ** 2)) ** (1 / 3)
