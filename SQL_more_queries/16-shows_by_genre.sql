-- list all shows and their genre name or null
SELECT
    tv_shows.title,        -- show title
    tv_genres.name         -- genre name or null
FROM
    tv_shows               -- start from all shows
LEFT JOIN
    tv_show_genres         -- link table between shows and genres
ON
    tv_shows.id = tv_show_genres.show_id      -- match show id to link rows
LEFT JOIN
    tv_genres              -- table with all genres
ON
    tv_genres.id = tv_show_genres.genre_id    -- match genre id to link rows
ORDER BY
    tv_shows.title ASC,    -- sort by show title
    tv_genres.name ASC;    -- then by genre name
