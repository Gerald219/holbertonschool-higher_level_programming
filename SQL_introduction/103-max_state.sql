-- show the highest temperature recorded in each state

SELECT
    state,                  -- show the state name
    MAX(value) AS max_temp  -- pick the highest temperature for that state
FROM
    temperatures            -- table with all temperature records
GROUP BY
    state                   -- group all rows of the same state together
ORDER BY
    state ASC;              -- list states in alphabetical order
