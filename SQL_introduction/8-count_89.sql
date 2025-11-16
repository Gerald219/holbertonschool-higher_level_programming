-- count how many rows in first_table have id equal to 89
SELECT COUNT(*)        -- count how many matching rows there are
FROM first_table       -- look only inside first_table
WHERE id = 89;         -- only rows where the id column is 89
