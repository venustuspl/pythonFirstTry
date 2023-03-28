class HeightOutOfRangeException(Exception):
    def __init__(self,w):
        super().__init__(f'Wzrost poza zakresem. Podany wzrost: {w}')

class WeightOutOfRangeException(Exception):
    def __init__(self, m):
        super().__init__(f'Waga poza zakresem. Podana waga: {m}')

def bmi(m,w):
    if w<1 or w>2.5:
        raise HeightOutOfRangeException(w)
    if m<1 or m > 200:
        raise WeightOutOfRangeException(m)
    return round(m/pow(w,2),2)

print( bmi(0,1.8) )