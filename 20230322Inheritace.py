class Pojazd:
    def jedz(self):
        print("wroom!")
    def name(self):
        print("Pojazd")

class Armata:
    def strzelaj(self):
        print("jeb, jeb, jeb!")
    def name(self):
        print("Armata")

class Czolg(Armata, Pojazd):
    pass


c=Czolg()
c.jedz()
c.strzelaj()
c.name() # zwraca metodę z klasy wymienionej jako pierwsza w dziedziczeniu
