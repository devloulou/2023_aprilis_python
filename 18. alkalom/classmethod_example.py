"""
classmethod

cls - class -t fogja jelenteni

class -al kapcsoaltos feladokat szeretnénk elvégezni
class állapotának változtatása
új objektum létrehozása

a classmethod nem látja az instance attributumokat

"""

class MyClass:
    temp = "Ricsi"
    def __init__(self, val):
        self.val = val

    def greetings(self):
        print(f"{self.val}")

    @classmethod
    def my_func(cls, val):
        # print(cls.temp)
        return cls(val) # új objektumot példányosítok az osztályból
    
    @classmethod
    def my_func2(cls, val):
        cls.temp = val

if __name__ == '__main__':
    test = MyClass(10)

    # test.my_func()
    # MyClass.my_func()

    test2 = MyClass.my_func(14)

    MyClass.my_func2("Karcsi")

    print(test.temp)
    print(test2.temp)