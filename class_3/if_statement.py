# if statement for purchase approval
cost = input("Enter the cost of the item in dollars: $")
if int(cost) > 1000:
    print("It's too expensive")
elif int(cost) < 500:
    print("Purchase is recommended at this price.")
else:
    print("Purchase is approved at this price.")
