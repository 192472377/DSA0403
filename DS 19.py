import pandas as pd
import string
from collections import Counter

# Step 1: Create a sample dataset of customer reviews
data = {
    'review_id': [1, 2, 3],
    'review_text': [
        "This product is amazing and easy to use",
        "I love this product, it is very useful",
        "The product is good but could be better"
    ]
}

# Step 2: Convert to DataFrame
reviews_data = pd.DataFrame(data)

# Step 3: Combine all reviews into one big text
all_reviews = " ".join(reviews_data['review_text'])

# Step 4: Clean text (lowercase + remove punctuation)
all_reviews = all_reviews.lower()
all_reviews = all_reviews.translate(str.maketrans("", "", string.punctuation))

# Step 5: Split into words
words = all_reviews.split()

# Step 6: Count word frequencies
word_freq = Counter(words)

# Step 7: Display results
print("Frequency Distribution of Words in Reviews:\n")
for word, freq in word_freq.items():
    print(f"{word}: {freq}")
