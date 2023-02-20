def podepnijBaze(nazwa):
    global podpietaBaza
    podpietaBaza=nazwa

def wykonajZapytanie():
    global podpietaBaza
    print('Wykonuję zapytanie z użyciem bazy {}'.format(podpietaBaza))
    if(podpietaBaza=='MS SQL'):
        raise Exception('FUUUUUUU')
    return "success"