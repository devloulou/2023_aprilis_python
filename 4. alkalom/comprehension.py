"""
Comprehension műveletek

list - list comprehension
dict - dictionary comprehension
tuple - generator comprehension - ő a kakutojás

comprehension szintaxis:

pl. list [amit_az_append_nél_megadok for valami in iterálható_objektum feltételek]

"""

my_list = []

# amikor elemekkel töltünk fel objektumokat, hogy populálunk
for item in range(0, 100):
    if item%3 == 0:
        my_list.append(str(item))

# list comprehension
# list [amit_az_append_nél_megadok for valami in iterálható_objektum feltételek]

# a list comprehension gyorsabban populálja a listát, 
# mint egy sima for ciklus + append művelet
my_list = [str(item) for item in range(0, 100) if item%3 == 0]

# print(my_list)

###################################################################################
# dictionary comprehension
my_dict = {}
for idx, item in enumerate(['Ricsi', 'Karcsi', 'Pisti']):
    # 2 féleképpen lehet kulcs - értéket hozzáadni a dicthez
    # my_dict[idx] = item
    my_dict.update({idx:item})

print(my_dict)


my_dict = {idx:item for idx, item in enumerate(['Ricsi', 'Karcsi', 'Pisti'])}

# print(my_dict)

######################################################################################
# generator comprehension

# a generator comprehension úgynevezett 'lazy evaluation'-t használ - laza kiértékelés
# nem értékeli ki a kifejezést futási időben és nem generálja le a memóriába a kifejezés eredményét
my_list = [str(item) for item in range(0, 1000000) if item%3 == 0]
my_gen = (str(item) for item in range(0, 10) if item%3 == 0)

import sys

# print(sys.getsizeof(my_list))
# print(sys.getsizeof(my_gen))

# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))

for item in my_gen:
    print(item)



