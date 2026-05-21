CREATE DATABASE students_db;

USE students_db;

CREATE TABLE students (
students_id INT PRIMARY KEY,
student_name VARCHAR(50),
department VARCHAR(20),
marks INT
);


INSERT INTO students VALUES
(1, "Anil", "CSE", 85),
(2, "Ram", "ECE", 78),
(3, "Sita", "MECH", 90),
(4, "Ravi", "CSE", 72),
(5, "Priya", "ECE", 88),
(6, "Arjun", "EEE", 67),
(7, "Nikhil", "CSE", 95),
(8, "Rahul", "ECE", 81),
(9, "Divya", "MECH", 76),
(10, "Manoj", "EEE", 89);

SELECT * FROM students WHERE marks > (SELECT AVG(marks) FROM students);
SELECT * FROM students WHERE marks = ANY ( SELECT marks FROM students WHERE department = "ECE");	
SELECT * FROM students WHERE marks > ALL ( SELECT marks FROM students WHERE department = "CSE");
SELECT * FROM students WHERE department IN ( SELECT department FROM students WHERE marks > 80);
SELECT * FROM students s1 WHERE marks = (SELECT MAX(marks) FROM students s2 WHERE s1.department = s2.department);
 

 

    