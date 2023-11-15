## 1. Finding Unique Values with SELECT DISTINCT ##

SELECT DISTINCT order_id, customer_name
  FROM orders
 WHERE city = 'Buffalo' and state = 'New York';

## 2. Filtering for Categories with IN ##

SELECT DISTINCT ship_mode, state
  FROM orders
 WHERE state IN ('District of Columbia', 'North Dakota', 'Vermont', 'West Virginia');

## 3. Flipping the Script with NOT ##

SELECT order_id, city, state, sales
  FROM orders
 WHERE sales > 5000 AND state NOT IN ('California', 'Texas', 'New York');

## 4. Searching for Text Patterns with LIKE (Part 1) ##

SELECT DISTINCT subcategory, product_name
  FROM orders
 WHERE product_name LIKE '%keyboard%'

## 5. Searching for Text Patterns with LIKE (Part 2) ##

SELECT DISTINCT product_name
  FROM orders
 WHERE product_name LIKE 'Pr___ C_l____ %';

## 6. Parentheses for Multiple Criteria ##

SELECT product_name, subcategory, sales, profit
  FROM orders
 WHERE (sales > 5000 AND profit > 1000) 
        OR (profit < -10 AND sales < 10)