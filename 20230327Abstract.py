from abc import ABC, abstractmethod

class Figura(ABC):
    nazwa=None
    def pokaz_nazwe(self):
        print(self.nazwa)

    @abstractmethod
    def oblicz_pole(self):
        pass

class Kwadrat(Figura):
    def __init__(self,dlugosc_boku):
        self.nazwa='Kwadrat'
        self.dlugosc_boku=dlugosc_boku

    def oblicz_pole(self):
        return pow(self.dlugosc_boku,2)


kw=Kwadrat(5)
print(kw.nazwa)
print(kw.oblicz_pole())


class Prostokat(Figura):
    def __init__(self,bok_a,bok_b):
        self.nazwa='Prostokąt'
        self.bok_a=bok_a
        self.bok_b=bok_b

    def oblicz_pole(self):
        return self.bok_a*self.bok_b

pr=Prostokat(4,5)
print(pr.nazwa)
print(pr.oblicz_pole())

class Trojkąt(Figura):
    def __init__(self, bok_a, wysokosc_h):
        self.nazwa='Trojkat'
        self.bok_a = bok_a
        self.wysokosc_h = wysokosc_h

    def oblicz_pole(self):
        return (self.bok_a * self.wysokosc_h)/2

t=Trojkąt(2,5)
print(t.nazwa)
print(t.oblicz_pole())