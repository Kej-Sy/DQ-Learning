## 1. Sorting, Ascending vs. Descending ##

SELECT order_id, product_name, profit
  FROM orders
 ORDER BY profit DESC;

## 2. Ordering by Multiple Fields ##

SELECT product_name, sales, discount, profit
  FROM orders
 ORDER BY discount DESC, profit;

## 4. ORDER BY with WHERE ##

SELECT subcategory, sales, profit
  FROM orders
 WHERE category = 'Furniture'
 ORDER BY sales DESC, profit;

## 5. ORDER BY vs LIMIT ##

SELECT order_id, quantity
  FROM orders
 WHERE category = 'Office Supplies' AND region = 'Central'
 ORDER BY quantity DESC
 LIMIT 10;

## 6. Revisiting the Order of Execution ##

SELECT product_name, sales/quantity AS price_per_unit
  FROM orders
 WHERE sales/quantity < 95
 ORDER BY price_per_unit DESC
 LIMIT 10;

## 7. Coding with Style ##

SELECT subcategory, product_name, quantity 
  FROM orders
 WHERE category = 'Furniture' 
 ORDER BY product_name 
 LIMIT 10;