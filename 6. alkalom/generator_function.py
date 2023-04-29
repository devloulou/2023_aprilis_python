"""
Generator függvények

lazy evaluation -t használnak - laza kiértékelés

Mire jó a generator function?

pl. nagy file-ok felolvasása
vagy amennyiben problémát okoz a memória használat a programom során
érdemes megvizsgálni a generator functiont

"""
# ez egy normál függvény
def my_func():
    return 1
    return 2
    return 3


# generator function

def my_gen():
    print("yield előtt ")
    yield ['almafa', 'barack']
    print(" 1. yield után")
    yield 32
    print("2. yield után")
    yield 100

func = my_gen()

# print(next(func))
# print(next(func))
# print(next(func))

for item in func:
    print(item)