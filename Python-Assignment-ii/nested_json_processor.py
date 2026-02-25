#  Extract all user IDs who have performed a specific action 
#  Count how many times each action occurred 
#  Output a sorted list of actions by frequency 
#  Use dictionary logic and comprehension.

import json

#Load json file
with open("../assignment_data/users.json","r") as f:
    data = json.load(f)
    
#Unique actions - set comprehension    
unique_actions = {act["action"] for user in data for act in user["profile"]["activity"]}

#Get user IDs who performed a specific action - list comprehension
def get_users_by_action(action_name):
    return [
        user["user_id"]
        for user in data
        if any(act["action"] == action_name for act in user["profile"]["activity"])
    ]

# Count total occurence of each action - Dictionary comprehension
action_counts = {
    action : sum(
        act["count"] 
        for user in data 
        for act in user["profile"]["activity"]
        if act["action"] == action
    )
    for action in unique_actions
}

#  Sort actions by frequency (highest first)
sorted_actions = sorted(action_counts.items(), key = lambda x: x[1], reverse=True)
   
#  Print user IDs for each action
print("User IDs for each action : ")
for action in unique_actions:
    print(f"{action} : {get_users_by_action(action)}")
    
#  Print total counts of each action
print("\nTotal counts of each action : ")
for action, total in action_counts.items():
    print(f"{action} : {total}")
    
#  Print actions sorted by frequency
print("\nActions sorted by total count (highest first) : ")
for action, total in sorted_actions:
    print(f"{action} : {total}")