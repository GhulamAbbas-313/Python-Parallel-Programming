import multiprocessing

# Operation functions
def add(a, b):
    print(f"Addition: {a + b}")

def subtract(a, b):
    print(f"Subtraction: {a - b}")

def multiply(a, b):
    print(f"Multiplication: {a * b}")

def divide(a, b):
    if b != 0:
        print(f"Division: {a / b}")
    else:
        print("Error: Division by zero!")

if __name__ == "__main__":
    multiprocessing.freeze_support()  # Windows friendly

    print("=== Simple Multiprocessing Calculator ===")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    # Create processes for all 4 operations
    processes = [
        multiprocessing.Process(target=add, args=(a, b)),
        multiprocessing.Process(target=subtract, args=(a, b)),
        multiprocessing.Process(target=multiply, args=(a, b)),
        multiprocessing.Process(target=divide, args=(a, b))
    ]

    # Start all processes
    for p in processes:
        p.start()

    # Wait for all processes to finish
    for p in processes:
        p.join()

    print("All calculations done using multiprocessing ✅")
