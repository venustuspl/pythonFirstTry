def dekorator(fun):
    def wewnetrzna(*args, **kwargs):
        print('dekorator!')
        fun(*args, **kwargs)

    return wewnetrzna


@dekorator
def dekorowana1():
    print('dekorowana 1')


@dekorator
def dekorowana2(argument):
    print(f'dekorowana 2. argument={argument}')


dekorowana1()
dekorowana2('test')


def dekorator(fun):
    def wewnetrzna(*args, **kwargs):
        print('dekorator!')
        return fun()

    return wewnetrzna


@dekorator
def oddaj():
    return "wartość"

print(oddaj())


def powtorz(x):
    def dekorator(fun):
        def wewnetrzna(*args, **kwargs):
            for i in range(x):
                fun(*args, **kwargs)

        return wewnetrzna

    return dekorator


def funkcja():
    xx = 10
    print(xx, 'cześć, jestem funkcją!')


f = powtorz(5)(funkcja)
f()