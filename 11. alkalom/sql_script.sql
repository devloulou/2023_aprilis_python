/*
 * Hogyan kell a táblákat összekapcsolni:.
 * join-okat
 * 
 *  
 * Hány ember dolgozik az IT departmenben és azon belül data engineerként
 *
 * Táblák közötti kapcsolat lehet,
 * 1. kulcsok mentén: primary key - foreign key
 * 2. nem kiépített kapcsolat
 * 
 */

select * from kapcsolat_test;

create table kapcsolat_test (
id serial primary key,
name text,
adozott_e boolean
);

insert into kapcsolat_test (name, adozott_e)
select name, true from employee;

select * from kapcsolat_test;

-----------------------------------------------
select * from employee;
select * from departments;
select * from positions;
select * from hiring;

-- iparági standard
--- inner join - csak a közös rekordokat jeleníti meg
select e.employee_id, e."name", e.salary, d.department_name 
from employee e 
inner join departments d on e.employee_id = d.employee_id 
--and d.department_id = 20
--where d.department_id = 20
;

-- ez nem az iparági standard
select e.employee_id, e."name", e.salary, d.department_name 
from employee e,
departments d
where e.employee_id = d.employee_id;

--------------------------------------
--- Descartes szorzat - ettől félni kell
select * from employee e,
departments d

---------------------------------------
-- left join


select * from employee;
select * from departments;
select * from positions;
select * from hiring;

insert into departments(department_id, department_name, employee_id)
values (nextval('seq_department_id'), 'HR', null);

select * from departments;

-- mely dolgozók azok akik nem vezetők
select * from employee e
left join departments d on e.employee_id = d.employee_id 
where d.department_id is null;

--- rigth join
select * from employee e
right join departments d on e.employee_id = d.employee_id ;

--- full outer join
select * from employee e
full outer join departments d on e.employee_id = d.employee_id ;
----------------------------------------------------------
--Hány ember dolgozik data engineerként:. jelenítse meg a dolgozó nevét,
-- fizetését, a department nevét, és legyen ott a vezető neve

-- Joinolni joinnal joinolj
select * from employee;
select * from departments d
inner join employee e on d.employee_id = e.employee_id ;
select * from positions;
select * from hiring;

--- JPE - józan paraszti ész
select e.name, e.salary, d.department_name, e2.name from employee e
inner join hiring h on e.employee_id = h.employee_id
inner join positions p on h.position_id = p.position_id
inner join departments d on p.department_id = d.department_id
inner join employee e2 on d.employee_id = e2.employee_id 
where h.position_id = 1
;

select * from employee;
select * from departments;
select * from positions;
select * from hiring;

/*
 * departmentenként hány db emberem van
 * és kik a vezetők 
 * */


select count(e.employee_id) as db, d.department_name, e2.name as vezeto
from employee e
inner join hiring h on e.employee_id = h.employee_id
inner join positions p on h.position_id = p.position_id
inner join departments d on p.department_id = d.department_id
inner join employee e2 on d.employee_id = e2.employee_id
group by d.department_name, e2.name;

-- egy adott dataset
-- subselect
select * from
(select
count(base_data.name) as db,
base_data.department_name,
base_data.boss as vezeto
from
(select e.name, e.salary, d.department_name, e2.name as boss from employee e
inner join hiring h on e.employee_id = h.employee_id
inner join positions p on h.position_id = p.position_id
inner join departments d on p.department_id = d.department_id
inner join employee e2 on d.employee_id = e2.employee_id) as base_data
group by base_data.department_name, base_data.boss) as t;

-----------------------------------------------------------

--- with
--- történik egy materializálás a with miatt : "szimulálja, hogy ez egy tábla"
with base_data as (
	select e.name, e.salary, d.department_name, e2.name as boss from employee e
		inner join hiring h on e.employee_id = h.employee_id
		inner join positions p on h.position_id = p.position_id
		inner join departments d on p.department_id = d.department_id
		inner join employee e2 on d.employee_id = e2.employee_id
), agg_data as (
	select count(base_data.name) as db,
		base_data.department_name,
		base_data.boss as vezeto 
	from base_data
	group by base_data.department_name, base_data.boss
), sum_data as (
	select *from python_test
)
select * from sum_data;

---------------------------------------------------
/*halmaz műveletek:
--- union, union all, intersect, except
-- dummy table
Minden halmaz művelet alap feltétele: meg kell egyeznie a halmazok
mezőinek számosságával

union vs union all:
az union distinctálja a rekordokat 
	- nagyon hosszú futási időt ereedményezhet nagy adatok esetében
az union all 'csak' egyesíti az adatokat -> nem szűr duplikációra

intersect - közös rekordokat adja vissza

except - ami az első táblában benn van, de hiányzik a másik táblából
*/
select * from
(select 30 as id, 'Ricsi' as name, 1000 as price
union
select 20 as id, 'Ricsi' as name, 1000 as price) as t2
intersect
select * from (
select 30 as id, 'Ricsi' as name, 1000 as price
union all
select 10 as id, 'Ricsi' as name, 1000 as price) as t;


select * from
(select 30 as id, 'Ricsi' as name, 1000 as price
union
select 10 as id, 'Ricsi' as name, 1000 as price) as t2
except
select * from (
select 30 as id, 'Ricsi' as name, 1000 as price
union all
select 10 as id, 'Ricsi' as name, 1000 as price
union all
select 20 as id, 'Ricsi' as name, 1000 as price) as t;


/*
 * window function
 * 
 * */

