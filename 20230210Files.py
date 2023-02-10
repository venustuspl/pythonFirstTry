import os
repo = 'c:\\android'
for p in os.walk(repo):
    print(p)

import os
for katalog,podkatalogi, pliki in os.walk("c:\\android"):
    print(f'KATALOG: {katalog}:')
    if(len(podkatalogi)>0):
        print(f'    PODKATALOGI: ')
        for po in podkatalogi:
            print(f'         {po}')
    if(len(pliki)>0):
        print(f'    PLIKI: ')
        for pl in pliki:
            print(f'         {pl}')

if os.path.exists(repo):
    print('jest taki katalog')
    size = os.path.getsize(repo)
    print(f'wielkość pliku={size} bajtów')

else:
    print('nie ma takiego katalogu')


os.mkdir(repo+'\\nowe')
os.remove(repo+'\\nowe')