CREATE DATABASE college_db;

USE college_db;

CREATE TABLE students (
student_id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(50) NOT NULL,
email VARCHAR(100) UNIQUE,
age INT CHECK (age >= 18),
department ENUM( "CSE", "ECE", "IT", "MECH"),
city VARCHAR(50) DEFAULT "Chennai"
);

CREATE TABLE courses (
course_id INT PRIMARY KEY,
course_name VARCHAR(50)
);

CREATE TABLE enrollments (
enrollment_id INT PRIMARY KEY,
student_id INT,
course_id INT,

FOREIGN KEY (student_id)
REFERENCES students(student_id),

FOREIGN KEY (course_id)
REFERENCES courses(course_id)
);

INSERT INTO students(name, email, age, department, city) VALUES
("Nivas", "nivas@gmail.com", 22, "CSE", "Kadapa"),
("Nisha", "Nisha@gmail.com", 20, "ECE", "Chennai"),
("Rahul", "Rahul@gmail.com", 21, "IT", "Hyderabad");

INSERT INTO courses(course_id, course_name) VALUES 
(101, "Python"),
(102, "Java"),
(103, "MySQL");

INSERT INTO emrollments(enrollment_id, student_id, course_id) VALUES
(1, 1,101),
(2, 2, 102),
(3, 3, 103);

INSERT INTO students(name, email, age, department) VALUES 
("kumar", "nivas@gmail.com", 22, "CSE");

INSERT INTO students(name, email, age, department) VALUES
(NULL, "test@gmail.com", 20, "IT");

INSERT INTO students(name, email, age, department) VALUES
("Ravi", "ravi@gmail.com", 20, "EEE");

INSERT INTO students(name, email, age, department) VALUES
("MIni", "mini@gmail.com", 16, "CSE");





