# x = 10
# y = -15

# print(x > y and y > x)

# name = "Faith"
# age = 35
# location = "Africa"

# And logic
# print(name == "Faith" and location == "Europe")
# print(name == "Faith" and age == "35" and location == "Africa")

# Or logic
# print(name == "Faith" or location == "Europe")
# print(name == "Faith" or age == "35" or location == "Europe")

# Not logic
# if name is not "Faith":
#     print("You are an imposter")
# else:
#     print("Welcome, {}".format(name))

# if name == "Faith":
#     print("Welcome, {} from {}".format(name, location))
#     if location == "Africa":
#         print("You are an African")
#     else:
#         print("You are an alien")
# else:
#     print("You are an imposter!!!!!")

# age = 18
#
# if age >= 19 and age <= 65:
#     print("You are of age")
# else:
#     print("We don't want people your age")

# num = 10
# num2 = "10"
# true = True
# true1 = "True"
# print(type(num))
# print(type(num2))
# print(type(true))
# print(type(true1))




"""
Breakout Session Task: Write a program that takes a student's score, (out of 100) as input, and prints
their grade based on the following conditions:
Grade A: Score >= 90
Grade B: Score >= 80 and < 90
Grade C: Score >= 70 and < 80
Grade D: Score >= 60 and < 70
Grade F: Score < 60
"""

# print(task)

# print(task.split(","))



print("Student Centre")
print("----------------")
print("Welcome to the student result centre")

subjects = ["Mathematics", "English", "Chemistry"]

print("subjects taken are:")
for subject in subjects:
    print(subject)

print("-------------------------")
print("Kindly input your scores to check your final grade")
maths = int(input("Mathematics: "))
english = int(input("English: "))
chem = int(input("Chemistry: "))


if maths >= 0:
    if english >= 0:
        if chem >= 0:
            total = maths + english + chem
            avg = int(total / 3)

            if avg < 60:
                grade = "F"
            elif avg >= 60 and avg < 70:
                grade = "D"
            elif avg >= 70 and avg < 80:
                grade = "C"
            elif avg >= 80 and avg < 90:
                grade = "B"
            else:
                grade = "A"
            print("Total score: {}".format(total))
            print("Average score: {}".format(avg))
            print("Your grade is {}".format(grade))
        else:
            print("You have an invalid grade for Chemistry")
    else:
        print("You have an invalid grade for English")
else:
    print("You have an invalid grade for Mathematics")