"""
Készíteni fogunk statisztikákat:

leghosszabb sor
hány oldalas a könyv: 3000 karakter / 1 oldal
legrövidebb sor -> az üres sorok nem számítjuk fele
leggyakrabban előforduló 5 szó -> legalább 5 karakter legyen 1 szó


A statisztikát ki fogjuk írni JSON file-ba.

Előtte megcsináljuk úgy, ahogyan most meg tudnánk oldani
Az egész megvalósítás moduláris fejlesztéssel fog történni
##################################################
Készíteni fogunk statisztikákat:

leghosszabb sor
hány oldalas a könyv: 3000 karakter / 1 oldal
legrövidebb sor -> az üres sorok nem számítjuk fele
leggyakrabban előforduló 5 szó -> legalább 5 karakter legyen 1 szó


A statisztikát ki fogjuk írni JSON file-ba.


1. meg kell nyitni a filet és kiolvassuk az adatot valamilyen módon
2. elkészíteni a statisztikai számításokat:
    - meghatározni az oldalak számát: string hosszúságát elosztom 3000-el
    - sortörések mentén létrehozok a beolvasott adatból 1 listát
        - leghosszabb és a legrrövidebbnél  - min és max - használjuk az adatot
    - legenerálni a leggyakrabban előforduló 5 szót: spacek mentén csinálok egy újabb listát
3. kiírni a JSON-t



"""
import os
import json

# CONSTANS változó - a változó értéke nem fog változni
FILE_PATH = r'C:\WORK\2023_aprilis_python\6. alkalom\data\Dracula.txt'
FILE_PATH = os.path.join(os.path.dirname(__file__), 'data\Dracula.txt')

def get_data_from_txt():
    with open(FILE_PATH, 'r', encoding="utf-8") as f_obj:
        data = f_obj.read()
        # data = f_obj.readlines() -> listaként olvassa fel az adatot, ahol a lista elemei 
        # a file sorai lesznek a sortárrel lezárva

    return data

# hibakezelés - exception handling
def write_json(json_path, data):

    if not os.path.exists(os.path.dirname(json_path)):
        raise FileNotFoundError(f'A megadott elérési útvonal {json_path} nem létezik')

    if type(data) == list:
        if type(data[0]) != dict:
            raise ValueError(f"A megadott adat nem írható ki valid JSON-ként")

    elif type(data) != dict:
        raise ValueError(f"A megadott adat nem írható ki valid JSON-ként")
    
    with open(json_path, "w", encoding="utf-8") as f_obj:
        json.dump(data, f_obj, ensure_ascii=False, indent=4)


def get_page_num(data):
    import math    
    return math.ceil(len(data)/3000)

def min_max_row(data):
    """
    data az egészben tartalmazza a felolvasott könyvet, egy nagy string
    sorokra kell bontani a nagy stringet -> stringet a split utasítással, \n karakter mentén
    szétvágom

    split függvény egy listát fog visszaadni
    """
    # aladar -> .split('a') -> ['', 'l', 'd', 'r'] 
    temp = []

    # rows = data.split('\n')

    # for item in rows:
    #     if len(item) > 0:
    #         temp.append(item)
    # for item in data.split('\n'):
    #     if len(item) > 0:
    #     # if item != '':
    #         temp.append(item)

    temp = [item for item in data.split('\n') if len(item) > 0]

    min_value = temp[0]
    max_value = temp[0]
    for item in temp:
        if len(item) < len(min_value):
            min_value = item

        if len(item) > len(max_value):
            max_value = item

    min_value = min(temp, key=len)
    maxocska = max(temp, key=len)

    sorted_list = sorted(temp, key=len)
    min_value = sorted_list[0]
    max_value = sorted(temp, key=len, reverse=True)[0]

    return {
        "min": {'value': min_value, 'len': len(min_value)},
        "max": {'value': max_value, 'len': len(max_value)}
    }

def most_common_5_words(data):
    from collections import Counter
    temp = []

    for item in data.split('\n'):
        temp.extend(item.split(' '))

    temp = [item for item in temp if len(item) >=5]

    c = Counter(temp)

    return c.most_common(5)


if __name__ == '__main__':
    data = get_data_from_txt()

    file_path = os.path.join(os.path.dirname(__file__), 'statistics.json')

    page_num = get_page_num(data)
    min_max = min_max_row(data)

    most_common_words = most_common_5_words(data)


    statistics = {
        "page_num": page_num, 
        "min_max": min_max,
        "most_common_words": most_common_words
    }

    write_json(file_path, statistics)