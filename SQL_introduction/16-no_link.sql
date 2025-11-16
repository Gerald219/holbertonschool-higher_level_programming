-- list rows where name is not null, sorted by score descending

SELECT 
    score,       -- show score
    name         -- show name
FROM 
    second_table
WHERE 
    name IS NOT NULL    -- only rows with a name
ORDER BY 
    score DESC;         -- highest score first
