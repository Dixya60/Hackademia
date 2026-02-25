# List/Dict/Set Challenge – Analytics 
# Write a program that analyzes text data from multiple files to produce:
#  - A list of the top 100 most common words 
#  - A dictionary mapping each word to its count
#  - A set of words longer than 7 characters 
# Use efficient data structures and avoid loading entire files into memory at once.

import os
import string

# Folder path
folder_path = "../assignment_data/texts"

word_counts = {}    # dictionary for word counts
long_words = set()  # set for words longer than 7 characters 

# Process files line by line
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(folder_path, filename)
        
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                #remove punctuation, convert to lowercase
                line = line.translate(str.maketrans("","", string.punctuation)).lower()
                words = line.split()
                
                for word in words:
                    if word in word_counts:
                        word_counts[word] += 1
                    else:
                        word_counts[word] = 1
                        
                    # Add to set if longer than 7 characters
                    if len(word) > 7:
                        long_words.add(word)
                    
# Top 100 most common words
# Convert dict to list of tuples and sort by count descending
sorted_words = sorted(word_counts.items(), key= lambda x: x[1], reverse=True)
top_100_words = sorted_words[:100]

# Print results
print("Top 100 most common words : ")
for word, count in top_100_words:
    print(f"{word} : {count}")

print("\nTotal unique words counted : ",len(word_counts))
print("\nWords longer than 7 characters : ", long_words)