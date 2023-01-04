def sayHello(imie):
    print("Hello my friend {}!".format(imie))


def dodaj(x, y):
    print(x + y)

dodaj(3, 5)


def sayHello(imie):
    imie = "Czesław"
    print("Hello my friend {}!".format(imie))


def sprawdz_typ(x):
    if (isinstance(x, int)):  # sposób na sprawdzenie czy parametr jest spodziewanego typu
        print('otrzymalem liczbe calkowita')
    else:
        print('otrzymalem cos innego niz liczba calkowita')


def domyslne_wartosci(a="brak", b="brak"):
    print('a=' + a)
    print('b=' + b)


domyslne_wartosci("X", "Y")

domyslne_wartosci()
domyslne_wartosci("coś")
domyslne_wartosci(b="coś innego")


def oddaj0():
    return 0


print(oddaj0())
x = oddaj0()
print(x)

def dajcyferki():
    l = list(range(10))
    return l


print(dajcyferki())