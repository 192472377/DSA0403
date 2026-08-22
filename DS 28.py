import pandas as pd
from sklearn.tree import DecisionTreeRegressor, export_text

# Synthetic dataset
data = {
    "Mileage":[20000,40000,60000,80000,100000],
    "Age":[2,4,6,8,10],
    "Brand":["A","B","A","C","B"],
    "EngineType":["Petrol","Diesel","Petrol","Diesel","Petrol"],
    "Price":[20000,15000,12000,10000,8000]
}
df = pd.DataFrame(data)

# Encode categorical
df_encoded = pd.get_dummies(df.drop("Price", axis=1))
y = df["Price"]

# Train CART
model = DecisionTreeRegressor()
model.fit(df_encoded, y)

# User input
new_car = pd.DataFrame({
    "Mileage":[50000],
    "Age":[5],
    "Brand":["A"],
    "EngineType":["Diesel"]
})
new_car_encoded = pd.get_dummies(new_car)
new_car_encoded = new_car_encoded.reindex(columns=df_encoded.columns, fill_value=0)

pred_price = model.predict(new_car_encoded)[0]
print("Predicted Price:", pred_price)

# Decision path
tree_rules = export_text(model, feature_names=list(df_encoded.columns))
print(tree_rules)
