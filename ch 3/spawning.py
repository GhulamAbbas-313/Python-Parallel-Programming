import multiprocessing
import random

# Calculator function
def calculator(task_id, a, b, op):
    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    elif op == '/':
        result = a / b if b != 0 else "Error! Division by zero"
    print(f'Process {task_id}: {a} {op} {b} = {result}')

if __name__ == '__main__':
    operators = ['+', '-', '*', '/']

    for i in range(6):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        op = random.choice(operators)

        process = multiprocessing.Process(target=calculator, args=(i, a, b, op))
        process.start()
        process.join()
