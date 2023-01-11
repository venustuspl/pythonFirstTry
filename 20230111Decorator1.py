def obrob(fun,a,b):
    print ( fun(a,b) )

def dodaj(a,b):
     return a+b

def odejmij(a,b):
    return a-b

obrob(dodaj,10,5)
obrob(odejmij,10,5)

def zewnetrzna():
     def wewnetrzna(a,b):
         return a*b
     x=wewnetrzna(4,5)
     return x

print(zewnetrzna())

def zewnetrzna():
     def wewnetrzna(a,b):
         return a*b
     return wewnetrzna

x=zewnetrzna()
print( x(19,13) )

def doopakowania():
     print('do opakowania')

def dekorator(fun):
     def opakowujaca():
         print('opakowująca')
         fun()
     return opakowujaca

dek=dekorator(doopakowania)
dek()

#funkcja "dekorator" zwraca referencję do obiektu funkcji a nie jej wywołanie - stąd brak nawiasów przy
# "return opakowujaca". W powyższym przypadku funkcja "opakowujaca" dodaje dodatkowe zadanie wydruku
# informacji na konsoli. Ten sam efekt możemy osiągnąć również w ten sposób:

print("#####################")
def dekorator(fun):
     def wewnetrzna():
         print('działania funkcji wykorzystującej dekorator')
         fun(2)
     return wewnetrzna

@dekorator
def funkcja(a):
     print(a)
     print('jestem funkcją dekorującą użytą jako argument')

funkcja()