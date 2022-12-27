# krotka = ();listy tylko do odczytu, bez sortowania i dopisowania,pobierania i iteracja taka jak na listahc
madness=("Longer","jeśli","to","czytasz i nie jesteś","lamus","to","podrzuć","jakiegoś","dobrego","mema")
print(madness[2:7])
print(madness[0:5:2])
if "Longer" in madness:
    print("Wygrałem! :D")
for m in madness:
    print(m)