# Write a script that reads a CSV where some fields are missing or malformed (e.g., number fields as text). 
# The script should: 
#   - Detect and correct common data problems 
#   - Fill missing numeric values with the column mean 
#   - Save both clean CSV and a JSON report of data quality issues (counts of errors per column). 

import csv
import json

rows = []      # Store all data rows from CSV
sums = {}      # Store total of numeric values per column
counts = {}    # Store no. of valid numbers per column
errors = {}    # Count missing/ wrong values

# List of numeric columns
numeric_cols = ["PassengerId","Survived","Pclass","Age","SibSp","Parch","Fare"]

# Read CSV file
with open("../assignment_data/titanic.csv","r") as f:
    read = csv.DictReader(f)    # Read CSV file as dictionary
    headers = read.fieldnames   # Get all columns name
    
    #Initialize
    for col in numeric_cols:
        sums[col], counts[col], errors[col] = 0, 0, 0
        
    #Loop through each row in file
    for row in read:
        rows.append(row)   # Store row for later use
        
        # Check each column value
        for col in numeric_cols:
            value = row[col].strip()  # Remove extra spaces
            
            if value == "":
                errors[col] += 1  #If value is empty, count as error
                continue
            
            # Try converting value to float (Check if numeric)
            try:
                num = float(value)
                sums[col] += num
                counts[col] += 1
            except:
                errors[col] += 1
                
# Calculate mean for numeric columns
means = {}

for col in numeric_cols:
    if counts[col] > 0 :
        means[col] = sums[col] / counts[col]

# Replace missing or invalid values
for row in rows:
    for col in numeric_cols:
        try:
            float(row[col])  #Try converting to check if valid number
        except:
            if col in means:
                row[col] = str(round(means[col], 2)) # Replace with mean upto 2 decimal places
                
                
# Save cleaned CSV file
with open("cleaned_titanic.csv","w", newline="") as f:
    write = csv.DictWriter(f, fieldnames=headers)
    write.writeheader()
    write.writerows(rows)
    
# Save error report to JSON file
with open("error_report_titanic.json","w") as f:
    json.dump(errors, f, indent=4)
    
print("Cleaning completed successfully.")
print("Check files : cleaned_titanic.csv and error_report_titanic.json !")