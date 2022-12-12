x = 1
while (x <= 10):
    print(x)
    x += 1

for x in range(1, 11):
    print(x)

for x in range(1, 11, 2):
    print(x)

for x in range(10, 0, -1):
    print(x)

for y in range (1,3):
    for x in range(10, 12):
        print('y={}, x={}'. format(y, x))


y, x = 1, 1
while (y <= 3):
    x = 1
    while (x <= 3):
        print('y={}, x={}'.format(y, x))
        x += 1
    y += 1


for x in range(1, 101):
    if (x % 17.5 == 0):
        print("szukana liczba to {}".format(x))
        break


for x in range(-10, 11):
    if (x == 0):
        continue
    print(1 / x)