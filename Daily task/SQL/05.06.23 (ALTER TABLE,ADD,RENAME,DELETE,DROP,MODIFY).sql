USE NAMEES ;
CREATE TABLE AHMEDABAD2 SELECT * FROM AHMEDABAD ;

SELECT * FROM AHMEDABAD2;

SELECT * FROM AHMEDABAD2
LIMIT 3;

SELECT DISTINCT CITYNAME FROM AHMEDABAD2 ;

ALTER TABLE AHMEDABAD2
MODIFY COLUMN CITYNAME TEXT;

ALTER TABLE AHMEDABAD2
ADD COLUMN AREA INT ;

ALTER TABLE AHMEDABAD2
DROP COLUMN STATENAME ;

ALTER TABLE AHMEDABAD2
RENAME COLUMN CITYNAME TO CITY ;

ALTER TABLE AHMEDABAD2
ADD COLUMN STATENAME INT ;

