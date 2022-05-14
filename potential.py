import numpy as np


def check_end(x, c, u, v):
    for i in range(0, len(x)):
        for j in range(0, len(x[i])):
            if x[i][j] is None:
                if v[j] - u[i] > c[i][j]:
                    return False
            else:
                if v[j] - u[i] != c[i][j]:
                    return False
    return True


def finalize(x):
    for row in x:
        for i in range(0, len(row)):
            if row[i] is None:
                row[i] = 0
    return np.matrix(x)


def optimize(x_initial, a, b, c):
    x = np.copy(x_initial)
    u = np.zeros(len(a))
    v = np.zeros(len(b))
    while not check_end(x, c, u, v):
        pass
    return finalize(x)
