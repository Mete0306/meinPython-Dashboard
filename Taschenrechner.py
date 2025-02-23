print ("Gebe die erste Zahl ein ")
zahl1= int(input("Zahl1 :"))
print ("Gebe die zweite Zahl ein ")
zahl2=int(input("Zahl2 :"))
print("Gebe eine Rechenoperation ein: ")
eingabe= input("")
summe=0

try:
    if eingabe=="+" :
        summe=zahl1+zahl2
    elif eingabe=="-":
        summe=zahl1-zahl2
    elif eingabe=="*":
        summe=zahl1*zahl2
    elif eingabe=="/":
        summe= zahl1/zahl2

    else :
        raise ValueError("Ungültige Eingabe!")

    print (f"{zahl1} {eingabe} {zahl2} = {summe}" )

except ValueError as e:
    print(f"Fehler: {e}")
