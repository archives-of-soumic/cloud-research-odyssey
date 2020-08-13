INSERT INTO playground (type, color, location, install_date) 
VALUES ('slide','blue', 'south','2020-08-13');

INSERT INTO playground (type, color, location, install_date) 
VALUES ('swing', 'yellow', 'north', '2018-08-16');

SELECT * FROM PLAYGROUND;

SELECT * FROM PLAYGROUND WHERE ID = 1;

ALTER TABLE playground ADD last_maint DATE;

ALTER TABLE PLAYGROUND DROP last_maint;

UPDATE playground SET color = 'red' 
WHERE type = 'swing';