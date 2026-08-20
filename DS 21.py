import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

# Dataset
age = [23,23,27,27,39,41,47,49,50,52,54,54,56,57,58,58,60,61]
fat = [9.5,26.5,7.8,17.8,31.4,25.9,27.4,27.2,31.2,34.6,42.5,28.8,33.4,30.2,34.1,32.9,41.2,35.7]

# Create DataFrame
df = pd.DataFrame({"Age": age, "Fat%": fat})

# Statistics
print("Mean Age:", df["Age"].mean())
print("Median Age:", df["Age"].median())
print("Std Dev Age:", df["Age"].std())

print("Mean Fat%:", df["Fat%"].mean())
print("Median Fat%:", df["Fat%"].median())
print("Std Dev Fat%:", df["Fat%"].std())

# Boxplots
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
sns.boxplot(y=df["Age"])
plt.title("Boxplot of Age")

plt.subplot(1,2,2)
sns.boxplot(y=df["Fat%"])
plt.title("Boxplot of Fat%")
plt.show()

# Scatter plot
plt.scatter(df["Age"], df["Fat%"], color="blue")
plt.xlabel("Age")
plt.ylabel("Fat%")
plt.title("Scatter Plot: Age vs Fat%")
plt.show()

# Q-Q plot
stats.probplot(df["Fat%"], dist="norm", plot=plt)
plt.title("Q-Q Plot for Fat%")
plt.show()
