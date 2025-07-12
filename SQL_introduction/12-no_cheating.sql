-- shows rows where name exists and isn’t empty, sorted by highest score
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
