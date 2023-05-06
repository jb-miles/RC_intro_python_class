# Create a list of numbers from 0 to 9
numbers = [num for num in range(10)]
print(numbers)
# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create a list of squares from 0 to 9
squares = [num**2 for num in range(10)]
print(squares)
# Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Create a list of odd numbers from 0 to 9
odd_numbers = [num for num in range(10) if num % 2 != 0]
print(odd_numbers)
# Output: [1, 3, 5, 7, 9]

# Create a list of the first letter of each word in a sentence
sentence = "I love learning python"
letters = [word[0] for word in sentence.split( )]
print(letters)
# Output: ['I', 'l', 'l', 'p']

# Create a list of tuples containing a number and its square
tuples = [(num, num**2) for num in range(5)]
print(tuples)
# Output: [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16)]

a = list(range(1, 11))
print(a)
squares = [number ** 2 for number in a]
cubes = [number ** 3 for number in a]
print(squares)
print(cubes)