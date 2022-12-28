slownik = {}
slownik2 = dict()

info = {
    "LG123": "Telewizor 60' z HD Ready, wejściem na internety i filtrem reklam",
    "SONY": "Bardzo dobry telewizor",
    "SZAJSUNG": "Telewizor świetnie nadający się do zakrycia dziury w ścianie (i niczego więcej)"
}

print(info["SONY"])

for i in info:
    print(info[i])

for k in info.keys():
    print(info[k])

print(info.keys())

print(info.values())

if "LG" in info:
    print("Mamy taki produkt")
else:
    print("niet :(")

if "Telewizor 60' z HD Ready, wejściem na internety i filtrem reklam" in info.values():
    print("mamy produkt o takim opisie")
else:
    print("taki opis nie pasuje do żadnego produktu")

info["KLUCZ"] = "WARTOŚĆ" #dodawanie na ten sam klucz nadpisuje

del info["LG123"]