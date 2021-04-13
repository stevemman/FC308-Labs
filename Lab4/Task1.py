# Create a string to store the items of the user.
suitcase = ""

# Create an infinite loop and break it when the user enters the word 'stop'.
while True:
    # Ask the user for an item.
    item = input("Enter an item into your suitcase: ")

    # Stop when the user enters the word 'stop'.
    if item == "stop":
        break

    # Add item to the suitcase.
    # We create a new suitcase that has all the items of the old suitcase plus the new item and a space " " so that
    # it's contents are not bunched up all together into a single word.
    suitcase = suitcase + item + " "

# Print the contents of the suitcase to the user.
print(suitcase)

# In this task we chose to use an infinite while loop that we break when we the user enters the word 'stop'. Of course
# this is not the only way to do this. For example we could have used a finite while loop with expression item != 'stop'
# like this: while item != 'stop'. Furthermore instead of using a String to represent out suitcase we could have used a
# data structure e.g. a list of Strings.
