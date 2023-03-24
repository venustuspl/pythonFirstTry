class FunkcjePrywatne:
    name='FunkcjeP'
    __author='TKO'
    def funkcjaPubliczna(self):
        print("Cześć, jestem funkcją publiczną!")
        self.__funkcjaPrywatna()
    def __funkcjaPrywatna(self):
        print("Cześć, jestem funkcją PRYWATNĄ!")
        print(self.__author)

fp = FunkcjePrywatne()
fp.funkcjaPubliczna()