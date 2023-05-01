city_list = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
for city in city_list:
    if len(city) < 10:
        continue
    print(city)
else:
    print("Another city")


def print_the_cities(city_1, city_2="Los Angeles", city_3="Chicago", **kwarg):
    print(f"The cities are {city_1}, {city_2}, {city_3} and {kwarg}.")


print_the_cities("New York", city_2="Los Angeles", city_4="Boston")
