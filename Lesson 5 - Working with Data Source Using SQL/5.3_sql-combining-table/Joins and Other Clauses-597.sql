## 1. The Order of Execution ##

SELECT *
  FROM track
  JOIN invoice_line
    ON track.track_id = invoice_line.track_id
 LIMIT 3;

## 3. Joining and WHERE ##

SELECT *
  FROM track
  JOIN invoice_line
    ON track.track_id = invoice_line.track_id
 WHERE invoice_line.invoice_id = 19;

## 4. Joining and GROUP BY ##

SELECT genre.name AS genre, COUNt(*) AS num_of_tracks
  FROM track
  JOIN genre
    ON track.genre_id = genre.genre_id
 GROUP BY genre.name;

## 6. Joining and JOIN ##

SELECT *
  FROM invoice
  JOIN customer
    ON invoice.customer_id = customer.customer_id
  JOIN employee
    ON employee.employee_id = customer.support_rep_id;

## 7. The Order of Execution (Revisited) ##

SELECT 1