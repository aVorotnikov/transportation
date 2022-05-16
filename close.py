import numpy as np


def close(a, b, c):
    A = sum(a)
    B = sum(b)
    if A == B:
        print("Already closed")
        return a, b, c
    if A < B:
        print("Need more resources")
        row = np.array([0 for i in range(0, len(b))])
        c = np.vstack([c, row])
        a = np.append(a, B - A)
        print("Resources: ", a)
        print("Costs:\n", c)
        return a, b, c
    print("Need more needs")
    column = np.array([0 for i in range(0, len(a))])
    c = np.hstack([c, np.atleast_2d(column).T])
    b = np.append(b, A - B)
    print("Needs: ", b)
    print("Costs:\n", c)
    return a, b, c