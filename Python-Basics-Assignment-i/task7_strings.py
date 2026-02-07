# TASK 7: String Processing & Traversal 

# Input
sentence = input("Enter a sentence : ")

# Initialize 
vowels = 0
consonants = 0
digits = 0
spaces = 0

# Count vowels, consonants, digits, spaces
for char in sentence:
    if char.isalpha() :
        if char.lower() in 'aeiou' :
            vowels += 1
        else:
            consonants += 1
    elif char.isdigit() :
        digits += 1
    elif char == ' ' :
        spaces += 1
    else:
        pass
    
# Convert case
converted_sentence = ""
for char in sentence :
    if char.islower() :
        converted_sentence += char.upper()
    elif char.isupper() :
        converted_sentence += char.lower()
    else:
        converted_sentence += char
    
# Remove extra spaces
cleaned_sentence = ' '.join(sentence.split())

# Outputs
print("Vowels : ", vowels)
print("Consonants : ", consonants)
print("Digits : ", digits)
print("Spaces : ", spaces)
print("Sentence after case conversion : ", converted_sentence)
print("Sentence after removing extra spaces is : ", cleaned_sentence)


# Reasoning Questions
# 1. Why is string processing critical in cybersecurity and NLP? 
# Ans :  String processing is important because cybersecurity systems analyze text to detect
#        attacks,while NLP uses strings to understand and process human language.

# 2. How can improper string handling introduce vulnerabilities? 
# Ans :  If strings are handled incorrectly, it can cause errors or security holes,
#        like allowing hackers to run unwanted commands or access data.