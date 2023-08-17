-- Create the database hbtn_0d_usa
-- Use the newly created database to define the cities table
-- Ensure the id column is an integer, primary key, and not null
-- Set the state_id column as a foreign key referencing the id in the states table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
id INT AUTO_INCREMENT PRIMARY KEY,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
FOREIGN KEY(state_id) references states(id)
);
