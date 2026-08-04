import pandas as pd

# Example DataFrame (replace with your actual property_data)
property_data = pd.DataFrame({
    "property_id": [1, 2, 3, 4],
    "location": ["CityA", "CityB", "CityA", "CityC"],
    "bedrooms": [3, 5, 2, 6],
    "area_sqft": [1200, 2500, 900, 3000],
    "listing_price": [200000, 350000, 150000, 500000]
})

# 1. Average listing price per location
average_price = property_data.groupby("location")["listing_price"].mean()

# 2. Number of properties with more than 4 bedrooms
count_large_bedrooms = property_data[property_data["bedrooms"] > 4].shape[0]

# 3. Property with the largest area
largest_area_property = property_data.loc[property_data["area_sqft"].idxmax()]

print("Average Price per Location:\n", average_price)
print("\nNumber of properties with >4 bedrooms:", count_large_bedrooms)
print("\nProperty with largest area:\n", largest_area_property)
