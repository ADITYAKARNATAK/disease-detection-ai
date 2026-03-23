import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier


# Load data

data = pd.read_csv("dataset/Training.csv")

if "Unnamed: 133" in data.columns:
    data = data.drop("Unnamed: 133", axis=1)


X = data.drop("prognosis", axis=1)
y = data["prognosis"]


# Better model

model = RandomForestClassifier(
    n_estimators=200,
    max_depth=None,
    random_state=42,
    n_jobs=-1
)


model.fit(X, y)

print("Model trained")


joblib.dump(model, "model.pkl")

print("Model saved")