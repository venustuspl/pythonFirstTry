# co jeśli podamy mniej wartości niż parametrów? Python przypisze je do parametrów wg. kolejności, a pozostałe przyjmą wartości domyślne -
# ale tylko jeśli takie wartości zostaną zadeklarowane. Bez tego dostalibyśmy wyjątek.


fun=lambda a,b: a+b
print (fun(10,20))  #wykorzystanie odebranego w ten sposob ciala funkcji.

def razy2(a): # funkcja która będzie użyta jako argument
    return a*2


def funkcja_jako_argument(f,x):
    print(f(x))


funkcja_jako_argument(razy2,33)

def powieksz(x):
    return x.upper()

def zastosuj_dla_wszystkich(fun,*args):
    for a in args:
        print(fun(a))

zastosuj_dla_wszystkich(powieksz,'siała','baba','mak')

#Funkcje mogą być przekazywane również jako listy. Poniższy przykład prezentuje zastosowanie rzędu funkcji na jednej zmiennej.


def pomnoz_razy_dwa(x):
    return x*2

def podziel_przez_trzy(x):
    return x/3

def dodaj_piec(x):
    return x+5

funkcje=[pomnoz_razy_dwa,podziel_przez_trzy,dodaj_piec]

def obrob(wartosc,*funkcs):
    for f in funkcs:
        wartosc=f(wartosc)
    return wartosc

print (obrob(1,pomnoz_razy_dwa,podziel_przez_trzy,dodaj_piec) )

def zewnetrzna(x):
    def wewnetrzna(x):
        return x*2
    print(wewnetrzna(x))

zewnetrzna(50)

def daj_funkcje(x):
    def podwoj(a):
        return a*2
    def polowa(a):
        return a/2
    if x==1:
        return podwoj
    elif x==2:
        return polowa

fun=daj_funkcje(2)
print ( fun(6) )

def silniaRek(n):
    if n==0:
        return 1
    else:
        return n*silniaRek(n-1)
print(silniaRek(3))

#Inny przykład rekurencji. Choć można wypisywanie wartości w wybranym zakresie zorganizować znacznie prościej, to tutaj użyłem do tego celu rekurencji:

def rekurencyjny_wypisywacz(n):
    print(n)
    if n>0:
        rekurencyjny_wypisywacz(n-1)
    else:
        return n
    return n