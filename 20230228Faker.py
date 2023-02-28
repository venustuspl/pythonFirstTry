#Losowe dane testowe do testów

from unittest import mock
import faker

m=mock.Mock()
f=faker.Faker()

m.losowaOsoba=f.name()
m.losowaSentencja=f.sentence()
m.losowaData=f.date()
m.time = f.time()
m.myaddress = f.address()

print(m.losowaOsoba)
print(m.losowaSentencja)
print(m.losowaData)
print(m.time)
print(m.myaddress)
print("again myaddress")
m.myaddress = f.address()
print(m.myaddress)

