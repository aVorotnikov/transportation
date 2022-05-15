import numpy as np
import copy


def get_potentials(x, a, b, c):
    u = np.zeros(len(a))
    v = np.zeros(len(b))

    A = [[0 for j in range(len(b) + len(a))] for i in range(len(b) + len(a))]
    b0 = [0 for i in range(len(b) + len(a))]

    A[0][0] = 1
    b0[0] = 0
    var = 1
    for i in range(0, len(a)):
        for j in range(0, len(b)):
            if x[i][j] is not None:
                A[var][i] = -1
                A[var][len(a) + j] = 1
                b0[var] = c.item(i, j)
                var = var + 1
    x = np.linalg.solve(A, b0)
    for i in range(len(a) + len(b)):
        if i < len(a):
            u[i] = x[i]
        else:
            v[i - len(a)] = x[i]

    return u, v


def get_next(x, a, b, c):
    u, v = get_potentials(x, a, b, c)
    delta = -1
    newStart = None
    for i in range(0, len(x)):
        for j in range(0, len(x[i])):
            if x[i][j] is None and v[j] - u[i] > c.item(i, j) and v[j] - u[i] - c.item(i, j) > delta:
                delta = v[j] - u[i] - c.item(i, j)
                newStart = (i, j)
    return newStart


def finalize(x):
    for row in x:
        for i in range(0, len(row)):
            if row[i] is None:
                row[i] = 0
    return np.matrix(x)


def optimize(x_initial, a, b, c):
    x = copy.deepcopy(x_initial)
    cell = get_next(x, a, b, c)
    while cell:
        cell = get_next(x, a, b, c)
    return finalize(x)
