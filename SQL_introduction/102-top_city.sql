-- show the top 3 hottest cities in july and august

SELECT
    city,                    -- show the city name
    AVG(value) AS avg_temp   -- get the average temp for that city
FROM
    temperatures             -- table with all temperature records
WHERE
    month IN (7, 8)          -- only use july and august rows
GROUP BY
    city                     -- group all rows of the same city together
ORDER BY
    avg_temp DESC            -- highest average temperature first
LIMIT
    3;                       -- keep only the top 3 cities
