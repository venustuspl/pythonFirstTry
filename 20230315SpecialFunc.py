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