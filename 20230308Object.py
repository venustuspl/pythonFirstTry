class Osoba:
    imie='Tomek'
    nazwisko=None
    ksywka=None
o1=Osoba()
o1.imie='Jerzy'
o1.nazwisko='Kiler'
o1.ksywka='Killer'
o1.wtf='omg!'

print(o1.imie,o1.nazwisko,o1.ksywka,o1.wtf)
Osoba.imie='zamienione...'
o3=Osoba()
print(o3.imie)