import numpy as np


def close(a, b, c):
    A = sum(a)
    B = sum(b)
    if A == B:
        print("Already closed")
        return
    if A > B:
        print("Need more resources")
        return
    print("Need more needs")
    return