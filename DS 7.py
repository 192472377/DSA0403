import pandas as pd

# Sample dataset
order_data = pd.DataFrame({
    'customer_id': [101, 102, 101, 103, 102, 104],
    'order_date': pd.to_datetime([
        '2026-07-01', '2026-07-02', '2026-07-05',
        '2026-07-03', '2026-07-06', '2026-07-04'
    ]),
    'product_name': ['Laptop', 'Mouse', 'Keyboard', 'Laptop', 'Mouse', 'Monitor'],
    'order_quantity': [1, 2, 1, 1, 3, 2]
})

# 1. Total number of orders made by each customer
total_orders_per_customer = order_data.groupby('customer_id').size()

# 2. Average order quantity for each product
avg_quantity_per_product = order_data.groupby('product_name')['order_quantity'].mean()

# 3. Earliest and latest order dates
earliest_order_date = order_data['order_date'].min()
latest_order_date = order_data['order_date'].max()

print("Total Orders per Customer:\n", total_orders_per_customer)
print("\nAverage Quantity per Product:\n", avg_quantity_per_product)
print("\nEarliest Order Date:", earliest_order_date)
print("Latest Order Date:", latest_order_date)
