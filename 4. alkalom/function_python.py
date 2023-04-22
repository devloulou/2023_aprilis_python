"""
Függvények, metódusok, function-ök

def func_name(opcionális_paraméterlista):
    a függvény belseje: különböző utasításokat
    [return value] -> ez is opcionális, de mindig van

Minden függvénynek van visszatérési értéke, függetlenül attól
hogy én rendekezek e róla, vagy sem

Ha nem rendelkezem, akkor mindig None a vissza térési érték

a függvény is egy objektum

"""
# paraméter nélküli függvény
def my_func():
    print("Hello világ")
    return 10

# példányosítani kell, meg kell hívni
# a () -jel jelzem azt, hogy meghívom a függvényemet -> példányosodik a függvényem
solution = my_func

# print(solution)

# ami összead 2 bármilyen számot
a = 10
a = 20

def osszead(num1, num2):
    sol = num1 + num2
    return sol

solution = osszead(5, 10)

# paramtéreneknek nincs típusa, nem lehet kikényszeríteni, hogy adott típussal rendelkezzen a 
# paraméter
# nincs megkötve, hogy 1 függvénynek hány paramétere lehet
def osszead(num1, num2):
    return num1 + num2

solution = osszead("Ricsi ", "Kovács")

# print(solution)
# print("Szia Ricsi vagyok")

# def print(param1):
#     return param1 * 100

# print(print(100))


# a paramétereknek lehet kezdő értéke
a = 10
b = 20
c = 30

# a kezdőértéke nélküli paramétereket kötelezően értéket kell kapjanak 
# a függvény hívása során
def my_func(a, b):
    a = 4
    b = 10
    c = 50
    return a + b

solution = my_func(1, 2)

# print(solution)


def my_func(a=10, b=13):
    return a + b

solution = my_func()

# print(solution)

def osszead(num1, num2):
    return num1 + num2

# pozíció alapú paraméter átadás
solution = osszead(10, 20)
# print(solution)

# nevesített paraméter átadást
solution = osszead(num1=10, num2=20)
# print(solution)


solution = osszead(num2=10, num1=20)
# print(solution)

############################################################################################

def my_func(param1):
    return param1

def my_func(param1, param2):
    return param1 + param2

def my_func(num1, num2, num3):
    return num1 * num2 - num3

# my_func(10)
# my_func(10, 20)
# my_func(10, 20, 30)
# function overloading - polimorph függvények - többalakúság

my_list = [1, 2]
my_tuple = (2, 3, 4)
my_str = "almafa"

# print(len(my_list))
# print(len(my_tuple))
# print(len(my_str))

#packing és unpacking a függvényeknél
# *args, **kwargs
# az *args pozíció alapon kapott paramétereket egy tuple-be becsomagolja
def my_func(*args):
    args = list(args)

    # print(args)


my_func(1, 2, 4, 5, 6, 7, 8, 9, 100, "Ricsi", print, [413515,3561635,163136,3])

# **kwargs - keyword argumentum
# nevesített paraméter átadás
def my_func(**kwargs):
    print(kwargs)

my_func(name="Ricsi", age=33, position="BD Tech Lead", eyecolor="brown")
my_func(name="Ricsi", age=34, position="BD Tech Lead", eyecolor="brown")

# ha mindkettő jelen van, akkor
# először pozíció alapú argumentumokat adom oda
# aztán a nevesített "kulcs - érték párokat"
def my_func(*args, **kwargs):
    print(args)
    print(kwargs)


my_func(1, 2, 3, 4, 10, name="Ricsi", age=33)