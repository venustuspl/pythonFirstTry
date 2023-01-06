#*args - konwencja argumentowania wielu elementów a nie listy
#The f means Formatted string literals
def dlakazdego(param1,*args):
    print(f'param1={param1}')
    for a in args:
        print(a, end=", ")

dlakazdego('pierwsza wartość','pierwszy arg','drugi arg', 3)