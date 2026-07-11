import numpy as np

sales_data = np.array([
    [120, 150, 130],  
    [200, 210, 190],  
    [90, 100, 95]     
])

average_price = np.mean(sales_data)

print("Sales Data:\n", sales_data)
print("\nAverage price of all products sold:", round(average_price, 2))
