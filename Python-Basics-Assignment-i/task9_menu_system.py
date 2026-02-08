# TASK 9: Mini System Integration Task 

def enter_details():
    name = input("Enter student name : ")
    roll_no = input("Enter roll number : ")
    return name, roll_no
    
def enter_marks(n):
    marks=[]
    for i in range(n):
        while True:
            m = float(input(f"Enter marks for subject {i+1} : "))
            if m>=0 and m<=100:
                marks.append(m)
                break
            else:
                print("Invalid marks! Must be between 0 and 100.")
    return marks

def calc_avg(marks, n):
    total_marks = 0
    for m in marks:
        total_marks += m
    return total_marks/ n

def determine_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B+"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "F"

def view_summary(name, roll_no, marks,n):
    average = calc_avg(marks, n)
    grade = determine_grade(average)
    print("\n------Result Summary------")
    print("Name : ", name)
    print("Roll : ", roll_no)
    print("Marks : ", marks)
    print("Average : ", average)
    print("Grade : ", grade)
    

#Main program
name = ""
roll_no = ""
marks = []

print("\n--- Student Utility System ---")
print("\n1. Enter student details")
print("2. Enter marks")
print("3. View result summary")
print("4. Exit")

while True:

    choice = input("\nEnter your choice (1-4) : ")

    if choice == "1" :
        name , roll_no = enter_details()
        print("Details saved !")
    elif choice == "2" :
        n = int(input("Enter number of subjects : "))
        marks = enter_marks(n)
        print("Marks saved !")
    elif choice == "3":
        if name=="" or roll_no=="" :
            print("Enter details first !")
        elif marks == []:
            print("Enter marks first !")
        else: 
            view_summary(name, roll_no, marks, n)
    elif choice == "4" :
        print("Exiting...")
        break
    else:
        print("Invalid Choice !")
        

# Reasoning Question
# 1. What changes would be required to convert this into a web application?
# Ans :   We have to replace console input/output with HTML forms and pages, 
#         use a backend to handle logic, and store data(student details) in a 
#         database instead of variables.