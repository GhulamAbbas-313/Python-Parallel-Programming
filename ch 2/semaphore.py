import logging
import threading
import time
import random

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

semaphore = threading.Semaphore(0)
task = None

# Calculator functions
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else "Error! Division by zero"

def consumer():
    global task
    logging.info('Consumer is waiting for a task')
    semaphore.acquire()  # wait until a task is produced
    if task:
        a, b, op = task
        if op == '+': result = add(a, b)
        elif op == '-': result = subtract(a, b)
        elif op == '*': result = multiply(a, b)
        else: result = divide(a, b)
        logging.info(f'Consumer executed task: {a} {op} {b} = {result}')

def producer():
    global task
    time.sleep(1)
    a, b = random.randint(1, 10), random.randint(1, 10)
    op = random.choice(['+', '-', '*', '/'])
    task = (a, b, op)
    logging.info(f'Producer generated task: {a} {op} {b}')
    semaphore.release()  # notify consumer

def main():
    for i in range(5):
        t_consumer = threading.Thread(target=consumer)
        t_producer = threading.Thread(target=producer)

        t_consumer.start()
        t_producer.start()

        t_consumer.join()
        t_producer.join()

if __name__ == "__main__":
    main()
