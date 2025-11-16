-- list all cities of california by id and name
SELECT
    id,                     -- city id
    name                    -- city name
FROM
    cities                  -- table with all cities
WHERE
    state_id = (            -- keep only rows for california
        SELECT id           -- get the id
        FROM states         -- from the states table
        WHERE name = 'California'  -- where the state name is california
    )
ORDER BY
    id ASC;                 -- sort by city id from smallest to biggest
