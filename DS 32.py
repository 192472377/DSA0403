import pandas as pd
from sklearn.linear_model import LinearRegression

# Synthetic dataset
data = {
    "Area":[1000,1500,2000,2500,3000],
    "Bedrooms":[2,3,3,4,4],
    "Price":[100000,150000,200000,250000,300000]
}
df = pd.DataFrame(data)

X = df[["Area","Bedrooms"]]
y = df["Price"]

model = LinearRegression()
model.fit(X, y)

# User input
new_house = pd.DataFrame([[2200,3]], columns=["Area","Bedrooms"])
pred_price = model.predict(new_house)[0]

print("Predicted Price:", pred_price)
