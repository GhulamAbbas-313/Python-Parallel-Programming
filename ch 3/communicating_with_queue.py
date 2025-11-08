import multiprocessing
import random
import time

# Calculator functions
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else "Error! Division by zero"

class Producer(multiprocessing.Process):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        operators = ['+', '-', '*', '/']
        for _ in range(10):
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            op = random.choice(operators)
            task = (a, b, op)
            self.queue.put(task)
            print(f'Producer {self.name}: Task {a} {op} {b} added to queue')
            time.sleep(1)
            print(f'Queue size: {self.queue.qsize()}')

class Consumer(multiprocessing.Process):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            if self.queue.empty():
                print("Queue is empty, consumer exiting.")
                break
            else:
                task = self.queue.get()
                a, b, op = task
                if op == '+': result = add(a, b)
                elif op == '-': result = subtract(a, b)
                elif op == '*': result = multiply(a, b)
                else: result = divide(a, b)
                print(f'Consumer {self.name}: {a} {op} {b} = {result}')
                time.sleep(1)

if __name__ == '__main__':
    queue = multiprocessing.Queue()
    process_producer = Producer(queue)
    process_consumer = Consumer(queue)

    process_producer.start()
    process_consumer.start()

    process_producer.join()
    process_consumer.join()
