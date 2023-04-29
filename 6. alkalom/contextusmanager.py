"""
Contextusmanager 

with utasítás

erőforrást managel -> file műveleteknél a file operációs renszer szintű 
lezárását elvégzi helyettünk
"""

file_path = r"C:\WORK\2023_aprilis_python\6. alkalom\test.txt"

with open(file_path, 'r', encoding="utf-8") as f_obj:
    data = f_obj.read()

print(data)