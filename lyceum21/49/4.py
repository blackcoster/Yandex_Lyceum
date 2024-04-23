sensor = tuple()


def annihilation(mode, charge, mass):
    global sensor
    if sensor:
        if mode == sensor[0] and charge == -sensor[1] and mass == sensor[2]:
            res = 2 * mass * 931.5
            sensor = tuple()
        else:
            res = 0
            sensor = mode, charge, mass
        return res
    sensor = mode, charge, mass
    return 0
