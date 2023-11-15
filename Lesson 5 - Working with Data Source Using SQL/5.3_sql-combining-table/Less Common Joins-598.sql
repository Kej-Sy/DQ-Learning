## 1. Self-joins ##

SELECT e1.first_name || ' ' || e1.last_name AS report,
       e2.first_name || ' ' || e2.last_name AS manager
  FROM employee AS e1
  JOIN employee AS e2
    ON e1.reports_to = e2.employee_id;

## 2. LEFT JOIN ##

SELECT 1

## 3. LEFT JOIN (continuation) ##

SELECT e1.first_name || ' ' || e1.last_name AS report,
       e2.first_name || ' ' || e2.last_name AS manager
  FROM employee AS e1
  LEFT JOIN employee AS e2
    ON e1.reports_to = e2.employee_id;

## 4. CROSS JOIN ##

SELECT c1.customer_id, c1.first_name, c1.last_name, c1.country, c1.email,
       c2.customer_id AS customer_id_2, c2.first_name AS first_name_2, c2.last_name AS last_name_2, c2.country AS country_2, c2.email AS email_2
  FROM customer AS c1
 CROSS JOIN customer AS c2
 WHERE c1.customer_id <> c2.customer_id;

## 6. Joining on Conditions ##

SELECT t.track_id, t.name,
       COUNT(i.invoice_id) AS no_of_purchases
  FROM track AS t
  LEFT JOIN invoice_line AS il
    ON t.track_id = il.track_id
  LEFT JOIN invoice AS i
    ON il.invoice_id = i.invoice_id AND invoice_date LIKE '2020%'
 GROUP BY t.track_id, t.name;

## 7. Joining on Conditions (continuation) ##

SELECT i1.invoice_id, i1.invoice_date, i1.total,
       ROUND(SUM(i2.total), 2) AS running_total
  FROM invoice i1
  JOIN invoice i2
    ON i1.invoice_id >= i2.invoice_id AND i1.invoice_date >= i2.invoice_date
 GROUP BY i1.invoice_id, i1.invoice_date, i1.total;