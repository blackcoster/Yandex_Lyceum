nuclears = {}
P, N = 1.00728, 1.00866


def mass_defect(p, n, el):
    return p*P + n*N - nuclears[el]