# 1. feladat:
# lista műveletekkel adjatok az alább megadott üres listához tetszőleges értékeket

my_list = []


# adjatok egy tetszőleges kulcs-érték párt a megadott dictionaryhez.
my_dict = {
    "auto": "BWM"
}

# 2. feladat:
# a megadott dictionaryben lévő autokhoz
# adjatok hozzá egy price kulcsot és egy tetszőleges értéket állítsatok be hozzá
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



# 2. feladat:
# az utolsó 2 értéket módosísátok tetszőleges értékre
my_list = ["Ricsi", "Géza", "Karcsi", "Peti"]


# print(my_list)
# 3. feladat:
# az alábbi dictionary-ben töröljük a zip_code értékét
my_dict = {
    "shop": {
        "shop_name": "Reál",
        "zip_code": "1111",
        "type": "general store"
    }
}


# 3. feladat
# a megadott litából hozzatok létre egy tuple-t úgy,
# hogy az első elemtől minden 2. elemet tartalmazza

my_list = ["alma", "körte", "banán", "narancs", "dinnye", "barack"]

# 4. Nem szeretjük a francia autót, töröljök a renault az autók közül. A többi érték ne változzon.

my_dict = {
            "auto": [{"type": "Volvo",
                     "color": "gold"
                    },
                    {"type": "Audi",
                     "color": "red"
                    },
                    {"type": "Reanult",
                     "color": "White"
                    } ],
            "driver": ["Heikki Kovalainen", "Bruno Senna", "Sebastien Buemi"],
            "licence": False,
            "age": 18
        }
