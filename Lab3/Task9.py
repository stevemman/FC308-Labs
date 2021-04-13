# We ask the user to enter a number1.
number1 = int(input("Enter the first number : "))

# We ask the user to enter a number2.
number2 = int(input("Enter the second number : "))

# Multiply the numbers.
product = number1 * number2

# Show the answer to the user.
print("The answer is :", product)

# Check if the product is greater that 1000.
if product > 1000:
    print("Thats a hard one!")
