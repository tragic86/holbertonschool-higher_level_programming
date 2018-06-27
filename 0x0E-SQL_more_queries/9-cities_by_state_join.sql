-- script to use join
SELECT cities.id, cities.name, states.name FROM cities JOIN states ON states.id = cities.state_id ORDER BY id ASC;
