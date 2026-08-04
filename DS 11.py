import matplotlib.pyplot as plt

# Example dataset
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [15000, 18000, 12000, 22000, 25000, 20000]

# 1. Line Plot
plt.figure(figsize=(8,5))
plt.plot(months, sales, marker='o', color='blue', linestyle='-')
plt.title("Monthly Sales - Line Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

# 2. Scatter Plot
plt.figure(figsize=(8,5))
plt.scatter(months, sales, color='red', marker='x')
plt.title("Monthly Sales - Scatter Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

# 3. Bar Plot
plt.figure(figsize=(8,5))
plt.bar(months, sales, color='green')
plt.title("Monthly Sales - Bar Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(axis='y')
plt.show()
