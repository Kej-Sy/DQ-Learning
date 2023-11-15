## 2. What Are Window Aggregate Functions? ##

SELECT *,
       AVG(quantity) OVER(PARTITION BY sales_date) AS average,
       quantity - AVG(quantity) OVER(PARTITION BY sales_date) AS difference
  FROM phone_sales_quantity;

## 3. Using Window Aggregate Functions ##

SELECT *,
       AVG(quantity*unit_price) OVER(PARTITION BY brand
                                     ORDER BY sales_date
                                    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_average,
       AVG(quantity*unit_price) OVER(PARTITION BY brand
                                     ORDER BY sales_date
                                     ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS three_month_average
  FROM phone_sales_by_month;

## 4. Window Functions and The WHERE Clause ##

SELECT e.first_name, e.last_name, e.salary
  FROM (SELECT first_name, last_name, salary, 
               AVG(salary) OVER() AS average_salary
          FROM employees) AS e
 WHERE e.salary > e.average_salary;

## 5. Window Functions and the Order of Execution ##

SELECT first_name, last_name, department, salary,
       AVG(salary) OVER(PARTITION BY department) AS dep_avg_salary
  FROM employees
 ORDER BY dep_avg_salary DESC;

## 6. Combining Window Aggregate Functions with Aggregate Queries ##

SELECT EXTRACT(MONTH FROM sales_date) AS month, 
       brand, 
       SUM(quantity * unit_price) AS monthly_brand_revenue,
       SUM(SUM(quantity * unit_price)) OVER(PARTITION BY brand) AS total_brand_revenue
  FROM phone_sales_by_month
 GROUP BY EXTRACT(MONTH FROM sales_date), brand
 ORDER BY brand, EXTRACT(MONTH FROM sales_date);