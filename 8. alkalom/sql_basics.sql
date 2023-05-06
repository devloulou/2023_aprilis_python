-- sor komment

/*
 * PostgreSQL adatbázis
 * 
 * Mire való az adatbázis? 
 * Az adatbázist az adatok tisztított, strukturált és könnyen elérhető
 * formában való tárolására használjuk
 * 
 * Miben lesz más az én kurzusom a neten található kurzukhoz képest?
 * A fő téma: hogyan kell adatbázis oldalon dolgozni != sql nyelv
 * 
 * Az adatokat hogyan kell letárolni
 * Miért úgy kell letárolni
 * Miért kell stuktúrálni
 * Mi a strukturálás módszertana
 * Hogyan lehet az adatokat gyorsan és megfelelően elérni
 * 
 * Adatmodellezés
 * 
 */

/*
 * PostgreSQL adatbázis - RDBMS - Relational Database Management System
 * Relációs adatbázis
 * 
 * SQL  - lekérdező nyelv - Structured Query Language
 * 
 * RDMS rendszerek közé tartozik a PostgreSQL, Oracle, MS SQL, MySQL, Teradata
 * 
 * Felhasználás módja szerint
 * 2 nagy csoportra szoktuk osztani az RDBMS adatbázisokat
 * 
 * OLTP - OLAP
 * OLTP - Online Transactinal Processing
 * OLAP - Online Analitical Processing
 * 
 * Mi OLTP -t fogunk fejleszteni
 * 
 * 
 * 
 * Tipikus OLTP rendszeresek: webshop, netbank, wizzair jegyértkesítéses rendszere
 * 
 * Tipikus OLAP rendszerek: Big Data adatelemzés, Data Science adatfeldolgozás,
 * 							adattárház, data lake, date lakehouse, 
 * 
 * OLTP
 * ahol a cél 1 ügyfélhez tartozó adatot létrehozz, módosíts vagy törölj
 * 	- kevés adat használat
 *  - általában az adat aktuális állapotát fogod használni
 * 
 * NoSQL - Nem relációs adatbázisok -> MongoDB
 * 
 * SQL
 * 
 * DDL - Data Definition Language
 * create, drop, alter, truncate, -- comment, rename
 * 
 * DML - Data Manipulation Language
 * insert, update, delete, --lock, call, explain plan
 *
 * DCL - Data Control Language - ezzel nem fogunk
 * grant, revoke 
 * 
 * DQL - Data Query Language
 * select
 * 
 * row based format - sor alapú adattárolás
 * 
 * */

-- schemas

-- create table
-- az adattípusok adatbázisonként eltérhetnek
create table my_test_table (
name text,
job text,
salary integer
);

select * from my_test_table;

-- adat betöltése táblába: insert utasítás

insert into my_test_table (name, job, salary)
values ('Ricsi', 'Big Data Tech Lead', 10000);

insert into my_test_table (name, job, salary)
values ('Ricsi', 'Big Data Tech Lead', 10000);

insert into my_test_table (name, job, salary)
values ('Ricsi', 'Big Data Tech Lead', 10000);

update my_test_table set salary = 20000 where name = 'Ricsi';

/*
 * Mi az a session?
 * Az adatbázis felé nyitott kapcsolat, ami az adatbázis
 * utasítást futtatja
 * Minden utasítást a session keresztül történik és csak akkor lépnek érvénybe
 * ezek az utasítások ha a végzett folyamatot valamilyen módon lezárom.
 * 
 * 2 állapota lehet: "élő" - idle (tétlen)
 * 
 * Mi az a tranzakció?
 * 
 * Minden SQL utasítás egy tranzakció.
 * A tranzakciónak 3 állapota van: jóváhagyott
 * 								   visszavont
 * 								   függőben lévő -> nem szabad így hagyni
 * Tranzakció jóváhagyása: commit utasítással történik
 * A jóváhagyás azt jelenti, hogy globálisan elérhetővé teszem a módosítást
 * 
 * Tranzakció visszavonása: rollback utasítás
 * 
 * Mi a baj a függőben lévő tranzakciókkal?
 * A le nem zárt tranzakciójk blokkolhatják az adott objektum használatát
 * lock mechanizmus
 * 
 *
 * 
 * */



