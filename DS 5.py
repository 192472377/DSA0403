import numpy as np

# Example dataset: each element = fuel efficiency (mpg) of a car model
fuel_efficiency = np.array([25, 30, 28, 35, 40])

# 1. Calculate average fuel efficiency
average_efficiency = np.mean(fuel_efficiency)

# 2. Calculate percentage improvement between two car models
# Let's compare model at index 1 (30 mpg) and model at index 4 (40 mpg)
model1 = fuel_efficiency[1]
model2 = fuel_efficiency[4]

percentage_improvement = ((model2 - model1) / model1) * 100

print("Average fuel efficiency:", average_efficiency)
print("Percentage improvement from model1 to model2:", percentage_improvement, "%")
