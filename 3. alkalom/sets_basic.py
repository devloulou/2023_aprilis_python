"""
Set - halmazok

my_set = {1, 2, 2, 2, 2, 2, 3, 4, 5, 6}
duplikáció mentes

Mutable adattípus - meváltoztatható:
    - lehet hozzáadni elemet
    - lehet törölni elemet
    - lehet módosítani elemet

a set nem támogatja a slicing műveletet -> nem tudok index mentén elemet lekérni

a set-et a matematikai halmazműveletek során érdemes használni

"""

my_set = {50, 2, 3}

# elem hozzáadása
my_set.add(10)
my_set.add(20)


my_set2 = {4, 5, 6, 3}

my_set.update(my_set2)

# print(my_set)
############################
# törlés setből

temp = my_set.pop()

my_set.remove(6)

# módosítani elemet - ezt valójában nem lehet elvégezni - nincs beépített megoldás

# print(my_set.)

# print(temp)
# print(my_set)

my_set = {1, 2, 3, 4, 5}
my_set2 = {4, 5, 6, 7, 8}

# a my_set elemei közzül melyek nincsenek a my_set2-ben
print(my_set.difference(my_set2))
print(my_set2.difference(my_set))


print(my_set.intersection(my_set2))




