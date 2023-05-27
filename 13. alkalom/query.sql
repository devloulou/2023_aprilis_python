/*
 * string fügvényeket
 * date függvényeket
 *  
 * */
select *from employees_hr;
-- concatenation - stringek összefűzése
-- 1. módszer: ||
select 
e.first_name, e.last_name,
e.last_name || ' ' || e.first_name || '_' || e.employee_id as full_name,
concat(e.last_name, ' ', e.first_name, '_', e.employee_id) as full_name2
from employees_hr e;

----------------------
-- position függvény: visszaadja egy string kezdő pozícióját
select
e.email,
position('@' in e.email),
substring(e.email from 0 for position('@' in e.email)) as user_name,
substring(e.email, 0, position('@' in e.email)) as user_name2,
substring(e.email, position('@' in e.email)+1),
length(e.email),
replace(e.email, 'sqltutorial.org', 'gmail.com'),
substring(e.email, 0, position('@' in e.email)) || '@google.com',

from employees_hr e;

--reguláris kifejezés egyelőre nem foglalkozunk
with base_data as (
select '     adhadhah  h eg   e   g   ' as col, 'ricsi' as col2)
select
replace(col, '  ', ' '),
col,
lpad(col2, 7, 'alma'),
rpad(col2, 7, 'a')
from base_data;


---------
-- to_char()
select
e.hire_date,
to_char(e.hire_date, 'day'),
to_char(e.hire_date, 'ww'),
to_char(e.hire_date, 'D'),
to_char(e.hire_date, 'DD'),
-----------
to_char(e.hire_date, 'YYYY'),
to_char(e.hire_date, 'Month'),
to_char(e.hire_date, 'dd'),
to_char(e.hire_date, 'day'),
------------
to_char(e.hire_date, 'YYYY/MM/DD -> Month.day DD')
from employees_hr e;

--- stringek dátummá alakítása
-- cast - változó cast-olása
with base_data as(
select now() as datum
),
string_data as (
select 
to_char(datum, 'YYYY/MM/DD -> Month - Day - ww') as date_string
from base_data
)
select
cast(substring(date_string, 1, 10) as date),
substring(date_string, 1, 10)::date,
to_date(substring(date_string, 1, 10), 'YYYY-MM-DD')
from string_data
;


SELECT '15 minute'::interval,
 '2 hour'::interval,
 '1 day'::interval,
 '2 week'::interval,
 '3 month'::interval;

SELECT
	now(),
	now() - INTERVAL '1 year 3 hours 20 minutes' 
             AS "3 hours 20 minutes ago of last year";
            
select eh.salary,
to_char(eh.salary, '9,999,999'),
to_char(7777666555, '9,999,999,999 l'),
to_char(7777666555, '9G999G999G999 l')
from employees_hr eh ;

-------------------------------------

--- extract


select extract(day from now()),
	   extract(year from now()),
	   extract(DOY from now()),
	   extract(DECADE from now());
	  
select
sum(salary) as top, negyed
from (
select
eh.salary,
eh.hire_date,
extract(quarter from eh.hire_date) as negyed
from employees_hr eh ) as a
group by negyed
order by top desc
;

-- add_months - interval

select *  from employees_hr eh 
where now() - interval '30 year' > eh.hire_date;


select now() - interval '5 hour';

select *  from employees_hr eh 
where eh.hire_date between date'1995-01-01' and date'2000-12-31';


select to_date('2023-05', 'YYYY-MM')

-------------------------------------------------------------------------

select * from employee e ;
select * from departments d;
select * from hiring;
select * from positions p ;

------- SQL performancia --------------
/*
 * Az adatbázisnak amikor egy utasítást elküldesz 
 * a legtöbb esetben egy "becslést" készít az adatbázis a futással kapcsolatban
 * 
 * Query Plan - ez egy terv arra vonatkozóan, hogy miként fogja a complex utasítást
 * futtatni az adatbázis
 * 
 * Ez a terv leggyakrabban Cost Based Optimizer alapú
 * */


explain analyze select
sum(salary) as top, negyed
from (
select
eh.salary,
eh.hire_date,
extract(quarter from eh.hire_date) as negyed
from employees_hr eh ) as a
group by negyed
order by top desc
;

 explain analyze with base_data as (
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
select * from agg_data;


