#egy sor kommentelése
"""
ez a multi line comment - Docustring
"""
'''
ez a multi line comment - Docustring
'''

"""
A Python egy dinamikusosan típusos nyelv
futási időben értékeli ki a változók adattípusát

c# - típusos nyelv
public int szam = 10;

Python változó:
van egy neve, ami a memóriában egy adott értékre mutat
"""
# értékadás művelet - példányosítás
szam = 10

# string - szöveges adat
szam = "Ricsi"
szam = 'Karcsi'

num = 10
num2 = num

num = 30

my_str = "Ricsi"
my_str2 = my_str

my_str = 'Pisti'

# print(my_str)
# print(my_str2)

"""
skaláris értékek - szám típusok

illetve aritmetikai műveletek: összeadás, kivonás, szorzás, osztás
"""
# egész szám: integer
num = 2

# lebegőpontos szám: float
num_f = 2.5

# print(num * num_f)

# complex szám
my_num = 2+3j
my_num2 = 4+5j

# print(my_num + my_num2)

# aritmetikai műveletek

num = 2
num2 = 5

osszeg = num + num2
osszeg = num - num2
osszeg = num * num2
osszeg = num / num2

"""
Érdekességek

A Python 1 értéket 1x tárol a memóriában, ha erre van lehetősége
amikor létrejön a válozó, akkor lefoglalódik az érték a memóriában -> ennek van egy memória címe
és a változó a memória címre mutat
"""

num = 20
num2 = 21

# a 20-as érték egyszer van a memóriában, de 2 változó mutat rá
print(id(num))
print(id(num2))