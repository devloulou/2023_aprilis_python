/*
 * Táblák kialakítani
 * 
 * Postgres adatbázisban minden objektumnak van 1 tulajdonosa
 * 
 * schema a tulajdonos
 * mire való a schema? más adatbázisban usernek nevezhetjük
 * - A schemában tudunk különböző adatbázis objektumokat létrehozni
 * - különböző megoldásokat különböző helyen tudok létrehozni
 * - Szabályozni tudom, hogy ki férhet hozzá a schemában lévő adatokhoz
 *   (ezt egyébként objektum szinten tudjuk:
 *     pl. van 10 táblám, de csak 1-hez adok írási jogot)
 * - a logikailag összetartozó megoldásokat el tudom különíteni
 * 
 * az objektumok schemanként kell hogy egyediek legyenek
 * 
 * vannak olyan objektum típusok, amelyek más objektumhoz tartoznak
 * ezeknél is egyedinek kell lennie a nevének a scheman belül
 * 
 */

create table employee_tst (
name text,
employee_id integer,
salary integer,
job_start_date date
);

select * from employee_tst;

insert into employee_tst (name, employee_id, salary, job_start_date)
values (null, null, 20000, date'2020-10-03');

/*
 * Megszorítások - Constraintek
 * 
 * Primary key constraint - elsődleges kulcs - összetett constraint
 * nem lehet null az értéke - not null constraint
 * és nem lehet duplikáció az értékei között - unique constraint
 * kapcsolatot táblák között csak primary key-ek mentén lehet kialakítani
 * 
 * 1 táblának csak 1 primary key mezője lehet
 * 
 * 
 * Primary key 2 constraintből áll: not null és unique constraint
 * 
 * 'Not Null' constraint: null value nem lehet az értéke 
 * Megjegyzés: a null != '' az üres stringgel
 * 
 * 
 * Unique constraint: csak egyedi értéke lehet az adott mezőnek
 * 
 * Check constraint - őt nem fogjuk haasználni, bizonyos esetekben hasznos
 * egyébként érdemes kerülni
 * 
 * */


drop table employee_tst;

create table employee_tst (
employee_id integer primary key,
name text not null,
position text unique,
salary integer,
job_start_date date
);

select * from employee_tst;

insert into employee_tst (name, employee_id, salary, job_start_date, position)
values ('Karcsi', 2, 20000, date'2020-10-03', 'IT');

------------------------------------------------------------
--- Adatmodellezésbe

/*
 * Composite key: speciális primary key,
 * több mező egyidejüleg viselkedik primary key-ként
 * ez 1 primary key attól függetlenül
 * 
 * Foreign key constraint - idegen kulcs
 * 
 * Kapcsolatot hozzak létre a táblák között
 * Szülő - gyermek kapcsolat lesz -> a foreign key a gyermek táblában lesz
 * és a foreign key rámutat a szülő tábla primary key mezőjére
 * 
 * reláció ez a kapcsolat - a tábla maga is egy reláció
 * 
 * PostgreSQL egy relációs adatbázis: az adatokat tábkákba csoportosítva
 * tárolom 
 * a táblák között képes vagyok kapcsolatot kialakítani
 * 
 * */

/*
 * a dolgozóhoz tartozó adatok - employee
 * munkakörhöz tartozó adatok
 * a cég szervezeti egységéhez tartozó adatok
 * 
 * */


--- Employee_id	Name	Salary	Hire_date	Position_id

--- Postion_id	Position	Department_id

--- Department_id	Depmartment_name	Employee_id

/*
 * adatmodellezés: normal form , 3rd normal form
 * 
 * Amit akarunk adatbázis oldalon:
 * ne legyen ismétlődés az adatokban - redundancia
 * konzistens legyen az adat - megbízható
 * 
 * 
 * */


create table employee (
employee_id serial primary key,
name text,
salary integer,
hire_date date
);

drop table departments;
drop table positions;
drop table hiring;

/*
 * Sequence - auto increment mezők - szekvencia
 * 
 * */

create sequence seq_department_id
start with 10
increment by 10;

----------------------------------------------------------

create table departments (
department_id integer primary key DEFAULT nextval('seq_department_id'),
department_name text,
employee_id integer,
constraint fk_employee_id_dep foreign key (employee_id) references employee(employee_id)
);

create table positions(
position_id serial primary key,
position_name text,
department_id integer,
constraint fk_department_id_pos foreign key (department_id) 
references departments(department_id)
);

create table hiring (
employee_id integer,
position_id integer,
constraint fk_employee_id_hiring foreign key (employee_id)
references employee(employee_id),
constraint fk_position_id_pos foreign key (position_id)
references positions(position_id)
);

select * from employee;
select * from departments;
select * from positions;
select * from hiring;

---------------------------------------------------------
--Employee insertek
insert into employee (name, salary, hire_date)
values ('Bill Gates', 100000, date'1989-03-04');

insert into employee (name, salary, hire_date)
values ('Elon Musk', 200000, date'2004-03-04');

insert into employee (name, salary, hire_date)
values ('Jeff Bezos', 150000, date'2000-03-04');

insert into employee (name, salary, hire_date)
values ('Mekk Elek', 130000, date'2013-03-04');

insert into employee (name, salary, hire_date)
values ('Mark Zuckerberg', 134000, date'2002-03-04');

-----------------------------------------
--Department insertek

insert into departments (department_name, employee_id)
values ('Engineering', 2);

insert into departments (department_name, employee_id)
values ('IT', 1);

------------------------------
--- Positions insertek
insert into positions (position_name, department_id)
values ('Data Engineer', 10);

insert into positions (position_name, department_id)
values ('Frontend Developer', 20);

insert into positions (position_name, department_id)
values ('Backend Developer', 20);

-----------------------------------------
-- Hiring inserts
insert into hiring (employee_id, position_id)
values (1, 1);

insert into hiring (employee_id, position_id)
values (2, 1);

insert into hiring (employee_id, position_id)
values (3, 3);

insert into hiring (employee_id, position_id)
values (4, 1);

insert into hiring (employee_id, position_id)
values (5, 2);

----------------------------------------------------------------------



