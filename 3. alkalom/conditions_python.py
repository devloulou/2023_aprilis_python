"""
Conditions - feltételek - if else utasításokra - elágazások

indentations - indentáció - bekezdés

Python feltétel
if feltétel_kiértékelése:
    ha fenti feltétel teljesült, akkor ezek a kódok fognak lefutni
    ha fenti feltétel teljesült, akkor ezek a kódok fognak lefutni
    ha fenti feltétel teljesült, akkor ezek a kódok fognak lefutni
    ha fenti feltétel teljesült, akkor ezek a kódok fognak lefutni
    ha fenti feltétel teljesült, akkor ezek a kódok fognak lefutni
    ha fenti feltétel teljesült, akkor ezek a kódok fognak lefutni
elif feltétel_kiértékelése:
    ha fenti feltétel teljesült, akkor ezek a kódok fognak lefutni
else:
    ha fenti feltétel teljesült, akkor ezek a kódok fognak lefutni

Python egy interpreter nyelv - futási időben a python kód egy köztes kódra fordul le
C nyelvű kód

Python - Cpython
C nyelven írt feltétel
if (feltétel_ha_igaz) {
    ha fenti feltétel teljesült, akkor ezek a kódok fognak lefutni;
}
elif (feltétel_ha_igaz) {
    ha fenti feltétel teljesült, akkor ezek a kódok fognak lefutni;
}
else {
    else esetén futnak;
}

"""

age = 17
# age >= 18 - egy logikai vizsgálat
# logikai adattípus - boolean
# 2 értéke lehet: igaz vagy hamis - True vagy False

# else ág: ha egyik előző feltételem sem igaz, akkor fut le

# print(age >= 18)
if age >= 18:
    print("Nagykorú")
elif age < 17:
    print("Kiskorú")
else:
    print("")

# print("Step over ide fog ugrani")

age = 18


# if age >= 18:
#     print("age >= 18")
# elif age > 17:
#     print("age > 17")
# else:
#     print("else ág")
##################################

age = 18
# if age >= 18:
#     print("age >= 18")

# if age > 17:
#     print("age > 17")

###################################
# age = 17
# if age >= 18:
#     print("ez egy új utasítás v1")
#     if age == 18:
#         print("age == 18")        
#     else:
#         print("age == 18 nek az else ága")     

#     print("ez egy új utasítás v2")

# if age >= 17:
#     print("age > 17")

###################################

# tagadás - ítéletkalkulus - 
# not False - True
# not True - False
my_list = [1, 2, 3, 4, 5]

item = 10

# print(not item in my_list)
# if not item in my_list:
#     print("valami")

# if item not in my_list:
#     print("valami")
# if item in my_list:
#     print(f"{item} benne van a listában")
# else:
#     print(f"{item} nincs benne a listában")

##################################################################
# az üres tuple, dict, list, set logikai vizsgálata pl if my_tuple: -> False
my_tuple = (0,)

if my_tuple:
    print("valami my_tuple")

my_list = [False, ]

if my_list:
    print("valami my_list")

my_dict = {None:0}

if my_dict:
    print("valami my_dict")

#None - az üres érték, gyakorlatilag a semmi, a null érték
# a None != '' 
my_set = {None,}

if my_set:
    print("valami my_set")


if not False:
    print("almafa")

# not 0 -> True 
# az üres tuple, dict, list, set, '', és a 0 logikai értéke : False

my_num = 0

if my_num:
    print("valami my_num")

if not 0:
    print("not 0")

if not '':
    print("üres string")


print(not [])