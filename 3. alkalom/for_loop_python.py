"""
For ciklus

A for ciklust arra használjuk, hogy végig iteráljunk 
egy iterálható objektumon

foreach - C#

A for ciklus az iterálható object utolsó eleme után kilép automatikusan

for ciklus_valtozó_neve in iterálható_object:
    műveletek

"""

my_list = [1, 2, 3, 4, "Ricsi", "Karcsi"]

# ciklusváltozó - 'placeholder' -> helyettesító megoldás
# for item in my_list[::2]:
#     print(item)


# for item in range(0, 10):
#     print(item)

my_list = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (10, 11)]

a, b = my_list[0:2]

(0, (1,2))
"""
my_list = [1, 2, 3]

enumerate(my_tuple) -> [(0, 1), (1, 2), (2, 3)] -> [(index, iterálható_object_eleme), ....]

"""
my_list = [(1, 2), 100, "Ricsi", (4, 5, 6, 7)]
# my_list = [(0, 1), (1, 2), (2, 3)]

for idx, item in enumerate(my_list):
    print(f"{idx} - {item}")