from abc import ABC,abstractmethod
class MatheHelfer:

    @staticmethod
    def addiere(a,b):
        return a+b


class Form(ABC):
    @abstractmethod
    def berechneFläche(self):
        pass


class Rechteck(Form):

    def __init__(self,breite,höhe):
        self._breite=breite
        self.__höhe=höhe

    def berechneFläche(self):
        fläche= self.höhe*self.breite
        return fläche

    def gethöhe(self):
        return self.__höhe

    def __str__(self):
        return "deine MUm"

class main:

    print(MatheHelfer.addiere(1,3))
    rechteck= Rechteck(2,4)

    print(rechteck)
  #  print(rechteck.berechneFläche())

alter= {1:"Mete",2:"Hans"}

alter2={}
alter2.get("Lara",2)

students= ["Max" , "Monika"]
print(",".join(students))

s="Hans deine Mum"
liste= s.split(" ")

print(" " .join(liste))


