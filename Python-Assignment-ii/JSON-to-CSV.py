# Build a script that takes multiple JSON files (each with potentially different keys) and:
#    -  Extracts a unified set of fields based on a mapping config
#    -  Outputs a combined CSV with consistent columns 
# Script should dynamically handle missing keys per record. 

import json
import csv

# Mapping Configuration
mapping = {
    "ID" : ["id"],
    "Name" : ["name", "username"],
    "Email" : ["email"],
    "Age" : ["age"]
}

columns = ["ID", "Name", "Email", "Age"]
all_rows = []

# Read file1 and file2
with open("../assignment_data/json_data/data1.json", "r") as f:
    data1 = json.load(f)
    
with open("../assignment_data/json_data/data2.json", "r") as f:
    data2 = json.load(f)
    
# Combine both files
combined_data = data1 + data2

# Process records
for record in combined_data:
    row = {}
    for col in columns:
        row[col] = ""     #default blank
        
        for key in mapping[col]:
            if key in record:
                row[col] = record[key]
                break
    all_rows.append(row)
        
# Write CSV file
with open("combined_JSON_file.csv", "w", newline="") as f:
    write = csv.DictWriter(f, fieldnames=columns)
    write.writeheader()
    write.writerows(all_rows)
    
print("CSV file created successfully !")
print("Check file : combined_JSON_file.csv ")