# Create an infinite loop and break it when the user enters the word 'stop'.
while True:
    # Ask the user for a word.
    word = input("Enter an word: ")

    # Stop when the user enters the word 'stop'.
    if word == "stop":
        break

    # Print the word back to the user followed by its length.
    print(word, len(word))

# Similarly to Task1 instead of an infinite while loop we could have used a finite while loop with the expression
# word != 'stop', like this: while word != 'stop'.
