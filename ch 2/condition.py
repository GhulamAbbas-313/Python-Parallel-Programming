import logging
import threading
import time
from random import randrange

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

# Shared resources
tasks = []
condition = threading.Condition()
MAX_TASKS = 10

# Calculator functions
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else "Error! Division by zero."

# Producer thread generates calculation tasks
class Producer(threading.Thread):
    def produce(self):
        with condition:
            if len(tasks) == MAX_TASKS:
                logging.info(f'Task queue full ({len(tasks)}). Waiting...')
                condition.wait()
            
            # Generate random calculation task
            a, b = randrange(1, 10), randrange(1, 10)
            op = randrange(1, 5)
            if op == 1: operator = '+'
            elif op == 2: operator = '-'
            elif op == 3: operator = '*'
            else: operator = '/'
            
            tasks.append((a, b, operator))
            logging.info(f'Produced task: {a} {operator} {b} | Queue size: {len(tasks)}')
            condition.notify()
    
    def run(self):
        for _ in range(20):
            time.sleep(0.5)
            self.produce()

# Consumer thread performs calculation tasks
class Consumer(threading.Thread):
    def consume(self):
        with condition:
            if len(tasks) == 0:
                logging.info('No tasks to consume. Waiting...')
                condition.wait()
            
            a, b, operator = tasks.pop(0)
            
            if operator == '+': result = add(a, b)
            elif operator == '-': result = subtract(a, b)
            elif operator == '*': result = multiply(a, b)
            else: result = divide(a, b)
            
            logging.info(f'Consumed task: {a} {operator} {b} = {result} | Queue size: {len(tasks)}')
            condition.notify()
    
    def run(self):
        for _ in range(20):
            time.sleep(2)
            self.consume()

def main():
    producer = Producer(name='Producer')
    consumer = Consumer(name='Consumer')

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()

if __name__ == "__main__":
    main()
