## 1. Introduction ##

SELECT COUNT(*) AS tracks_tally
  FROM track
 WHERE media_type_id IN (SELECT media_type_id
                           FROM media_type
                          WHERE name LIKE '%MPEG%');

## 2. Subqueries as Lists ##

SELECT *
  FROM invoice
 WHERE customer_id IN (SELECT customer_id
                        FROM customer
                       WHERE first_name LIKE 'A%')

## 3. NOT IN Operator ##

/* SELECT customer_id
     FROM invoice
    WHERE total < 100 */
    
SELECT first_name, last_name
  FROM customer
 WHERE customer_id NOT IN (SELECT customer_id
                             FROM invoice
                            GROUP BY customer_id
                           HAVING SUM(total) < 100);

## 4. Subqueries as Tables ##

SELECT AVG(billing_city_tally) AS billing_city_tally_avg
  FROM (SELECT COUNT(*) AS billing_city_tally
          FROM invoice
         GROUP BY billing_city);

## 5. Multi-Column Subqueries and Joins ##

SELECT c.first_name, c.last_name, i.total_avg
  FROM customer AS c
  JOIN (SELECT customer_id, AVG(total) AS total_avg
          FROM invoice
         GROUP BY customer_id) AS i
    ON c.customer_id = i.customer_id;

## 6. Join Multi-Columns Subqueries ##

SELECT ct.country, 
        i.invoice_tally / ct.customer_tally AS sale_avg_tally
  FROM (SELECT billing_country, COUNT(*) AS invoice_tally
          FROM invoice
         GROUP BY billing_country) AS i
  JOIN (SELECT country, COUNT(*) AS customer_tally
          FROM customer
         GROUP BY country) AS ct
    ON i.billing_country = ct.country
 ORDER BY sale_avg_tally DESC;