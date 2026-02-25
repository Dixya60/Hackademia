# Write a program that: 
#  -  Reads a large unstructured text file 
#  -  Extracts only valid IP addresses, dates, and email addresses using regex 
#  -  Aggregates these into separate CSV files 
#  -  Outputs a final JSON report of how many of each type were found Handle overlapping
#     matches and avoid partial capture conflicts.

import re
import json
import csv

# File path
input_file = "../assignment_data/raw_dump.txt"

# Patterns
ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
date_pattern = r"\b\d{4}-\d{2}-\d{2}\b|\b\d{2}/\d{2}/\d{4}\b" 
email_pattern = r"\b[\w\.-]+@[\w\.-]+\.\w{2,}\b"

# Set to store unique matches
ips, dates, emails = set(), set(), set()

# Read file and extract matches
with open(input_file) as f:
    for line in f:
        ips.update(re.findall(ip_pattern,line))
        dates.update(re.findall(date_pattern,line))
        emails.update(re.findall(email_pattern, line))
        
# Function to save csv
def save_csv(filename,header,data):
    with open(filename,"w",newline="") as f:
        write = csv.writer(f)
        write.writerow([header])
        
        for item in sorted(data):
            write.writerow([item])
            
# Save csvs
save_csv("ips.csv","IP Address",ips)
save_csv("dates.csv","Date",dates)
save_csv("emails.csv","Email", emails)

# Create JSON report
report = {
    "Total IPS " : len(ips),
    "Total Dates " : len(dates),
    "Total Emails " : len(emails)
}

# Save JSON report
with open("data_report.json","w") as f:
    json.dump(report, f, indent=4)
    
print("\nExtraction completed !\n")
print("Check files :- \n a)  ips.csv \n b)  dates.csv  \n c)  emails.csv  \n d)  data_report.json")