-- FIRST START USE WEEK3 DATABASE
USE WEEK3 ;
-- THEN TABLE
SELECT * FROM RECORDES3 ;
SELECT * FROM RECORDES3 WHERE F_CITY = "MUMB" OR F_AGE = 30 ;
SELECT * FROM RECORDES3 WHERE NOT F_CITY = "BOSTAN"; 

SELECT * FROM RECORDES3 ORDER BY F_CITY DESC ;

SELECT F_AGE FROM RECORDES3 ORDER BY F_NAME ASC ;

SELECT * FROM RECORDES3 ORDER BY F_ID DESC , F_AGE ASC ;

SELECT MIN(F_ID)AS MINIMUM_ID FROM RECORDES3  ;

SELECT MIN(F_AGE)AS MINIMUM_AGE FROM RECORDES3 ;

SELECT MAX(F_ID)AS MAXIMUM_ID FROM RECORDES3 ;

SELECT MAX(F_AGE)AS MAXIMUM_AGE FROM RECORDES3 ;

SELECT AVG(F_AGE)AS AVERAGE_AGE FROM RECORDES3 ;

SELECT SUM(F_AGE)AS COUNT_AGE FROM RECORDES3 ;




