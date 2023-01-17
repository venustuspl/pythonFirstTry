#Generator jest funkcją która może zostać wstrzymana i wznowiona od miejsca w którym została wstrzymana.
# Generatory cechują się leniwą ewaluacją. Tworzą kolejne elementy dopiero w momencie odwołania się do generatora.
# Pozwala nam to wydajniej wykorzystywać pamięć operacyjną i zwracać z generatora nieskończoną liczbę elementów

def potegi2(n):
    for x in range(1, n + 1):
        yield pow(2, x)

for p in potegi2(3):
    print(p)

def dziesieci():
    i=1
    while True:
       yield i*10
       i+=1

dz=dziesieci()
print( dz.__next__() )
print( dz.__next__() )
print( dz.__next__() )

dz1=dziesieci()
print(next(dz))
print(next(dz))
print(next(dz))

def literki():
    for x in range(97,123):
        yield(chr(x))

for l in literki():
    print(l)


def rozbijacz_csv(np,r):
    plik=open(np,encoding='utf-8')
    while True:
        linia=plik.readline()
        if not linia:
            break
        yield linia.strip().split(r)

rc=rozbijacz_csv('plik.csv',';')
print(next(rc))
print(next(rc))
print( rc.__next__() )