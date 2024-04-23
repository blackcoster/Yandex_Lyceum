spectrum = {}

def elements(lines):
    res = []
    for element in spectrum:
        marker = True
        for wave in spectrum[element]:
            if wave not in lines:
                marker = False
                break
        if marker:
            res.append(element)
        return res
