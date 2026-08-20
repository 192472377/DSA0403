import pandas as pd

# Step 1: Create a sample dataset
data = {
    'customer_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'customer_age': [25, 30, 22, 25, 40, 30, 22, 35, 25, 40],
    'purchase_amount': [100, 200, 150, 120, 300, 250, 180, 220, 130, 310]
}

# Step 2: Convert to DataFrame
sales_data = pd.DataFrame(data)

# Step 3: Find frequency distribution of ages
age_distribution = sales_data['customer_age'].value_counts().sort_index()

# Step 4: Display results
print("Frequency Distribution of Customer Ages:\n")
print(age_distribution)
