CREATE DATABASE employees_db;

USE employees_db;

CREATE TABLE sales (
product_id INT PRIMARY KEY,
product_name VARCHAR(50),
category VARCHAR(50),
quantity INT,
price DECIMAL(10,2)
);

INSERT INTO sales VALUES
(1, "Laptop", "Electronics", 5, 60000),
(2, "Mouse", "Electronics", 15, 500),
(3, "Keyboard", "Electronics", 10, 1200),
(4, "Shampoo", "Cosmetics", 20, 250),
(5, "Soap", "Cosmetics", 30, 60),
(6, "Ricebag", "Groceries", 18, 1500),
(7, "Oil", "Groceries", 12, 180),
(8, "Book", "Stationary", 25, 40),
(9, "Pen", "Stationary", 50, 10),
(10, "Water Bottle", "Accessories", 8, 300);

SELECT SUM(quantity) AS total_quantity_sold FROM sales;
SELECT AVG(price) AS average_price FROM sales;
SELECT MAX(price) AS highest_price FROM sales;
SELECT MIN(price) AS lowest_price FROM sales;
SELECT COUNT(*) AS total_products FROM sales;
SELECT category, SUM(quantity) AS total_quantity FROM sales GROUP BY category;
SELECT category, SUM(quantity) AS total_quantity FROM sales GROUP BY category HAVING SUM(quantity) > 10;



