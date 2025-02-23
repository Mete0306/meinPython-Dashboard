import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


st.title("Data Insights Dashboard")


dateiUser = st.file_uploader("Lade eine CSV-Datei hoch", type=["csv"])

if dateiUser is not None:
    df = pd.read_csv(dateiUser, sep=";")


    st.subheader("Vorschau der Daten")
    st.write(df.head())


    mean_values = df.mean(numeric_only=True)
    max_values = df.max(numeric_only=True)


    st.subheader("Statistische Werte")
    st.write("**Mittelwerte:**")
    st.write(mean_values)

    st.write("**Maximalwerte:**")
    st.write(max_values)


    st.subheader("Datenvisualisierung")



    spalte = st.selectbox("Wähle eine Spalte", df.columns)


    diagrammTyp = st.radio("Diagrammart wählen", ["Balkendiagramm", "Kreisdiagramm"])


    fig, ax = plt.subplots()

    if diagrammTyp == "Balkendiagramm":
        df[spalte].value_counts().plot(kind="bar", ax=ax)
        ax.set_ylabel("Anzahl")
        ax.set_title(f"Balkendiagramm von {spalte}")

    elif diagrammTyp == "Kreisdiagramm":
        df[spalte].value_counts().plot(kind="pie", autopct="%1.1f%%", ax=ax)
        ax.set_ylabel("")
        ax.set_title(f"Kreisdiagramm von {spalte}")


    st.pyplot(fig)