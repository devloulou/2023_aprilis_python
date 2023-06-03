"""
Tanulók vizsgaeredményét kellene kiértékelni
1. feladat
Írjunk egy olyan programot, ami a következők alapján kiértékeli a tanulókat:
Minden tanuló, minden tárgyból 3 pontszámmal rendelkezik.
Az első pontszám minden tárgy esetében: a témazáró vizsga eredmény
A második pontszám minden tárgy esetében: a beadandó feladat eredménye
A harmadik pontszám minden tárgy esetében: a szóbeli Vizsga
A kiértékelés logikája:
 1. ha valaki nem szóbelizett, azonnal elégtelen, nem kaphat jegyet
 2. ha valaki a beadandót nem adta meg, akkor is átlagot kell számolni,
    0 eredményye legyen a beadandónak
 3. a vizsga 70%-ot ér, a beadandó 10-et, a maradék 20% pedig a szóbeli eredmény
 2. feladat:
Csináljuk meg tantárgyanként az osztály átlagot: jegyek és pontszám
Jegyek:
50 alatt 1-es
50 - 60 2-es
60 - 70 3 -as
70 - 80 4-es
80+ - 5-ös
 
"""
kati = {
    "matek": [75, 85, 73],
    'irodalom': [65, 87, 52],
    'tortenelem': [86, None, 93]
}
pisti = {
    "matek": [54, 64, 73],
    'irodalom': [65, 94, 52],
    'tortenelem': [86, 74, None]
}
karcsi = {
    "matek": [73, 85, 62],
    'irodalom': [65, None, 60],
    'tortenelem': [86, 90, 93]
}
peti = {
    "matek": [43, 85, 53],
    'irodalom': [65, 87, None],
    'tortenelem': [86, None, 23]
}