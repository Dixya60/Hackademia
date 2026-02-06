# TASK 2: User Input, Type Casting & Runtime Errors 

print("=== Financial Calculator WITHOUT Type Casting ===\n")
# Ask user for monthly income and expenses
try:
    monthly_income = input("Enter your monthly income: ")
    monthly_expenses = input("Enter your monthly expenses: ")

    # Try to calculate savings
    savings = monthly_income - monthly_expenses
    print("Your savings are:", savings)
except TypeError as e:
    print("Error Occured :", e)
    
    
print("\n===Financial calculator WITH type casting===\n")
# Ask user for monthly income and expenses
try:
    monthly_income = float(input("Enter your monthly income: "))
    monthly_expenses = float(input("Enter your monthly expenses: "))

    # Try to calculate savings
    savings = monthly_income - monthly_expenses

    if savings >= 0 :
        print("You are saving : ", savings)
    else:
        print("You are in deficit:", abs(savings))
except ValueError as e:
    print("Invalid input! Please enter numeric values only.")
    
    
#Reasoning Questions
#1. Why does Python delay type errors until runtime, unlike compiled languages? 
# Ans : Python is an interpreted, dynamically-typed language.
#       Variables do not have a fixed type at compile time — their type is determined when the program runs.

#2. How could unvalidated user input compromise real-world systems (e.g., billing, voting)? 
# Ans : Users can enter wrong or malicious data, causing program crashes or incorrect results.
#       In critical systems like billing or voting, this can lead to financial errors, wrong calculations, or security vulnerabilities.