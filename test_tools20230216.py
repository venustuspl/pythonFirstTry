import pytest

import tools20230216 as n
def test_sumuj():
    assert n.sumuj(5,3)==8

@pytest.mark.podstawowe
def test_sumuj():
    assert n.sumuj(5,3)==8

@pytest.mark.szczegolowe
def test_dajCyfryMin():
    tab=n.dajCyfry()
    assert min(tab)==1

@pytest.mark.szczegolowe
def test_dajCyfryMax():
    tab=n.dajCyfry()
    assert max(tab)==10

@pytest.mark.len
def test_dajCyfryLen():
    tab=n.dajCyfry()
    assert len(tab)==10

#pip install -U pytest
# -v  info o wartościach wcześniej i aktualnych, lub nazwy wykonanych testów
# -k uruchamianie testów z ciągiem znaków w nazwie
# -m wywołanie testów z tagiem

