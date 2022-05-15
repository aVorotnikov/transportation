import numpy as np


def generate_initial(a, b):
    x = [[None for j in range(0, len(b))] for i in range(0, len(a))]
    b0 = np.copy(b)

    for need in range(0, len(a)):
        val = a[need]
        for sup in range(0, len(b0)):
            if b0[sup] == 0:
                continue
            if b0[sup] < val:
                x[need][sup] = b0[sup]
                val -= b0[sup]
                b0[sup] = 0
            else:
                x[need][sup] = val
                b0[sup] -= val
                val = 0
                break
        if val != 0:
            raise Exception("Task cannot be solved")
    return x