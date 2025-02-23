import random



beenden=True
randomNumber= random.randint(1, 100)

while beenden:

    eingabeUser= int(input("Gebe eine Zahl zwischen 1 und 100 ein: "));

    if eingabeUser==randomNumber:
        print("Zahl gefunden Glückwunsch!")
        break

    elif eingabeUser > randomNumber:
        print("Zahl stimmt nicht. Leider zu Hoch !")

    else:
        print("Zahl stimmt nicht. Leider zu Niedrig!")
