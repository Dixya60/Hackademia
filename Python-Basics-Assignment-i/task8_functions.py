# TASK 8: Functions 

# Calculating average marks
def calc_avg(total_marks, n):
     return total_marks / n

# Determining grade 
def determine_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "B+"
    elif average >= 50:
        return "C"
    else:
        return "F"
    
# Display results/outputs
def display_result(average, grade):
    print("----Result----")
    print(f"Average marks : {average:.2f}")
    print("Grade : ", grade)

# Main Program
n = int(input("Enter number of subjects : "))
total_marks = 0

for i in range(n):
    marks = float(input(f"Enter marks for subject {i+1}: "))
    total_marks += marks

# Call function
average = calc_avg(total_marks, n)
grade = determine_grade(average)
display_result(average, grade)


# Conceptual / Brainstorming Question
# 1. Why is returning values better than printing inside functions? 
# Ans :  Returning values is better because it makes functions reusable and flexible, 
#        i.e function's result can be used elsewhere; unlike printing which just shows
#        output and cannot be reused.
