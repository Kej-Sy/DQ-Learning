## 2. The LEAD() Function ##

SELECT brand, sales_date, quantity,
       LEAD(quantity) OVER(PARTITION BY brand ORDER BY sales_date) AS next_month_sales,
         ((LEAD(quantity) OVER(PARTITION BY brand ORDER BY sales_date) - quantity) / quantity::numeric) * 100 AS sales_percentage_change
  FROM phone_sales_quantity_by_month
 ORDER BY brand, sales_date;

## 3. The LAG() Function ##

SELECT sales_date, brand, revenue,
       CASE
           WHEN revenue - LAG(revenue) OVER(PARTITION BY brand ORDER
                                     BY sales_date) > 0 THEN 'Increase'
           WHEN revenue - LAG(revenue) OVER(PARTITION BY brand ORDER
                                     BY sales_date) < 0 THEN 'Decrease'
           ELSE 'No Change'
           END AS revenue_change
  FROM phone_sales_revenue_by_month;

## 4. The FIRST_VALUE() Function ##

WITH hired_first AS (
    SELECT department, first_name ||' ' || last_name as full_name, hire_date,
           FIRST_VALUE(hire_date) OVER (
            PARTITION BY department
             ORDER BY hire_date) AS first_hire_date
      FROM employees
     WHERE department IN ('IT', 'Sales')
)

SELECT department, full_name, hire_date
  FROM hired_first
 WHERE hire_date = first_hire_date;

## 5. The LAST_VALUE() Function ##

SELECT sales_date, brand, revenue,
       ROUND(((revenue - FIRST_VALUE(revenue) OVER(PARTITION BY brand 
                                             ORDER BY sales_date
                                             ROWS BETWEEN UNBOUNDED PRECEDING 
                                             AND CURRENT ROW))/ FIRST_VALUE(revenue) OVER(PARTITION BY brand 
                                             ORDER BY sales_date
                                             ROWS BETWEEN UNBOUNDED PRECEDING 
                                             AND CURRENT ROW)) * 100, 2) AS first_month_pct_change,
       ROUND(((revenue - LAST_VALUE(revenue) OVER(PARTITION BY brand 
                                             ORDER BY sales_date
                                             ROWS BETWEEN CURRENT ROW
                                             AND UNBOUNDED FOLLOWING))/ LAST_VALUE(revenue) OVER(PARTITION BY brand 
                                             ORDER BY sales_date
                                             ROWS BETWEEN CURRENT ROW
                                             AND UNBOUNDED FOLLOWING)) * 100, 2) AS last_month_pct_change
  FROM phone_sales_revenue_by_month;

## 6. The NTH_VALUE() Function ##

WITH second_highest_rev AS 
(
    SELECT brand, sales_date, revenue,
           NTH_VALUE(revenue, 2) OVER(
               PARTITION BY brand
               ORDER BY revenue DESC
               ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
               ) AS second_highest_revenue
      FROM phone_sales_revenue_by_month
)

SELECT brand, sales_date, second_highest_revenue
  FROM second_highest_rev
 WHERE revenue = second_highest_revenue;

## 7. Offset Window Functions in Solving Real-World Problems ##

WITH silver_month_range AS
(
    SELECT *,
           FIRST_VALUE(revenue) OVER(
               PARTITION BY brand ORDER BY sales_date) AS first_month_49K_60K
      FROM phone_sales_revenue_by_month
     WHERE revenue >= 49000 AND revenue < 60000
)

SELECT sales_date, brand, revenue
  FROM silver_month_range
 WHERE revenue = first_month_49K_60K;