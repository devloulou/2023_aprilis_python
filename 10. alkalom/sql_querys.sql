select * from employee;
select * from departments;
select * from positions;
select * from hiring;

/*
 * SQL utasítások fejlesztését
 * 
 *  a * karakter azt jelenti: minden mezőt
 * 
 * alias az sql-ben
 * mezőket is lehet aliasolni és táblát lehet aliasolni
 * */

select
--public.employee."name", public.employee.salary
e.name,
e.salary / 1000 as fezites
from public.employee e;

/*
 * szűrések - where feltétel
 * 
 * where feltétel mindig a from után van , 
 * 
 * or - vagy feltétel : ha bármelyik feltétel igaz, akkor visszatér az adatom
 * and - és feltétel: mindkét feltételnek igaznak kell lennie 
 * * */

select * from employee e
where (employee_id = 2 and name = 'Elon Musk')
		or employee_id > 4;

/*
 * group by - csoportosítás
 * aggregált függvényeket tudjunk használni
 * 
 * aggregált függvények:
 * count, min, max, avg, sum
 * 
 * ha van where feltétel, a group by mindig a where feltétel van
 * ha nincs, akkor from után
 * 
 * */

select
count(employee_id) as cnt_employee,
sum(salary),
min(salary),
max(salary),
avg(salary)
from employee e;

-- pozíciónként számoljuk meg, hogy hány ember dolgozik
-- 1 adott pozícióban

select count(h.employee_id) from hiring h;

select position_id, count(employee_id) from hiring
group by position_id;

-----------------------------------
/*
 * having - mindig a group by következik
 * 
 * */

select position_id, count(employee_id) from hiring
group by position_id
having count(employee_id) > 1;


/*
 * order by - sorba rendezés
 * 
 * az order by helye:
 *  ha van having, akkor utána
 *  ha nincs having, de van group by akkor utána
 *  ha nincs group by de van where feltétel, akkor utána
 *  ha semmilyen utasaítás nincs a from tábla után
 *  akkor a from után van
 * 
 * default rendezés: növekvő - asc - ascendaris
 * 
 * vagy növekvő - asc
 * vagy csökkenő rendezés - desc
 */

select * from employee e 
order by salary desc, hire_date desc;

/*
 * limit utasítás
 * 
 * */

select * from employee
order by employee_id desc
limit 4;
