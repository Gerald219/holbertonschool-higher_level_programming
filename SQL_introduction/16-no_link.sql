-- Show score and name of people with score 10 or higher
SELECT SCORE, NAME
FROM second_table
WHERE SCORE >= 10
ORDER BY SCORE DESC;
