age = 32
age = int(32)

name = "Ricsi"
name = str("Ricsi")

# típus konverzió: amikor egy fajta típusból egy másik adattípusra akarod
# átalakítani az értéket, ha lehet

final_str = name + ' ' +str(float(age))

# print(final_str)

##############################String Formatting###############################
##############################################################################

# 1. Old Style formatting: 2.# pythonban volt jelentősen jelen
# Ricsi vagyok és 32 éves.

name = "Ricsi"
age = 32

# %s - string típusú placeholder
my_str = "%s vagyok és %x éves" %(name, age)


# 2. New Style formatting

name = "Ricsi"
age = 32

# string template: 
my_str = "{name} vagyok és {eletkor:x} éves"

# print(my_str.format(name=name, eletkor=age))

# 3. String Interpoláció - f' string formázás
s = "Ricsi"
age = 32

my_str = f"{s} vagyok és {age} éves"

print(my_str)

# Template formázást mutassam, ha az importokat vettük