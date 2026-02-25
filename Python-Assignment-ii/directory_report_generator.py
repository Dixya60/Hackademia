# Scan all files in a folder recursively and produce: 
#  -  A JSON file listing each file path, size, and last modified timestamp
#  -  A set of unique file extensions 
#  -  A count of how many files per extension type 
# Handle permission exceptions and skip unreadable files cleanly. 

import os
import json

# Path
folder = "../assignment_data/"

file_data = []
extensions = set()
extension_count = {}

# Scan folder
for root, dirs, files in os.walk(folder):
    for file in files:
        path = os.path.join(root,file)
        
        try:
            size = os.path.getsize(path)
            last_modified = os.path.getmtime(path)
            extension = os.path.splitext(file)[1]
            
            file_data.append(
                {
                    "Path " : path,
                    "Size " : size,
                    "Last modified " : last_modified
                })
            
            extensions.add(extension)
            
            if extension in extension_count:
                extension_count[extension] += 1
            else:
                extension_count[extension] = 1
                
        except:
            continue  # Skip unreadable files
   
# Create final report
report = {
    "Files " : file_data,
    "Unique extensions " : list(extensions),  # Convert set to list for json
    "Count per extension type " : extension_count
}

# Save json report     
with open("Dir_Report.json","w") as f:
    json.dump(report, f, indent=4)
    
print("Report saved to Dir_Report.json!")        