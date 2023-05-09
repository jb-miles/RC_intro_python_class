# a function for recommending outdoor exercise for seniors
def exercise_recommendation(temp):
    if 85 > temp > 32:
        print("Outdoor exercise is recommended at this temperature.")
    else:
        print("Caution should be taken when exercising outdoors in this temperature")


if __name__ == "__main__":
    import sys
    exercise_recommendation(int(sys.argv[1]))
