# app.py
from db import insert_data, get_history
from flask import Flask, render_template, request
import os
from db import insert_data

from predict import predict_disease, predict_from_text
from report_reader import read_report

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# -------------------------
# Home
# -------------------------

@app.route("/")
def home():
    return render_template("index.html")


# -------------------------
# Predict from symptoms
# -------------------------

@app.route("/predict", methods=["POST"])
def predict():

    symptoms = request.form.get("symptoms")

    symptom_list = symptoms.split(",")

    result = predict_disease(symptom_list)

    insert_data(symptoms, "", result)

    return render_template("index.html", result=result)


# -------------------------
# Predict from text
# -------------------------

@app.route("/predict_text", methods=["POST"])
def predict_text():

    text = request.form.get("report_text")

    result = predict_from_text(text)

    insert_data("", text, result)

    return render_template("index.html", result=result)


# -------------------------
# Upload file
# -------------------------

@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["file"]

    if file.filename == "":
        return render_template("index.html", result="No file")

    path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)

    file.save(path)

    text = read_report(path)

    result = predict_from_text(text)
    insert_data("", text, result)

    return render_template("index.html", result=result)


# -------------------------



@app.route("/history")
def history():

    data = get_history()

    return render_template("history.html", data=data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)