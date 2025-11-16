-- list all cities with their state name
SELECT
    cities.id,          -- city id
    cities.name,        -- city name
    states.name         -- state name
FROM
    cities              -- table with all cities
INNER JOIN
    states              -- table with all states
ON
    cities.state_id = states.id  -- match each city to its state by id
ORDER BY
    cities.id ASC;      -- sort by city id from smallest to biggest
