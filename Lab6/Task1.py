def print_mult_table(number):
    """
    Prints the multiplication table of a number.
    :param number: The number.
    """
    # range() will give a sequence of numbers from 1 up to but not including 11.
    for i in range(1, 11):
        print(i, "*", number, "=", i * number)


# Ask the user for a number.
number = int(input("Please enter a number between 1-10: "))

# Check if the number is between 1-10 and call the function.
if number < 1 or number > 10:
    print(number, "is outside of the 1-10 range!")
else:
    print_mult_table(number)
