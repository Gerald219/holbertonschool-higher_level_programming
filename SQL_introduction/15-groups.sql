-- shows how many times each score appears in the table, most frequent first
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
