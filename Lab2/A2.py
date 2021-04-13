# Ask the user to enter a speed in Mph.
speed_mph = float(input("Please enter a speed in Mph into the converter: "))

# Convert it into Kmh.
speed_kmh = speed_mph * 1.609344

# Print the result to the user, after rounding the result to 2 decimal places.
print(speed_mph, "Mph is equivalent to", round(speed_kmh, 2), "Kmh")
