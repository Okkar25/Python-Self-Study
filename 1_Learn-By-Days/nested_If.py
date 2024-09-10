# Problem 1: Determine the Largest of Three Numbers
# Problem: Write a Python program that takes three numbers as input and prints the largest number using nested if statements.


# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# c = int(input("Enter the third number: "))

# if a > b:
#     if a > c:
#         largest = a
#     else:
#         largest = c
        
# else:
#     if b > c:
#         largest = b
#     else:
#         largest = c
    
# # 20  10  25
# # 5   10  25
        
        
# print("The largest number is:", largest)



# ==============================================================



# Problem 3: Grade Classification Based on Marks
# Problem: Write a Python program to classify grades based on marks using nested if statements.


# marks = int(input("Enter your marks: "))

# if marks >= 90:
#     grade = 'A'
# elif marks >= 80:
#     if marks >= 85:
#         grade = 'B+'
#     else:
#         grade = 'B'
# elif marks >= 70:
#     if marks >= 75:
#         grade = 'C+'
#     else:
#         grade = 'C'
# else:
#     grade = 'D'

# print("The grade is:", grade)



# ==============================================================



# Problem 4: Determine the Type of Triangle
# Problem: Write a Python program that takes the lengths of three sides of a triangle as input and determines whether the triangle is equilateral, isosceles, or scalene using nested if statements.


# side1 = int(input("Enter the length of the first side: "))
# side2 = int(input("Enter the length of the second side: "))
# side3 = int(input("Enter the length of the third side: "))

# if side1 == side2:
#     if side2 == side3:
#         triangle_type = "Equilateral"
#     else:
#         triangle_type = "Isosceles"
# else:
#     if side1 == side3 or side2 == side3:
#         triangle_type = "Isosceles"
#     else:
#         triangle_type = "Scalene"

# print("The triangle is:", triangle_type)



# ==============================================================


# Problem 6: Discount Calculation Based on Price
# Problem: Write a Python program that takes the price of an item as input and calculates the final price after applying a discount using nested if statements.

# for price > 200 => discount 20%
# for price > 100 => discount 10%
# for price < 100 => discount 5%


# Input the price

price = float(input("Enter the price of the item: "))

# Nested if statements for discount calculation
if price > 100:
    if price > 200:
        discount = 20  # 20% discount
    else:
        discount = 10  # 10% discount
else:
    discount = 5  # 5% discount

final_price = price - (price * discount / 100)
print("The final price after discount is:", final_price)



# ==============================================================



# Problem: University Admission Decision
# Problem: Write a Python program to determine a student's admission status based on several criteria. The criteria include academic performance, extracurricular activities, volunteer work, and entrance exam scores.


# The program should prompt the user for their GPA, number of extracurricular activities, volunteer work hours, and entrance exam score. Based on the following conditions, the program should decide if the student gets "Full Admission", "Conditional Admission", or "No Admission":


# Full Admission: -------------------
# GPA is 3.5 or higher.
# If GPA is 3.5 or higher:
# Entrance exam score must be 85 or higher.
# If entrance exam score is 85 or higher:
# At least 2 extracurricular activities.
# If 2 or more extracurricular activities:
# At least 30 volunteer work hours.

# Conditional Admission: ------------
# If the GPA is between 3.0 and 3.49 and the entrance exam score is between 75 and 84.
# If so:
# At least 1 extracurricular activity or 20 volunteer work hours.

# No Admission: ---------------------
# If none of the above conditions are met.



# Input the required details


gpa = float(input("Enter your GPA: "))
activities = int(input("Enter the number of extracurricular activities: "))
volunteer_hours = int(input("Enter the number of volunteer work hours: "))
exam_score = int(input("Enter your entrance exam score: "))

# Nested if statements for admission decision
if gpa >= 3.5:
    if exam_score >= 85:
        if activities >= 2:
            if volunteer_hours >= 30:
                admission_status = "Full Admission"
            else:
                admission_status = "No Admission"
        else:
            admission_status = "No Admission"
    else:
        admission_status = "No Admission"
elif 3.0 <= gpa < 3.5:
    if 75 <= exam_score < 85:
        if activities >= 1 or volunteer_hours >= 20:
            admission_status = "Conditional Admission"
        else:
            admission_status = "No Admission"
    else:
        admission_status = "No Admission"
else:
    admission_status = "No Admission"

print("Admission Status:", admission_status)


