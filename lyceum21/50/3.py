velocities = [0.9991, 0.993, 0.995, 0.9915]
tau = 2.2e-6
c = 3e8

def muon(dist):
    res = []
    for v in velocities:
        t = tau/ ((1- v**2))

    return res