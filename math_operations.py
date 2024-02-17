###### made our own custom modules
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multi(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

def power(a, b):
    if b == 0:
        return 1
    else:
        return a ** b
