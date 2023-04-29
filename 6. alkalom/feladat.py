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

def get_data_from_txt():
    with open(FILE_PATH, 'r', encoding="utf-8") as f_obj:
        data = f_obj.read()

    return data


if __name__ == '__main__':
    data = get_data_from_txt()
    print(data)