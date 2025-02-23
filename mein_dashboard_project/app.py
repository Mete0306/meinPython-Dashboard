from flask import Flask, render_template, request
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

app = Flask(__name__)

# Sicherstellen, dass der Upload-Ordner existiert
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# 📌 Startseite mit Datei-Upload
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Datei speichern
        file = request.files["file"]
        if file:
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)
            return analyze(file.filename)
    return render_template("index.html")


# 📌 Analyse-Seite
@app.route("/analyze/<filename>")
def analyze(filename):
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)

    # CSV-Datei einlesen
    df = pd.read_csv(filepath, sep=";")

    # 📊 Berechnungen mit NumPy
    mean_values = df.mean(numeric_only=True).to_dict()
    max_values = df.max(numeric_only=True).to_dict()

    # 📈 Matplotlib-Plot speichern
    plt.figure(figsize=(6, 4))
    df["Gehalt"].hist(bins=20)
    plt.xlabel("Gehalt")
    plt.ylabel("Anzahl")
    plt.title("Gehaltsverteilung")
    plot_path = os.path.join("static", "plot.png")
    plt.savefig(plot_path)
    plt.close()

    return render_template("upload.html", filename=filename, mean_values=mean_values, max_values=max_values,
                           plot_path=plot_path)


if __name__ == "__main__":
    app.run(debug=True)