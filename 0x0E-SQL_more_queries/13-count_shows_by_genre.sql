-- Lists all genres from hbtn_0d_tvshows and displays the count of shows associated with each genre
-- Lists all rows from tables in a database that meet a specific condition
SELECT tv_genres.name AS 'genre', COUNT(tv_show_genres.genre_id) AS 'number_of_shows'
FROM tv_genres
RIGHT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
