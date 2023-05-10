from datetime import date as dt

# Assuming the birthdate is '1990-05-10'
birth_date = dt(1990, 5, 10)
current_date = dt.today()

# Calculate the age
age = current_date.year - birth_date.year

# Check if the birthday has already occurred this year
if current_date.month < birth_date.month or (current_date.month == birth_date.month and current_date.day < birth_date.day):
   age -= 1

name = "Jonathan"
print("%s is %d years old." % (name, age)) # output: Jonathan is 33 years old.
