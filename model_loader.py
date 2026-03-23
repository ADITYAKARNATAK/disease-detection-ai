import joblib
import pandas as pd

import config


# ---------------------
# load dataset
# ---------------------

data = pd.read_csv(config.DATASET_PATH)

if "Unnamed: 133" in data.columns:
    data = data.drop("Unnamed: 133", axis=1)

FEATURES = data.drop("prognosis", axis=1).columns


# ---------------------
# load disease model
# ---------------------

disease_model = joblib.load(config.DISEASE_MODEL)


# ---------------------
# load cancer model (optional)
# ---------------------

try:
    cancer_model = joblib.load(config.CANCER_MODEL)
except:
    cancer_model = None