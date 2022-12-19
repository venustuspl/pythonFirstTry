lista4= ['nie', 'toperz', 123, 'aa', 'bb', [1, 2, 3, 'Baba Jaga patrzy!']]
print(lista4[1:-1])
print(lista4[1:len(lista4)-1])
for i in lista4:
    print(i)
for i in range(len(lista4)):
    print(i)
if ('nie1' in lista4):
    print('tak')
else:
    print('nie')
lista4.append(8)
print(lista4)
lista4.insert(0,"X")
print(lista4)
lista4[1]="Y" #podmiana elementu o danym indexie
print(lista4)

lista=[1,0,2,0,3,0,4,0,5,0,6,0,7,0,3]
del lista[2] #element o danym indeksie
print(lista)
lista.remove(3) #pierwszą znalezioną trójkę
print(lista)
del lista[0:4]
print(lista)

pdk=["Ogórek","Pomidor","Ziemniak","1"]
pdk.sort()
#pdk.reverse()
print(pdk)

from operator import itemgetter #posortowanie po danym elemencie
furki=[[3,"Renault"],[2,"Citroen"],[1,"Audi"],[4,"Zaporożec"]]
furki.sort(key=itemgetter(1))
print(furki)

# "kopia=lista"? Takie przypisanie odbywa się przez wskaźnik a nie przez kopię i

lista=[1,3,5,8,13,21,34,55,1,1,1,"Batman"]
podlista=lista[2:7]
print(podlista)
kopia=lista.copy()
print(kopia)


fib=[1,3,5,8,13,21,34,55]
print( sum(fib) , max(fib), min(fib) )
print( sum(fib) , max(fib), min(fib) )

fib=[1,3,5,8,13,21,34,55]
print(     fib.index(13)    )

#Dotychczas funkcja "print" przyjmowała tylko jeden argument, a tu nagle trzy (?)... Nadal przyjmuje jeden argument, z tym że argumentem tym jest krotka :) Jest to specjalny złożony typ danych, którym zajmiemy się w kolejnym podrozdziale.