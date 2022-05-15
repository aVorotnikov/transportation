import numpy as np


def make_canon(a, b, c):
    min_task = list()
    for i in range(len(a)):
        for j in range(len(b)):
            min_task.append(c.item(i, j))

    b_vec = [a[i] if i < len(a) else b[i - len(a)] for i in range(len(a) + len(b))]
    a_matr = [[0 for i in range(len(a) * len(b))] for i in range (len(a) + len(b))]

    for i in range(0, len(a)):
        for j in range(0, len(b)):
            a_matr[i][i * len(b) + j] = 1

    for i in range(0, len(b)):
        for j in range(0, len(a)):
            a_matr[len(a) + i][i + j * len(b)] = 1

    return min_task, a_matr, b_vec