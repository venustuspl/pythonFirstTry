pl=open('dane.txt', encoding='utf-8')
linie=pl.read()
pl.seek(0)
linie2=pl.readlines();
pl.close()
print(pl.__sizeof__())
print(linie)
print(linie2)
print(type(linie))

plik=open('nowy1.txt',encoding='utf-8',mode='w')
plik.write(plik.name+'\n')
linie=[]
for x in range(10):
    linie.append("linia numer {} \n".format(x))
plik.writelines(linie) # to nas interesuje
plik.close()