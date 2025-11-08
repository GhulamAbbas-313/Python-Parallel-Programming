import multiprocessing
import time
import random

# Calculator function
def calculator_task():
    print('Starting calculator task')
    for i in range(10):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        op = random.choice(['+', '-', '*', '/'])
        
        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        else:
            result = a / b if b != 0 else "Error! Division by zero"
        
        print(f'Calculation {i}: {a} {op} {b} = {result}')
        time.sleep(1)
    
    print('Finished calculator task')

if __name__ == '__main__':
    p = multiprocessing.Process(target=calculator_task)
    
    print('Process before execution:', p, p.is_alive())
    p.start()
    print('Process running:', p, p.is_alive())
    
    # Terminate process after 3 seconds
    time.sleep(3)
    p.terminate()
    print('Process terminated:', p, p.is_alive())
    
    p.join()
    print('Process joined:', p, p.is_alive())
    print('Process exit code:', p.exitcode)
