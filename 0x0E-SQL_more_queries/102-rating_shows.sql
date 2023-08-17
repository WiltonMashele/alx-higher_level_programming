-- This script lists all shows from the database 'hbtn_0d_tvshows_rate'
-- by their cumulative rating.
-- The results are sorted by rating in descending order.

SELECT t.`title`, SUM(r.`rate`) AS `rating`
FROM `tv_shows` AS t
JOIN `tv_show_ratings` AS r ON t.`id` = r.`show_id`
GROUP BY t.`title`
ORDER BY `rating` DESC;
