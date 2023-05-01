# Define a function using a while loop to display the tip amounts at different percentages
def tip_calculator(bill_amount, tip_percentage, end_percent):
    while tip_percentage <= end_percent:
        tip_amount = bill_amount * (tip_percentage / 100)
        total_amount = bill_amount + tip_amount
        print(f"Tip at {tip_percentage}% = {tip_amount:.2f}, Total = {total_amount:.2f}")
        tip_percentage += 1
    else:
        print("End of calculation.")


# Input and function call
bill = float(input("Enter the bill amount: "))
tip = int(input("Enter starting percentage: "))
end = int(input("Enter ending percentage: "))
tip_calculator(bill, tip, end)
