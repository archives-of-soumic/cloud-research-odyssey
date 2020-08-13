# Basic Commands
## Creating and Deleting Tables
Basic command:
```
CREATE TABLE table_name (
    column_name1 col_type (field_length) column_constraints,
    column_name2 col_type (field_length),
    column_name3 col_type (field_length)
);
```
So for example:
```
CREATE TABLE playground (
    id serial PRIMARY KEY,
    type varchar (50) NOT NULL,
    color varchar (25) NOT NULL,
    location varchar(25) check (location in ('north', 'south', 'east', 'west')),
    install_date date
);
```

We can see out table by typing:

```
admindb=# \d
```
![create a table](create-a-table.png)

##  Adding, Querying, and Deleting Data in a Table
* Adding
```
INSERT INTO playground (type, color, location, install_date) 
VALUES ('slide','blue', 'south','2020-08-13');

INSERT INTO playground (type, color, location, install_date) 
VALUES ('swing', 'yellow', 'north', '2018-08-16');
```
* Quering:
We can see these values such as:
```
SELECT * FROM PLAYGROUND;
SELECT * FROM PLAYGROUND WHERE ID = 1;
```
* Adding and Deleting Columns from a Table
```
ALTER TABLE playground ADD last_maint DATE;
```
sO NOW THE TABLE LOOKS LIKE THIS:
```
admindb=# SELECT * FROM PLAYGROUND;
 id | type  | color  | location | install_date | last_maint 
----+-------+--------+----------+--------------+------------
  1 | slide | blue   | south    | 2020-08-13   | 
  3 | swing | yellow | north    | 2018-08-16   | 
(2 rows)
```

```
ALTER TABLE PLAYGROUND DROP last_maint;
```

* Updating Data in a Table
```
UPDATE playground SET color = 'red' 
WHERE type = 'swing';
```

![update a value](update-a-value.png)