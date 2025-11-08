from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

num_runners = 3
finish_line = Barrier(num_runners)
runners = ['Huey', 'Dewey', 'Louie']

# Calculator functions
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b if b != 0 else "Error! Division by zero."

# Each runner performs a calculation
def runner():
    name = runners.pop()
    sleep(randrange(1, 4))
    # Random numbers and operation for demo
    a, b = randrange(1, 10), randrange(1, 10)
    op = randrange(1, 5)
    if op == 1:
        result = add(a, b)
        operation = f"{a} + {b}"
    elif op == 2:
        result = subtract(a, b)
        operation = f"{a} - {b}"
    elif op == 3:
        result = multiply(a, b)
        operation = f"{a} * {b}"
    else:
        result = divide(a, b)
        operation = f"{a} / {b}"
    
    print(f'{name} calculated: {operation} = {result} at {ctime()}')
    finish_line.wait()  # wait for other runners

def main():
    threads = []
    print('START CALCULATION RACE!!!!')
    for i in range(num_runners):
        threads.append(Thread(target=runner))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('All calculations are done!')

if __name__ == "__main__":
    main()
