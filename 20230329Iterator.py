class IncrementIterator:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n == self.i:
            raise StopIteration
        self.i += 1
        return self.i

for e in IncrementIterator(2):
    print(e)
print('--')
class NieskonczonyIterator:
    x=0
    def __iter__(self):
        return self
    def __next__(self):
        self.x+=1
        return self.x

ni=NieskonczonyIterator()
for i in range(10):
    print(  next(ni)  )
print('--')
print(  next(ni)  )
print(  next(ni)  )