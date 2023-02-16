import tools20230216 as tools

def test_dodaj():
    assert tools.dodaj(2,6)==8

def test_dodaj_bad():
    assert tools.dodaj(2,6)==9

#pip install -U pytest
# -v  info o wartościach wcześniej i aktualnych