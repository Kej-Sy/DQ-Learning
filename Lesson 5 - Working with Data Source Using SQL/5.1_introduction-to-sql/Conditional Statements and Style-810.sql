## 1. Conditional Statements ##

SELECT order_id, state, sales,
       CASE
       WHEN region IN ('Central', 'South') THEN 'Territory 1'
       ELSE 'Territory 2'
       END AS territory
  FROM orders;

## 2. Binning Continuous Variables With CASE ##

SELECT order_id, product_id, sales,
       CASE
       WHEN sales BETWEEN 0 AND 49.99 THEN 'small sale'
       WHEN sales BETWEEN 50 AND 99.99 THEN 'medium sale'
       ELSE 'large sale'
       END AS sales_size
  FROM orders;

## 3. Grouping Categorical Values With CASE ##

SELECT order_date, order_id, ship_mode,
       CASE
       WHEN ship_mode = 'Same Day' THEN 'High Priority'
       WHEN ship_mode = 'First Class' THEN 'Medium Priority'
       ELSE 'Low Priority'
       END AS ship_priority
  FROM orders
 ORDER BY order_date DESC;

## 4. Not Accounting for ELSE ##

SELECT order_id, product_name, profit/sales AS profit_margin,
       CASE
       WHEN profit/sales > 0.3 THEN 'Great'
       WHEN profit/sales < 0.1 THEN 'Terrible'
       END AS profit_category
  FROM orders
 WHERE subcategory = 'Supplies' AND city = 'Los Angeles'
 ORDER BY profit_category DESC;

## 5. Ordering by Expressions ##

SELECT segment, subcategory, product_name, sales, profit
  FROM orders
 WHERE city = 'Watertown'
 ORDER BY CASE
          WHEN segment = 'Corporate' THEN 1
          WHEN segment = 'Consumer' THEN 2
          ELSE 3
          END;