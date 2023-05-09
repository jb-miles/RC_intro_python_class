"""
Script for counting words in a sentence or the number of letters in the words.

Usage:
    python strlength.py [argument1] [argument2]

Arguments:
    argument 1: "w" to count the number of words,  "l" to count the letters in the words
    argument 2: enter the string for counting
"""


# a function to return the number of words in a sentence
def words_in_sentence(sentence):
    words = sentence.split()
    return len(words)


# a function to return the number of letters in each word of a sentence
def letters_in_words(sentence):
    words = sentence.split()
    letter_count = [len(word) for word in words]
    return letter_count


# a function for running this module as a script
def counting_script(choice, user_sentence):
    if "w" in choice:
        print(words_in_sentence(user_sentence))
    if "l" in choice:
        print(letters_in_words(user_sentence))


if __name__ == "__main__":
    import sys
    counting_script(sys.argv[1], sys.argv[2])
