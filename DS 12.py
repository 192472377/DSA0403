import matplotlib.pyplot as plt

days = list(range(1, 31))  # Days in a month
sales = [50, 60, 55, 70, 65, 80, 75, 90, 85, 100,
         95, 110, 105, 120, 115, 130, 125, 140, 135, 150,
         145, 160, 155, 170, 165, 180, 175, 190, 185, 200]

plt.plot(days, sales, marker='o')
plt.title("Sales Over a Month (Line Plot)")
plt.xlabel("Day")
plt.ylabel("Sales")
plt.show()
