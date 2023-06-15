#Wzorzec kreacyjny. Pozwala tworzyć rodziny obiektów dziedziczących po tej samej
# klasie bez określania ich konkretnych klas. Wzorzec ten powinniśmy stosować wtedy
# gdy zawsze chcemy użyć tego samego zestawu metod na dowolnym wybranym obiekcie z danej
# rodziny (klas mających wspólną klasę bazową po której dziedziczą).
from abc import ABC,abstractmethod
class Samochod(ABC):
     @abstractmethod
     def jedz(self):
         pass

class SportowySamochod(Samochod):
     def jedz(self):
         print('sportowy wydech robi wroom!')

class Limuzyna(Samochod):
     def jedz(self):
         print('nawet nie usłyszysz dzwięku silnika...')

class SamochodMiejski(Samochod):
     def jedz(self):
         print('no niby jedzie...')

class FabrykaSamochodow(ABC):
     @abstractmethod
     def produkuj_samochod(self):
         pass

class FabrykaSportowych(FabrykaSamochodow):
     def produkuj_samochod(self):
         return SportowySamochod()

class FabrykaLimuzyn(FabrykaSamochodow):
     def produkuj_samochod(self):
         return Limuzyna()

class FabrykaMiejskich(FabrykaSamochodow):
     def produkuj_samochod(self):
         return SamochodMiejski()

rodzaj='limuzyna'
if rodzaj=='sportowy':
     fabryka=FabrykaSportowych()
elif rodzaj=='limuzyna':
     fabryka=FabrykaLimuzyn()
elif rodzaj=='miejski':
     fabryka=FabrykaMiejskich()
else:
     raise NotImplementedError(f"nie ma fabryki dla typu {rodzaj}");

samochod=fabryka.produkuj_samochod();
samochod.jedz()
samochod2=fabryka.produkuj_samochod();
samochod2.jedz()