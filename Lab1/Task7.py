# Declare and initialise the variables that we will use later on in our program.
# Remember that this is not necessary, since in Python variables can be created dynamically.
# For example if you delete lines 4, 5, 6 the program will still work.
number1 = 0
number2 = 0
mult = 0

# Ask the user for two numbers using the input() function.
# Remember that input() returns strings (str) by default. You can control how the user's input will be interpreted
# by casting into the desired datatype. Here we surround input() with int() so we are expecting whole numbers.
# You can use casting in other parts of your code as well, for example see line 15.
# The casting functions are int(), float(), str().
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

# Multiply the two numbers and store the result into mult.
mult = number1 * number2

# Print the result.
# Remember there are multiple ways to print, here we are constructing a single string by concatenating (+) two strings
# before printing (mult must be casted into a string before that happens). Alternatively we could pass the elements
# that need to be printed as arguments, and print() will take care of any casting for us.
# print("The two numbers multiplied are: ", mult)
print("The two number multiplied are: " + str(mult))

# BONUS : Adapt the code so that the user can enter decimal numbers (float) and then print out the two numbers squared.
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

# The ** operator raises a number to a certain power.
# Example : a ** b, will raise a to the power b.
print("The squares of the two numbers are", number1 ** 2, "and", number2 ** 2)
