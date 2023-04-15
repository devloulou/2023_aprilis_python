"""
Tuple data type

A tuple egy immutable adattípus és összetett adattípus
    - a meglévő elemeket nem lehet módosítani
    - nem lehet a tuple-höz elemet hozzáadni
    - nem lehet törölni elemet
Iterable object - iterálható objektum
Lehet használni a slicing műveletet

Mire jó a tuple?

"""

my_tuple = (1, 2,2, 30,1, 400, (3, 4, 5), 'Ricsi', print,)
# my_tuple = tuple(1, 2, 30, 400, 'Ricsi', print)

# print(my_tuple.count(2))
# print(my_tuple.count(400))

# print(my_tuple.index(0))

# print(my_tuple[0:3])

my_tuple = (1, [1, 2, 3], "Ricsi")

my_tuple2 = my_tuple

my_tuple[1].append(100)

print(my_tuple)