#map
liczby = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

parzyste=list(map(lambda x:x/2,liczby))
print(parzyste)

parzyste=[i/2 for i in liczby]
print(parzyste)

#filter
liczby1=[i for i in range(1,21)]
parzyste=list(filter(lambda x: x%3==0 ,liczby1))
print(parzyste)
