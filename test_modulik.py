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