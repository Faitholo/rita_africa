# Invoice creating tool

# Welcome users and receive their info
print("Welcome to Unique Furniture Store, We are glad to have you. Kindly select a number to proceed.")
options = ["1: Place order", "2: Other"]
category = ["BRONZE", "SILVER", "GOLD", "PLATINUM"]

for action in options:
    print(action)
selection = int(input("Kindly select a number to proceed: "))

if selection == 1:
    amount = int(input("How much is your total order?"))

    if amount >= 1:
        for member in category:
            print(member)
        membership = input("Please select your membership category").upper()
        if membership in category and membership == "BRONZE":
            discount = 5
            print("The current price is {}".format(amount))
            print("Your total amount after {}% discount is {}, kindly proceed to payment.".format(discount, amount - (discount / amount) * 100))
        elif membership in category and membership == "SILVER":
            discount = 10
            print("The current price is {}".format(amount))
            print("Your total amount after {}% discount is {}, kindly proceed to payment.".format(discount, amount - (discount / amount) * 100))
        elif membership in category and membership == "GOLD":
            discount = 15
            print("The current price is {}".format(amount))
            print("Your total amount after {}% discount is {}, kindly proceed to payment.".format(discount, amount - (discount / amount) * 100))
        elif membership in category and membership == "PLATINUM":
            discount = 20
            print("The current price is {}".format(amount))
            print("Your total amount after {}% discount is {}, kindly proceed to payment.".format(discount, amount - (discount / amount) * 100))
        else:
            print("You are not eligible for a discount and your total amount is {}".format(amount))
    else:
        print("We do not have anything for that price, bye.")
else:
    print("This is an order only page, bye")