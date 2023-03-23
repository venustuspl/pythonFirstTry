class Samochod:
    def jedz(self):
        print("pyr pyr")

class SuperSamochod(Samochod):
    def jedz(self):
        print("WROOOOOOOOM!!!!")

s=Samochod()
ss=SuperSamochod()
ss.jedz()


class OtherSamochod(Samochod):
    def jedz(self):
        print("WROOOOOOOOM!!!!")
        super().jedz()

os = OtherSamochod();
os.jedz()