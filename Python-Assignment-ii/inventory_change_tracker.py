# You have two CSV files representing inventory snapshots at times T1 and T2. 
# Write a script that: 
#   -  Reads both CSVs into dictionaries 
#   -  Outputs added, removed, and quantity-changed items 
# Results should be saved to JSON and printed in a human-friendly report. 

import csv
import json

# Read T1 inventory
t1 = {}
with open("../assignment_data/inventory_T1.csv") as f:
    read = csv.DictReader(f)
    for row in read:
        t1[row["item_id"]] = {"name" : row["item_name"], "quantity" : int(row["quantity"])}

# Read T2 inventory
t2 = {}
with open("../assignment_data/inventory_T2.csv") as f:
    read = csv.DictReader(f)
    for row in read:
        t2[row["item_id"]] = {"name" : row["item_name"], "quantity" : int(row["quantity"])}
        
# Prepare dictionaries for changes
added = {}
removed = {}
changed = {}

# Check for added items or quantity changes
for item_id in t2:
    if item_id not in t1:
        added[item_id] = t2[item_id]
    elif t2[item_id]["quantity"] != t1[item_id]["quantity"]:
        changed[item_id] = {
            "Name" : t2[item_id]["name"],
            "Old" : t1[item_id]["quantity"],
            "New" : t2[item_id]["quantity"]
        }
        
# Check for removed items
for item_id in t1:
    if item_id not in t2:
        removed[item_id] = t1[item_id]
        
# Create JSON report
report = {
    "Added" : added,
    "Removed" : removed,
    "Quantity Changed" : changed
}
    
# Save report 
with open("inventory_report.json", "w") as f:
    json.dump(report, f, indent=4)
    
print("Done! Check file : inventory_report.json")