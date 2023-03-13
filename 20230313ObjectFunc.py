class Polska:
    def roszczenie(self):
        return "Mienie bezspadkowe"

p=Polska()
print(p.roszczenie())

class Programista:
    jezyk="Python"
    def funkcja(self):
        print('programuję w języku '+self.jezyk)

p=Programista()
p.funkcja()

class Owoc:
    pass

jablko=Owoc()
pomarancza=Owoc()
print(jablko)
print(pomarancza)

if(jablko==pomarancza):
    print('to samo')
else:
    print('inne')

#Jeśli porównuje się dwa obiekty w taki sposób, w rzeczywistości sprawdzasz czy chodzi o ten sam obiekt -
# w skrócie czy oba obiekty odnoszą się do  tego samego adresu w pamięci operacyjnej. Oczywiście tak nie jest, dlatego kod zwraca nam informację że obiekty są różne