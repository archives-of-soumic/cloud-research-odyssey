# Free Code Camp Postgresql Tutorial

## create table
```sql
CREATE TABLE person (
    ID BIGSERIAL NOT NULL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    LAST_NAME VARCHAR(50) NOT NULL,
    gender VARCHAR(5) NOT NULL,
    date_of_birth DATE NOT NULL
);
```

## output:
```sql
                                       Table "public.person"
    Column     |         Type          | Collation | Nullable |              Default               
---------------+-----------------------+-----------+----------+------------------------------------
 id            | bigint                |           | not null | nextval('person_id_seq'::regclass)
 first_name    | character varying(50) |           | not null | 
 last_name     | character varying(50) |           | not null | 
 gender        | character varying(5)  |           | not null | 
 date_of_birth | date                  |           | not null | 
Indexes:
    "person_pkey" PRIMARY KEY, btree (id)
```

## Insert
```sql
INSERT INTO person 
(first_name, last_name, gender, date_of_birth)
VALUES ('Anne', 'Smith', 'FEMALE', DATE '1998-01-09');
```

```alter table person add email varchar(50);```

```
INSERT INTO person 
(first_name, last_name, gender, date_of_birth, email)
VALUES ('Cole', 'Anderson', 'FEMALE', DATE '1998-01-09', 'coleanderson@outlook.com');
```

## Bulk insert from a file
Go to https://mockaroo.com/ for some dummy data. Download it as sql file. I kept it in the project directory under a folder ignored by git, so you won't see it. Use it to bulk insert data into our table.

```
admindb=# \i /home/soumic/Codes/cloud-research-odyssey/files-n-datasets/person.sql
```

## Select from
```
select * from person;
select first_name from person;
select first_name, last_name from person;
```

## Order by
`select * from person order by country_of_birth;`
OR `select * from person order by country_of_birth ASC;` 
they both give the same result.

`select * from person order by country_of_birth DESC;` gives result in reverse order.
`select * from person order by id DESC;`
`select * from person order by date_of_birth DESC;`
`select country_of_birth from person order by date_of_birth DESC;`

## Distinct
`select distinct country_of_birth from person order by country_of_birth DESC;`

## WHERE clause and AND
```
select * from person where gender = 'Female';
select * from person where gender = 'Male' AND country_of_birth = 'Poland';
select * from person where gender = 'Male' AND (country_of_birth = 'Poland' OR country_of_birth = 'China');
```

## Comparison Operator
```sql
select 1 = 1; # output: t
select 1 = 2; # output: f
select 1 <= 2; # t
select 1 <> 2; # t
select 1 <> 1; # f
... ...
```
Here in sql <> is the != operator.

## Limit, Offset and Fetch
Limit restricts the number of rows:
```select * from person limit 10;```
Output:
```sql
admindb=# select * from person limit 10;
 id | first_name | last_name  | date_of_birth | gender |            email             | country_of_birth 
----+------------+------------+---------------+--------+------------------------------+------------------
  1 | Anne       | Smith      | 1998-01-09    | FEMALE |                              | 
  2 | Cole       | Anderson   | 1998-01-09    | FEMALE | coleanderson@outlook.com     | 
  3 | Wren       | Mackie     | 2020-04-04    | Female | wmackie2@ebay.co.uk          | China
  4 | Griff      | Quincey    | 2020-04-02    | Male   | gquincey3@yolasite.com       | Norway
  5 | Curr       | Whitchurch | 2019-10-25    | Male   | cwhitchurch4@istockphoto.com | United States
  6 | Rosaleen   | O Sullivan | 2020-07-22    | Female | rosullivan5@meetup.com       | Indonesia
  7 | Giovanni   | Oury       | 2019-11-20    | Male   | goury6@elegantthemes.com     | Russia
  8 | Kaiser     | Potts      | 2019-09-04    | Male   |                              | Germany
  9 | Sidonia    | Ginnell    | 2020-02-29    | Female |                              | Jamaica
 10 | Glenna     | Greenrodd  | 2019-10-07    | Female |                              | China
(10 rows)
```

Offset allows us to start after a certain row:
``` select * from person offset 5 limit 5;```
Output:
```sql
 id | first_name | last_name  | date_of_birth | gender |          email           | country_of_birth 
----+------------+------------+---------------+--------+--------------------------+------------------
  6 | Rosaleen   | O Sullivan | 2020-07-22    | Female | rosullivan5@meetup.com   | Indonesia
  7 | Giovanni   | Oury       | 2019-11-20    | Male   | goury6@elegantthemes.com | Russia
  8 | Kaiser     | Potts      | 2019-09-04    | Male   |                          | Germany
  9 | Sidonia    | Ginnell    | 2020-02-29    | Female |                          | Jamaica
 10 | Glenna     | Greenrodd  | 2019-10-07    | Female |                          | China
(5 rows)
```

Fetch is an alternative to limit:
`select * from person offset 5 fetch first 5 row only;`
`select * from person offset 5 fetch first 1 row only;` OR `select * from person offset 5 fetch first row only;`
***Fetch is sql standard.***

## IN
```sql
select * from person where
country_of_birth = 'China' OR
country_of_birth = 'France' OR
country_of_birth = 'Poland';
```

This is equivalent to:
```sql
select * from person where country_of_birth in ('China', 'France', 'Poland');
```
```sql
select * from person where country_of_birth in ('China', 'France', 'Poland') order by country_of_birth;
```
## Between
```sql
select * from person where date_of_birth between '2000-01-01' and '2020-01-01';
select first_name from person where date_of_birth between date '2018-01-01' and '2020-01-01';
```
## Like and iLike
Like is used for regular expression / pattern matching.
```sql
select * from person where email like '%.com';
select * from person where email like '%outlook.com';
select * from person where email like '%gmail.com';
select * from person where email like '%@gmail%';
```
Like is case sensitive. iLike is case insensitive.
```sql
select * from person where country_of_birth like 'p%'; <-- no result
select * from person where country_of_birth like 'P%'; <-- ok result
select * from person where country_of_birth ilike 'p%'; <-- ok result
```
## Group By
```sql
select distinct country_of_birth from person;
select distinct country_of_birth, count(*) from person group by country_of_birth order by country_of_birth;
```
## Group By Having
```sql
select distinct country_of_birth, count(*) from person group by country_of_birth having count(*)>5 order by country_of_birth;
```
## Adding New Table and Data with Mockaroo
Go to mockaroo website, create a table for cars.
Then,
```bash
admindb=# \i /home/soumic/Codes/cloud-research-odyssey/files-n-datasets/car.sql
```

## Min, Max, Average
```sql
SELECT MAX(price) FROM car;
SELECT MIN(price) FROM car;
SELECT AVG(price) FROM car;
SELECT ROUND(AVG(price)) FROM car;
```

We can use it with other commands:
```sql
SELECT make, model, MIN(price) FROM car GROUP BY make, model; 

SELECT make, MAX(price) FROM car GROUP BY make; 

SELECT make, model, AVG(price) FROM car GROUP BY make, model; 

SELECT make, model, ROUND(AVG(price)) FROM car GROUP BY make, model; 
```

## Sum

```sql
SELECT SUM(price) FROM car; 
SELECT make, SUM(price) FROM car GROUP BY make; 

```

## Basic Arithmetic Operations
```sql
select 10 + 2;
select 1 - 2;
select 10 * 2 + 6 / 2 - 1;
select 10 ^ 2;
select 5!;
select 10 % 3;
```

Question: Say, we want to sell the cars at 10% discount. So we have to display a new column showing discount.

```SELECT * FROM CAR; == SELECT id, make, model, price FROM car; ``` these both give the same results.

```sql
SELECT id, make, model, price, price * 0.10 FROM car;
SELECT id, make, model, price, ROUND(price * 0.10) FROM car;
SELECT id, make, model, price, ROUND(price * 0.10, 2) FROM car;
SELECT id, make, model, price, ROUND(price * 0.10, 2), ROUND(price * 0.90, 2) FROM car;
```

## Alias
```sql
SELECT id, make, model, price as original_price, ROUND(price * 0.10, 2) as ten_percent, ROUND(price * 0.90, 2) as discount_after_10_percent FROM car;
```

## Coalesce
Coalesce means try the 1st non-null value from list.
```sql
select coalesce(1);
select coalesce(null, 1);
select coalesce(null, null, 1);
select coalesce(null, null, 1, 10) as number;
```

```bash
admindb=# select coalesce(null, null, 1, 10);
 coalesce 
----------
        1
(1 row)

admindb=# select coalesce(null, null, 1, 10) as number;
 number 
--------
      1
(1 row)
```

Person table has some emails null. so we can replace the null with 'email not provided'  or some default value.
```sql
select email from person;
select coalesce(email, 'email not provided') from person;
```

## NULLIF
```sql
admindb=# select 10 / 0;
ERROR:  division by zero
```
nullif is used to handle these kind of stuffs. nullif takes 2 arguments. it kinda works like this:
```sql
fun NULLIF(arg1, arg2)
    if arg1 == arg2
        return null;
    else return arg1;
```

If we do any thing with null, the result is null:

```sql
admindb=# select 10 / null;
 ?column? 
----------
         
(1 row)

admindb=# 
```
So we want to remove the exception and return a null instead. So we can do this:
```sql
select 10 / NULLIF(0,0);
```
This will not crash, and return null. Now we can use a coalesce to replace null with some default value (say 0):
```sql
select coalesce( 10 / NULLIF(0,0) , 0 );
== select coalesce( null , 0 );
== 0
```

Output:
```sql
admindb=# select coalesce( 10 / NULLIF(0,0) , 0 );
 coalesce 
----------
        0
(1 row)

admindb=# ^C
```

## Timestamps and Dates
```sql
admindb=# SELECT NOW();
             now              
------------------------------
 2020-08-14 20:18:30.57867+06
(1 row)

admindb=# ^C
```
Casr time to date:
```sql
admindb=# SELECT NOW()::DATE;
    now     
------------
 2020-08-14
(1 row)

admindb=# 
```
Cast to time:
```sql
admindb=# SELECT NOW()::Time;
       now       
-----------------
 20:21:05.541056
(1 row)
```

Substract 1 year from now:
```sql
admindb=# select NOW() - Interval '1 year';
           ?column?            
-------------------------------
 2019-08-14 20:22:31.332229+06
(1 row)

admindb=# select NOW() - Interval '10 month';
           ?column?            
-------------------------------
 2019-10-14 20:23:25.450441+06
(1 row)

admindb=# select NOW() - Interval '10 year';
           ?column?            
-------------------------------
 2010-08-14 20:23:15.151256+06
(1 row)
admindb=# select NOW() - Interval '10 day';
admindb=# select NOW() + Interval '10 day';
admindb=# select (NOW() + Interval '10 day')::DATE;
```

## Extracting Fields
select Now(); this gives all the time.
Say, we want to extract only the year part. We can do it like this way:
```sql
SELECT EXTRACT(YEAR FROM NOW());
SELECT EXTRACT(MONTH FROM NOW());
SELECT EXTRACT(DAY FROM NOW());
SELECT EXTRACT(Century FROM NOW());
```

## Age Function
AGE(NOW(), date_of_birth)
```sql
SELECT first_name, last_name, date_of_birth, country_of_birth FROM person;
SELECT first_name, last_name, country_of_birth, date_of_birth, AGE(NOW(),date_of_birth) AS age FROM person;
SELECT first_name, last_name, country_of_birth, date_of_birth, Extract(YEAR FROM AGE(NOW(),date_of_birth) )  AS age FROM person;
```

## Primary Key
todo: google how to change primary key constraints(id to email etc...)
```Alter table person add primary key (id);```
```Delete from person where id = 2;```

## Unique Constraint
```sql
SELECT email , count(*) from person group by email having count(*) > 1;
```
To make some columns unique in an existing table:
```sql
ALTER TABLE person ADD CONSTRAINT unique_email_address UNIQUE(email);
```
OR,
```sql
ALTER TABLE person ADD UNIQUE(email);   //<-- much better in my opinion
```

To drop the constraint:
```sql
ALTER TABLE person DROP CONSTRAINT unique_email_address;
```
## Distinct
```sql
admindb=# select distinct gender from person;
 gender 
--------
 Male
 Female
 FEMALE
(3 rows)
```
## Check Constraints
```sql
Alter table person add constraint gender_constraint check (gender = 'Female' OR gender = 'Male');
```

## Delete records
```sql
DELETE from person; // deletes all 1000 rows
```
```sql
DELETE from person where gender = 'FEMALE' and country_of_birth = 'England';
```

## Update Records
```sql
UPDATE person SET email = 'coleanderson1@outlook.com' WHERE id = 10;
```

## On Conflict Do Nothing
```sql
insert into person (id, first_name, last_name, email, gender, country_of_birth, date_of_birth) values (1, 'Marleah', 'McInulty', null, 'Female', 'China', '9/10/2019')
ON CONFLICT DO NOTHING;

insert into person (id, first_name, last_name, email, gender, country_of_birth, date_of_birth) values (1, 'Marleah', 'McInulty', null, 'Female', 'China', '9/10/2019')
ON CONFLICT(id) DO NOTHING;

insert into person (id, first_name, last_name, email, gender, country_of_birth, date_of_birth) values (1013, 'Marleah', 'McInulty', 'coleanderson@outlook.com', 'Female', 'China', '9/10/2019')
ON CONFLICT(email) DO NOTHING;
```

but 
insert into person (id, first_name, last_name, email, gender, country_of_birth, date_of_birth) values (1, 'Marleah', 'McInulty', null, 'Female', 'China', '9/10/2019')
ON CONFLICT(id, email) DO NOTHING; <-- this gives error

## Upsert
Sometimes, say in a distributed system, you may want to update on conflict. For those cases, we use upsert.

```sql
insert into person (id, first_name, last_name, email, gender, country_of_birth, date_of_birth) 
values (1014, 'Marleah', 'McInulty', 'coleanderson@outlook.com.bd', 'Female', 'China', '9/10/2019')
ON CONFLICT(id) DO UPDATE SET email = EXCLUDED.email;   <-- this line is important
```
We can update multiple / all other fields like this way:
```sql
insert into person (id, first_name, last_name, email, gender, country_of_birth, date_of_birth) 
values (1014, 'Marleah', 'Anderson', 'coleanderson@outlook.com.uk', 'Female', 'China', '9/10/2019')
ON CONFLICT(id) DO UPDATE SET 
email = EXCLUDED.email,
last_name = EXCLUDED.last_name;
```

## Foreign Keys, Joins & Relationships

## Adding Relationships Between Tables
drop table person;
drop table car;
\i /home/soumic/Codes/cloud-research-odyssey/files-n-datasets/car_person_dataset.sql
(***NOTE*** I think the data set that I found has some errors).

car_person_dataset.sql:
```sql
create table car (
	id BIGSERIAL NOT NULL PRIMARY KEY,
	make VARCHAR(100) NOT NULL,
	model VARCHAR(100) NOT NULL,
	price NUMERIC(19, 2) NOT NULL
);


CREATE TABLE person (
	id BIGSERIAL NOT NULL PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	gender VARCHAR(6) NOT NULL,
	date_of_birth TIMESTAMP NOT NULL,
	email VARCHAR(150),
	country_of_birth VARCHAR(50),
    car_id BIGINT REFERENCES  car(id),
    UNIQUE(car_id)
);
```
```sql
Update person set car_id = 2 where id = 1;
```

## Inner Joins
```sql
admindb=# SELECT * FROM person JOIN car ON person.car_id = car.id;


 id | first_name | last_name | gender |    date_of_birth    |             email             | country_of_birth | car_id | id |   make   |  model  |  price   
----+------------+-----------+--------+---------------------+-------------------------------+------------------+--------+----+----------+---------+----------
  1 | Miguel     | Wetherell | Male   | 1985-07-21 00:00:00 | mwetherell0@wp.com            | Norway           |      1 |  1 | Plymouth | Horizon | 45195.78
  3 | Ettore     | Pitt      | Male   | 1985-11-20 00:00:00 | epitt2@seattletimes.com       | Guatemala        |      3 |  3 | Suzuki   | Vitara  | 88945.57
  4 | Lynde      | Gresswell | Female | 1981-11-13 00:00:00 | lgresswell3@deliciousdays.com | Kuwait           |      4 |  4 | Ford     | Ranger  | 15626.18
  5 | Faunie     | Volker    | Female | 1992-12-21 00:00:00 |                               | China            |      5 |  5 | Ford     | Ranger  | 94639.10
(4 rows)

admindb=# 

```
***Note*** Donot use WHERE as it gives error, use ON. (I thought where worked. maybe it worked in oracle. meh))

sometimes, it is hard to read data in this way. so we can use `\x` command to toogle between 
`expanded display on/off` make it vertical and thus making it a bit easier to read.

```sql
SELECT person.first_name , car.make, car.model, car.price 
FROM person JOIN car ON person.car_id = car.id;
```

## Left Joins
```sql
admindb=# SELECT * FROM person LEFT JOIN car ON person.car_id = car.id;
```
output:
```sql
 id | first_name | last_name | gender |    date_of_birth    |             email             | country_of_birth | car_id | id |   make   |  model  |  price   
----+------------+-----------+--------+---------------------+-------------------------------+------------------+--------+----+----------+---------+----------
  1 | Miguel     | Wetherell | Male   | 1985-07-21 00:00:00 | mwetherell0@wp.com            | Norway           |      1 |  1 | Plymouth | Horizon | 45195.78
  3 | Ettore     | Pitt      | Male   | 1985-11-20 00:00:00 | epitt2@seattletimes.com       | Guatemala        |      3 |  3 | Suzuki   | Vitara  | 88945.57
  4 | Lynde      | Gresswell | Female | 1981-11-13 00:00:00 | lgresswell3@deliciousdays.com | Kuwait           |      4 |  4 | Ford     | Ranger  | 15626.18
  5 | Faunie     | Volker    | Female | 1992-12-21 00:00:00 |                               | China            |      5 |  5 | Ford     | Ranger  | 94639.10
  7 | Jack       | Gegay     | Male   | 1984-08-27 00:00:00 | jgegay6@merriam-webster.com   | China            |        |    |          |         |         
  6 | Clary      | Armsby    | Female | 1992-04-09 00:00:00 | carmsby5@edublogs.org         | Czech Republic   |        |    |          |         |         
  2 | Elga       | Balmer    | Female | 1991-07-20 00:00:00 | ebalmer1@tripod.com           | Brazil           |        |    |          |         |         
(7 rows)
```

```sql
admindb=# SELECT * FROM person LEFT JOIN car ON person.car_id = car.id where car.* IS NULL;
admindb=# SELECT * FROM person LEFT JOIN car ON person.car_id = car.id where car.id IS NULL;
admindb=# SELECT * FROM person LEFT JOIN car ON person.car_id = car.id where person.car_id IS NULL;

output:

 id | first_name | last_name | gender |    date_of_birth    |            email            | country_of_birth | car_id | id | make | model | price 
----+------------+-----------+--------+---------------------+-----------------------------+------------------+--------+----+------+-------+-------
  2 | Elga       | Balmer    | Female | 1991-07-20 00:00:00 | ebalmer1@tripod.com         | Brazil           |        |    |      |       |      
  6 | Clary      | Armsby    | Female | 1992-04-09 00:00:00 | carmsby5@edublogs.org       | Czech Republic   |        |    |      |       |      
  7 | Jack       | Gegay     | Male   | 1984-08-27 00:00:00 | jgegay6@merriam-webster.com | China            |        |    |      |       |      
(3 rows)
```
***NOTE*** Use `IS` Not `=` such as `car.id IS NULL;`

## Deleting Records with Foreign Keys
```sql
 id | first_name | last_name | gender |    date_of_birth    |             email             | country_of_birth | car_id | id |   make   |  model  |  price   
----+------------+-----------+--------+---------------------+-------------------------------+------------------+--------+----+----------+---------+----------
  1 | Miguel     | Wetherell | Male   | 1985-07-21 00:00:00 | mwetherell0@wp.com            | Norway           |      1 |  1 | Plymouth | Horizon | 45195.78
```

We cannot delete this car 1 cz it has a relation with person.id = 1;
So either: 1. change person.car_id for person 1, then delete car 1.
Or 2. first delete person 1, then delete car 1;

*** Note *** cascade delete is a bad practice. One should manually handle seperately for each record. Otherwise
you could delete vital data.

## Exporting results to CSV
``` admindb=#  SELECT * FROM person LEFT JOIN car ON person.car_id = car.id; ```
Let we want to export this into a csv file.

```sql
\copy (SELECT * FROM person LEFT JOIN car ON person.car_id = car.id) TO '/home/soumic/Codes/cloud-research-odyssey/files-n-datasets/output.csv' DELIMITER ',' CSV HEADER;
```

## Serial and Sequences

## Extensions

## UUID