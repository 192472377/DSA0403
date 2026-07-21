import numpy as np

# Example dataset: columns = [bedrooms, square footage, sale price]
house_data = np.array([
    [3, 1500, 250000],
    [5, 2200, 400000],
    [4, 1800, 300000],
    [6, 3000, 550000],
    [7, 3500, 700000]
])

# Filter houses with more than 4 bedrooms
houses_with_more_than_4_bedrooms = house_data[house_data[:, 0] > 4]

# Compute average sale price (column index 2 = sale price)
average_sale_price = np.mean(houses_with_more_than_4_bedrooms[:, 2])

print("Average sale price of houses with >4 bedrooms:", average_sale_price)
