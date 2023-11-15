## 1. Understanding Data Types ##

SELECT sales, discount, profit
  FROM orders;

## 2. Table Information with PRAGMA ##

PRAGMA table_info(orders);

## 3. Operating on Numeric Columns ##

SELECT order_id, 
       sales, 
       profit,
       profit/sales AS profit_margin
  FROM orders
 LIMIT 8;

## 4. Integer Division ##

SELECT product_id, quantity, CAST(quantity AS REAL)/2 AS even_or_odd
  FROM orders
 LIMIT 5;

## 5. Functions on Fields: ROUND() ##

SELECT order_id,
       sales,
       quantity,
       ROUND(sales/quantity, 2) AS price_per_unit
  FROM orders
 LIMIT 10;

## 6. Functions on Fields: UPPER() and LOWER() ##

SELECT LOWER(customer_name) AS customer_name_lower
  FROM orders;

## 7. Concatenating Fields ##

SELECT order_id,
       region,
       state,
       "Superstore" || " " || city AS local_store
  FROM orders
 LIMIT 10;

## 8. Constant Values ##

SELECT *, 51000 AS salary
  FROM managers;

## 9. Challenge: Tying it All Together ##

SELECT city || ", " || state || " " || postal_code AS address,
       sales,
       ROUND(sales*0.07, 2) AS tax,
       4.99 AS shipping_cost,
       ROUND(sales + 4.99 + sales*0.07, 2) AS total_cost
  FROM orders
 LIMIT 10;