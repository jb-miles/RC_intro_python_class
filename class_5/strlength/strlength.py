"""
Script for counting words in a sentence or the number of letters in the words.

Usage:
    python strlength.py [argument1] [argument2]

Arguments:
    argument 1: "w" to count the number of words,  "l" to count the letters in the words
    argument 2: enter the string for counting
"""


# a function for running this module as a script
def counting_script(choice, user_sentence):
    from .utils.functions import words_in_sentence, letters_in_words
    if "w" in choice:
        print(words_in_sentence(user_sentence))
    if "l" in choice:
        print(letters_in_words(user_sentence))



if __name__ == "__main__":
    import sys
    counting_script(sys.argv[1], sys.argv[2])
