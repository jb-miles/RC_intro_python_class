# Input the bill amount and start tip percentage
bill_amount = float(input("Enter the bill amount: "))
tip_percentage = 15

# Use a while loop to display the tip amounts at different percentages
while tip_percentage <= 20:
    tip_amount = bill_amount * (tip_percentage / 100)
    total_amount = bill_amount + tip_amount
    print(f"Tip at {tip_percentage}% = {tip_amount:.2f}, Total = {total_amount:.2f}")
    tip_percentage += 1
else:
    print("End of calculation.")
