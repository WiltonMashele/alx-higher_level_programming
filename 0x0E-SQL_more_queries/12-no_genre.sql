-- Lists all shows from hbtn_0d_tvshows that don't have a genre associated
-- Lists all rows from tables in a database missing a value in a specific column
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC;
