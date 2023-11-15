## 1. Introduction ##

SELECT order_id, product_name, sales, quantity,
       CASE 
       WHEN sales BETWEEN 0 AND 50 THEN 'small sale'
       WHEN sales BETWEEN 51 AND 100 THEN 'medium sale'
       ELSE 'large sale'
       END AS sales_amount                        
  FROM orders
 WHERE order_id LIKE 'CA%'
 ORDER BY quantity
 LIMIT 3;

## 2. Reading From a Table ##

SELECT *
FROM orders
LIMIT 5;

## 3. Different SQL Dialects ##

SELECT *
    FROM returns
 LIMIT 4;

## 4. SELECT Rows and Fields ##

SELECT order_date, order_id, product_name, sales, quantity
    FROM orders
 LIMIT 5;
 

## 5. Defining Relational Databases ##

SELECT city, state, region
  FROM orders
 LIMIT 10;

## 6. Aliasing Results ##

SELECT city AS "City",
       state AS "State",
       postal_code AS "ZIP Code"
  FROM orders
 LIMIT 10;

## 7. Hello, Comments! ##

-- This query shows city, state, postal code, and country information.
SELECT city, state, postal_code, country
  FROM orders
 LIMIT 4;
 
/*SELECT country, state, postal_code, city
   FROM orders
  LIMIT 4;*/