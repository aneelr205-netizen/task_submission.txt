CREATE DATABASE employees_db; 

USE employees_db;

CREATE TABLE employees (
emp_id INT PRIMARY KEY,
emp_name VARCHAR(50),
department VARCHAR(50),
salary DECIMAL(10,2),
city VARCHAR(50)
);

INSERT INTO  employees VALUES
(1, "Manisha", "HR", 25000, "Chennai"),
(2, "Swathi", "IT", 45000, "Banglore"),
(3, "khan", "Finance", 32000, "Hyderabad"),
(4, "Meena", "HR", 28000, "Mumbai"),
(5, "Suresh", "IT", 55000, "Delhi"),
(6, "Divya", "Marketing", 27000, "Pune"),
(7, "Arun", "Finance", 38000, "Chennai"),
(8, "Priya", "IT", 60000, "Banglore"),
(9, "Rahul", "Marketing", 28000, "Kolkata"),
(10, "Sneha", "HR", 35000, "Hyderabad");

CREATE VIEW employee_view AS SELECT emp_id, emp_name, department FROM employees;
SELECT * FROM employee_view;

UPDATE employees SET department = "Admin" WHERE emp_id = 1;
SELECT * FROM employee_view;

CREATE VIEW high_salary_view AS SELECT emp_id, emp_name, salary FROM employees WHERE salary > 30000;
SELECT * FROM high_salary_view;

DROP VIEW employee_view;
DROP VIEW high_salary_view;




