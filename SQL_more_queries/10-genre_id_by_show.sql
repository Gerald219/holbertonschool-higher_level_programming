-- list all shows that have at least one genre
SELECT
    tv_shows.title,            -- show title
    tv_show_genres.genre_id    -- linked genre id
FROM
    tv_shows                   -- table with all shows
INNER JOIN
    tv_show_genres             -- table that links shows to genres
ON
    tv_shows.id = tv_show_genres.show_id  -- match show row to its genre rows
ORDER BY
    tv_shows.title ASC,        -- sort by show title alphabetically
    tv_show_genres.genre_id ASC;  -- then by genre id (smallest to largest)
