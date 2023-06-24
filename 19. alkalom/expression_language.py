"""
Expression language - egyfajta ORM

ORM - Object Relational Mapping

Lesznek Python objectek, amelyek hivatkozni fognak az adatbázis objektumokra
És mivel lesznek python objectek, minden objecttel kapcsolatos műveletet
a Python objektumon keresztül fogunk elvégezni

itt is szükség van egy engine definícióra
"""
from sqlalchemy import create_engine, text, or_, func, select
from sqlalchemy import MetaData, Table, Column, String, Integer

engine = create_engine("postgresql://postgres:postgres@localhost/postgres")
# engine = create_engine("sqlite:///test.db")

meta = MetaData(schema="python_test")
# meta = MetaData()

movies = Table('movies',
               meta,
               Column('id', Integer, primary_key=True),
               Column('title', String(50)),
               Column('director', String(50)))

songs = Table('songs',
               meta,
               Column('id', Integer, primary_key=True),
               Column('song_name', String(50)),
               Column('singer', String(50)))

# movies.create(engine, checkfirst=True)
movies.drop(engine, checkfirst=True)


with engine.connect() as conn:
    songs.create(conn, checkfirst=True)
    conn.commit()
    songs.drop(conn)
    conn.commit()

# [movies, songs, ...]
meta.create_all(engine, checkfirst=True)

# CRUD utasítást: create, read, update, delete - insert, select, update, delete

# insert - create

insert_statement = movies.insert()

data = [{'id': 1, 'title': 'Alien', 'director': 'Ridley Scott'},
        {'id': 2, 'title': 'Aliens', 'director': 'James Cameron'},
        {'id': 3, 'title': 'Valami', 'director': 'Rendező'}]

with engine.connect() as conn:
    """
    az adatok behellyettesítésére bind változókat használok
    """
    # print(insert_statement)
    conn.execute(insert_statement, data)

    """
    manuálisan adom meg az értékeket
    """
    test = "INSERT INTO python_test.movies (id, title, director) VALUES (5, 'valami', 'valami')"
    
    test_table = """create table python_test.employee (
employee_id serial primary key,
name text,
salary integer,
hire_date date
)"""
    
    temp = insert_statement.values(id=4, title="Prey", director="VAlaki")
    # print(temp)
    # print(test)
    conn.execute(temp)
    conn.execute(text(test))
    conn.execute(text(test_table))
    conn.commit()

select_statement = movies.select().where(movies.c.id==1)
select_statement = movies.select().where(movies.columns.id==1)

select_statement = movies.select()\
                    .where(or_(movies.c.id <= 3, movies.c.id==5))

select_statement = select(func.count(movies.c.id))\
                    .where(or_(movies.c.id <= 3, movies.c.id==5))   

delete_statement = movies.delete().where(movies.c.id == 2)

update_statement = movies.update().where(movies.c.id == 3).values(title="Robocop")

# print(select_statement)
with engine.connect() as conn:
    conn.execute(delete_statement)
    conn.execute(update_statement)
    conn.commit()
    result = conn.execute(select_statement)

my_data = result.fetchall()
print(my_data)
# print(result.fetchmany(3))