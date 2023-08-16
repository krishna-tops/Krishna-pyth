CREATE DATABASE ASSIGNMENTSQL ;
USE ASSIGNMENTSQL ;
CREATE TABLE EMP
(
 SR INT PRIMARY KEY AUTO_INCREMENT,
 JOB_ID INT,
 EMP_FNAME VARCHAR(40),
 EMP_LNAME VARCHAR(40),
 HIRE_DATE DATE,
 DEP VARCHAR(30),
 SALARY INT
) ;
/* Display all information in the tables EMP. */
SELECT *  FROM EMP ;
SELECT * FROM EMP ;
ALTER TABLE EMP ADD COLUMN ENAME VARCHAR(30) ;
INSERT INTO EMP (SR, JOB_ID, EMP_FNAME, EMP_LNAME, HIRE_DATE, DEP, SALARY) VALUES ('1','11',"RAJESH","ROSHAN",'2020-01-01',"ADMIN",'2000');
INSERT INTO EMP VALUES ('2','22',"ROCKEY","MAKWANA",'2020-03-05',"SALES",'2500');
SELECT EMP_FNAME,DEP FROM EMP  ; 

/* Display all information in the tables EMP and DEPT. */

SELECT HIRE_DATE,EMP_FNAME FROM EMP  ; 


/* Display the ename concatenated with the job ID, separated by a comma and space, and 
name the column Employee and Title  */

	
SELECT CONCAT(EMP_Fname, ' ', EMP_Lname) AS 'EMPLOYEE' ,HIRE_DATE AS  'Title'FROM EMP;



SELECT HIRE_DATE,EMP_FNAME,DEP FROM EMP ;
SELECT * FROM EMP ;

/*  Display the names and salaries of all employees with a salary greater than 2000. */

SELECT EMP_FNAME,SALARY FROM EMP WHERE SALARY > '2000' ;

/* Display the names and dates of employees with the column headers "Name" and "Start 
Date" */

SELECT CONCAT(EMP_Fname, ' ', EMP_Lname) AS 'Name', HIRE_DATE AS 'Start Date' FROM EMP;

/* Display the names and hire dates of all employees in the order they were hired. */

SELECT CONCAT(EMP_Fname, ' ', EMP_Lname) AS 'Name', SALARY FROM emp ORDER BY SALARY;

 /*  Display the names and salaries of all employees in reverse salary order.  */
 
SELECT CONCAT(EMP_Fname, ' ', EMP_Lname) AS 'Name', DEP FROM emp ORDER BY SALARY DESC;

/* Display 'ename" and "deptno" who are all earned commission and display salary in 
reverse order.  */

SELECT EMP_FNAME, DEP_NUM FROM EMP
WHERE COMISSION IS NOT NULL ;
  
/* Display the last name, job, and salary for all employees whose job is sales representative 
or stock clerk and whose salary is not equal to $2,500, $3,500, or $5,000 */


SELECT EMP_FNAME , DEP , SALARY 
FROM EMP 
WHERE DEP = 'CLERK'
AND SALARY NOT IN (2500,3500,5000);

/* Display the maximum, minimum and average salary and commission earned.*/



SELECT MIN(SALARY) AS MINIMUM_SALARY FROM EMP ;
SELECT MAX(SALARY) AS MINIMUM_SALARY FROM EMP ;
SELECT AVG(SALARY) AS MINIMUM_SALARY FROM EMP ;

USE ASSIGNMENTSQL;

/*  Display the department number, total salary payout and total commission payout for 
each department.  */

SELECT
    DEP_NUM,
    SUM(SALARY) AS TOTAL_SALAR_PAYOUT,
    SUM(COMISSION) AS TOTAL_COMMISSION_PAYOUT
FROM
    EMP
WHERE COMISSION IS NOT NULL
GROUP BY
    DEP_NUM ;
    
    -- OR 
 SELECT SUM(SALARY) , SUM(COMISSION) 
FROM EMP
GROUP BY DEP;   
    
    
    
    
    
    
    
    
    SELECT
    SUM(commission) AS total_commission_payout
FROM
    sales
WHERE
    commission IS NOT NULL;



SELECT DEP_NUM,SR,DEP FROM EMP ;
SELECT COUNT(SALARY), DEP
FROM EMP
GROUP BY SR;

SELECT SUM(SALARY), DEP
FROM EMP
GROUP BY DEP;


SELECT CONCAT(EMP_Fname, ' ', EMP_Lname) AS 'Name'
FROM EMP
WHERE COMISSION IS NULL 
;


/* Display the employee's name who doesn't earn a commission. Order the result set 
without using the column name */

SELECT CONCAT(EMP_Fname, ' ', EMP_Lname) AS 'Name', DEP_NUM AS Department_ID, 
	CASE 
	WHEN comission IS NULL THEN 'No commission'
	ELSE EMP.COMISSION 
	END AS Commission
FROM emP ;

SELECT CONCAT(EMP_Fname, ' ', EMP_Lname) AS 'Name', DEP_NUM AS Department_ID, 
	CASE 
	WHEN comission IS NULL THEN 'No commission'
	ELSE EMP.COMISSION * 2
	END AS Commission
FROM emP ;



SELECT CONCAT(EMP_Fname, ' ', EMP_Lname) AS 'Name', DEP_NUM AS Department_ID
FROM EMP
WHERE EXISTS (
  SELECT *
  FROM EMP 
  WHERE  EMP_FNAME= EMP_FNAME 
    
);



SELECT COUNT(EMP_FNAME), COUNT(DEP) ,DEP FROM EMP 
 GROUP BY DEP ;
 
 SELECT CONCAT(EMP_Fname, ' ', EMP_Lname) AS 'Name', DEP_NUM AS Department_ID
FROM EMP
WHERE EXISTS (
 SELECT COUNT(EMP_FNAME), COUNT(DEP) ,DEP FROM EMP 
 GROUP BY DEP 
);
 
 









