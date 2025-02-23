
wort1= "anna"
wort2=""
gleich=True
index=0

liste=[len(wort1)]
for buchstabe in reversed(wort1) :
    zeichen=buchstabe
    wort2+=zeichen

if not wort1==wort2:
    print("Sind nicht gleich")
else :
    print("Sind gleich")


