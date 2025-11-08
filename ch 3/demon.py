import multiprocessing
import time
import random

# Calculator function
def calculator_task():
    name = multiprocessing.current_process().name
    print(f"Starting {name}\n")
    
    if name == 'background_process':
        # Perform 5 random additions
        for _ in range(5):
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            result = a + b
            print(f"[{name}] {a} + {b} = {result}")
            time.sleep(0.5)
    else:
        # Perform 5 random multiplications
        for _ in range(5):
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            result = a * b
            print(f"[{name}] {a} * {b} = {result}")
            time.sleep(0.5)
    
    print(f"Exiting {name}\n")

if __name__ == '__main__':
    background_process = multiprocessing.Process(
        name='background_process',
        target=calculator_task
    )
    background_process.daemon = False

    no_background_process = multiprocessing.Process(
        name='NO_background_process',
        target=calculator_task
    )
    no_background_process.daemon = False

    background_process.start()
    no_background_process.start()

    background_process.join()
    no_background_process.join()
