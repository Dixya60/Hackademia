#TASK 1: Variable Modeling & Data Representation

# Student information
Full_name = "Emily Johnson" 
Age = 21                     
CGPA = 3.88                 
Current_semester = 5         
Enrollment_status = True     

# Printing values with their data types
print("Full Name : ", Full_name)
print("Type of Full name : ", type(Full_name))

print("Age : ", Age)
print("Type of Age : ", type(Age))

print("CGPA : ", CGPA)
print("Type of CGPA : ", type(CGPA))

print("Current Semester  : ", Current_semester)
print("Type of Current Semester  : ", type(Current_semester))

print("Enrollment Status : ", Enrollment_status)
print("Type of Enrollment Status : ", type(Enrollment_status))

# Reassigning age from int to string
age = "Twenty one"
print("\nAge after reassignment:", age)
print("Type of age:", type(age)) #This shows Python doesn’t restrict a variable to a single type; 
                                 #it adapts at runtime.

#Reasoning Questions
#1. How does Python’s dynamic typing influence memory allocation and runtime behavior?
# Ans :  Python’s dynamic typing allows variables to change type at runtime.
#        Memory is allocated dynamically, and type checks happen during execution.
#        This makes coding flexible but can cause runtime errors.

#2. Why is strict type enforcement preferred in system-level software but not in scripting languages? 
# Ans :  Strict typing is preferred in system-level software for efficiency, safety, 
#        and predictable memory usage. In scripting languages, flexibility and rapid 
#        development are more important, so dynamic typing is used.