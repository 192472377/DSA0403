import string
from collections import Counter

# Step 1: Read the file
with open("sample_text.txt", "r") as file:
    text = file.read()

# Step 2: Convert to lowercase
text = text.lower()

# Step 3: Remove punctuation
text = text.translate(str.maketrans("", "", string.punctuation))

# Step 4: Split into words
words = text.split()

# Step 5: Count word frequencies
word_freq = Counter(words)

# Step 6: Display results
print("Word Frequency Distribution:\n")
for word, freq in word_freq.items():
    print(f"{word}: {freq}")
