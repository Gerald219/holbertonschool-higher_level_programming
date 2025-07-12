-- Show rows with real names and scores 10 or more, sorted high to low
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != '' AND score >= 10
ORDER BY score DESC;
