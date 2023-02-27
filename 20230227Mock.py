#Makiety służą zastępowaniu prawdziwych danych na czas testów.
from unittest import mock
makieta=mock.Mock()
makieta.pole1=20
makieta.pole2='Element tekstowy'
print('pole1={}, pole2={}'.format(makieta.pole1,makieta.pole2))

#dynamiczne wstawienie wartości do mocka
makieta.dajPi.return_value=3.14
print( makieta.dajPi())
