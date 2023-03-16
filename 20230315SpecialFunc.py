# __init__ używana po stworzeniu obiektu
# __str__ toString
class Samochod:
    marka=None
    model=None
    def __init__(self,marka,model):
        self.marka=marka
        self.model=model
    def __str__(self):
        return "marka={} model={}".format(self.marka,self.model)


s = Samochod("Renault","Megane")
print(s.marka,s.model)
print(s)

#__add__ dodanie 2 obiektów
class Samochod:
    marka=None
    model=None
    def __add__(self, other):
        return "Kraksa 2 Sebastianów w dresie. Jeden jechał {}, drugi {}".format(self,other)
    def __init__(self,marka,model):
        self.marka=marka
        self.model=model
    def __str__(self):
        return "marka={} model={}".format(self.marka,self.model)

s=Samochod("Audi","A4")
print(s)
s2=Samochod("Bmw","e46")
s3=s+s2
print(s3)

#__getitem__ i __setitem__
class MyDictionary:
    dict=dict()
    def __setitem__(self, key, value):
        self.dict[key]=value
    def __getitem__(self, key):
        return self.dict[key]

md = MyDictionary()
md['klucz']='wartość'
md['klucz1']='wartość1'
md['klucz2']='wartość2'
print(md['klucz'])
print(md['klucz1'])
print(md['klucz2'])