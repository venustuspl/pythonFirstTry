import matplotlib.pyplot as plt
from random import random
x=list(range(12))
y=[random()*10000 for e in range(12)]
z=[random()*10000 for e in range(12)]
plt.bar(x,y)
plt.plot(z,'g')
wykres=plt.bar(x,y)
for i in range(len(wykres)):
    if (i % 2 == 0):
        wykres[i].set_color('r')
    else:
        wykres[i].set_color("b")
plt.show()