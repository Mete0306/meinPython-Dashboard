import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class DataDashboard:
    def __init__(self):
        self.df = None

    def loadData(self, file):
        if file.name.endswith(".csv"):
            self.df = pd.read_csv(file, sep=";")
        else:
            self.df = pd.read_excel(file)

    def filterByName(self, letter):
        if letter:
            self.df = self.df[self.df["Name"].str.lower().str.startswith(letter.lower())]

    def filterByAge(self, minAge, maxAge):
        self.df = self.df[(self.df["Alter"] >= minAge) & (self.df["Alter"] <= maxAge)]

    def filterBySalary(self, minSalary, maxSalary):
        self.df["Gehalt"] = self.df["Gehalt"].astype(str).str.replace(",", "").astype(float)
        self.df = self.df[(self.df["Gehalt"] >= minSalary) & (self.df["Gehalt"] <= maxSalary)]


dashboard = DataDashboard()
st.title("📊 Data Insights Dashboard")

dateiUser = st.file_uploader("Lade eine CSV-Datei hoch", type=["csv", "xlsx"])

if dateiUser is not None:
    dashboard.loadData(dateiUser)
    df = dashboard.df

    st.subheader("🔍 Name-Filter")
    buchstabe = st.text_input("Gib einen Anfangsbuchstaben ein:", "").strip()
    dashboard.filterByName(buchstabe)
    df = dashboard.df

    st.subheader("📌 Vorschau der Daten")
    st.dataframe(df, height=300, use_container_width=True)

    st.subheader("📊 Statistische Werte")
    col1, col2 = st.columns(2)

    with col1:
        st.write("**Mittelwerte:**")
        st.table(df.mean(numeric_only=True))

    with col2:
        st.write("**Maximalwerte:**")
        st.table(df.max(numeric_only=True))

    maxSpalte = st.selectbox("Wähle eine Spalte für den maximalen Wert", df.select_dtypes(include=["number"]).columns, key="maxSpalte")
    maxPerson = df[df[maxSpalte] == df[maxSpalte].max()]
    st.write(f"### Person mit höchstem Wert in {maxSpalte}:")
    st.write(maxPerson)

    st.subheader("🗏 Interaktive Filter")
    minAge, maxAge = st.slider("Alter filtern", int(df["Alter"].min()), int(df["Alter"].max()), (25, 35))
    dashboard.filterByAge(minAge, maxAge)

    if "Gehalt" in df.columns:
        df["Gehalt"] = df["Gehalt"].astype(str).str.replace(",", "").astype(float)
        minSalary, maxSalary = int(df["Gehalt"].min()), int(df["Gehalt"].max())
        minSelected, maxSelected = st.slider("Gehalt filtern", minSalary, maxSalary, (minSalary, maxSalary))
        dashboard.filterBySalary(minSelected, maxSelected)

    st.write("### Gefilterte Daten:")
    st.write(dashboard.df)

    st.subheader("📈 Datenvisualisierung")
    numerischeSpalten = df.select_dtypes(include=["int64", "float64"]).columns

    if len(numerischeSpalten) > 0:
        spalte = st.selectbox("Wähle eine numerische Spalte", numerischeSpalten, key="visualisierungSpalte")
        diagrammTyp = st.radio("Diagrammart wählen", ["Histogramm", "Kreisdiagramm"], key="diagrammTyp")

        fig, ax = plt.subplots()
        if diagrammTyp == "Histogramm":
            sns.histplot(df[spalte], bins=20, kde=True, ax=ax, color="royalblue")
            plt.xlabel(spalte)
            plt.ylabel("Anzahl")
            plt.title(f"Histogramm von {spalte}")
        elif diagrammTyp == "Kreisdiagramm":
            if spalte == "Alter":
                bins = [18, 25, 35, 45, 55, 65]
                labels = ["18-25", "25-35", "35-45", "45-55", "55-65"]
            else:
                bins = [3000, 4000, 5000, 6000, 7000, 8000]
                labels = ["3k-4k", "4k-5k", "5k-6k", "6k-7k", "7k-8k"]
            df["Kategorie"] = pd.cut(df[spalte], bins=bins, labels=labels, include_lowest=True)
            anteile = df["Kategorie"].value_counts()
            plt.pie(anteile, labels=anteile.index, autopct="%1.1f%%", colors=sns.color_palette("pastel"))
            plt.title(f"Kreisdiagramm von {spalte}")

        st.pyplot(fig)