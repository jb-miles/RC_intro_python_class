# print that a city has a river
def river_city(city="Las Vegas", has_river=False):
    if has_river is True:
        print(f"{city} has a river.")
    else:
        print(f"{city} does not have a river.")


river_city(city="Berlin", has_river=True)