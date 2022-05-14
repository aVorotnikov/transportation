from get_task import get_task
from north_west import generate_initial

try:
    a, b, c = get_task("task.txt")
    print("Need: ", a)
    print("Suppliers: ", b)
    print("Costs:\n", c)
    x_initial = generate_initial(a, b)
    print("Initial matrix:\n", x_initial)
except Exception as error:
    print(error)
