# TASK 4: Branching & Decision Making 

# Inputs
attendance = float(input("Enter attendance percentage: "))
total_marks = float(input("Enter total marks (out of 100): "))

# Check eligibility
if attendance >= 75:
    print("You are eligible.")
    
    #Assigning grades if eligible
    if total_marks >= 90:
         grade = "A+"
    elif total_marks >= 80:
        grade = "A"
    elif total_marks >= 70:
        grade = "B+"
    elif total_marks >= 60:
        grade = "B"
    elif total_marks >= 50:
         grade = "C"
    else:
        grade = "F"
    
    print("Your grade is : ", grade)
    
else:
     print("You are not eligible due to low attendance.")
    
    
# Scholarship eligibility Checker
cgpa = float(input("\nEnter your CGPA (out of 4): "))
family_income = float(input("Enter your family annual income (in USD): "))
attendance = float(input("Re-enter your attendance percentage for scholarship check: "))
    
# Scholarship conditions
if cgpa >= 3.6 and family_income < 50000 and attendance >= 75:
    print("You are eligible for the scholarship!")
else:
    print("You are NOT eligible for the scholarship.")
    