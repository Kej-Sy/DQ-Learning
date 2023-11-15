## 3. The RANGE and ROWS Operators ##

SELECT *,
       SUM(quantity) OVER(ORDER BY sales_date
                          RANGE BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING) AS reverse_running_total_quantity
  FROM apple_sales_quantity_by_month;

## 4. The RANGE and ROWS Operators - Syntax Shortcut ##

SELECT *,
       AVG(quantity) OVER(ORDER BY sales_date) AS running_avg
  FROM apple_sales_quantity_by_month;

## 5. Framing using n PRECEDING and n FOLLOWING ##

SELECT *,
       AVG(revenue) OVER(PARTITION BY brand
            ORDER BY sales_date
            ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING) AS avg_previous_revenues
  FROM phone_sales_revenue_by_month;

## 6. The Difference Between ROWS and RANGE ##

SELECT *,
       SUM(quantity) OVER(
            ORDER BY sales_date
            RANGE BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING) AS rev_run_quantity
  FROM samsung_sales_quantity;