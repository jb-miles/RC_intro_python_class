# function for revealing the encoding value of each letter in a word
def reveal(word):
    for letter in word:
        print(ord(letter), end=" ")
    else:
        print()


# function calls
reveal("Python") # output: 80 121 116 104 111 110
reveal("Apple") # output: 65 112 112 108 101
reveal("apple") # output: 97 112 112 108 101

"Apple" > "Python"
"apple" > "python"
"apple" > "Python"
"apple".casefold() > "Python".casefold()