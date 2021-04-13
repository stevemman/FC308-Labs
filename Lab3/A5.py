# Create a String with the calculator menu.
menu = "Welcome to the Super Basic Calculator 9000!\nLets start by selecting a valid mathematical " \
       "operator (1,2,3,4)\n1. Addition +\n2. Subtraction -\n3. Division /\n4. Multiplication * "

# Print the menu to the user.
print(menu)

# Get the input from the user.
choice = input("Option: ")

if choice == "1":
    print("Congratulations! You selected the Addition + operator")
    print("Your mathematical expression looks like this: a + b")
    a = float(input("Please enter a value for the 'a' operand: "))
    b = float(input("Please enter a value for the 'b' operand: "))
    result = a + b
    print("The result of the expression", a, "+", b, "is", result)
elif choice == "2":
    print("Congratulations! You selected the Subtraction - operator")
    print("Your mathematical expression looks like this: a - b")
    a = float(input("Please enter a value for the 'a' operand: "))
    b = float(input("Please enter a value for the 'b' operand: "))
    result = a - b
    print("The result of the expression", a, "-", b, "is", result)
elif choice == "3":
    print("Congratulations! You selected the Division / operator")
    print("Your mathematical expression looks like this: a / b")
    a = float(input("Please enter a value for the 'a' operand: "))
    b = float(input("Please enter a value for the 'b' operand: "))
    result = a / b
    print("The result of the expression", a, "/", b, "is", result)
elif choice == "4":
    print("Congratulations! You selected the Multiplication * operator")
    print("Your mathematical expression looks like this: a * b")
    a = float(input("Please enter a value for the 'a' operand: "))
    b = float(input("Please enter a value for the 'b' operand: "))
    result = a * b
    print("The result of the expression", a, "*", b, "is", result)
else:
    print("Error! Invalid input.")

print("Bye bye!")
