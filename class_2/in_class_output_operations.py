X = 3
Y = 7
X += 2
pi = 3.14156
r = 15
cir = (pi * r) ** 2
code = "hello"
code += " world"
month = "February"
print(dir())
int_list = [1, 2, 3, 4, 5]
veggie_list = ["celery", "carrot", "lettuce", "onion"]
int_list.append(X)
int_list.append(Y)
print(int_list)
veggie_list.insert(1, "bok choy")
veggie_list.remove("carrot")
print(veggie_list)
print(2 in int_list)
print("lettuce" in veggie_list)
print("carrot" in veggie_list)
print(veggie_list[3][2])
first_primes = (2, 3, 5, 7, 11, 13, 17)
print(first_primes)
more_primes = first_primes + (19, 23, 29, 31)
print(more_primes)
greetings = {"hello": "a formal greeting", "hey": "an informal greeting"}
print(greetings["hey"])
greetings["ahoy hoy"] = "correct way to answer the phone"
print(greetings)
greetings["ahoy hoy"] += " or an old-fashioned way to answer the phone"
print(greetings["ahoy hoy"])
showcase = {"beef", "9"}
print(showcase)
print(showcase == {"beef", "9", "9", "9"})
veggie_set = set(veggie_list)
print(veggie_set)
showcase.add("chicken")
showcase.discard("9")
print(showcase)
foods = showcase.union(veggie_set)
print(foods)
