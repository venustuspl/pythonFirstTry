import modulik
import pytest

dbs = ["Oracle", 'PostgreSQL', 'MS SQL', 'MySQL', 'MongoDB']

@pytest.mark.parametrize('baza',dbs)
def test_podepnijBaze(baza):
    modulik.podepnijBaze(baza)
    print('{}\n'.format(baza))
    assert modulik.wykonajZapytanie()=='success'


#What is pytest Mark parametrize do?
#@pytest. mark. parametrize allows one to define multiple sets of arguments and fixtures
#at the test function or class. pytest_generate_tests allows one to define custom parametrization schemes or extensions.

#Pytest fixtures are functions that can be used to manage our apps states and dependencies. Most importantly,
# they can provide data for testing and a wide range of value types when explicitly called by our testing software.
# You can use the mock data that fixtures create across multiple tests

#"(scope="module") - uruchamianie funkcji jednorazowo
# "autouse": - dodanie funkcji w każdym teście
#Fikstura to funkcja która przygotowuje dane, lub wykonuje czynności inicjalizacyjne na potrzeby testów.
#a global variable in Python means having a scope throughout the program, i.e., a global variable value is accessible
# throughout the program unless shadowed. A global variable in Python is often declared as the top of the program.

baza=[]

def loadDB():
    print("############## ŁADOWANIE BAZY ##############")
    global baza
    baza=[
        (1,"Marian"),
        (2,"Czesław"),
        (3,"Zenon"),
        (4,"Florian")
    ]

def getData():
    global baza
    return baza

def getOne(x):
    global baza
    return baza[x]

@pytest.fixture(autouse=True,scope="module")
def load_stuff():
    print("\n############## load ##############")
    loadDB()

def test_getData():
    assert len( getData()  )>0
    pass

def test_getOne():
    assert getOne(0)[1]=='Marian'
    pass
