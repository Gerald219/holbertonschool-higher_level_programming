-- count how many rows have each score

SELECT 
    score,               -- the score value
    COUNT(*) AS number   -- how many rows have that score
FROM 
    second_table         -- the table with scores
GROUP BY 
    score                -- group the results by score
ORDER BY 
    number DESC;         -- show the biggest groups first
