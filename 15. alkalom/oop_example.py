"""
Szimuláljuk le egy önkiszolgáló kassza működését

legyenek termékek, amelyeket pénzért megveszek
a termékeknek legyen értéke

legyen egy kosaram: az összeválogatott termékeket tartalmazza: hány db és melyik termék
legyen maga a gép: ami visszaadja a blokkot, hogy mennyibe kerül nekem a vásárlás


Termék: 
    lesz ára
    lesz neve

Kosár:   
    milyen termék, milyen áron, hány db

Kassza:
    adja össze a termékek árát
    generáljon ez alapján egy blokkot
"""

class Product:
    def __init__(self, price, name):
        self.price = price
        self.name = name

    def __str__(self):
        return self.name

class Cart:
    def __init__(self):
        self.my_cart = {}

    def add_to_cart(self, db, obj):
        self.my_cart.update({obj:db})

    def __str__(self):
        temp = "{"
        for obj, val in self.my_cart.items():
            temp += f"{obj}: {val}, \n"

        return temp + "}"


class Kassza:
    def __init__(self):
        self.cart = Cart()

    def generate_bill(self):
        bill = ""
        for obj, val in self.cart.my_cart.items():
            bill += f"{obj.name}/{val} db: {obj.price * val} Ft \n"

        return bill

if __name__ == '__main__':
    # értékadás - példányosítás
    kassza = Kassza()

    kenyer = Product(970, 'fehér kenyér')
    szalami = Product(1970, 'szalámi')
    beer = Product(750, 'sör')

    kassza.cart.add_to_cart(3, kenyer)
    kassza.cart.add_to_cart(2, szalami)
    kassza.cart.add_to_cart(24, beer)

    # print(kassza.cart)
    print(kassza.generate_bill())