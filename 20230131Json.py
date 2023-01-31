import json
plik=open('dane.json',encoding='utf-8')
obj=json.load(plik)
print(obj)
print(  obj['adres']['miasto']  )

for j in obj['jezyki']:
    print(j)
print(type(obj))
plik.close()