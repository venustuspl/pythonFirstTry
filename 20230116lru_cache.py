#Do używania cache służy moduł "functools" i zawarty   w nim dekorator "lru_cache".
# Przeanalizujmy teraz ten przykład po pewnych zmianach. Nad funkcją czekacz wpisałem dekorator "@functools.lru_cache".
# Dekorator ten sprawia że wynik działania naszej funkcji czekacz ląduje w cache i jest pobierana przy kolejnych wywołaniach
# tej funkcji dla tych samych argumentów (w naszym przypadku brak argumentu - funkcja zawsze zwraca 1):

from datetime import datetime
import time
import functools

@functools.lru_cache(maxsize=None)
def czekacz():
    time.sleep(1)
    return 1

poczatek=datetime.now()
for x in range(10):
    czekacz()
koniec=datetime.now()
print(koniec-poczatek)

#kolejne wywołania tej funkcji odczytywały wartość z cache nie wykonując tej funkcji
# Argument tego dekoratora (maxsize=None) określa dla ilu wartości wejściowych funkcja ma przechowywać dane w cache.
#Cache można stosować tylko do funkcji deterministycznych - czyli w skrócie takich które dla tych samych parametrów
# wejściowych zwrócą nam zawsze te same dane wyjściowe.