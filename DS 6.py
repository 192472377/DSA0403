# Item prices and quantities
prices = [100, 200, 50]       # Example prices
quantities = [2, 1, 4]        # Example quantities

# Discount and tax rates (in %)
discount_rate = 10
tax_rate = 5

# Step 1: Calculate subtotal
subtotal = sum(p * q for p, q in zip(prices, quantities))

# Step 2: Apply discount
discount = subtotal * (discount_rate / 100)
after_discount = subtotal - discount

# Step 3: Apply tax
tax = after_discount * (tax_rate / 100)

# Step 4: Final total cost
total_cost = after_discount + tax

# Output
print("Subtotal:", subtotal)
print("Discount:", discount)
print("After Discount:", after_discount)
print("Tax:", tax)
print("Total Cost:", total_cost)
