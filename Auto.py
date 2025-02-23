
class Auto:

    def __init__(self,marke):
        self.marke= marke
        self.geschwindigkeit=0


    def info(self):
        print(f"Das ist ein {self.marke} und ist {self.geschwindigkeit} KmH schnell.")

    def beschleunige(self,kmh):
        self.geschwindigkeit+=kmh

    def bremse(self,wert):
       self.geschwindigkeit-=wert
