## 1. Introduction ##

SELECT billing_state, COUNT(*) AS num_row, AVG(total) AS avg_sale
  FROM invoice
 WHERE billing_country = 'USA'
 GROUP BY billing_state
 ORDER BY  billing_state;

## 2. Grouping over Several Columns ##

SELECT billing_country, billing_state, COUNT(*) AS num_row, AVG(total) AS avg_sale
  FROM invoice
 GROUP BY billing_country, billing_state;

## 5. Adding Conditions on an Aggregated Column: the Correct Way ##

SELECT billing_country, billing_state, COUNT(*) AS num_row, AVG(total) AS avg_sale
  FROM invoice
 GROUP BY billing_country, billing_state
HAVING COUNT(*) > 40;

## 7. Adding Conditions on Not-Displayed Aggregate Column ##

SELECT billing_country, billing_state, MIN(total) AS min_sale, MAX(total) AS max_sale
  FROM invoice
 GROUP BY billing_country, billing_state
HAVING AVG(total) < 10;

## 8. Combining WHERE and HAVING Clauses ##

SELECT billing_country, billing_state, MIN(total) AS min_sale, MAX(total) AS max_sale 
  FROM invoice
 WHERE billing_state NOT IN ('None')
 GROUP BY billing_country, billing_state
HAVING AVG(total) < 10;