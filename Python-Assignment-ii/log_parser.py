# Log Parser with Regex & File I/O

# 1. Reads all .log files from a directory
# 2. Extracts ERROR and WARNING log entries
# 3. Saves extracted logs into CSV file
# 4. Creates JSON summary of severity count
# 5. Handles malformed lines and errors gracefully

import re
import os
import csv
import json

#Pattern 
pattern = r"^(.*?) \[(ERROR|WARNING)\] (.*?)$" 

#Log Folder Path
folder_path = "../assignment_data/logs"

data = []
summary = {
    "ERROR" : 0,
    "WARNING" : 0
}

#Read all files in folder
try:
    files = os.listdir(folder_path)
    
    for file in files:
        if file.endswith(".log"):
            file_path = os.path.join(folder_path,file)
            
            with open(file_path,"r") as f:
                for line in f:
                    line = line.strip()
                    match = re.search(pattern,line)
                    
                    if match:
                        timestamp = match.group(1)
                        level = match.group(2)
                        message = match.group(3)
                        
                        data.append([timestamp,level,message])
                        summary[level] += 1
                        #If line doesn't match, ignore it
                        
except FileNotFoundError:
    print("Folder not found !")
    
#Write CSV file 
with open("output.csv","w",newline="") as f:
    write = csv.writer(f)
    write.writerow([" Timestamp "," Log level ", " Message "])
    write.writerows(data)
    
#Write JSON summary
with open("summary.json","w") as f:
    json.dump(summary,f,indent=4)
    
print("Done! Check output.csv and summary.json")

