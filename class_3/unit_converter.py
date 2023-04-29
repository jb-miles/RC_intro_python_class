# Get the list of measurements from the user
inches_list = input("Enter a list of measurements in inches, separated by commas: ").split(",")

# Convert the measurements to metric units
for inches in inches_list:
    inches = float(inches.strip())  # convert the string to a float and remove any whitespace
    centimeters = inches * 2.54    # convert the measurement to centimeters
    print(f"{inches:.2f} in. = {centimeters:.2f} cm.")
