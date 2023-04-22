"""
Dictionary,
listákhoz
"""

my_list = [10, 8, 6, 4, 2, 1, 3, 5, 7, 9]
#           0  1  2  3  4  5  6  7  8  9

# töröljük minden páratlan számot
"""
Ha for ciklunál listán iterálok végig, akkor a listából ne töröljek futás közben adatot
mert a törölt elemek utáni értékek a vizsgált index pozíciójára kerülnek
ergo ki fog hagyni értékeket a ciklus a vizsgálatból
"""
temp = []
for item in my_list:
    if item%2 == 0:
        # itt kellene a törlést elvégeznem
        # my_list.pop(idx)
        # my_list.remove(item)
        temp.append(item)

my_list = temp

# print(my_list)

#################################################################

my_dict = {
    "name": "Ricsi",
    "age": 33,
    "position": "Big Data Tech Lead"
}

# a dictionaryből való lekérdezés nagyon gyors

# my_dict.keys()
# my_dict.values()

for key, value in my_dict.items():
    # print(my_dict[item])
    print(key, value)