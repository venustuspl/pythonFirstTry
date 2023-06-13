class Singleton:
    pole=None
    __instancja=None
    def __new__(cls, *args, **kwargs):
        if cls.__instancja is None:
            cls.__instancja=super().__new__(cls,*args,**kwargs)
        return cls.__instancja



a=Singleton()
b=Singleton()
print(id(a))
print(id(b))
print(a is b)

a.pole='Zawartość pola'
print(b.pole)


#Singleton to wzorzec kreacyjny.
# Zapewnia istnienie co najwyżej jednej instancji danej klasy. Instancja ta musi być dostępna z dowolnego miejsca.
#Obiekt naszej klasy "Singleton" będzie zawierał obiekt klasy "Singleton". Teraz zasada działania kodu wewnątrz
# metody "__new__" jest taka: jeśli nie mam jeszcze zainicjalizowanego obiektu to go tworzymy, a niezależnie czy
# właśnie go stworzyliśmy czy był już wcześniej zwracamy go. To jest mechanizm który pilnuje istnienia tylko
# jednego obiektu klasy Singleton.