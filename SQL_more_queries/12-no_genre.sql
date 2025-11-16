-- list shows that do not have any genre
SELECT
    tv_shows.title,            -- show title
    tv_show_genres.genre_id    -- will be null for these shows
FROM
    tv_shows                   -- start from all shows
LEFT JOIN
    tv_show_genres             -- try to link genres
ON
    tv_shows.id = tv_show_genres.show_id  -- match show to genre rows
WHERE
    tv_show_genres.genre_id IS NULL       -- keep only shows without any genre
ORDER BY
    tv_shows.title ASC,        -- sort by title
    tv_show_genres.genre_id ASC;  -- genre_id stays null
