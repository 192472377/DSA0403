import nltk
nltk.download('stopwords')
import pandas as pd
import string
from collections import Counter
import matplotlib.pyplot as plt
from nltk.corpus import stopwords

# Step 1: Load dataset
data = pd.read_csv("data.csv")

# Step 2: Combine all feedback into one big text
all_feedback = " ".join(data['feedback'])

# Step 3: Preprocess text
# Convert to lowercase
all_feedback = all_feedback.lower()

# Remove punctuation
all_feedback = all_feedback.translate(str.maketrans("", "", string.punctuation))

# Split into words
words = all_feedback.split()

# Remove stopwords (common words like 'the', 'and', 'is')
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word not in stop_words]

# Step 4: Calculate frequency distribution
word_freq = Counter(filtered_words)

# Step 5: Ask user for N (top N words)
N = int(input("Enter the number of top frequent words to display: "))

# Step 6: Display top N words
top_words = word_freq.most_common(N)
print("\nTop", N, "Most Frequent Words:\n")
for word, freq in top_words:
    print(f"{word}: {freq}")

# Step 7: Plot bar graph
words_list, freq_list = zip(*top_words)
plt.bar(words_list, freq_list, color='skyblue')
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title(f"Top {N} Most Frequent Words in Feedback")
plt.show()
