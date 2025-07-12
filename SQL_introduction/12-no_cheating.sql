-- Change bobs score to 10 without using his ID, only the name field
UPDATE second_table
SET score = 10
WHERE name = 'Bob';
