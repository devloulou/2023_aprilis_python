"""
Loops - Ciklusok

while
for loop


while feltétel_amíg_igaz:
    utasítások

while akkor érdemes használni, amikor event működést szeretnénk fejleszteni

iterálható object: list, tuple, dict, set etc...
for ciklus_valotozk in iterálható_object:
    utasítások

"""

# while ciklus

my_num = 10

# iteráció - a ciklus futásait
while my_num >= 0:
    # print(my_num)
    # my_num = my_num - 1
    my_num -= 1

my_num = 10

# 10%2 -> maradákos osztás - modulo - ha maradék 0, akkor a 10 osztható 2-vel
# pass - üres művelet
# continue - elindítja az új iterációt

# = jel az értékadás operátor
# == értéket vizsgálsz

while my_num >= 0:
    if my_num%2 == 0:
        # print(my_num)
        my_num -= 1
    else:
        # pass
        my_num -= 1
        continue

    # print("utasítás futás")

while my_num >= 0:
    if my_num%2 != 0:
        my_num -= 1
        continue
   
    # print(my_num)
    my_num -= 1

    # print("utasítás futás")

while my_num >= 0:
    if my_num%2 == 0:
        # print(my_num)
        my_num -= 1
        # print("utasítás futás")
    
    my_num -= 1

# meg akarom állítani idő ellőtt a ciklusomat: break utasítás kilép a ciklusból

my_num = 10

while my_num >= 0:
    print(my_num)
    break
    print(my_num)
    if my_num == 7:
        break
    my_num -= 1