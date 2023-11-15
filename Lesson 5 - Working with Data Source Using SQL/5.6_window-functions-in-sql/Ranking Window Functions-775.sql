## 3. The ROW_NUMBER() Function ##

SELECT start_date, bike_number, member_type, rider_rating,
       ROW_NUMBER() OVER(ORDER BY start_date)
  FROM trips;

## 4. The RANK() Function ##

SELECT *,
       RANK() OVER(PARTITION BY EXTRACT(DAY FROM start_date) ORDER BY duration DESC)
  FROM trips;

## 5. The DENSE_RANK() Function ##

WITH dr_query AS
        (SELECT *,
                DENSE_RANK() OVER(PARTITION BY EXTRACT(DAY FROM start_date) ORDER BY duration DESC) AS trip_dense_rank
          FROM trips
         )
SELECT *
  FROM dr_query
 WHERE trip_dense_rank = 1;

## 7. The NTILE() Function ##

SELECT start_date, bike_number, rider_rating,
       NTILE(2) OVER(PARTITION BY EXTRACT(DAY FROM start_date) ORDER BY rider_rating DESC)
  FROM trips;

## 8. Solving Real-World Problems with Window Ranking Functions ##

WITH bonus_value AS
        (
            SELECT start_date, bike_number, member_type, duration,
                   NTILE(4) OVER(ORDER BY duration) + 1 AS bonus
              FROM trips
         )
         
SELECT *
  FROM bonus_value
 ORDER BY bonus DESC;