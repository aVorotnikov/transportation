from get_task import get_task
from close import close
from north_west import generate_initial
from potential import optimize


try:
    a, b, c = get_task("task.txt")
    print("Resources: ", a)
    print("Needs: ", b)
    print("Costs:\n", c)
    close(a, b, c)
    x_initial = generate_initial(a, b)
    print("Initial matrix:\n", x_initial)
    x = optimize(x_initial, a, b, c)
    print("Result:\n", x)
except Exception as error:
    print(error)
