# Ask the user to enter two numbers.
a = int(input("Enter a value for a: "))
b = int(input("Enter a value for b: "))

# Approach 1. Use a third variable to help us with the swap.
temp = a
a = b
b = temp

# Approach 2. Without using an extra variable.
# a = a + b
# b = a - b
# a = a - b

print("Swap!")

# Print a and b.
print("The value of a is:", a)
print("The value of b is:", b)



