def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b != 0:
        return a / b
    else:
        return 'Error: Division by zero is not allowed.'

def power_number(a, b):
    return a ** b

def sqrt_number(a):
    return a ** 0.5

if __name__ == "__main__":
    print("Adding:", add_numbers(2,4))
    print("Subtracting:", subtract_numbers(9,2))
    print("Multiplying:", multiply_numbers(2,4))
    print("Dividing:", divide_numbers(10,2))
    print("Power:", power_number(2,3))
    print("Square Root:", sqrt_number(9))
