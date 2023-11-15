## 2. The Rank Distribution Functions - CUME_DIST() ##

WITH fast_rides AS (
    SELECT start_date, duration, bike_number,
           CUME_DIST() OVER(
               PARTITION BY EXTRACT(DAY FROM start_date)
               ORDER BY duration DESC),
           CASE
           WHEN CUME_DIST() OVER(
               PARTITION BY EXTRACT(DAY FROM start_date)
               ORDER BY duration DESC) >= 0.95 THEN 'Fast Rider'
           ELSE ''
           END AS fast_riders
      FROM tbl_bikeshare
     ORDER BY start_date, duration
    )
    
SELECT *
  FROM fast_rides
 WHERE fast_riders = 'Fast Rider'
 ORDER BY start_date, duration;

## 3. The Rank Distribution Functions - PERCENT_RANK() ##

WITH monthly_sales AS (
    SELECT sales_date, brand, model,
           SUM(quantity * unit_price) AS total_sales,
           PERCENT_RANK() OVER(PARTITION BY sales_date 
                               ORDER BY SUM(quantity * unit_price) DESC) AS revenue_percentile_rank
      FROM phone_sales_by_month
     GROUP BY sales_date, brand, model
    )
    
SELECT sales_date, brand, model, total_sales
  FROM monthly_sales
 WHERE revenue_percentile_rank <= 0.25;

## 5. The Inverse Distribution Functions - Part 2 ##

SELECT *
  FROM phone_sales_quantity_by_month
 WHERE quantity >= (SELECT PERCENTILE_DISC(0.75) 
                    WITHIN GROUP(ORDER BY quantity) AS "75th percentile of Quantity"
                      FROM phone_sales_quantity_by_month);

## 6. Solving a Real-World Problem with the Distribution Window Functions ##

WITH per_start_end_station AS (
    SELECT start_station, end_station, member_type,
           ROUND(PERCENT_RANK() OVER win::numeric, 4) AS rental_percentile
      FROM tbl_bikeshare
     GROUP BY start_station, end_station, member_type
    WINDOW win AS
                 (PARTITION BY member_type ORDER BY COUNT(*))
     ORDER BY rental_percentile DESC
    )

SELECT *
  FROM per_start_end_station
 WHERE member_type = 'Member' AND rental_percentile > 0.99;