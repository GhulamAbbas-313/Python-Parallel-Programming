import multiprocessing
import time
import random

# Calculator function
def calculator_task():
    name = multiprocessing.current_process().name
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    op = random.choice(['+', '-', '*', '/'])
    
    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    elif op == '/':
        result = a / b if b != 0 else "Error! Division by zero"

    print(f"[{name}] Starting calculation: {a} {op} {b}")
    time.sleep(2)
    print(f"[{name}] Result: {a} {op} {b} = {result}\n")

if __name__ == '__main__':
    # Named process
    process_named = multiprocessing.Process(
        name='Calculator Process 1',
        target=calculator_task
    )

    # Default name process
    process_default = multiprocessing.Process(target=calculator_task)

    process_named.start()
    process_default.start()

    process_named.join()
    process_default.join()
