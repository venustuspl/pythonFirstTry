import matplotlib.pyplot as plt
from random import random
y=[random()*100 for e in range(100)]
z=[random()*5 for e in range(100)]
plt.plot(y,'r--',label='Seria y')
plt.plot(z,'g:',label='Seria z')
plt.grid()
plt.xlabel('oś X')
plt.ylabel('oś Z')
plt.show()

#random()	Returns a random float number between 0 and 1