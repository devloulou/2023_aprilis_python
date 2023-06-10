"""
Namespace: ahonnan az adott objektumokat elérem - 
A pythonban minden egy objektum: változók, függvények, osztályok, modulok, packagek, fileok

Scope: az objektumok láthatóságát szabályozza - nem összekeverendő a public és
private dolgokkal
honnan használom

Namespace és Scope szintjei:
- built -in 
- global
- enclosing - köztes
- local

"""
"""
Built -in namespace: 'a beépített szint'
Nem szükséges hozzá import
és azokat az objektumokat, változókat, osztályokat
bárhol el tudod érni - függvényeken velül, modulokon, packageken és osztályokon
"""
# print(), len(), __file__, int(), list() stb.


"""
Global namespace: 0. indentációs szint

A file-on belül bárhol meg tudom hivatkozni az adott objektumot,
egészen addig, amíg az objektum létezik

"""
'''
my_list = [10, 20, 30, 40]

def my_func(a, b):
    return a + b

my_func(10, 20)
'''

my_list = [10, 20, 30]

def my_func(a):
    my_list.append(a)

def pelda():
    # masik nevű fv nem a global namespacen van, ezért nem tudom meghívni kívülről
    def masik():
        print("Szia")

my_func(40)

# print(my_list)

"""
Local namespace: adott objektumokon belül definiált objektumok
pl.
függvényben létrehozott változó,
függvényben létrehozott függvény
osztályban létrehozott tulajdonságok 
stb.

Enclosing namespace: egymásba ágyazott függvények és osztályok esetén jön létrre
hasonlóan működik, mint a local namespace

Ha létrejön az enclosing namespace, akkor az enclosing lesz "előrébb" és az ő része
lesz a local namespace
"""



def my_func():
    # ő egy local namespacen létrehozott változó
    temp = []
    for i in range(10):
        temp3 = []
        temp.append(i)

    print(temp3)

# my_func()
my_list = [1, 2, 3]

def my_func():
    # létrejön a local namespacen egy my_list nevű változó
    # az inner function megléte miatt a my_list immár az enclosing - köztes namespacehez tartozik
    my_list = [10, 20, 30]

    def inner():
        # ő lett a local namespace
        my_list = [100, 200, 300]

##########################################################################################

my_list = [1, 2, 3]

def my_func():
    my_list = [10, 20, 30]
    # print(my_list)

my_func()
##########################################
# változó deklarálásnak
# példányosításnak
my_list = [1, 2, 3]

def my_func():
    for idx, item in enumerate(my_list):
        my_list[idx] = "Ricsi"

my_func()
# print(my_list) 
################################
# referencia használatával is tudom módosítani
my_list = [1, 2, 3]
def my_func(m_l):
    for idx, item in enumerate(m_l):
        m_l[idx] = "Ricsi"

my_func(my_list)
# print(my_list) 

################################

my_list = [1, 2, 3]
my_str = "Ricsi"

def my_func():
    global my_list, my_str
    my_list = "Karcsi"

my_func()

my_list = [1, 2, 3]

##################################
def my_func():
    return "Ricsi"

my_list = my_func()

##################################

my_str = "Ricsi"
def my_func():
    # enclosing namespace
    # global my_str
    my_str = "Karcsi"
    def inner():
        # local namespace
        # global my_str
        nonlocal my_str
        my_str = "Béla"
        print(my_str)
    inner()
    print(my_str)

my_func()
print(my_str)


# print(my_list)