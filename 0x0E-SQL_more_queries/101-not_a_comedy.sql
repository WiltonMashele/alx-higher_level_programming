-- This script lists all shows from the database 'hbtn_0d_tvshows' 
-- that are not of the 'Comedy' genre.
-- The results are sorted by show title in ascending order.

SELECT DISTINCT t.`title`
FROM `tv_shows` AS t
LEFT JOIN `tv_show_genres` AS s ON t.`id` = s.`show_id`
LEFT JOIN `tv_genres` AS g ON s.`genre_id` = g.`id`
WHERE t.`title` NOT IN (
    SELECT t1.`title`
    FROM `tv_shows` AS t1
    JOIN `tv_show_genres` AS s1 ON t1.`id` = s1.`show_id`
    JOIN `tv_genres` AS g1 ON s1.`genre_id` = g1.`id`
    WHERE g1.`name` = "Comedy"
)
ORDER BY t.`title` ASC;
