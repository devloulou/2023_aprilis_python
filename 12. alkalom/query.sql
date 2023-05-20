/*
 * window functions
 * 
 * analitikus függvények
 * 
 * */
-- ki a 3. legjobban fizetett ember
/*
 * analitikus függvények:
 * over(partition by mezo_nevek order by mezo_nevek)
 * */


select * from employees_hr eh ;
select * from departments_hr dh ;
select * from dependents_hr dh ;
select * from jobs_hr;
/*
 * departmentenként a 3. legnagyobb fizetés,
 * amennyiben van legalábbb 3 ember a departmentben, ha nincs,
 * akkor az elsőt add vissza
 * */
with base_data as (
	select
		row_number()over(partition by department_id order by salary desc) as row_num,
		rank()over(partition by department_id order by salary desc) as rnk_num,
		dense_rank()over(partition by department_id order by salary desc) as dns_rnk,
		--min(salary)over(partition by department_id order by salary asc) as min_sal,
		eh.salary,
		eh.employee_id,
		eh.first_name,
		eh.last_name,
		eh.job_id,
		eh.department_id,
		count(employee_id)over(partition by department_id) as cnt
	from employees_hr eh 
)
select
t.*
from base_data t
where (cnt < 3 and row_num = 1) or dns_rnk = 3


/*
select
t.*
from base_data t
where dns_rnk = 3
union all*/

-----------------------------------------------------
-- keresés like -al: csak a where feltételben lehet haszálni
select * from employees_hr eh 
where
--eh.phone_number like '515%'
--eh.phone_number like '%45%'
--eh.phone_number like '%45__'
eh.phone_number like '%12_%';

select * from employees_hr eh 
where eh.salary between 8000 and 22000;


select * from departments d ;
select * from employee e ;
select * from hiring;
select * from positions p ;

--------------------------------------------------------------------
select * from departments d 
left join positions p on d.department_id  = p.department_id 
where p.department_id is null;

--------- subselect - nested query
--- where és select from között KERÜLJÉTEK A BEÁGYAZOTT SELECTEKET, ha tudjátok
select * from departments d 
where d.department_id not in (select p.department_id from positions p);

--------------------------
select * from hiring h;

select
(select e."name" from employee e where h.employee_id = e.employee_id),
(select p.position_name from positions p where h.position_id = p.position_id)
from hiring h;


select e.name, p.position_name  from hiring h
inner join employee e on h.employee_id = e.employee_id 
inner join positions p on h.position_id = p.position_id;


----exists használata - az exists egy true false értéket ad vissza
select * from departments d 
where not exists
			(select 1 from positions p
					where d.department_id = p.department_id);

/*
 * 1. join-ok
 * 2. exists - bizonyos adatbázisok nem jó performanciával futtatják az exists-et
 * 3. subquery - ezt ha tudjuk kerüljük
 * */
