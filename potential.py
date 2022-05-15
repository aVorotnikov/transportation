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


def get_shortest_loop(x, c, beginning):
    return []


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


def get_loop_min(x, loop):
    min = None
    num = 0
    for cell in loop:
        i, j = cell
        if x[i][j] is not None and num % 2 == 1 and (min is None or x[i][j] < min):
            min = x[i][j]
        num += 1
    return min


def correct(x, loop):
    sign = 1
    min = get_loop_min(x, loop)
    was_new_zero = False
    for cell in loop:
        i, j = cell
        if x[i][j] is None:
            x[i][j] = min
        else:
            x[i][j] = x[i][j] + sign * min
            if x[i][j] == 0 and not was_new_zero:
                was_new_zero = True
                x[i][j] = None
        sign *= -1


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
        correct(x, get_shortest_loop(x, c, cell))
        cell = get_next(x, a, b, c)
    return finalize(x)
