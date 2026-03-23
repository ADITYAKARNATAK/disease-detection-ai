import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_DIR = os.path.join(BASE_DIR, "models")

DATASET_PATH = os.path.join(BASE_DIR, "dataset", "Training.csv")

DISEASE_MODEL = os.path.join(MODEL_DIR, "disease_model.pkl")

CANCER_MODEL = os.path.join(MODEL_DIR, "cancer_model.pkl")

DB_PATH = os.path.join(BASE_DIR, "database.db")