import multiprocessing
import random

# Calculator function
def calculator(task):
    a, b, op = task
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b if b != 0 else "Error! Division by zero"

if __name__ == '__main__':
    # Generate 20 random calculator tasks
    operators = ['+', '-', '*', '/']
    tasks = [(random.randint(1, 10), random.randint(1, 10), random.choice(operators)) for _ in range(20)]

    # Use a pool of 4 processes to calculate in parallel
    pool = multiprocessing.Pool(processes=4)
    results = pool.map(calculator, tasks)

    pool.close()
    pool.join()

    # Print results
    for task, result in zip(tasks, results):
        a, b, op = task
        print(f'{a} {op} {b} = {result}')
