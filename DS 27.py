import pandas as pd
import matplotlib.pyplot as plt

# Synthetic dataset
data = {
    "Name": ["PlayerA","PlayerB","PlayerC","PlayerD","PlayerE","PlayerF","PlayerG","PlayerH"],
    "Age": [22, 28, 25, 30, 27, 24, 29, 26],
    "Position": ["Forward","Midfielder","Defender","Forward","Goalkeeper","Midfielder","Forward","Defender"],
    "Goals": [15, 8, 2, 20, 0, 5, 12, 3],
    "Salary": [5000, 7000, 4000, 9000, 3000, 6000, 8000, 4500]
}
df = pd.DataFrame(data)
df.to_csv("soccer.csv", index=False)

# Read CSV
df = pd.read_csv("soccer.csv")

# Top 5 by goals
print("Top 5 Goal Scorers:\n", df.nlargest(5, "Goals")[["Name","Goals"]])

# Top 5 by salary
print("Top 5 Salaries:\n", df.nlargest(5, "Salary")[["Name","Salary"]])

# Average age
avg_age = df["Age"].mean()
print("Average Age:", avg_age)
print("Players above average age:\n", df[df["Age"] > avg_age]["Name"])

# Bar chart by position
df["Position"].value_counts().plot(kind="bar")
plt.title("Distribution of Players by Position")
plt.show()
