#Wyrażenia z dwoma gwiazdkami (**) stosujemy gdy do funkcji chcemy przekazać zestaw argumentów klucz wartość.
# W przeciwieństwie do *args argumentom przypiszemy nazwy, a nazwy te staną się kluczem dla wartości.
# Po argumentach przekazanych w ten sposób poruszamy się jak po słowniku:


def parametr_kwargs( **kwargs):
    for k in kwargs:
        print(k,kwargs[k])

parametr_kwargs(dodatkowy=48, nastepny=111)

#Jeśli zechcielibyśmy do funkcji przekazać jakieś dodatkowe poza **kwargs parametry to musimy wymienić je jako pierwsze:

def zapisz_parametry_do_pliku(nazwa_pliku,**parametry):
    plik=open(nazwa_pliku,mode='w', encoding='utf-8')
    for p in parametry:
        plik.write(f'{p};{parametry[p]}\n')
        print(p, parametry[p])
    plik.close()

zapisz_parametry_do_pliku('mojplik.csv',parametr1='var1',parametr2=2, parametr=3)

