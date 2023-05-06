import feladat
import os

print(__name__)
print(feladat.__name__)

print(__file__)

print(os.path.basename(__file__))
print(os.path.dirname(__file__) + '\data\Dracula.txt')

print(os.path.join(os.path.dirname(__file__), 'data\Dracula.txt'))