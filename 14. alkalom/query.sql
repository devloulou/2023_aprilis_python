/*
 * Indexek
 * 
 * gyorsabban érjük el az adatokat
 * 
 * (1, 2, 3, 4, 5, 6, 7, 8, 10)
 * 
 * select * from tabla -> full table scan
 * 
 * select * from table
 * where mezo > 5   --> full table scan
 * 
 * full table scan -> minden adatot megvizsgálok
 * 
 * 2 féle indexel lehet dolgunk:
 * 1. btree - b-fa index - normal index 
 * 2. bitmap index 
 * 
 * bitmap index használata: ha olyan mezőm van, ahol nagyon sok az adat
 * de az adat ismétlődik 
 * 
 * indexek az alábbi utasításokat segítik:
 * select, delete, update
 * 	amennyiben az update nem az indexált mező értékét változtatja
 * 
 * az index struktúrájára hatással van:
 * delete, insert
 * 
 * és az index struktúrájára hatással lehet:
 * update
 * 
 * az indexek az alábbi utasításokat lassítják:
 * insert (deletet, update)
 * 
 * btree index típusai:
 * unique index - pl. primary key
 * normal index - pl. foreign key - vannak olyan adatbázisok, amelyek
 * maguktól nem indexálják fel a foreign key-t. a best practice az, hogy legalább 1
 * normal index legyen a foreign key-eken
 * 
 * best practice indexekhez:
 * kerüljük a táblán a túl sok index használatot
 *    -> lassítani fogja az adat integrációt
 *    -> a rendszernek minden indexet karban kell tartania
 * 
 * Honnan tudom, hogy milyen mezőre kell index?
 * megvizsgálom, hogy a táblában lávő mezőket hogyan akarják használni:
 * szűrésekhez, módosításokhoz és törléshez
 * */

explain analyze select * from employee e 
where e."name" = 'Bill Gates';

select * from hiring h ;

explain analyze select * from employees_hr eh 
where 
--eh.first_name = 'Steven'
eh.employee_id = 100

/*
 * reguláris kifejezések
 * 
 * regexp_substr
 * regexp_like
 * regexp_match
 * regexp_replace
 * regexp_count
 * regexp_instr
 * 
 * */
with b_data as (
select 'írni32 akarok valamit hosszú ível' as col)
select
	substring(col, 1, regexp_instr(col, '(?![[:ascii:]]+).', 1, 1)),
	regexp_match(col, '(?![[:ascii:]]+).'),
	regexp_instr(col, '(?![[:ascii:]]+).', 1, 1),
	regexp_count(col, '(?![[:ascii:]]+).'),
	regexp_replace(col, '(?![[:ascii:]]+).', '-', 'g'),
	regexp_substr(col, '(?![[:ascii:]]+).', 1, 1)
from b_data
where regexp_like(col, '(?![[:ascii:]]+).')






