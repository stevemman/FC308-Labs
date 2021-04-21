import math


def area_circle(radius):
    """
    Returns the area of a circle.
    :param radius: The radius of the circle.
    :return: The area of the circle.
    """
    # We are using the pi constant from the imported math library.
    return math.pi * (radius ** 2)


# Ask the user for the radius of the circle.
radius = float(input("Please enter the radius of the circle: "))

# Call the function area and show the result to the user.
print("The area of a circle with radius", radius, "is", area_circle(radius))
