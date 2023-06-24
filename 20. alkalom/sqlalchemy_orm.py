"""
ORM - Object Relational Mapping

mi fogunk class-okat definiálni, 
amelyek maguk a táblák lesznek

A classokból objectumokat fogunk létrehozni
és a műveleteket az objektumok segítségével fogjuk elvégezni

"""

from sqlalchemy import create_engine, select, delete, update, insert
from sqlalchemy import MetaData, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("postgresql://postgres:postgres@localhost/postgres")
meta = MetaData(schema="python_test")
base = declarative_base(metadata=meta)

print(base)

# ORM model - a tábla python oldali reprezentációja
class FilmTable(base):
    __tablename__ = 'films'

    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    director = Column(String(50))

    # def __repr__(self):
    #     return f"{self.title} object"

class Actors(base):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))

Session = sessionmaker(engine)
session = Session()

# egy adatbázis record fog létrejönni - record 1 sor adat a táblában
alien = FilmTable(id=1, title='Alien', director='Ridley Scott')
starwars = FilmTable(id=2, title='Star Wars', director='George Lucas')

base.metadata.drop_all(engine)
base.metadata.create_all(engine)

data = [{'id': 1, 'title': 'Alien', 'director': 'Ridley Scott'},
        {'id': 2, 'title': 'Aliens', 'director': 'James Cameron'},
        {'id': 3, 'title': 'Valami', 'director': 'Rendező'}]

temp = [FilmTable(**item) for item in data]
# FilTable(id=1, title='Alien1)

my_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
}

my_dict2 = {"kulcs": "érték"}

my_dict3 = {**my_dict, **my_dict2}

print(my_dict3)


# for item in data:
#     temp.append(FilmTable(**item))

# bulk insert
# session.add_all([alien, starwars])
session.add_all(temp)
session.commit()

# deserializáció - adatbázis recordból egy ORM model objectet kapok vissza
filmek = session.execute(select(FilmTable))

# print(filmek)

for item in filmek:
    print(item[0])

print("##################################")

filmek = session.query(FilmTable)

# print(filmek)
# lekérdezés és update
for item in filmek:
    item.title = "Frizbi"
    session.commit()


update_statement = update(FilmTable).where(FilmTable.id == 1).values(title="Terminator")

session.execute(update_statement)
session.commit()


filmek = session.query(FilmTable).filter(FilmTable.id == 3).delete()
session.commit()

delete_statement = delete(FilmTable).where(FilmTable.id == 2)
session.execute(delete_statement)
session.commit()