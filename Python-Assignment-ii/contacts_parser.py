# Structured Data Extraction & Transformation

# 1. Reads a text file containing mixed structured records(name, email, phone number)
# 2. Extracts valid emails and names with valid phone numbers
# 3. Deduplicates emails
# 4. Saves results to a JSON file

import re
import json

# Regex Patterns
email_pattern = r"[a-zA-Z0-9._+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
phone_pattern = r"\(?\d{3}\)?[- ]?\d{3}[- ]?\d{4}"

# File path
file_path = "../assignment_data/contacts.txt"

# Data
contacts = []  # list of dictionaries with valid name + email + phone
seen_contacts = set()  #set of (name, email, phone) tuples for fast duplicate check

# Read file
try:
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            # Extract emails
            correct_email = re.findall(email_pattern, line)

            # Extract phone numbers
            phone_match = re.search(phone_pattern, line)

            if phone_match and correct_email:
                name = line.split(",")[0].strip()
                email = correct_email[0]
                phone = phone_match.group()

                # Avoid duplicate contacts (same name + phone + email)
                contact_key = (name, phone, email)
                if contact_key not in seen_contacts:
                 contacts.append(
                    {
                        "name": name,
                        "email": email,
                        "phone": phone
                    })
                 seen_contacts.add(contact_key)

except FileNotFoundError:
    print("File not found! Check file path.")
    exit()

# Prepare JSON data
output_data = {
    "contacts": contacts
}

# Write JSON file
with open("contacts_summary.json", "w") as f:
    json.dump(output_data, f, indent=4)

print("Done! Check contacts_summary.json")
