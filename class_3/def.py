# a function for squaring numbers
def square(n):
    print(n ** 2)


# a function for introducing yourself
def intro(name, hobby):
    print(f"My name is {name} and I enjoy {hobby}.")


user = input("What is your name? ")
activity = input("What do you like to do for fun? ")
intro(user, activity)
