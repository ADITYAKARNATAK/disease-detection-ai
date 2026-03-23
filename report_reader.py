# report_reader.py

import PyPDF2
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def read_txt(file_path):

    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def read_pdf(file_path):

    text = ""

    with open(file_path, "rb") as f:

        reader = PyPDF2.PdfReader(f)

        for page in reader.pages:
            text += page.extract_text()

    return text


def read_image(file_path):

    img = Image.open(file_path)

    text = pytesseract.image_to_string(img)

    return text


def find_symptoms(text, symptoms):

    found = []

    text = text.lower()

    for s in symptoms:

        if s in text:
            found.append(s)

    return found


def read_report(file_path):

    ext = file_path.split(".")[-1].lower()

    if ext == "txt":
        return read_txt(file_path)

    elif ext == "pdf":
        return read_pdf(file_path)

    elif ext in ["png", "jpg", "jpeg"]:
        return read_image(file_path)

    else:
        return ""