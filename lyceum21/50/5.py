measures = []

def aliens(a,b,c):
    greatest = max(measures) if measures else 1
    if max(a,b,c) / min(a,b,c) > 10 * greatest:
        res = 'Strangely'
    else:
        res = 'Typically'
    measures.append(max(a,b,c) / min(a,b,c))
    return res