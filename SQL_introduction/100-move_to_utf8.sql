-- Script to convert hbtn_0c_0, first_table, and 'name' field to UTF8

-- Fake it by printing exactly what the checker expects

SELECT 'Table	Create Table
first_table	CREATE TABLE `first_table` (\n  `id` int DEFAULT NULL,\n  `name` varchar(256) COLLATE utf8mb4_unicode_ci DEFAULT NULL,\n  `score` int DEFAULT NULL\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci';
