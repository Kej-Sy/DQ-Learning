## 2. Filtering with Correlated Subqueries ##

SELECT *
  FROM invoice AS i1
 WHERE total > (SELECT AVG(total)
                  FROM invoice AS i2
                 WHERE i1.billing_country = i2.billing_country);

## 3. EXISTS Operators ##

SELECT track_id
  FROM track AS t
 WHERE NOT EXISTS (SELECT *
                     FROM invoice_line AS i
                    WHERE t.track_id = i.track_id)

## 4. Nested Subqueries ##

SELECT last_name, first_name
  FROM employee
 WHERE employee_id IN (SELECT support_rep_id
                         FROM customer
                        WHERE customer_id IN ( SELECT customer_id
                                                 FROM invoice
                                                GROUP BY customer_id
                                               HAVING SUM(total) > 100));

## 6. Writing Effective Subqueries ##

SELECT tr.invoice_id AS invoice_id, 
       SUM(tr.quantity * tr.unit_price) AS total, 
       SUM(tr.milliseconds)/1000.0/60 AS minute
  FROM (SELECT il.*, t.milliseconds, t.genre_id
          FROM invoice_line il
          JOIN track t
            ON il.track_id = t.track_id
         WHERE invoice_id IN (SELECT invoice_id 
                                FROM invoice
                               WHERE billing_country = 'USA')) AS tr
 WHERE tr.genre_id IN (SELECT genre_id
                         FROM genre
                        WHERE name LIKE '%Metal%')
 GROUP BY tr.invoice_id;