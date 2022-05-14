from get_task import get_task


a, b, c = get_task("task.txt")
print("Need: ", a)
print("Suppliers: ", b)
print("Costs: \n", c)
