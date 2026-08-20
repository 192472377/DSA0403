import pandas as pd
import scipy.stats as stats

# Load dataset
data = pd.read_csv("rare_elements.csv")

# Sample up to 30 rows (or fewer if dataset smaller)
sample = data.sample(n=min(30, len(data)), replace=False)

# Select the first column (assuming it's numeric)
mean = sample.iloc[:, 0].mean()

# Compute 95% confidence interval
ci = stats.t.interval(
    0.95,
    len(sample)-1,
    loc=mean,
    scale=stats.sem(sample.iloc[:, 0])
)

print("Sample Mean:", mean)
print("95% CI:", ci)
