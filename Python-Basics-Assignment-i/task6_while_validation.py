# TASK 6: Input Validation with while Loops 

n = int(input("Enter number of subjects : "))

for i in range(n):
    while True :
        marks = int(input(f"Enter the marks for subject {i+1} (0-100) : "))
        
        if marks < 0 or marks > 100 :
            print("Invalid marks! Please enter the marks between 0 and 100.")
        else:
            print("Valid marks entered is : ", marks)
            break
    

# Conceptual Questions 
# 1. Why is validation better handled with while loops than for loops? 
# Ans :  While loops repeat until the input is valid, no matter how many times the user enters wrong data.
#        However, For loops run a fixed number of times, so we cannot guarantee that the user will enter valid 
#        input within that number of attempts.
