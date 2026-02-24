import numpy as np

def getBondDuration(y, face, couponRate, m, ppy=1):
    n = int(m * ppy)
    r = y / ppy
    t = np.arange(1, n + 1)
    df = (1 + r) ** (-t)
    cf = np.full(n, face * couponRate / ppy)
    cf[-1] += face
    pvcf = cf * df
    return np.dot(t, pvcf) / pvcf.sum() / ppy
