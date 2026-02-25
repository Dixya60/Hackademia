#  Create a module with regex-based validation functions for: 
#  Username rules (start with a letter, no spaces, no trailing underscore)
#  Password rules (min 10 chars, uppercase, digit, special char) 
#  Email validation 
#  Then write a CLI interface that reads user input CSV and validates each row’s credentials, outputting results to a new CSV. 

import re
import csv

#Validation functions
# 1. Username validation
def validate_username(username):
    pattern = "^[A-Za-z][A-za-z0-9_]*[A-Za-z0-9]$"
    if re.match(pattern, username):
        return True
    else:
        return False
    
# 2. Password validation
def validate_password(password):
    pattern = r"^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()]).{10,}$"
    if re.match(pattern, password) :
        return True
    else:
        return False
    
# 3. Email validation
def validate_email(email):
    pattern = "^[A-Za-z0-9._-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    if re.match(pattern, email):
        return True
    else:
        return False
    
#  CSV Files
input_file = open("","r")
output_file = open("validated_users.csv","w",newline="")

read = csv.reader(input_file)
write = csv.writer(output_file)

header = next(read)
write.writerow(header + ["username_valid", "password_valid", "email_valid"])

#Process each row
for row in read:
    username = row[0]
    password = row[1]
    email=row[2]
    
    #validate each field
    username_valid = validate_username(username)
    password_valid = validate_password(password)
    email_valid = validate_email(email)
    
    #Write row + validation 
    write.writerow(row + [username_valid, password_valid, email_valid])
    
#close files
input_file.close()
output_file.close()

print("Validation complete ! Check validated_users.csv")
