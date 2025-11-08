import threading
import time
import random

class CalculatorBox:
    def __init__(self):
        self.lock = threading.RLock()
        self.total = 0

    def execute(self, value, operator):
        with self.lock:
            if operator == '+':
                self.total += value
            elif operator == '-':
                self.total -= value
            elif operator == '*':
                self.total *= value
            elif operator == '/':
                if value != 0:
                    self.total /= value
                else:
                    print("Division by zero ignored")
            print(f"Performed {operator} {value} --> Total: {self.total}")

    def add(self, value):
        self.execute(value, '+')

    def subtract(self, value):
        self.execute(value, '-')

    def multiply(self, value):
        self.execute(value, '*')

    def divide(self, value):
        self.execute(value, '/')

def adder(box, operations):
    print(f"{len(operations)} operations to ADD\n")
    for value in operations:
        box.add(value)
        time.sleep(1)

def subtractor(box, operations):
    print(f"{len(operations)} operations to SUBTRACT\n")
    for value in operations:
        box.subtract(value)
        time.sleep(1)

def main():
    box = CalculatorBox()
    add_ops = [random.randint(1, 10) for _ in range(5)]
    sub_ops = [random.randint(1, 5) for _ in range(5)]

    t1 = threading.Thread(target=adder, args=(box, add_ops))
    t2 = threading.Thread(target=subtractor, args=(box, sub_ops))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f"Final Total: {box.total}")

if __name__ == "__main__":
    main()
