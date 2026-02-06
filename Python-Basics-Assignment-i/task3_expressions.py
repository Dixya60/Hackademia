# TASK 3: Arithmetic Logic & Expressions 

# Input scores
assignment_score = float(input("Enter assignment score (out of 100) : "))
lab_score = float(input("Enter lab score (out of 100) : "))
exam_score = float(input("Enter exam score (out of 100): "))

#Calculate final score
# Assume Assignment = 30%, Lab = 20%, Exam = 50%
final_score = (0.3*assignment_score) + (0.2*lab_score) + (0.5*exam_score)

# Display result 
print(f"\nFinal score of the student is : {final_score:.2f}")

#Reasoning Questions
# 1. Why is operator precedence critical in scientific or financial software? 
# Ans :  Operator precedence determines the order in which calculations are performed.
#        If the order is wrong, the results can be incorrect, which in scientific or financial applications can cause serious errors or losses.

# 2. How could floating-point precision errors affect real-world applications? 
# Ans : Computers store decimals approximately.
#       Small rounding errors can accumulate, causing financial discrepancies, scientific inaccuracies, or measurement errors.