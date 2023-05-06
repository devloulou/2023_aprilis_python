"""
Exception handling - hibakezelés - kivétel kezelés

try:
    funkciók hivása
except:
    ez a hiba ág
    itt azon megoldásokat futtatom, amit hiba esetén kell
finally:
    ez mindig lefut, függetlenül attól, hogy sikerült vagy hibára futott a futtatás

Exception - általános hiba, minden hiba egy exception

"""
# print(5/0)

# print("Hello")

# num1 = 100
# num2 = 200
# if num1 - num2 < 0:
#     # user defined exception
#     raise Exception("Nincs megfelelő fedezeted")



try:
    num1 = 100
    num2 = 200    
    if num1 - num2 < 0:
        # user defined exception
        raise ZeroDivisionError("Nincs megfelelő fedezeted")
    print(5/0)
    print(num1-num2)

except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print(f"Hiba van: {err}")
    # raise - manuálisan hibát okozok / manual error throw
    # raise

finally:
    print("Én mindig lefutok")


print("Hiba után vagyok")