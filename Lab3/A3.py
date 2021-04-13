# We create a string that has the menu to be displayed.
# We use the \n symbol to print whatever comes after it into a new line.
menu = "Please select an option from the menu (1,2,3)\n1. Open file.\n2. Close file.\n3. Exit."

# Print the menu to the user.
print(menu)

# Ask the user for input.
choice = input("Option : ")

# Since choice is a String we compare it (==) with a String ("1").
if choice == "1":
    print("You selected the option 'Open File'.")
elif choice == "2":
    print("You selected the option 'Close File'.")
elif choice == "3":
    print("You selected the option 'Exit'.")
else:
    print("Invalid option.")