-- Lists all cities contained in the database
-- Lists all entries from a specific column in a specific table
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id;
