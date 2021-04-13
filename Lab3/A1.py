# Ask the user to enter their age.
age = int(input("Please enter your age :"))

# Depending on the age group display a different ticket price.
if age > 0 and age < 18:
    print("The ticket costs : 1.50£")
elif age >= 18 and age < 65:
    print("The ticket costs : 2.20£")
elif age >= 65 and age < 100:
    print("The ticket costs : 1.20£")
