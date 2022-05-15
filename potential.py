import numpy as np

import copy
import enum


class EndType(enum.Enum):
    NONE = -1
    HORZ = 0
    VERT = 1


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


def get_pos_on_row(x, rec_lvls, pos_row,  pos_column):
    result = []
    for j in range(0, len(x[pos_row])):
        if x[pos_row][j] is not None and rec_lvls[pos_row][j] is None and j != pos_column:
            result.append((pos_row, j))
    return result


def get_pos_on_column(x, rec_lvls, pos_row,  pos_column):
    result = []
    for i in range(0, len(x)):
        if x[i][pos_column] is not None and rec_lvls[i][pos_column] is None and i != pos_row:
            result.append((i, pos_column))

    return result


def check_beginning_near(rec_lvls, pos_row, pos_column, rec_lvl):
    if rec_lvl < 3:
        return False

    for i in range(0, len(rec_lvls[pos_row])):
        if rec_lvls[pos_row][i] == 0 and i != pos_column:
            return True

    for i in range(0, len(rec_lvls)):
        if rec_lvls[i][pos_column] == 0 and i != pos_row:
            return True

    return False


def get_shortest_rec(x, rec_lvls, cur_point, from_where, rec_lvl, shortest_loop, cur_loop):
    rec_lvls[cur_point[0]][cur_point[1]] = rec_lvl
    cur_loop.append(cur_point)

    if check_beginning_near(rec_lvls, cur_point[0], cur_point[1], rec_lvl) and (len(shortest_loop) == 0 or len(shortest_loop) > len(cur_loop)):
        shortest_loop.clear()
        for cell in cur_loop:
            shortest_loop.append(cell)
    elif len(shortest_loop) == 0 or len(shortest_loop) > rec_lvl:
        if from_where != EndType.HORZ:
            ways = get_pos_on_row(x, rec_lvls, cur_point[0], cur_point[1])
            for way in ways:
                get_shortest_rec(x, rec_lvls, way, EndType.HORZ, rec_lvl + 1, shortest_loop, cur_loop)
        if from_where != EndType.VERT:
            ways = get_pos_on_column(x, rec_lvls, cur_point[0], cur_point[1])
            for way in ways:
                get_shortest_rec(x, rec_lvls, way, EndType.VERT, rec_lvl + 1, shortest_loop, cur_loop)

    rec_lvls[cur_point[0]][cur_point[1]] = None
    cur_loop.pop(len(cur_loop) - 1)


def get_shortest_loop(x, beginning):
    rec_lvls = [[None for j in range(0, len(x[i]))] for i in range(0, len(x))]
    shortest_loop = []
    cur_loop = []
    get_shortest_rec(x, rec_lvls, beginning, EndType.NONE, 0, shortest_loop, cur_loop)
    return shortest_loop


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
        loop = get_shortest_loop(x, cell)
        print("Loop: ", end="")
        for cell in loop:
            print(cell, "->", end=" ")
        print(loop[0])
        correct(x, loop)
        cell = get_next(x, a, b, c)
    return finalize(x)
