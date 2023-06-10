"""
a 'self': a self ahhoz kell, hogy ún. instance tulajdonságokat hozzunk létre
a self az maga a példányosított objektum referenciája

a self-el ellátott tulajdonságok instance szintűek -> minden self-el elátott dolog az osztályon belül
és az objektumon kívül használható / elérhető / módosítható!?

instance - object - 1 példánya az osztálynak - 1 létrehozott objektum egy adott osztályból

------------------------------------------------
staticmethod: nem látja az objektum tulajdonságait
általban utility megoldásokhoz szoktuk használni

az példányosított objektumon keresztül is tudom használni
és magán az osztályon keresztül is - nem szükséges példányosítani

------------------------------------------------
class attributumok
classmethod és class változók

class változó: példányosítás nélkül, az osztályon keresztül tudjuk használni
               de osztályon belül a self szó használatával tudjuk meghivatkozni

"""
def is_adult(age):
    if not age >= 18:
        return False
    return True

class Human:
    # azért akarsz class változót használni
    # hogy minden példányosított objektum ugyan azt az értéket kapja meg
    my_class_val = "This is test"
    def __init__(self, name, age):
        # instance változó - self.valtozo - __init__ metódusban van létrehozva
        self.name = name
        self.age = age
        temp = 10
    
    def greetings(self):        
        print(f"Szia {self.name}")
        print(f"object: {self.my_class_val}")
        # self.my_class_val = "Baltazár"
        print(f"class: {Human.my_class_val}")

    # @staticmethod
    # def is_adult(age):
    #     if not age >= 18:
    #         return False
    #     return True
    
    @staticmethod
    def is_adult2(age):
        return is_adult(age)


if __name__ == '__main__':
    ricsi = Human("Ricsi", 32)
    balint = Human('Bálint', 20)

    # print(ricsi.is_adult(15))
    # print(Human.is_adult(18))
    ricsi.my_class_val = "Ricsi my_class_val"
    ricsi.greetings()
    print("------------------")
    balint.greetings()

    print("--------------------")
    print(f"Human class érték: {Human.my_class_val}")
    # print(is_adult(22))

    # print(Human.is_adult2(13))
    # print(ricsi.is_adult2(13))

    