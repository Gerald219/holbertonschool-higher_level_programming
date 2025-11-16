-- make the database use utf8mb4 (better text support for all languages)
ALTER DATABASE hbtn_0c_0
CHARACTER SET utf8mb4         -- store text using utf8mb4
COLLATE utf8mb4_unicode_ci;   -- compare and sort text using utf8mb4 rules


-- make the whole table use utf8mb4 too (so all fields follow the same rules)
ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4   -- convert every text column in this table
COLLATE utf8mb4_unicode_ci;        -- match the utf8mb4 sorting rules


-- make the "name" column use utf8mb4 (keeps the size, only changes text format)
ALTER TABLE first_table
MODIFY name VARCHAR(256)           -- keep 256 characters, same as before
CHARACTER SET utf8mb4              -- this column now stores utf8mb4 text
COLLATE utf8mb4_unicode_ci;        -- this column follows utf8mb4 sorting rules
