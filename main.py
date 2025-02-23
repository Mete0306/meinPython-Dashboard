

print("hello world");





max=int(input("Gebe hier die folge ein"));

zahl = 1;
vorherigeZahl =0;
for i in range(1, max):
    if i==1:
        print(0)
        print(1)
        print(1)
        vorherigeZahl=1;



    folge=zahl+vorherigeZahl;
    vorherigeZahl = zahl;
    zahl=folge;


    print(folge)
