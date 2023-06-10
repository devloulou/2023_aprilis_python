
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

ricsi = Human("Ricsi", 32)

ricsi.age

import os
from os import path, listdir

print(os.path.basename(__file__))
print(path.basename(__file__))