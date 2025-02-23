
class Tier:
    anzahlTiere=0
    def __init__(self,name,laut):

        self.name=name
        self.laut=laut
        Tier.anzahlTiere+=1


    def macheLaut(self):
        print(self.laut)

    @staticmethod
    def anzahl():
        print(f"Anzahl Tiere: {Tier.anzahlTiere}")







class Hund(Tier):

    def __init__(self,name):
        super().__init__(name,laut="Wuff")

    def macheLaut(self):
        print(f"Der {self.name} macht : {self.laut}")