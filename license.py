# Simple code to check driver's license eligibility
# Using conditional statements

first_name = input("What is your first name?: ")
last_name = input("What is your last name?: ")
country = input("What is your country of origin?: ").upper()
age = int(input("How old are you?: "))
usa = ["USA", "UNITED STATES", "UNITED STATES OF AMERICA"]

# Check if age is above 18 for non-US citizens
if country not in usa and age >= 18:
    print("Dear {} {}, you are eligible to apply, please proceed.".format(first_name, last_name))

# Check if age is below 13 for non-US citizens
elif country not in usa and age < 13:
    print("Dear {}, you are way too young to apply kindly wait for {} more year(s) to apply".format(first_name, 18 - age))

# Check if age is above 16 for US citizens
elif country in usa and age >= 16:
    print("Dear {} {}, you are eligible to apply, please proceed.".format(first_name, last_name))

# Check if age is below 13 for US citizens
elif country in usa and age < 13:
    print("Dear {}, you are way too young to apply kindly wait for {} more year(s) to apply".format(first_name, 16 - age))

# Check for other criteria
else:
    print("Dear {} {}, you are ineligible for a driver's license, kindly wait for {} more year(s)".format(first_name, last_name, 18 - age))
