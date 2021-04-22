def reverse_it(sentence):
    """
    Returns the sentence with all the letters in reverse order.
    :param sentence: The sentence.
    :return: The reversed sentence.
    """

    # Create an empty string that will store our new reversed string.
    new_sentence = ""

    # len() will return the length of a sequence, in this case the string 'sentence'.
    # range() will return a sequence of integers from 0 to len(sentence) - 1.
    # reversed() will reverse the sequence of integers so that it starts from len(sentence) - 1 to 0.
    # These integers will be used as indexes to get each letter from 'sentence' in reverse order.
    for i in reversed(range(len(sentence))):
        new_sentence = new_sentence + sentence[i]

    return new_sentence


# Ask the user to enter a sentence.
sentence = input("Please write a sentence and the program will reverse it!: ")

# Show the result to the user.
print(reverse_it(sentence))
