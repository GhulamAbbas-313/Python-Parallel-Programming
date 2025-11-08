import logging
import threading
import time
import random

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

tasks = []
event = threading.Event()

# Calculator functions
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else "Error! Division by zero."

class Consumer(threading.Thread):
    def run(self):
        while True:
            time.sleep(2)
            event.wait()  # wait until producer sets event
            if tasks:     # check if any task exists
                a, b, operator = tasks.pop(0)
                
                if operator == '+': result = add(a, b)
                elif operator == '-': result = subtract(a, b)
                elif operator == '*': result = multiply(a, b)
                else: result = divide(a, b)
                
                logging.info(f'Consumer executed: {a} {operator} {b} = {result}')
            else:
                logging.info('No tasks to consume.')

class Producer(threading.Thread):
    def run(self):
        for _ in range(10):
            time.sleep(2)
            a, b = random.randint(1, 10), random.randint(1, 10)
            operator = random.choice(['+', '-', '*', '/'])
            tasks.append((a, b, operator))
            logging.info(f'Producer generated task: {a} {operator} {b}')
            event.set()    # notify consumer
            event.clear()  # reset for next task

if __name__ == "__main__":
    t1 = Producer(name='Producer')
    t2 = Consumer(name='Consumer')

    t1.start()
    t2.start()

    t1.join()
    # t2 runs infinitely; you can stop it after some time if needed
