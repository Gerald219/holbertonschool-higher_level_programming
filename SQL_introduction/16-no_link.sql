-- list rows where name is not null

SELECT 
    score,        -- show score
    name          -- show name
FROM 
    second_table  -- table with data
WHERE 
    name IS NOT NULL;  -- only keep rows that have a name
