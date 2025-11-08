import multiprocessing
import random

# Calculator functions
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else "Error! Division by zero"

# First process: create calculator tasks
def create_tasks(pipe):
    output_pipe, _ = pipe
    operators = ['+', '-', '*', '/']
    for _ in range(10):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        op = random.choice(operators)
        output_pipe.send((a, b, op))
    output_pipe.close()

# Second process: perform calculation
def execute_tasks(input_pipe, output_pipe):
    close, in_pipe = input_pipe
    close.close()
    out_pipe, _ = output_pipe
    try:
        while True:
            a, b, op = in_pipe.recv()
            if op == '+': result = add(a, b)
            elif op == '-': result = subtract(a, b)
            elif op == '*': result = multiply(a, b)
            else: result = divide(a, b)
            out_pipe.send(f'{a} {op} {b} = {result}')
    except EOFError:
        out_pipe.close()

if __name__ == '__main__':
    # Pipe 1: tasks from creator to executor
    pipe_1 = multiprocessing.Pipe(True)
    process_1 = multiprocessing.Process(target=create_tasks, args=(pipe_1,))
    process_1.start()

    # Pipe 2: results from executor to main process
    pipe_2 = multiprocessing.Pipe(True)
    process_2 = multiprocessing.Process(target=execute_tasks, args=(pipe_1, pipe_2))
    process_2.start()

    # Close unused ends in main
    pipe_1[0].close()
    pipe_2[0].close()

    try:
        while True:
            print(pipe_2[1].recv())
    except EOFError:
        print("All tasks completed.")
