import pandas as pd
import joblib

from logger import log


# -------------------------
# load model
# -------------------------

model = joblib.load("models/disease_model.pkl")


data = pd.read_csv("dataset/Training.csv")

if "Unnamed: 133" in data.columns:
    data = data.drop("Unnamed: 133", axis=1)


FEATURES = list(data.drop("prognosis", axis=1).columns)


# -------------------------
# clean symptoms
# -------------------------

def clean_symptoms(text):

    if not text:
        return []

    text = text.lower()

    text = text.replace(" ", "_")
    text = text.replace("-", "_")

    parts = text.split(",")

    result = []

    for p in parts:

        p = p.strip()

        if p in FEATURES:
            result.append(p)

    return result


# -------------------------
# create vector
# -------------------------

def create_vector(symptoms):

    vector = [0] * len(FEATURES)

    for s in symptoms:

        if s in FEATURES:

            i = FEATURES.index(s)

            vector[i] = 1

    df = pd.DataFrame(
        [vector],
        columns=FEATURES
    )

    return df


# -------------------------
# main prediction
# -------------------------

def predict_disease(symptom_text):

    symptoms = clean_symptoms(symptom_text)

    if len(symptoms) == 0:

        return {
            "disease": "No symptoms found",
            "score": 0,
            "top3": []
        }

    X = create_vector(symptoms)

    probs = model.predict_proba(X)[0]

    classes = model.classes_

    pairs = list(zip(classes, probs))

    pairs.sort(key=lambda x: x[1], reverse=True)

    top3 = pairs[:3]

    disease = top3[0][0]
    score = round(top3[0][1] * 100, 2)

    log(f"SYMPTOMS={symptom_text} RESULT={disease}")

    return {
        "disease": disease,
        "score": score,
        "top3": top3
    }


# -------------------------
# text prediction
# -------------------------

def predict_from_text(text):

    if not text:

        return {
            "disease": "No symptoms",
            "score": 0,
            "top3": []
        }

    text = text.lower()

    text = text.replace(" ", "_")

    found = []

    for f in FEATURES:

        if f in text:
            found.append(f)

    if len(found) == 0:

        return {
            "disease": "No symptoms",
            "score": 0,
            "top3": []
        }

    return predict_disease(",".join(found))