import requests
odpowiedz=requests.get("http://jsystems.pl/static/blog/python/dane.json",auth=('user','pass'))
print(odpowiedz.status_code)
dane = odpowiedz.json()
print(dane)
print(dane['nazwisko'])
for j in dane['jezyki']:
    print(j)


odpowiedzWysylka=requests.post("http://jsystems.pl/static/blog/python/dane.json",data=dane,headers={"Content-Type":"application/json"})
print(odpowiedzWysylka.status_code)