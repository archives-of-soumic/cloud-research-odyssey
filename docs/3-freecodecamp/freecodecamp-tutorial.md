# Free Code Camp Postgresql Tutorial

## create table
```
CREATE TABLE person (
    ID BIGSERIAL NOT NULL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    LAST_NAME VARCHAR(50) NOT NULL,
    gender VARCHAR(5) NOT NULL,
    date_of_birth DATE NOT NULL
);
```

## output:
```
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
```
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
```
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
```
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
```
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
```
select * from person where
country_of_birth = 'China' OR
country_of_birth = 'France' OR
country_of_birth = 'Poland';
```

This is equivalent to:
```
select * from person where country_of_birth in ('China', 'France', 'Poland');
```
```
select * from person where country_of_birth in ('China', 'France', 'Poland') order by country_of_birth;
```
## Between
```
select * from person where date_of_birth between '2000-01-01' and '2020-01-01';
select first_name from person where date_of_birth between date '2018-01-01' and '2020-01-01';
```
## Like and iLike
Like is used for regular expression / pattern matching.
```
select * from person where email like '%.com';
select * from person where email like '%outlook.com';
select * from person where email like '%gmail.com';
select * from person where email like '%@gmail%';
```
Like is case sensitive. iLike is case insensitive.
```
select * from person where country_of_birth like 'p%'; <-- no result
select * from person where country_of_birth like 'P%'; <-- ok result
select * from person where country_of_birth ilike 'p%'; <-- ok result
```
## Group By
```
select distinct country_of_birth from person;
select distinct country_of_birth, count(*) from person group by country_of_birth order by country_of_birth;
```
## Group By Having
```
select distinct country_of_birth, count(*) from person group by country_of_birth having count(*)>5 order by country_of_birth;
```
## Adding new table and data with mockaroo