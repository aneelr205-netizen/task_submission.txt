CREATE DATABASE employee_db;

USE employee_db;

CREATE TABLE employees (
emp_id INT PRIMARY KEY,
name VARCHAR(50),
department VARCHAR (50),
salary FLOAT,
joining_date DATE
);

INSERT INTO employees VALUES 
(1, "Ram", "HR", 35000.95, "2022-02-08"),
(2, "Sham", "Finance", 53000.64, "2023-04-17"),
(3, "Ravi", "Marketing", 42000.35, "2021-08-16"),
(4, "Jaya", "IT", 47000.16, "2020-04-01"),
(5, "Jeshu", "Developer", 55000.99, "2022-11-05"),
(6, "Sneha", "HR", 60000.70, "2019-07-06");


SELECT name, ROUND(salary, 2) AS rounded_salary FROM employees;
SELECT name, CEIL(salary) AS ceil_salary FROM employees;
SELECT name, FLOOR(salary) AS floor_salary FROM employees;
SELECT name, MOD(salary, 1000) AS remainder FROM employees;
SELECT ABS(-4500) AS abs_value1;
SELECT ABS(-99) AS abs_value2;


SELECT CONCAT(name, " - ", department) AS employees_details FROM employees;
SELECT name, LENGTH(name) AS name_length FROM employees;
SELECT UPPER(name) AS uppercase_name FROM employees;
SELECT LOWER(name) AS lowercase_name FROM employees;
SELECT REPLACE(department, "HR", "Human Resources") AS updated_department FROM employees;
SELECT SUBSTRING(name, 1, 3) AS first_three_characters FROM employees;

SELECT CURDATE() AS currentdate;
SELECT CURTIME() AS currenttime;
SELECT NOW() AS current_datetime;
SELECT name, DATEDIFF(CURDATE(), joining_date) AS working_days FROM employees;


