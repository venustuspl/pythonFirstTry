import xml.etree.ElementTree as et
drzewo=et.parse('dane.xml')
root=drzewo.getroot()
imie=root.find('imie')
print(imie)

#pare pobranie całego pliku lub przeładowanie
#root korzeń xml

print(root.find('adres').find('miasto').text)

zag=root[3][1].text
print(zag)

for e in root.findall('jezyki'): # tylko po elementach "jezyki"
    print(e.text)

print (root.findall('jezyki')[1].text)