-- This script lists all genres from the database 'hbtn_0d_tvshows'
-- that are not linked to the show 'Dexter'.
-- The results are sorted by genre name in ascending order.

SELECT DISTINCT g.`name`
FROM `tv_genres` AS g
JOIN `tv_show_genres` AS s ON g.`id` = s.`genre_id`
JOIN `tv_shows` AS t ON s.`show_id` = t.`id`
WHERE g.`name` NOT IN (
    SELECT `name`
    FROM `tv_genres` AS g1
    JOIN `tv_show_genres` AS s1 ON g1.`id` = s1.`genre_id`
    JOIN `tv_shows` AS t1 ON s1.`show_id` = t1.`id`
    WHERE t1.`title` = "Dexter"
)
ORDER BY g.`name` ASC;
