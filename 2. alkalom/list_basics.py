"""
List data type

A lista egy mutable data type, azaz megváltoztatható

A listához lehet:
    - hozzáadni elemeket
    - törölni elemeket
    - meglévő elemeket lehet módosítani

A lista iterálható objektum, mert vannak elemei
Nincs megkötés, hogy milyen elemeket tartalmazhat

my_list = [1, 2, 3, "Ricsi", [5, 6, 7], (4, 25,51)]

"""

#### Elem hozzáadása listához

my_list = list()
my_list = []

# 1 elem hozzáadása
my_list.append(10)

# több érték hozzáadása

my_list.extend(("Ricsi",))
my_list.extend("Ricsi")

# my_list.extend([1, 2, 3, 4, 5, 6, 7])
temp = [1, 2, 3, 4, 5, 6, 7]
my_list.extend(temp)

# adott pozícióra történő elem hozzáadás

my_list.insert(0, "Jani") # ez a művelet ez nagyon költséges tud lenni

# print(my_list)
################################################
# listából való törlés

my_list = ["Ricsi", 1, 2, 1, 2, "Karcsi", "Pisti"]

# my_list.clear() - töröl minden elemet a listából

# index mentén való törlés
my_list.pop(5)

# érték alapon való törlés
my_list.remove(1)

del my_list[3], my_list[3] # OOP esetén beszélni róla

# print(my_list)
##################################################
# elemek megváltozatása: slicing

my_list = ["Ricsi", 1, 2, 1, 2, "Karcsi", "Pisti"]

my_list[1] = 10

# packing  - becsomagolja tuple-ként
my_list[1] = 10, 20, 30

# unpacking
my_list[2:5] = (50, 60, 70)
my_list[2:5] = [500, 600, 700]
my_list[2:5] = [500, 600, 700, 800, 900, 1000]

my_list = [10, 30, 50, 70, 90]

# unpacking
# a, b, c = my_list[0:3]

# * becsomagoljuk az adatok -> packing
# a, b	=	my_list[0:2]

a, *b = my_list


# print(a, b, c)
# print(a, b)

###################################################################################
# referencia

my_list = [1, 2, 3]

my_list2 = my_list

my_list2.append(10)

my_list.pop(0)

my_list[2] = 400

# print(my_list)
# print(my_list2)

# nested list - belső lista
my_list = [1, 23, [1, 23, [12, 3, 4]]]

my_list[2].pop(0)

my_list[2][1].append(300)
# print(my_list)
# print(id(my_list2))

####################################################################

# listák egyesítése

my_list = ["Karics", "Pisti"]
my_list2 = [1, 2, 3, 4]

# 1. extend függvény
my_list.extend(my_list2)

my_list2.append(10)

print(my_list)

# 2. 'concatenation
my_list = ["Karics", "Pisti"]
my_list2 = [1, 2, 3, 4]

my_list3 = my_list + my_list2

my_list.append(10)

print(my_list3)

# 3. packing - unpacking
my_list = ["Karics", "Pisti"]
my_list2 = [1, 2, 3, 4]

my_list3 = [*my_list, *my_list2]

my_list.append(10)

print(my_list3)
