-- list all shows and their genre id or null
SELECT
    tv_shows.title,            -- show title
    tv_show_genres.genre_id    -- genre id or null
FROM
    tv_shows                   -- start from all shows
LEFT JOIN
    tv_show_genres             -- link shows to their genres
ON
    tv_shows.id = tv_show_genres.show_id  -- match show rows to genre rows
ORDER BY
    tv_shows.title ASC,        -- sort by show title
    tv_show_genres.genre_id ASC;  -- then by genre id
