# 1. feladat: írjatok egy olyan megoldást, amely a lenn megadott listából
# minden 2. elemet kitörli

my_list = ['alma', 'körte', 'barack', 'bizili', "banán", "narancs"]

temp = []

for idx, gyumolcs in enumerate(my_list):
    if idx%2 == 0:
        temp.append(gyumolcs)

# print(temp)
# my_list = temp
my_list = my_list[::2]
# print(my_list)
######################################
# 2. feladat: A megadott listából töröljétek minden 3-al osztható számot

my_list = [item for item in range(100)]
my_list2 = [3, 4, 5, 6, 7]

def my_func(m_list):
    temp = []
    for item in m_list:
        if item%3 != 0:
            temp.append(item)    

    return temp

# my_list = my_func(my_list)

my_list = my_func(my_list)
my_list2 = my_func(my_list2)


# 3. feladat: a my_dict-et töltsétek fel elemekkel az elvárt eredménynek megfelelően.
# elvárt eredmény: {0:1, 1:2, 2:3, 3:4 ... 9:10}
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_dict = {}


def my_func(m_list):
    temp = {}
    for idx, item in enumerate(m_list):
        temp.update({idx:item})

    return temp

my_dict = my_func(my_list)

# print(my_dict)
##########################

my_dict = {}
for idx, item in enumerate(my_list):
    my_dict.update({idx:item})

# my_dict = temp

# print(my_dict)
#################################################################################
# feladat:
# a megadott dictionaryben lévő autokhoz 
# adjatok hozzá egy price kulcsot és egy tetszőleges értéket állítsatok be hozzá
# ez úttal ne manuálisan oldjátok meg

my_dict = {
    "auto": [
        {
            "brand": "BMW",
            "color": "white",
            "type": "diesel"
        },
        {
            "brand": "Volvo",
            "color": "yellow",
            "type": "benzin"
        },
        {
            "brand": "Tesla",
            "color": "black",
            "type": "electric"
        }
    ]
}

new_key = {'price': 10_000}

key_numbers = len(my_dict['auto'])

# for i in range(0, key_numbers):
#     my_dict['auto'][i].update(new_key)

# print(my_dict)

for item in my_dict['auto']:
    item.update(new_key)

# print(my_dict)

# töröljétek ki azt az elemet, ahol nem szerepel író

my_dict = {
    "books": [
        {
            "writer": "J.K. Rowlings",
            "book": "Harry Potter and the Goblet of the Fire"
        },
        {
            "writer": "Mikszáth Kálmán",
            "book": "Szent Péter esernyője"
        },
        {            
            "book": "Sorstalanság",
            "writer": ""
        },
         {            
            "book": "Sorstalanság"
        }
    ]

}


def my_func(m_dict):
    temp = []
    for item in m_dict['books']:
        if item.get('writer'):
        # if 'writer' in item.keys():
            # itt kellene törölnöm a listából az értéket
            temp.append(item)

    m_dict['books'] = temp

    return m_dict

# függvény paraméter átadás mint referencia
my_func(my_dict)

# print(my_dict)

# 5. feladat:
# írjatok egy olyan programot, amely a 2 listából csinál egy dictionary-t
# pl: {
#   1: "alma",
#   2: "körte"
#   .
#   .
#   5: "dinnye"
# }
my_dict = {}
my_list = [1, 2, 3, "Józsi", 5]
my_list2 = ["alma", "körte", "barack", "banán", "kivi"]

def my_func(m_lst, m2_lst):
    temp = {}
    # 
    for idx in range(0, len(m_lst)):
        temp.update({m_lst[idx]: m2_lst[idx]})

    for idx, _ in enumerate(m_lst):
        temp.update({m_lst[idx]: m2_lst[idx]})

    return temp

my_dict = my_func(my_list, my_list2)

# print(my_dict)

#Írj egy Python programot, amely paraméterként kap 3 számot és kiírja a képernyőre a
# legkisebb értéket ezek közül!

def my_func(*args):
    return min(args)

legkisebb = my_func(1, 2, 3, 0, 4, 5, 6, 0, -2)

# print(legkisebb)

# Bbálint megoldás
def my_func():
    list = []
    osszes = int(input("elemek száma: "))
    for i in range(0,osszes):
        elem = int(input(str(i+1) + ". elem érték:"))
        list.append(elem)
    min_value=list[0]


    for k in range(0, osszes):
        if min_value > list[k]:
            min_value=list[k]
    print("a legkisebb érték a ", min_value)


#Írj egy Python programot, amely bekér egy dolgozat pontszámot (x) a felhasználótól és kiír egy
# érdemjegyet az alábbiak szerint! 1: ; 2: 50<=x<60; 
# 3: 60<=x<70; 4: 70<=x<85; 5: x>=85.

def my_func(x):
    jegy = 0
    if x <50:
        jegy = 1
    elif x<60:
        jegy = 2
    elif x<70:
        jegy = 3
    elif x<85:
        jegy = 4
    else:
        jegy = 5

    return jegy


jegy = my_func(98)

print(f"A jegy: {jegy}")

