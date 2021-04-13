# Ask the user for a mathematical operator.
mathOp = input("Please enter a mathematical operator: ")

# Compare with all the mathematical operators and print the appropriate message.
if mathOp == "+":
    print("You entered the addition operator +")
elif mathOp == "-":
    print("You entered the subtraction operator -")
elif mathOp == "/":
    print("You entered the division operator /")
elif mathOp == "*":
    print("You entered the multiplication operator *")
else:
    # With the else clause we can warn the user that mathOp is not a mathematical operator.
    print("Invalid mathematical operator!")
