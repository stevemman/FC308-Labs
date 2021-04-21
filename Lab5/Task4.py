def BMI(height, weight):
    """
    Returns the Body Mass Index (BMI).
    :param height: The height of the person.
    :param weight: The weight of the person.
    :return: The BMI.
    """
    return weight / (height ** 2)


# Ask the user for the height of a person.
height = float(input("Please enter your height: "))

# Ask the user for the weight of a person.
weight = float(input("Please enter your weight: "))

# Call the function and show the result to the user.
print("An individual with height", height, "and weight", weight, "has a BMI of", BMI(height, weight))
