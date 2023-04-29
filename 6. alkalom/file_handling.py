"""
File műveletek

1. lépés: meg kell nyitni valamilyen módon a file-t
2. lépés: vagy kiolvassuk az adatot és dolgozunk az adattal
          vagy előállítunk valahonnan, valamilyen adatot és kiírjuk file-ba
3. lépés: lezárjuk a file objektumot

A python 3.x alapértelmezetten unicode karakterkódolást használ

"""
# test.py -> relatív path - relatív 'útvonal'

# C:\WORK\2023_aprilis_python\6. alkalom\test.txt -> absolute path - teljes elérési útvonal

"""
\n - sortörés
\t - tabulátor
"""


file_path = r"C:\WORK\2023_aprilis_python\6. alkalom\test.txt"
f = open(file_path, 'r', encoding="utf-8")

data = f.read()

f.close()

# 'w' - megnyitja írásra a filet -> ha nem létezik a file akkor létrehoz 1 üres filet
# ha létezik a file, akkor törli a tartalmát
f = open(file_path, 'w', encoding="utf-8")

my_str = "Ez egy nagyon furcsa időjárás \n"
f.write(my_str)
f.write(my_str)
f.write(my_str)
f.write(my_str)
f.write(my_str)


f.close()