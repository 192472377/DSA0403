import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

# Synthetic dataset
data = {
    "Symptom1":[1,0,1,0,1,0],
    "Symptom2":[0,1,1,0,0,1],
    "Symptom3":[1,1,0,0,1,0],
    "Condition":[1,0,1,0,1,0]
}
df = pd.DataFrame(data)

X = df.drop("Condition", axis=1)
y = df["Condition"]

# Train KNN
k = 3
model = KNeighborsClassifier(n_neighbors=k)
model.fit(X, y)

# User input (with column names to match training)
new_patient = pd.DataFrame([[1,0,1]], columns=X.columns)

pred = model.predict(new_patient)[0]
print("Predicted Condition:", "Yes" if pred==1 else "No")
