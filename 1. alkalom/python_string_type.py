"""
Pythonnak van több megvalósítása
CPython - C nyelvben megírt kód -> 
interpreter nyelv - a futtatás során a Python kód egy köztes állapotra fordul -> 

Jython
"""

"""
String adattípus

my_str = 'ez egy string'
my_str = "ez egy másik string"

A string egy immutable adattípus: megváltoztathatatlan
A string egy iterálható adattípus -> iterable object

"""
# ezek értékadás operátorok
my_str = "Ricsi"
my_str = "Pisti"

"""
Slicing művelet: indexek mentén tudunk részhalmazát elérni az adott objektumnak

MY_STRING[HONNAN:MEDDIG:LÉPTÉK_MÉRTÉKE] -> meddig (nem tartalmazza azt az adott indexen lévő értéket)

my_string = "miskolc"

print(my_string)
my_string[:]
my_string[::]

"""

my_str = "indul a görög aludni"

# print(my_str[0:5])
# print(my_str[:5])

# print(my_str)
# print(my_str[:7]) # elejétől a végéig
# print(my_str[:7:1]) # elejétől a végéig, egyesével

my_str = "indul a görög aludni"

# print(my_str[::2])
# print(my_str[::-1])

# print(my_str[-3:])

# print(my_str[0])

# my_str[0] = 'z'

my_str = "indul a görög aludni"

str_begin = my_str[0:8]
str_end = my_str[13:]

# print(str_begin)
# print(str_end)

# stringek összefűzése - concatenation - konkatenáció
final_str = str_begin + 'német' + str_end

print(final_str)

