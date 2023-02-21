matrix = [5, 4, 5, 7, 6, 3, 4 ]

def wyliczMaxPlusDifference(table):
    result = -1
    start = 0;
    for i in table:
        print('i{}'.format(table[i-1]))
        for j in range(start, len(table)):
            value = table[j-1] - table[start]
            if value > 0 and value > result:
                result = value
                print(result)
        start = start + 1

    print('maxPlusDifference: {}'.format(result))

wyliczMaxPlusDifference(matrix)