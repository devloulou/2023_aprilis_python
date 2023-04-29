"""
JSON - Javascript Object Notation

In JSON, values must be one of the following data types:

a string
a number
an object (JSON object)
an array
a boolean
null

"""

import json

"""
dump,
dumps,
load,
loads
"""

my_dict = {
    "cars": [
        {
            "color": "white",
            "motor_type": "benzin"
        },
        {
            "color": "white",
            "motor_type": "benzin",
            "type": {
                "sedan": {
                    "price": {
                        "loan": 12345677,
                        "cash": 12346246
                    }
                },
                "combi": {
                    "func": True,
                    "func_name": "print"
                }
            }
        },
        {
            "color": "white",
            "motor_type": "benzin",
            "price": {
                "loan": 123450000,
                "cash": 123456756
            }
        },
        {
            "color": "white",
            "motor_type": "benzin",
            "manufacture_date": "1990"
        }
    ]
}
# JSON kiírás
# a JSON kiírás: serialization - serializáció -> Python objectből JSON objectet állítok elő
with open('test.json', 'w', encoding="utf-8") as f_obj:
    json.dump(my_dict, f_obj, ensure_ascii=False, indent=4)


# JSON felolvasást ->
# deserialization - deserializáció -> JSON objectből Python objectet képzek
with open('test.json', 'r', encoding="utf-8") as f_obj:
    data = json.load(f_obj)


# dumps
print(type(data))

json_string = json.dumps(data)

print(json_string)

# loads
temp = json.loads(json_string)

print(temp)
