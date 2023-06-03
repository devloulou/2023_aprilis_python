"""
OOP - Object Oriented Programming
osztályokat fogunk fejleszteni, amelyekből objektumokat fogunk példányosítani

az OOP nem a cél

4 alapelv - 4 priciples

abstraction - absztrakció
inheritencia - öröklődés
encapsulation - egységbe zárás
polimorfizmus - többalakúság
"""

class MyClass:
    pass


"""
Abstraction - 'rejtsd el' a kódot a használat helyétől

osztályok 'típusa': 
1. behavoural - 'viselkedés'
2. data related - valamilyen adat leírásához tartozó osztály


az osztálynak lehetnek tulajdonságai -> ezeket attribútumoknak nevezzük
minden, az osztályhoz tartozó változó, függvény etc. egy attributum
"""

class Human:
    """
    def __init__() - az osztály konstruktora
    a konstruktor feladatai:
      a 'kívülről' érkező attributumokat ha elérhetővé szeretném tenni az osztály számára
      ha bizonyos alap attributumokat szeretnék beállítani - véltozókra, függvényekre gondolok
      ha azt szeretném, hogy a példányosítás során valamilyen automata futás történjen
    
    a példányosításnál ő automatikusan lefut

    minden függvény, ami az osztályból példányosított objektumhoz tartozik
    az első paramétere kötelezően a 'self' kulcsszó kell legyen
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greetings(self, salary=None):
        """
        This function print out a sentence. There is no return statement
        """
        print(f"Szia {self.name}, te tényleg {self.age} éves vagy? {salary}")



#########################################################################
ricsi = Human("Ricsi", 32)
kati = Human('Kati', 25)

ricsi.name = 'Pisti'
ricsi.salary = 10_000


# print(ricsi.salary)

# ricsi.greetings(ricsi.salary)
# kati.greetings()

########################################################################################

"""
Inheritance - öröklődéds

szülő (ős) - gyermek kapcsolat kialakítása 2 vagy több osztály között
Python le tudja kezelni a többszörös öröklődést -> a gyermek osztálynak több ősosztálya lehet

öröklődés: a gyermek osztály az ős osztály minden attributumát: változóit, függvényeit leszármaztatja
           a gyermek osztály az ős osztály minden tulajdonságát tudja használni és módosítani
"""

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greetings(self):
        print(f"Szia {self.name}")


class Woman(Human):
    def __init__(self, name, age):
        # 'supercharging' az ősosztályt
        super().__init__(name, age)
        self.sex = 'woman'

    def greetings(self):
        print(f"Szia,  {self.name} vagyok és {self.sex} vagyok.")


kati = Woman('Kati', 25)

# kati.greetings()
# print(kati.sex)

#######################################################################################

"""
Encapsulation - egységbe zárás
Minden az objektumhoz tartozó attributum legyen private addig, amíg nem akarom
publikusan használni az adott tulajdonságot

Osztály attributumainak a láthatósága lehet:
1. public - publikus
2. private - privát
3. protected - átmenet a private és public között -> ilyen nincs a pythonban

Private attributum: Kívülről semmilyen formában nem tudod az értékét
    - lekérni
    - módosítani

A Pythonban nincs valódi private attributum, 
"""

class TestClass:
    def __init__(self):
        self.val = "alma"
        self.__name = 'Ricsi' # private attributum

test = TestClass()

test._TestClass__name = "Pista"
# print(test._TestClass__name)

test.__name = 'Karcsi' # ez publikus
# print(test.__name)


##################################################################
"""
Polimorphism - többalakúság
"""

# polimorph függvény

my_string = "Ricsi"
my_lst = [1, 2, 3]
my_dict = {
    "kulcs": 10
}

# print(len(my_string))
# print(len(my_lst))
# print(len(my_dict))


class India:
    def language(self):
        print("Indians speak Hindi")

    def landsize(self):
        print("India is very very big")


class Hungary:
    def language(self):
        print("Hungarians speak Hungarian")

    def landsize(self):
        print("Hungary is very very small")


india = India()
hun = Hungary()

temp = (india, hun)

# for item in temp:
#     item.landsize()
#     item.language()

"""
Minden esetben szükség van e __init__ metódusra? - Nem minden esetben kell constructor - __init__ metódus

Pythonban minden objektumnak van 1 ősosztálya -> 'object' osztály

a constructornak van egy ellentéte - destructor: megszüntetni és felszabatítani a változókat
memóra management célból

A Python dinamikius memória managementet használ
    -> van beépíteett garbage collector 
        -> nem kell a destructort használnunk

__func_name__ típusú függvények a 'magic' metódusok, double underscore metódusok - dunderscore metódusok
Ezek speciális, beépített függvények, amelyek speciális feladatokat látnak el
"""

class MyClass:
    def __init__(self):
        self.name = "Pista"

    # destructor
    def __del__(self):
        print('meghívódtam')

    def __str__(self):
        return f"Felüldefinálva: {self.name}"


    def greetings(self, name):
        print(f"Hi {name}")

test = MyClass()

# test.greetings('Amanda')

print(test)

my_list = [1, 2]
my_list2 = [3, 4]

my_list3 = my_list + my_list2
print(my_list3)