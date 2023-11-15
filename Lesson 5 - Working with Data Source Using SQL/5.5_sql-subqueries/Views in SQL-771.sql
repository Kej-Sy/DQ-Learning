## 2. Creating and Querying Views ##

CREATE VIEW customer_email (
       customer_id, first_name, last_name, country, partial_email
  ) AS
SELECT customer_id, first_name,
       last_name, country,
       '****' || SUBSTRING(email, 5) AS email
  FROM customer;
  
SELECT *
  FROM customer_email
 LIMIT 3;

## 3. Destroying Views ##

CREATE VIEW manager AS
SELECT employee_id, first_name, last_name, title, email
  FROM employee
 WHERE employee_id IN (SELECT DISTINCT reports_to FROM employee);
 
 DROP VIEW manager;
 
SELECT *
  FROM manager;

## 4. Optional Column Names ##

CREATE VIEW german_customers AS
SELECT customer_id, first_name, last_name
  FROM customer
 WHERE country = 'Germany';
 
SELECT *
  FROM german_customers;

## 5. Creating Complex Views ##

CREATE VIEW genres_most_revenue (genre_name, quantity, revenue) AS
SELECT g.name, COUNT(i.quantity),
       ROUND(SUM(i.unit_price * i.quantity), 2) AS revenue
  FROM invoice_line AS i
  JOIN track as t
    ON i.track_id = t.track_id
  JOIN genre AS g
    ON t.genre_id = g.genre_id
 GROUP BY g.genre_id
HAVING ROUND(SUM(i.unit_price * i.quantity), 2) > 100
 ORDER BY revenue DESC;
 
SELECT *
  FROM genres_most_revenue;

## 6. Creating Views from Views ##

CREATE VIEW customer_purchase (genre_name, unit_price, quantity, customer_id) AS
SELECT g.name, il.unit_price, il.quantity, i.customer_id
  FROM genre AS g
  JOIN track AS t
    ON g.genre_id = t.genre_id
  JOIN invoice_line AS il
    ON t.track_id = il.track_id
  JOIN invoice AS i
    ON il.invoice_id = il.invoice_id;
    
CREATE VIEW total_sales_customers AS
SELECT genre_name, SUM(unit_price * quantity) AS total_amount,
       COUNT(customer_id) AS customer_count
  FROM customer_purchase
 GROUP BY genre_name;
 
SELECT *
  FROM total_sales_customers
 ORDER BY customer_count DESC;

## 7. Dropping Views with Dependencies ##

DROP VIEW customer_purchase CASCADE;

SELECT *
  FROM total_sales_customer;