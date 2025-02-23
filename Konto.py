
class Konto:

    def __init__(self,kontonummer,kontostand):

        self.kontonummer=kontonummer
        self.kontostand=kontostand


    def einzahlen(self,betrag):
        self.kontostand+=betrag

    def abheben(self,betrag):
        self.kontostand-=betrag

    def anzeigen(self):
        print(f" Konto: {self.kontonummer} Kontostand:  {self.kontostand}")