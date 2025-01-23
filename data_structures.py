# Lists

my_list = []
str_list = ["Sample string", "Silly string", "Happy string"]
int_list = [177, 85, 93, 105, 40]
float_list = [4.3, 5.0, 2.2, 10.5]
bool_list = [True, True, True, False]
mixed_list = [True, 4.9, 155, "System"]


# print(type(my_list))
# print(type(str_list))
# print(type(int_list))
# print(type(float_list))
# print(type(bool_list))
# print(type(mixed_list))

# print(str_list[1])
# print(str_list[0])
# print("-----------")
# first_item = str_list[0]
# print(first_item)


# bool_list.remove(True)
# int_list.pop()
# float_list.pop(1)
# print(int_list)
# print(float_list)
# print(bool_list)

#
# int_list.insert(3, 40)
# float_list.insert(1, 5.0)
# int_list.append(1550)
# print(int_list)
# print(float_list)

alphabets = ["b", "h", "a", "l", "z"]
# sorting_alpha = alphabets.sort()
# print(sorting_alpha)

# sorted_alpha = sorted(alphabets)
# print("--------------------")
# print(sorted_alpha)

# print(len(alphabets))

# my_tuple = ("b", "h", "a", "l", "z")


# if "b" in alphabets:
#     print("Yay!", file=open("yay_file.txt", "a"))
# else:
#     print("Nay", file=open("nay_file.txt", "a"))

# if "h" in my_tuple:
#     print("Yay!", file=open("yay_file.txt", "a"))
# else:
#     print("Nay", file=open("nay_file.txt", "a"))



# my_list.append("No longer empty!")
# my_list.insert(1, "Don't mind being the last!")
# my_list.insert(2, "I came first!")
#
# print(my_list)
#
# print("----------------")
#
# my_list[1] = "I've changed!"
# print(my_list)
#
# print(sorted(my_list))
# print(len(my_list))

# print(str_list[2])
# print(bool_list[2])



# Dictionaries in Python!!!

# my_dict = {}
# new_dict = {"Name": "Faith", "Age": 40, "Location": "Nigeria"}
# print(new_dict)
#
# Accessing a dictionary value using its key
# print(new_dict["Location"])

#
# Updating a dictionary's value
# new_dict["Location"] = "Denmark"
# print(new_dict)
#

# sample_dict = {
#      "person 1": {"Name": "Gerald"}, 
#      "person 2": {"Name": "Faith"}
#      }
# print(sample_dict.get("person 3"))
# print(sample_dict["person 3"])

# for item, val in sample_dict.items():
#     print(item, val)
#
# "----------------------------------"
#
# print(sample_dict["person 1"]["Name"])
# print(sample_dict["person 2"]["Name"])

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict1.update(dict2)
print(dict1)


# for item in sample_dict:
#    print(item)
#    print(sample_dict.get(item))

# gerald = {"age": [2,3,4,5]}
# print(gerald.values())


""""
Simple program that stores student names as keys and their grades as values.
Then:
     - Prints the average grade.
     - Prints the names of students who scored above the average.
"""
# Isreal

# # Initialize a dictionary to store student names and grades
# students = {}
 
# # Input the number of students
# num_students = int(input("Enter the number of students: "))
 
# # Collect student names and their grades
# for _ in range(num_students):
#     name = input("Enter the student's name: ")
#     grade = float(input(f"Enter {name}'s grade: "))
#     students[name] = grade
 
# # Calculate the average grade
# average_grade = sum(students.values()) / len(students)
 
# # Find students who scored above the average
# above_average_students = [name for name, grade in students.items() if grade > average_grade]
 
# # Print the results
# print("\n--- Results ---")
# print(f"Average Grade: {average_grade:.2f}")
# print("Students who scored above the average:")
# if above_average_students:
#     for student in above_average_students:
#         print(student)
# else:
#     print("No students scored above the average.")



# Nour
# students_grades = {
#     'Alice': 85,
#     'Bob': 78,
#     'Charlie': 92,
 
# }
 
# average_grade = sum(students_grades.values()) / len(students_grades)
 
# print(f"Average grade: {average_grade}")
 
# print("Students who scored above the average:")
# for student, grade in students_grades.items():
#     if grade > average_grade:
#         print(student)




# Osei
# Store three student names and their grades
# students = {
#     "Mary": 88,
#     "Jamie": 92,
#     "Cole": 85
# }
 
# # Calculate average grade
# average = sum(students.values()) / len(students)
 
# # Print results with formatting
# print(f"Average grade: {average:.1f}")
# print("Students above average:")
# for name, grade in students.items():
#     if grade > average:
#         print(f"- {name}")



# Newman
# def read_test_scores():
#     print("ENTER STUDENT ID: ")
#     student_id = input()  # Read student ID
#     print("ENTER EXAM SCORE: ")
#     exam_score = float(input())  # Read exam score
#     print("ENTER ALL TEST SCORES (7 total): ")
    
#     # Initialize a list to store test scores
#     test_scores = []
    
#     # Loop to read 7 test scores
#     for i in range(7):
#         score = float(input(f"Test Score {i + 1}: "))
#         test_scores.append(score)
    
#     # Calculate average of test scores
#     average_test_score = sum(test_scores) / len(test_scores)
    
#     return average_test_score, exam_score

# def compute_final_score(average_test_score, exam_score):
#     final_score = (0.4 * average_test_score) + (0.6 * exam_score)
#     return final_score

# def get_letter_grade(final_score):
#     if 90 <= final_score <= 100:
#         return 'A'
#     elif 80 <= final_score < 90:
#         return 'B'
#     elif 70 <= final_score < 80:
#         return 'C'
#     elif 60 <= final_score < 70:
#         return 'D'
#     else:
#         return 'F'
# def print_comment(grade):
#     comments = {
#         'A': "COMMENT: Very Good",
#         'B': "COMMENT: Good",
#         'C': "COMMENT: Satisfactory",
#         'D': "COMMENT: Need Improvement",
#         'F': "COMMENT: Poor"
#     }
    
#     print(comments.get(grade, "COMMENT: Invalid Grade"))
# # Main function to execute the program
# def main():
#     average_test_score, exam_score = read_test_scores()
    
#     print(f"TEST AVERAGE IS: {average_test_score:.2f}")
    
#     final_score = compute_final_score(average_test_score, exam_score)
    
#     print(f"FINAL SCORE IS: {final_score:.2f}")
    
#     grade = get_letter_grade(final_score)
    
#     print(f"LETTER GRADE IS: {grade}")
    
#     print_comment(grade)
# # Run the program
# main()


# Ofoe
# student_map = {    
#      "Jamie": 83.2,    
#      "Cersei": 76.3,    
#      "Tyrion": 55,
#      }
# average = sum(student_map.values()) / len(student_map)

# print("The average age is", average)
# print("Students that made it above the average grade are as follows:")

# for student in student_map:    
#      if student_map[student] > average:        
#           print(student)



# Newman 2
# Step 1: Create a dictionary to store student names and their grades
# students_grades = {    
#      "Alice": 85,    
#      "Bob": 78,    
#      "Charlie": 92,    
#      "David": 88,    
#      "Eva": 76
#      }

# # Step 2: Calculate the average grade
# def calculate_average(grades):    
#      total = sum(grades)    
#      count = len(grades)  

#      return total / count if count > 0 else 0
     
# # Step 3: Get all grades from the dictionary
# grades = list(students_grades.values())

# # Step 4: Calculate the average grade
# average_grade = calculate_average(grades)

# # Step 5: Print the average grade
# print(f"Average Grade: {average_grade:.2f}")

# # Step 6: Find and print names of students who scored above the average
# print("Students who scored above the average:")
# for student, grade in students_grades.items():    
#      if grade > average_grade:        
#           print(student)



# Daniel
# Student Score

student_scores ={    
     "Kofi": 90,    
     "Ama": 85,    
     "Kojo": 55
     }
# Calculate Students Average Score
average = sum(student_scores.values()) / len(student_scores)

# Outputs Average Grade
print(average)

# Outputs Student Scores Greater than Average
for student, scores in student_scores.items():    
     if scores > average:        
          print("The following student scored above average:", student, scores)






# students = {
#     "Faith": 60,
#     "Esi": 70,
#     "Isaac": 75,
#     "Dorcas": 76,
#     "Gerald": 73,
#     "Michael": 70,
#     "Felix": 79,
#     "Michael O.": 71
# }
#
#
# no_of_students = len(students)
# scores = students.values()
# avg = sum(students.values()) / no_of_students
#
# # Felix's solution
# print("Average: {}".format(avg))
# for item in students.items():
#     if item[1] >= avg:
#         print(f"{item[0]} scored above average" )
#
# print("----------------------------------")
#
# # Faith's code
# avg1 = sum(scores) / no_of_students
# print("Average: {}".format(avg1))
#
# for student, score in students.items():
#     if score >= avg1:
#         print("{} scored above average".format(student))
#
# print("----------------------------------")
#
# # Isaac
# students = {'a': 56, 'b':73, 'c':38}
# total = 0
# for key, val in students.items():
#     total += val
# average = total / len(students)
# print(f'The average score is {average}')
# for key, val in students.items():
#     if val >= average:
#         print(key, 'is above the average score')
#
# print("------------------------------------------------")
#
# # Gerald
# students ={"gebo": 99, "ge": 98, "geboyi": 99, "gift": 89, "Ella": 88}
# no_students = len(students)
# avg_score = sum(students.values())/no_students
# print(f"The average score is {avg_score:.2f}") #for students who scored above average
# for student, score in  students.items():
#     if score >= avg_score:
#         print(f"{student} passed, scored above average.")
#     else:
#         print(f"{student} scored below average.")