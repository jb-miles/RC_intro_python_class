# function for writing a Fibonacci series up to n
def fib(n):
    a, b = 1, 2
    while a < n:
        print(a, end=", ")
        a, b = b, a + b
    else:
        print("End of series.")


# Call the function:
fib(100)
