CREATE DATABASE college_db;

USE college_db;

CREATE TABLE departments (
department_id INT PRIMARY KEY,
department_name VARCHAR(50)
);

CREATE TABLE students (
student_id INT PRIMARY KEY,
student_name VARCHAR(50),
department_id INT,
FOREIGN KEY (department_id)
REFERENCES departments(department_id)
);

INSERT INTO departments VALUES 
(101, "Computer Science"),
(102, "Mechanical"),
(103, "Electronics"),
(104, "Civil"),
(105, "Mathematics");

INSERT INTO students VALUES
(1, "nithin", 101),
(2, "Priya", 102),
(3, "Kyra", 103),
(4, "Kanth", 101),
(5, "Supriya", NULL);


SELECT s.student_name, d.department_name FROM students s INNER JOIN departments d ON s.department_id = d.department_id;
SELECT s.student_name, d.department_name FROM students s LEFT OUTER JOIN departments d ON s.department_id = d.department_id;
SELECT s.student_name, d.department_name FROM students s RIGHT OUTER JOIN departments d ON s.department_id = d.department_id;
SELECT s.student_name, d.department_name FROM students s LEFT JOIN departments d ON s.department_id = d.department_id
UNION
SELECT s.student_name, d.department_name FROM students s RIGHT JOIN departments d ON s.department_id = d.department_id;
SELECT s.student_name, d.department_name FROM students s CROSS JOIN departments d;








