## 1. Basic Comparison Operators ##

SELECT order_id, product_name, sales, discount, profit
  FROM orders
 WHERE profit<-1000;

## 2. Order of Execution ##

SELECT order_id, subcategory, product_name, sales/quantity AS price_per_unit
  FROM orders
 WHERE sales/quantity < 0.50;

## 4. Checking for Membership in a Consecutive Range ##

SELECT order_id, product_id, sales*0.1 as sales_tax
  FROM orders
 WHERE sales*0.1 BETWEEN 1 AND 2;

## 5. Checking for Membership in a Non-Consecutive Range ##

SELECT order_id, product_name, sales, quantity
  FROM orders
 WHERE sales in (3, 14, 15);

## 6. Checking for Missing Values ##

SELECT *
  FROM orders
 WHERE segment IS NULL
 
 --Nat Gilpin is the only customer with missing segment information.

## 7. AND Statements ##

SELECT product_name, sales/quantity AS price_per_unit
  FROM orders
 WHERE subcategory = 'Storage'
   AND sales/quantity > 300;

## 8. OR Statements ##

SELECT product_name, profit, quantity
  FROM orders
 WHERE profit < -100 OR quantity = 1;