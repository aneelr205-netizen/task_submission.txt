USE company_db;

INSERT INTO employees VALUES
(8, "Viswa", 24, "Testing", 40000 ),
(9, "Arjun", 22, "Sales", 25000),
(10, "Sruthi", 28, "HR", 35000),
(11, "Amar", 30, "IT", 50000),
(12, "kamal", 26, "HR", 40000),
(13, "Lakshmi", 25, "Marketing", 38000);
 

 SELECT * FROM employees WHERE salary > 30000;
 SELECT * FROM employees WHERE age BETWEEN 22 AND 30;
 SELECT * FROM employees WHERE department IN ( 'HR','IT');
 SELECT * FROM employees WHERE department NOT IN ('Sales');
 
 SELECT * FROM employees WHERE name LIKE 'A%';
 SELECT * FROM employees WHERE name LIKE '%n';
 SELECT * FROM employees WHERE name LIKE '-----';
   
    SELECT * FROM employees ORDER BY salary ASC;
    SELECT * FROM employees ORDER BY age DESC; 
    SELECT * FROM employees  LIMIT 3;
    SELECT * FROM employees LIMIT 3 OFFSET 2;
   
   
 