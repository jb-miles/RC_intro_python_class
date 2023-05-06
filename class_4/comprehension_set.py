even_square_set = {(x, x**2) for x in range(2, 11) if x % 2 == 0}
print(even_square_set)
even_square_tuple = tuple((x, x**2) for x in range(2, 11) if x % 2 == 0)
print(even_square_tuple)