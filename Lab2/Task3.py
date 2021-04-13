# Ask user for the amount of pounds.
pounds = int(input("Enter the amount of pounds: "))

# Current exchange rate of pounds to dollars.
rate = 1.39

# Convert amount into dollars and round the result into two decimal digits
dollars = round(pounds * rate, 2)

# Convert amount into dollars and print to the user.
print("With", pounds, "£ you can buy", dollars, "$")

