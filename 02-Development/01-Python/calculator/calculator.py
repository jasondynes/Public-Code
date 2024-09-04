# Calculator
import art


# Add
def add(num1, num2):
    return num1 + num2


# Subtract
def subtract(num1, num2):
    return num1 - num2


# Multiply
def multiply(num1, num2):
    return num1 * num2


# Divide
def divide(num1, num2):
    return num1 / num2


# operations dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(art.logo)
    num1 = float(input("What's the first number?: "))
    num2 = float(input("What's the second number?: "))
    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick an operation from the line above: ")

    # calculate answer
    answer = operations[operation_symbol](num1, num2)
    # print answer
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    continue_flag = "y"

    while continue_flag == "y":
        continue_flag = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ")
        if continue_flag == "n":
            break
        else:
            num1 = answer
            num2 = float(input("What's the next number?: "))
            operation_symbol = input("Pick an operation: ")
            answer = operations[operation_symbol](num1, num2)
            # print answer
            print(f"{num1} {operation_symbol} {num2} = {answer}")


calculator()
