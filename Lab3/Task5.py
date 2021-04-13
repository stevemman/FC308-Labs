# We ask the user to enter a number1.
number1 = int(input("Enter the first number : "))

# If number1 is not between 0-9, warn the user and set to 0.
if number1 < 0 or number1 > 9:
    print("Error, invalid number!")
    number1 = 0

# We ask the user to enter a number1.
number2 = int(input("Enter the second number : "))

# If number1 is not between 0-9, warn the user and set to 0.
if number2 < 0 or number2 > 9:
    print("Error, invalid number!")
    number2 = 0

# We ask the user to enter a number1.
number3 = int(input("Enter the third number : "))

# If number1 is not between 0-9, warn the user and set to 0.
if number3 < 0 or number3 > 9:
    print("Error, invalid number!")
    number3 = 0

# We ask the user to enter a number1.
number4 = int(input("Enter the fourth number : "))

# If number1 is not between 0-9, warn the user and set to 0.
if number4 < 0 or number4 > 9:
    print("Error, invalid number!")
    number4 = 0

# We ask the user to enter a number1.
number5 = int(input("Enter the fifth number : "))

# If number1 is not between 0-9, warn the user and set to 0.
if number5 < 0 or number5 > 9:
    print("Error, invalid number!")
    number5 = 0

# Print the sum of all 5 numbers.
print("The sum of all the numbers is:", number1 + number2 + number3 + number4 + number5)

# Our approach to this task is suboptimal, as programmers we try to avoid code repetition because it makes our programs
# inflexible and hard to maintain. A better approach would be to use some iteration control structure (While, for) and
# instead having one variable per number we could use some compound data structure e.g. a list.
