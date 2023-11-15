## 1. Introduction ##

SELECT billing_country, 
       ROUND(COUNT(*)*100.0/
             (SELECT COUNT(*) 
                FROM invoice), 2)  AS sales_prop
  FROM invoice
 GROUP BY billing_country
 ORDER BY sales_prop DESC
 LIMIT 5;

## 3. Subqueries Vocabulary ##

/*SELECT SUM(total)
  FROM invoice;*/
  
SELECT billing_country, 
       SUM(total) / 
       (SELECT SUM(total)
          FROM invoice) AS country_share
  FROM invoice
 GROUP BY  billing_country
 ORDER BY country_share DESC
 LIMIT 5;

## 4. Subqueries Guidelines ##

SELECT COUNT(*) AS rows_tally 
  FROM invoice 
 WHERE total > 
       (SELECT AVG(total) AS total_avg 
          FROM invoice);

## 5. Filtering with Scalar Subqueries ##

SELECT *
  FROM invoice
 WHERE total > (SELECT MAX(total) * 0.75 AS total_max
                  FROM invoice);

## 6. Filtering Aggregate Results with Scalar Subqueries ##

/* SELECT AVG(total)
     FROM invoice
    LIMIT 5;*/
     
SELECT customer_id, AVG(total) AS customer_avg
  FROM invoice
 GROUP BY customer_id
HAVING AVG(total) > (SELECT AVG(total) AS customer5_avg
                       FROM invoice
                      WHERE customer_id =  5);