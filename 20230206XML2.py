#Atrybuty
import xml.etree.ElementTree as et
tree=et.parse("dane.xml")
root=tree.getroot()
nazwisko=root.find('nazwisko')
print(nazwisko.attrib['param'])

import xml.etree.ElementTree as et
print(et.parse("dane.xml").getroot().find("nazwisko").attrib['param'])

#zwykły tekst
print(root)

print(et.tostring(root))

#elementy
for e in root:
    print(e.tag, e.attrib, e.text)

#zmiana wartości
root.find('nazwisko').text="Klusiewicz po zmianie"

print("-------------------")
for e in root:
    print(e.tag,e.text)

#dodawanie i modyfikowanie elementu odbywa się za pomocą attrib

root.find('nazwisko').attrib['encoding']="utf-8"
#wstawianie elementu , insert w określone miejsce
print("-------------------")
for e in root:
    print(e.tag,e.text,e.attrib)

nowy = et.SubElement(root, "masa")
nowy.text = 78

print("-------------------")
for e in root:
    print(e.tag, e.text, e.attrib)

for e in root:
    print(e.tag, e.text, e.attrib)

nowy = et.Element("samochod")
nowy.text = "Renault"
root.insert(0, nowy)

print("-------------------")
for e in root:
    print(e.tag, e.text, e.attrib)

for e in root:
    print(e.tag, e.text)
#kasowanie
del root[0]
print("-------------------")
for e in root:
    print(e.tag, e.text)

for e in root:
    print(e.tag, e.text)

naz = root.find('nazwisko')
root.remove(naz)

print("-------------------")
for e in root:
    print(e.tag, e.text)
#zapis do pliku
d = et.parse("dane.xml")
d.write("dane2.xml", encoding="utf-8")