import numpy as np


def eratosthenes(n):
    n = (n + 1) >> 1
    p = np.ones(n, dtype=np.int8)
    i, j = 1, 3

    while i < n:
        if p[i]:
            p[j * j >> 1::j] = 0
        i, j = i + 1, j + 2

    return p.sum()


print(eratosthenes(1000000))