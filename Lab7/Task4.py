def cube_length(length):
    """
    Returns the cube of a string's length.
    :param length: The length of the string.
    :return: The length cubed.
    """
    return length ** 3


while True:  # Added to make the program repeat as per additional task 2.
    # Ask the user to enter a string and then call the function.
    string_length = len(input("Please enter a string : "))
    length_cubed = cube_length(string_length)

    # Show the result to the user.
    print("The length of the string you entered is :", string_length)
    print("The cubed length of the string you entered is :", length_cubed)

    # Ask the user if they want to start again.
    if input("Continue? (y/n) : ") == "n":
        break
