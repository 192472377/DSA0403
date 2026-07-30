import pandas as pd

# Sample dataset
sales_data = pd.DataFrame({
    'product_name': ['Laptop', 'Mouse', 'Keyboard', 'Laptop', 'Mouse', 'Monitor', 'Mouse', 'Keyboard'],
    'order_quantity': [1, 2, 1, 1, 3, 2, 4, 2]
})

# Total quantity sold per product
product_sales = sales_data.groupby('product_name')['order_quantity'].sum()

# Top 5 products
top_5_products = product_sales.sort_values(ascending=False).head(5)

print("Top 5 Products Sold:\n", top_5_products)
