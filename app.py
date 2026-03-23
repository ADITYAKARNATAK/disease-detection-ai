from flask import Flask, render_template, request

from predict import predict_disease, predict_from_text
from report_reader import read_report

from db import insert_data, get_history
from logger import log


app = Flask(__name__)


# -------------------------
# home
# -------------------------

@app.route("/")
def home():

    return render_template("index.html")


# -------------------------
# symptoms
# -------------------------

@app.route("/predict", methods=["POST"])
def predict():

    try:

        symptoms = request.form.get("symptoms", "")

        data = predict_disease(symptoms)

        result = data["disease"]
        score = data["score"]
        top3 = data["top3"]

        insert_data(symptoms, "", result)

        return render_template(
            "index.html",
            result=result,
            score=score,
            top3=top3
        )

    except Exception as e:

        log(str(e))

        return render_template(
            "index.html",
            result="Error",
            score=0
        )


# -------------------------
# text
# -------------------------

@app.route("/predict_text", methods=["POST"])
def predict_text():

    try:

        text = request.form.get("report_text", "")

        data = predict_from_text(text)

        result = data["disease"]
        score = data["score"]
        top3 = data["top3"]

        insert_data("", text, result)

        return render_template(
            "index.html",
            result=result,
            score=score,
            top3=top3
        )

    except Exception as e:

        log(str(e))

        return render_template(
            "index.html",
            result="Error",
            score=0
        )


# -------------------------
# upload
# -------------------------

@app.route("/upload", methods=["POST"])
def upload():

    try:

        file = request.files["file"]

        text = read_report(file)

        data = predict_from_text(text)

        result = data["disease"]
        score = data["score"]
        top3 = data["top3"]

        insert_data("", text, result)

        return render_template(
            "index.html",
            result=result,
            score=score,
            top3=top3
        )

    except Exception as e:

        log(str(e))

        return render_template(
            "index.html",
            result="Error",
            score=0
        )


# -------------------------
# history
# -------------------------

@app.route("/history")
def history():

    data = get_history()

    return render_template(
        "history.html",
        data=data
    )


# -------------------------

import os

if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    app.run(host="0.0.0.0", port=port)