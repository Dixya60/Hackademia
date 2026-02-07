# TASK 5: Iteration Using for Loops 

n = int(input("Enter number of subjects : "))

total = 0

for i in range(n):
    marks = float(input(f"Enter marks for subject {i+1} : "))
    
    total = total + marks
    
    if i == 0:
        highest = marks
        lowest = marks
    else:
        if marks > highest:
            highest = marks
        if marks < lowest:
            lowest = marks
    
average = total/n

print("\nTotal marks : ", total)
print("Average marks : ", average)
print("Highest marks : ", highest)
print("Lowest marks : ", lowest)
