# Invoice creating tool

# Welcome users and receive their info
print("Welcome to Unique Furniture Store, We are glad to have you. Kindly select a number to proceed.")
options = ["1: Place order", "2: Other"]
category = ["BRONZE", "SILVER", "GOLD", "PLATINUM"]

# Get the selection from the list all available actions
for action in options:
    print(action)
selection = int(input("Kindly select a number to proceed: "))

# Get the amount if greater than 1
if selection == 1:
    amount = int(input("How much is your total order?"))

    if amount >= 1:
        # Get the membership if available within the category
        for member in category:
            print(member)
        membership = input("Please select your membership category").upper()
        # Check if the category is BRONZE
        if membership in category and membership == "BRONZE":
            discount = 5
            print("The current price is {}".format(amount))
            print("Your total amount after {}% discount is {}, kindly proceed to payment.".format(discount, amount - (discount / amount) * 100))
        # Check if the category is SILVER
        elif membership in category and membership == "SILVER":
            discount = 10
            print("The current price is {}".format(amount))
            print("Your total amount after {}% discount is {}, kindly proceed to payment.".format(discount, amount - (discount / amount) * 100))
        # Check if the category is GOLD
        elif membership in category and membership == "GOLD":
            discount = 15
            print("The current price is {}".format(amount))
            print("Your total amount after {}% discount is {}, kindly proceed to payment.".format(discount, amount - (discount / amount) * 100))
        # Check if the category is PLATINUM
        elif membership in category and membership == "PLATINUM":
            discount = 20
            print("The current price is {}".format(amount))
            print("Your total amount after {}% discount is {}, kindly proceed to payment.".format(discount, amount - (discount / amount) * 100))
        # If not in category
        else:
            print("You are not eligible for a discount and your total amount is {}".format(amount))
    # If less than 1
    else:
        print("We do not have anything for that price, bye.")
# If not interested in placing an order
else:
    print("This is an order only page, bye")