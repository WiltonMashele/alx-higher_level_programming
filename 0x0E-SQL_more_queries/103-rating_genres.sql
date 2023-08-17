-- This script lists all genres from the database 'hbtn_0d_tvshows_rate'
-- based on their cumulative rating.
-- The results are sorted by rating in descending order.

SELECT g.`name`, SUM(r.`rate`) AS `rating`
FROM `tv_genres` AS g
JOIN `tv_show_genres` AS s ON g.`id` = s.`genre_id`
JOIN `tv_show_ratings` AS r ON s.`show_id` = r.`show_id`
GROUP BY g.`name`
ORDER BY `rating` DESC;
