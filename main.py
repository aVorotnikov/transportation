from get_task import get_task
from close import close

from north_west import generate_initial
from potential import optimize

from make_canon import make_canon
from ext_point_search import solve_brute_force


import numpy as np


try:
    print("GETTING TASK")
    a, b, c = get_task("task.txt")
    print("Resources: ", a)
    print("Needs: ", b)
    print("Costs:\n", c)
    print("CLOSING TASK")
    close(a, b, c)
    print("CHAINS")
    x_initial = generate_initial(a, b)
    print("Initial matrix:\n", x_initial)
    x = optimize(x_initial, a, b, c)
    print("Result:\n", x)
    sum = 0
    for i in range(0, len(x)):
        for j in range(0, len(x[i])):
            sum += x.item(i, j) * c.item(i, j)
    print("Total: ", sum)
    print("BRUTE-FORCE")
    c_canon, a_canon, b_canon = make_canon(a, b, c)
    a_canon.pop(len(a_canon) - 1)
    b_canon.pop(len(b_canon) - 1)
    sol, function = solve_brute_force(a_canon, b_canon, c_canon)
    sol = np.reshape(sol, (len(a), len(b)))
    print("Result:\n", sol)
    sum = 0
    for i in range(0, len(x)):
        for j in range(0, len(x[i])):
            sum += x.item(i, j) * c.item(i, j)
    print("Total: ", sum)
except Exception as error:
    print(error)
