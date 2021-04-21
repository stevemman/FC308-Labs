def find_keyword(sentence, keyword):
    """
    Returns whether a keyword exists inside a sentence or not.
    :param sentence: The sentence.
    :param keyword: The keyword to be searched in the sentence.
    :return: True if it exists, False otherwise.
    """
    if keyword in sentence:
        return True
    else:
        return False


# Change this variable and experiment with different keywords.
keyword = "happy"

# Ask the user for a sentence.
sentence = input("Please enter a sentence to the program: ")

# Call the function and print out an appropriate message to the user.
if find_keyword(sentence, keyword):
    print("The keyword", keyword, "has been found in the sentence")
else:
    print("The keyword", keyword, "has not been found in the sentence")
