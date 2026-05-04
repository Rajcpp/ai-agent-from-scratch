# tools/calculator.py
def calculate(operation, input1, input2):
    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }

    if operation in operations:
        return {"status": "success", "result": operations[operation](input1, input2)}
    else:
        return {
            "status": "error",
            "message": "Error: Invalid operation. Supported operations are add, subtract, multiply, divide.",
        }


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero is undefined."
    return a / b
