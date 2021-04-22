# We create functions for each one of the supported operations.
def open_file():
    print("--Executing Open file")


def new_file():
    print("--Executing New file")


def close_file():
    print("--Executing Close file")


print("Welcome to the ultimate menu!")

# Infinite loop that will stop only when the user types "exit".
while True:
    option = input("Select one of the options bellow.\n"
                   "(O)pen File\n"
                   "(N)ew File\n"
                   "(C)lose File\n"
                   "Or type \"exit\" to stop.\n"
                   ">> ")

    # The use of the lower() string function ensures that our program will accept both lowercase and uppercase letters
    if option.lower() == "o":
        open_file()
    elif option.lower() == "n":
        new_file()
    elif option.lower() == "c":
        close_file()
    elif option.lower() == "exit":
        break   # This will break the loop and terminate the program.
    else:
        print("--ERROR! Invalid input.")
