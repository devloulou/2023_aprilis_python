"""
SQLAlchemy egy python library,
amely azt teszi lehetővé, hogy pythonból
majdhogynem adatbázis független módon SQL utasításokaat tudjuk futtatni

3 féleképpen lehet használni:
1. raw sql - natív sql utasítokkal
2. expression language 
3. ORM alapú felhasználás - ORM - Object Relational Mapping

Raw SQL: stringként fogjuk az SQL utasítésokat megírni Pythonban és a libraryvel fogjuk futtatni
majd az adatábisban

"""

"""
Általánosságban minden adatbázissal kapcsotos library a következő képpen működik:

1. kell egy kapcsolat az adatbázis felé
2. a kapcsolaton keresztül futtatjuk az utasítást
3. az utasítás / hiba esetén annak megfelelően lezárjuk a kapcsolatot / tranzakciót

Round trip: tartsd alacsonyan a round trippek számát

egy utasítás pythonból -> adatbázisba eljut az utasítás -> az adatbázis lefuttatja -> a választ visszaküldi a pythonnak

"""

from sqlalchemy import create_engine, text

engine = create_engine("postgresql://postgres:postgres@localhost/postgres")


cre_table = "create table if not exists engineer_test (col text, col2 text, col3 text, col4 text, col5 text, col6 text)"

delete = "delete from engineer_test where cast(col as integer) > 50"
update = ""

select_statement = "select * from engineer_test"

insert_table = """insert into engineer_test (col, col2, col3, col4, col5, col6)
values (:col, :col2, :col3, :col4, :col5, :col6)""" # bind változó
data = [{'col': str(item), 'col2': str(item*10), 'col3': str(item*100), 'col4': str(item*100), 'col5': str(item*1000), 'col6': str(item*100)} for item in range(1,100000)]

import time
# session létrehozása
with engine.connect() as conn:
    conn.execute(text(cre_table))

    start_time = time.time()

    #conn.execute(text(delete))
    
    result = conn.execute(text(select_statement))
    print(result)
    for item in result:
        print(item)
    # conn.execute(text(insert_table), data) > ezt javaslom használni

    # for item in data:
    #     conn.execute(text(insert_table), item)
    print(f"took me: {time.time() - start_time}")
    conn.commit()
    conn.close()