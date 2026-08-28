# Sample Python File

def greet(name):
    """Function to greet a person"""
    return f"Hello, {name}!"

def add_numbers(a, b):
    """Function to add two numbers"""
    return a + b

def factorial(n):
    """Function to calculate factorial"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

class Calculator:
    """Simple Calculator class"""
    
    def __init__(self):
        self.result = 0
    
    def add(self, x, y):
        self.result = x + y
        return self.result
    
    def subtract(self, x, y):
        self.result = x - y
        return self.result
    
    def multiply(self, x, y):
        self.result = x * y
        return self.result
    
    def divide(self, x, y):
        if y == 0:
            return "Cannot divide by zero"
        self.result = x / y
        return self.result

if __name__ == "__main__":
    # Test the functions
    print(greet("Srikanth"))
    print(f"5 + 3 = {add_numbers(5, 3)}")
    print(f"Factorial of 5 = {factorial(5)}")
    
    # Test the Calculator class
    calc = Calculator()
    print(f"10 + 5 = {calc.add(10, 5)}")
    print(f"10 - 5 = {calc.subtract(10, 5)}")
    print(f"10 * 5 = {calc.multiply(10, 5)}")
    print(f"10 / 5 = {calc.divide(10, 5)}")
