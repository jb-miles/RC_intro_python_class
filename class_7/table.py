desserts = {"peach": "peach cobbler", "apple": "apple pie", "vanilla": "vanilla ice cream"}
print("apple: {0[apple]}, peach: {0[peach]}".format(desserts))
print("apple: {apple}, peach: {peach}".format(**desserts))

for ingredient, dish in desserts.items():
    print(f"{ingredient:7} ->  {dish!r}")