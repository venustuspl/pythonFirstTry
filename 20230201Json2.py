import json
dane={
    "ksiazka": "Finansowy Ninja",
    "film_na_wieczor": "https://www.youtube.com/watch?v=sCNrK-n68CM",
    "banknoty": [10,20,50,100,200,500],
    "liczba":22
}
plik=open('jsonout2.json',encoding='utf-8',mode="w")
json.dump(dane,plik)

plik.close()

