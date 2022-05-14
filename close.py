import numpy as np


def close(a, b, c):
    VERI_BIG_NUMBER = 0xFFFFFFFF
    A = sum(a)
    B = sum(b)
    if A == B:
        print("Already closed")
        return
    if A > B:
        print("Need more resources")
        row = np.array([VERI_BIG_NUMBER for i in range(0, len(b))])
        c = np.vstack([c, row])
        a = np.append(a, A - B)
        print("Resources: ", a)
        print("Costs:\n", c)
        return
    print("Need more needs")
    column = np.array([VERI_BIG_NUMBER for i in range(0, len(a))])
    c = np.hstack([c, np.atleast_2d(column).T])
    b = np.append(b, B - A)
    print("Needs: ", b)
    print("Costs:\n", c)
    return