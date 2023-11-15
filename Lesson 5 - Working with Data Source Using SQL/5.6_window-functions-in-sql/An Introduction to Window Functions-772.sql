## 4. The OVER() Clause ##

SELECT first_name, last_name, salary,
       salary - AVG(salary) OVER() AS difference
  FROM employee; 

## 5. Partitioning a Window ##

SELECT first_name, last_name, department, title,
       COUNT(first_name) OVER(PARTITION BY department) AS num_employees_department
  FROM employee;

## 6. Ordering a Window ##

SELECT sales_date, brand, quantity,
       SUM(quantity) OVER(ORDER BY sales_date) AS running_total_quantity
  FROM apple_sales_quantity_by_month;