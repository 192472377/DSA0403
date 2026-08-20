import pandas as pd

# Step 1: Create a sample dataset
data = {
    'post_id': [101, 102, 103, 104, 105, 106, 107],
    'likes': [10, 25, 10, 40, 25, 10, 50]
}

# Step 2: Convert to DataFrame
posts_data = pd.DataFrame(data)

# Step 3: Calculate frequency distribution of likes
likes_distribution = posts_data['likes'].value_counts().sort_index()

# Step 4: Display results
print("Frequency Distribution of Likes:\n")
print(likes_distribution)
