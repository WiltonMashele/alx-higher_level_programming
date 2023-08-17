-- Lists all the cities of California from the database hbtn_0d_usa
-- Lists all entries from a specified column in a specific table
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = "California")
ORDER BY id;
