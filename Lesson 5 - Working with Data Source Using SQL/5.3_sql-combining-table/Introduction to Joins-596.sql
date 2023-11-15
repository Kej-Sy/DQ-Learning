## 3. The Syntax ##

SELECT *
  FROM track
 INNER JOIN invoice_line
    ON track.track_id = invoice_line.track_id

## 4. How Joins Work ##

SELECT *
  FROM track
  JOIN invoice_line
    ON track.track_id = invoice_line.track_id; 

## 5. Selecting Columns ##

SELECT customer.customer_id, first_name, last_name, email, invoice_id, invoice_date, total
  FROM invoice
  JOIN customer
    ON customer.customer_id = invoice.customer_id;

## 6. Selecting All Columns from One Table ##

SELECT album.album_id, album.title, album.artist_id,
       artist.name
  FROM album
  JOIN artist
    ON album.artist_id = artist.artist_id;

-- album: album_id, title, artist_id
-- artist: artist_id, name

## 7. Aliasing in Joins ##

SELECT t.track_id, t.name AS track_name, t.composer, g.name AS genre
  FROM genre AS g
  JOIN track AS t
    ON t.genre_id = g.genre_id;

-- track_id, name, album_id, media_type_id, genre_id, composer, milliseconds, bytes, unit_price
-- genre_id, name