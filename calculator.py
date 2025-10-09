print("Welcome to our group calculator project!")

#===== Addition function here =====

def add_numbers(a, b):
    # a: first number
    # b: second number
    # returns: the sum of a and b
    return a + b



#==== Subtraction function here =====

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

subtraction_result = num1 - num2

print(num1, "-", num2, "=", subtraction_result)


#==== Multiplication function here ======
#multiplication of two numbers
num1= float(input("Enter the first number:"))
num2= float(input ("Enter the second number:"))
multiplication_result= num1 * num2
print("The result of multiplication is: ",multiplication_result)




#==== Division function here =====





#==== Validation funtion here ====
# ==== Abdinour Shil - 671040 ====

def _to_number(x):
    """
    Convert input to a float or raise ValueError.
    Accepts ints/floats/strings (e.g. '12', '-3.5').
    """
    if isinstance(x, (int, float)):
        return float(x)
    try:
        return float(str(x).strip())
    except Exception:
        raise ValueError("Invalid input: please enter a valid number.")


def safe_divide(a, b):
    """
    Divide a by b with a clear error when b is zero.
    """
    a = _to_number(a)
    b = _to_number(b)
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b


def perform_with_validation(op, a, b):
    """
    Validate inputs and perform one of: +, -, *, /.
    Returns the numeric result or raises a clear error.
    """
    a = _to_number(a)
    b = _to_number(b)

    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return safe_divide(a, b)
    else:
        raise ValueError("Invalid operation. Use one of: +, -, *, /.")


# Optional: interactive input helpers
def read_number(prompt):
    """
    Loop until the user types a valid number.
    """
    while True:
        raw = input(prompt)
        try:
            return _to_number(raw)
        except ValueError as e:
            print(e)


def read_operator(prompt="Choose operation (+, -, *, /): "):
    """
    Loop until the user picks a supported operator.
    """
    while True:
        op = input(prompt).strip()
        if op in {"+", "-", "*", "/"}:
            return op
        print("Invalid operation. Use one of: +, -, *, /.")

