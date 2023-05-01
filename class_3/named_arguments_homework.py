# print that a city has a river and/or is on the coast
def river_city(city="Los Angeles", has_river=True, coastal=True):
    if has_river is True and coastal is True:
        print(f"{city} has a river and is on the coast.")
    elif has_river is True and coastal is False:
        print(f"{city} has a river and is not on the coast.")
    elif has_river is False and coastal is True:
        print(f"{city} does not have a river and is on the coast.")
    else:
        print(f"{city} does not have a river and is not on the coast.")


river_city("Portland, OR", True, True)