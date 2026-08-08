import pandas as pd

# Example dataset
data = pd.DataFrame({
    "City": ["Delhi","Delhi","Delhi","Mumbai","Mumbai","Mumbai","Chennai","Chennai","Chennai"],
    "Temperature": [30, 35, 40, 28, 29, 30, 32, 33, 34]
})

# Group by city
grouped = data.groupby("City")["Temperature"]

mean_temp = grouped.mean()
std_temp = grouped.std()
range_temp = grouped.max() - grouped.min()

highest_range_city = range_temp.idxmax()
most_consistent_city = std_temp.idxmin()

print("Mean Temperature:\n", mean_temp)
print("\nStandard Deviation:\n", std_temp)
print("\nTemperature Range:\n", range_temp)
print("\nCity with Highest Range:", highest_range_city)
print("Most Consistent City:", most_consistent_city)
