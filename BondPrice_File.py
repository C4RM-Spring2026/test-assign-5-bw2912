import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    n = int(m * ppy)
    r = y / ppy
    t = np.arange(1, n + 1)
    df = (1 + r) ** (-t)
    cf = np.full(n, face * couponRate / ppy)
    cf[-1] += face
    return np.dot(cf, df)
