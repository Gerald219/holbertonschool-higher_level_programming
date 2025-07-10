-- shows only scores 10 and up, sorted from highest to lowest
SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;
