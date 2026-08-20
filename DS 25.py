import pandas as pd
import scipy.stats as stats

# Step 1: Load dataset
data = pd.read_csv("customer_reviews.csv")

# Step 2: Extract ratings column
ratings = data["rating"]

# Step 3: Calculate mean rating
mean_rating = ratings.mean()

# Step 4: Calculate 95% confidence interval
ci = stats.t.interval(
    0.95,                      # confidence level
    len(ratings) - 1,          # degrees of freedom
    loc=mean_rating,           # mean
    scale=stats.sem(ratings)   # standard error of mean
)

# Step 5: Display results
print("Average Rating:", mean_rating)
print("95% Confidence Interval:", ci)
