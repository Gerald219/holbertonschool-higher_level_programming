-- list rows where name starts with A, sorted by score

SELECT
    score,        -- show score
    name          -- show name
FROM
    second_table  -- the table with data
WHERE
    name LIKE 'A%'    -- name begins with A
ORDER BY
    score DESC;       -- highest score first
