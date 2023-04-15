"""
Dictionary - hash tábla

my_dict = {
    "kulcs": "érték",
    "color": "black",
    "salary": 10000,
}

A dictionary is mutable adattípus
    lehet hozzá kulcs - érték párokat felvenni
    lehet törölni kulcs - érték párokat
    lehet módosítani kulcshoz tartozó értékeket

A kulcs mindig egyedi. Nem lehet 2 ugyanonalyn nevű kulcs 1 szinten

A kulcsoknak hashalhető adattípusnak kell lennie: str, int, float, tuple, NoneType
"""

my_dict = {
    "brand": "BMW",
    "color": "black",
    "price": 100_000
}

# érték lekérése kulcs alapján

# print(my_dict['brand'])
# print(my_dict['color'])


# kulcs - érték hozzáadása , módosítani
my_dict = {
    "brand": "BMW",
    "color": "black",
    "price": 100_000
}

my_dict.update({"test": "data", "horsepower": 1100, "lising": True})
my_dict['utasok_szama'] = 10

my_dict['utasok_szama'] = 15
my_dict.update({"test": "érték", "horsepower": 100, "lising": False})

# {'brand': 'BMW', 'color': 'black', 'price': 100000, 'test': 'data',
# 'horsepower': 1100, 'lising': True, 'utasok_szama': 10}

# kulcs - érték pár törlése

my_dict = {
    "brand": "BMW",
    "color": "black",
    "price": 100_000
}

my_dict.pop("brand")

retval = my_dict.popitem()


# print(retval)
# print(my_dict)

##########################################################
my_dict['fruit']['deli']['egyeb'][0]['test']
my_dict = {
    "fruits": {
        "deli": {
            "banan": 10,
            "narancs": 10,
            "egyeb": [
                {
                    "test": 1
                }
            ]
        },
        "bogyos": {
            'cseresznye': 10,
            'szolo': 10
        },
        "hazai": {
            "bogyos": {
                "cseresznye": 10,
                "szolo": 10,
            },
            "egyeb": {
                "alma": 10,
                "körte": 10
            }
        }
        
    }
}


######################
# "deli": {
#             "banan": 10,
#             "narancs": 10,
#             "egyeb": [
#                 {
#                     "test": 1
#                 }
#             ]
#         }


my_dict = {
    "fruit":{
        "deli":{
            "categories": [
                {
                    "category_name": "banan",
                    "measurement": "kg",
                    "amount": 10,
                },
                   {
                    "category_name": "narancs",
                    "measurement": "kg",
                    "amount": 10,
                },
                {
                    "category_name": "egyeb",
                    "measurement": "kg",
                    "amount": 10,
                    "parts": [
                        {...}
                    ]
                }
            ]
        }

    }
}