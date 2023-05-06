# a function for demonstrating the special value None
def something_or_nothing(text=None):
    if text:
        print(f"This is what it says: {text}")
    else:
        print("There's nothing here!")


# function calls
something_or_nothing("I wrote this!")  # output This is what it says: I wrote this!
something_or_nothing()  # output: There's nothing here!
