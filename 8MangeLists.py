liczby=[]
for x in range(1,5): liczby.append(x)
print(liczby)
parzyste=[i*10 for i in liczby if i%2==0]
print(parzyste)

liczby=[]
for x in range(1,21): liczby.append(x)
print(liczby)

print(  [i for i in range(1,21) if i%2==0]  )

print([i for i in range(1,21) if i%3==0])