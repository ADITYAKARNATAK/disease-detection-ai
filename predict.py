# predict.py

import joblib
import pandas as pd
from report_reader import find_symptoms


# -------------------------
# Load model
# -------------------------

model = joblib.load("model.pkl")


# -------------------------
# Load dataset columns
# -------------------------

data = pd.read_csv("dataset/Training.csv")

if "Unnamed: 133" in data.columns:
    data = data.drop("Unnamed: 133", axis=1)

symptoms = list(data.drop("prognosis", axis=1).columns)


# -------------------------
# Predict from symptoms list
# -------------------------

def predict_disease(symptom_list):

    input_data = [0] * len(symptoms)

    for s in symptom_list:

        s = s.lower().strip()

        if s in symptoms:
            index = symptoms.index(s)
            input_data[index] = 1

    prediction = model.predict([input_data])

    return prediction[0]


# -------------------------
# Predict from text
# -------------------------

def predict_from_text(text):

    found = find_symptoms(text, symptoms)

    if len(found) == 0:
        return "No symptoms detected"

    return predict_disease(found)


# -------------------------
# Test
# -------------------------

if __name__ == "__main__":

    text = "patient has itching and skin_rash"

    print(predict_from_text(text))