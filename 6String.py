
napis = "ministerstwo do spraw niezbyt istotnych spraw"
print(napis.upper())

napis = "MINISTERSTWO DO SPRAW NIEZBYT ISTOTNYCH SPRAW"
print(napis.lower())

napis = "MINISTERSTWO DO SPRAW NIEZBYT ISTOTNYCH SPRAW"
print(napis.title())

napis = "MINISTERSTWO DO SPRAW NIEZBYT ISTOTNYCH SPRAW"
print(napis.replace("I", "X"))
x = len("MINISTERSTWO DO SPRAW NIEZBYT ISTOTNYCH SPRAW")
print(x)

napis = "MINISTERSTWO DO SPRAW NIEZBYT ISTOTNYCH SPRAW"
print(napis.count('IS'))
napis = "           MINISTERSTWO DO SPRAW NIEZBYT ISTOTNYCH SPRAW  "
print(napis.strip())
napis = "MINISTERSTWO DO SPRAW NIEZBYT ISTOTNYCH SPRAW"
print(napis.strip("MINI")) #wycina MINI

napis = "MINISTERSTWO DO SPRAW NIEZBYT ISTOTNYCH SPRAW"
print(napis.split()) #tworzy tablicę


['MINISTERSTWO', 'DO', 'SPRAW', 'NIEZBYT', 'ISTOTNYCH', 'SPRAW']
napis = "MINISTERSTWO;DO;SPRAW;NIEZBYT;ISTOTNYCH;SPRAW"
print(napis.split(";"))

napis = "MINISTERSTWO DO SPRAW NIEZBYT ISTOTNYCH SPRAW"
print(napis.strip("MINI").title().replace('i', 'X'))
nazwa = "Llanfairpwllgwyngyllgogerychwyrndrobwlll­lantysiliogogogoch"
for n in nazwa:
    print(n)

kriszna = "rama " * 5 + " " + 5 * "hare "
print(kriszna)

if ("X" in "SpaceX"):
    print("ten ciąg zawiera X!")

if ("Python" > "Java"):
    print("really?")
else:
    print("maybe maybe")
lancuch = "123456789"
print(lancuch[2])
print(lancuch[-2])
print(lancuch[:5])
print(lancuch[:-3])
print(lancuch[0:6:2]) # od pierwszej do 7 pozycji wycinamy co drugi znak
print(lancuch[0:len(lancuch):2])
print(lancuch[::2])