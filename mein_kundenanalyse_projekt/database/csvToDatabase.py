import sqlite3
import pandas as pd

dbName= "database/kundenanalyse.db"

def erstelleDatenbank ():
    c=sqlite3.connect(dbName)
    cursor= c.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS kunden "
                   "(KundeID INTEGER PRIMARY KEY , "
                   "Name TEXT ,"
                   "Alter INTEGER, "
                   "Einkommen INTEGER, "
                   "Kaufwarscheinlichkeit REAL) ")

    c.commit()
    c.close()

def insertDatenVonCSV (csvPfad):
    c= sqlite3.connect(dbName)
    datei=  pd.read_csv(csvPfad)
    datei.to_sql("kunden",c,if_exists="replace", index=False)
    c.close()

if __name__ == "__main__":
    erstelleDatenbank()
    insertDatenVonCSV("data/kunden.csv")
    print("Datenbank erstellt und CSV-Daten importiert!")



