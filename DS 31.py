import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Synthetic dataset
data = {
    "Age":[25,40,35,60,50,30,45,55],
    "Gender":[0,1,1,0,1,0,1,0],  # 0=Male, 1=Female
    "BloodPressure":[120,140,130,150,135,125,145,155],
    "Cholesterol":[180,220,200,240,210,190,230,250],
    "Outcome":["Good","Bad","Good","Bad","Good","Good","Bad","Bad"]
}
df = pd.DataFrame(data)

X = df.drop("Outcome", axis=1)
y = df["Outcome"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred, pos_label="Good"))
print("Recall:", recall_score(y_test, y_pred, pos_label="Good"))
print("F1-score:", f1_score(y_test, y_pred, pos_label="Good"))

print("Predictions:", list(zip(y_test, y_pred)))
