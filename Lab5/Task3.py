def area_rectangle(height, width):
    """
    Returns the area of a rectangle.
    :param height: The height of the rectangle.
    :param width:  The width of the rectange.
    :return: The area of the rectangle.
    """
    return height * width


# Ask the user for the height of the rectangle.
height = float(input("Please enter the height of the rectangle: "))

# Ask the user for the width of the rectangle.
width = float(input("Please enter the width of the rectangle: "))

# Call the function area and show the result to the user.
print("The area of the rectangle with height", height, "and width", width, "is", area_rectangle(height, width))
