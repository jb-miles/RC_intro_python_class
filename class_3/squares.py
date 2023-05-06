def square_numbers(n):
    """
    This function takes an integer n and returns a list of squares of all numbers up to n.
    """
    squares = []
    for i in range(1, n+1):
        squares.append(i*i)
    return squares