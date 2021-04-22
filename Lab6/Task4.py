# One function per calculator operation.
def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


print("Welcome to the advanced calculator 9001")

# Infinite loop that will stop only when the user types "exit".
while True:
    option = input("Select one of the options bellow.\n"
                   "(A)dd\n"
                   "(S)ubtract\n"
                   "(M)ultiply\n"
                   "(D)ivide\n"
                   "Or type \"exit\" to stop.\n"
                   ">> ")

    # This will break the loop and terminate the program.
    if option.lower() == "exit":
        break

    # Ask the user to enter two numbers.
    num1 = float(input("Please enter the first number: "))
    num2 = float(input("Please enter the second number: "))

    # The use of the lower() string function ensures that our program will accept both lowercase and uppercase letters.
    if option.lower() == "a":
        print("--", num1, "+", num2, "=", add(num1, num2))
    elif option.lower() == "s":
        print("--", num1, "-", num2, "=", subtract(num1, num2))
    elif option.lower() == "m":
        print("--", num1, "*", num2, "=", multiply(num1, num2))
    elif option.lower() == "d":
        print("--", num1, "/", num2, "=", divide(num1, num2))
    else:
        print("--ERROR! Invalid input.")
