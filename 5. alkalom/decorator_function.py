"""
Olyan függvények amelyek meglévő függvényekhez fognak hozzáadni plusz tulajdonságot
anélkül, hogy változtatna a függvények működésén

Mire használjuk a decorator függvényeket?:
logolás
futási idő mérés
debug - hibát keresel
register - ilyet egyáltalán nem fogunk
lassítani akarsz a futáson
caching

"""

def my_func(name):
    print(f"Hello {name}")

def my_func2(func, name):
    func(name)


# my_func2(my_func, "Ricsi")

def start_end_decor(my_func):
    def wrapper():
        print("Start")
        my_func()
        print("Finished")
    return wrapper


@start_end_decor
def my_func():
    print("Hello Ricsi")

# my_func()


@start_end_decor
def countdown():
    num = 10
    while num > 0:
        print(num)
        num -= 1
# countdown()

from time import time, sleep

def timeit(my_func):
    def wrapper(*args, **kwargs):
        ts = time()
        sleep(2)
        result = my_func(*args, **kwargs)
        print((time() - ts)) # seconds - másodperceket
        return result
    return wrapper


@timeit
def add_numbers(a, b):    
    return a + b

sol = add_numbers(10, 20)

# print(sol)
def repeat(*arg):
    def decorator_repeat(my_func):
        def wrapper(*args, **kwargs):
            ts = time()       
            for i in range(0, arg[0]):
                my_func(*args, **kwargs)
            print((time() - ts)) # seconds - másodperceket
        return wrapper
    return decorator_repeat



@repeat(5, 10)
def greet(name):
    print(f"Hello, {name}")


greet(name="Aranka")