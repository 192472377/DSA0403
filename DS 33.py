import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Synthetic dataset
data = {
    "Size":[1000,1500,2000,2500,3000],
    "Price":[100000,150000,200000,250000,300000]
}
df = pd.DataFrame(data)

X = df[["Size"]]
y = df["Price"]

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)

print("MSE:", mean_squared_error(y, y_pred))
print("R2 Score:", r2_score(y, y_pred))

# Predict new house
new_house = pd.DataFrame([[2200]], columns=["Size"])
print("Predicted Price:", model.predict(new_house)[0])
