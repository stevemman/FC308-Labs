# Import the math library.
# Visit https://docs.python.org/3/library/math.html to see details about all the functions in this library.
import math

# Ask the user for a number.
number = float(input("Please enter a number: "))

# Use the function sqrt() to find the square root of number.
# After importing any library you can use the "." to access the specific function that you want to use.
square = math.sqrt(number)

# Print the result back to the user.
print("The square root of", number, "is", square)
