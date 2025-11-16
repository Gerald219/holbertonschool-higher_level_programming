-- show the average temperature for each city

SELECT
    city,                     -- the city name we want to show
    AVG(value) AS avg_temp    -- average temperature for that city
FROM
    temperatures              -- table that holds all temperature records
GROUP BY
    city                      -- group all rows of the same city together
ORDER BY
    avg_temp DESC;            -- show the hottest cities first
